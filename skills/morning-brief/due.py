#!/usr/bin/env python3
"""List what the wiki says is due: the "Due in the wiki" part of a brief.

Usage: python3 skills/morning-brief/due.py [--days N] [--today YYYY-MM-DD]

Run it from the repo root. It prints one candidate per line and a RESULT
line. The lines are candidates: the model reads each one and drops those
that are already done. Standard library only, Python 3.9+.

Kinds:
  OVERDUE   a dated check, revisit, review or end date that has passed
            (a check date with a result on or after it is left out)
  SOON      the same, within the next N days (default 7)
  GOAL      an active goal whose period ended, or with no recent check-in
  STRATEGY  the active strategy has had no review for over 90 days
  QUEUE     a review-queue line still waiting
  STALE     a page past its freshness window (from tools/lint_wiki.py)
"""

import argparse
import datetime
import os
import re
import subprocess
import sys

DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
# Wiki links often hold a dated source name; their dates aren't due dates.
LINK = re.compile(r"\[\[[^\]]*\]\]")
# Lines that set a future date to act on.
DUE_WORDS = re.compile(
    r"check dates?|check on|revisit|review|decide by|decide-by|"
    r"deadline|due\b|ends? on|end date|watch|rollout|launch on",
    re.I,
)
# Lines whose dates are check dates; a recorded result closes them.
CHECK_WORDS = re.compile(r"check dates?|check on", re.I)
# Sections that record the past, so their dates are history, not due dates.
HISTORY = {
    "check-ins", "results at check dates", "result", "results", "reviews",
    "open issues", "last contact", "deviations", "contradictions",
    "baseline history", "definition changes", "decisions", "signals",
    "requests and feedback", "feedback",
}
SKIP_DIRS = {"sources"}
SKIP_FILES = {"index.md", "source-index.md", "log.md", "ways-of-working.md"}
GOAL_CHECKIN_DAYS = 14
STRATEGY_REVIEW_DAYS = 90


def parse_date(text):
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def frontmatter(lines):
    fields = {}
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
    return fields


def wiki_pages(root):
    wiki = os.path.join(root, "wiki")
    for folder, dirs, files in os.walk(wiki):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name.endswith(".md") and name not in SKIP_FILES:
                path = os.path.join(folder, name)
                yield os.path.relpath(path, root), path


def short(line, width=110):
    line = " ".join(line.strip().lstrip("-").split())
    return line if len(line) <= width else line[: width - 3] + "..."


def dated_lines(lines):
    """Yield (line number, line, section) for lines outside history sections."""
    section = ""
    in_front = lines and lines[0].strip() == "---"
    for number, line in enumerate(lines, 1):
        if in_front:
            if number > 1 and line.strip() == "---":
                in_front = False
            continue
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if section in HISTORY:
            continue
        yield number, line, section


def scan_page(rel, lines, today, horizon, out):
    fields = frontmatter(lines)
    if fields.get("state") == "archived":
        return
    kind = fields.get("type", "")
    if kind in ("goal", "strategy", "decision", "experiment") and \
            fields.get("status") in ("met", "missed", "dropped", "replaced",
                                     "done", "stopped"):
        return
    if rel.endswith("review-queue.md"):
        for number, line in enumerate(lines, 1):
            m = re.match(r"^- \[(\d{4}-\d{2}-\d{2})\]", line)
            if m:
                age = (today - parse_date(m.group(1))).days
                out.append(("QUEUE", m.group(1), rel, number,
                            "waiting {} days: {}".format(age, short(line))))
        return
    results = result_dates(lines)
    last_result = max(results) if results else None
    for number, line, _ in dated_lines(lines):
        bare = LINK.sub("", line)
        if not DUE_WORDS.search(bare):
            continue
        is_check = CHECK_WORDS.search(bare)
        for text in DATE.findall(bare):
            day = parse_date(text)
            if day is None:
                continue
            # A check date is done once a result dated on or after it exists.
            if is_check and last_result and last_result >= day:
                continue
            if day < today:
                out.append(("OVERDUE", text, rel, number, short(line)))
            elif day <= horizon:
                out.append(("SOON", text, rel, number, short(line)))
    if kind == "goal" and fields.get("status") == "active":
        scan_goal(rel, lines, fields, today, out)
    if kind == "strategy" and fields.get("status") == "active":
        scan_strategy(rel, lines, today, out)


def result_dates(lines):
    """Dates of the lines under Results at check dates, links left out."""
    dates, section = [], ""
    for line in lines:
        if line.startswith("## "):
            section = line[3:].strip().lower()
        elif section == "results at check dates" and line.startswith("- "):
            found = DATE.findall(LINK.sub("", line))
            day = parse_date(found[0]) if found else None
            if day:
                dates.append(day)
    return dates


def section_dates(lines, name):
    dates, section = [], ""
    for line in lines:
        if line.startswith("## "):
            section = line[3:].strip().lower()
        elif section == name:
            m = re.match(r"^- (\d{4}-\d{2}-\d{2})", line)
            if m and parse_date(m.group(1)):
                dates.append(parse_date(m.group(1)))
    return dates


def scan_goal(rel, lines, fields, today, out):
    period = DATE.findall(fields.get("period", ""))
    if len(period) == 2:
        end = parse_date(period[1])
        if end and end < today:
            out.append(("GOAL", period[1], rel, 1,
                        "period ended, status still active: needs a result"))
            return
    checkins = section_dates(lines, "check-ins")
    last = max(checkins) if checkins else None
    if last is None or (today - last).days > GOAL_CHECKIN_DAYS:
        out.append(("GOAL", last.isoformat() if last else "none", rel, 1,
                    "no check-in in the last {} days".format(GOAL_CHECKIN_DAYS)))


def scan_strategy(rel, lines, today, out):
    reviews = section_dates(lines, "reviews")
    adopted = None
    for line in lines:
        m = re.match(r"^- Adopted: (\d{4}-\d{2}-\d{2})", line)
        if m:
            adopted = parse_date(m.group(1))
    last = max(reviews) if reviews else adopted
    if last is None or (today - last).days > STRATEGY_REVIEW_DAYS:
        label = "last review" if reviews else "adopted, never reviewed"
        out.append(("STRATEGY", last.isoformat() if last else "none", rel, 1,
                    "{} over {} days ago: review due".format(
                        label, STRATEGY_REVIEW_DAYS)))


def stale_pages(root):
    lint = os.path.join(root, "tools", "lint_wiki.py")
    if not os.path.exists(lint):
        return [("STALE", "-", "tools/lint_wiki.py", 0, "check script not found")]
    run = subprocess.run([sys.executable, lint], cwd=root,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         universal_newlines=True)
    out = []
    for line in run.stdout.splitlines():
        m = re.match(r"^WARN\s+outdated (\S+): (.*)$", line)
        if m:
            out.append(("STALE", "-", m.group(1), 0, m.group(2)))
    return out


ORDER = ["OVERDUE", "STRATEGY", "GOAL", "SOON", "QUEUE", "STALE"]


def collect(root, today, days, with_lint=True):
    horizon = today + datetime.timedelta(days=days)
    out = []
    for rel, path in wiki_pages(root):
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
        scan_page(rel, lines, today, horizon, out)
    if with_lint:
        out.extend(stale_pages(root))
    out.sort(key=lambda item: (ORDER.index(item[0]), item[1], item[2], item[3]))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--today", help="YYYY-MM-DD, for tests")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    today = parse_date(args.today) if args.today else datetime.date.today()
    if today is None:
        sys.exit("--today must be YYYY-MM-DD")
    if not os.path.isdir(os.path.join(args.root, "wiki")):
        sys.exit("No wiki/ folder here. Run from the repo root.")
    items = collect(args.root, today, args.days)
    for kind, day, rel, number, text in items:
        where = "{}:{}".format(rel, number) if number else rel
        print("{:<9} {:<10} {}  {}".format(kind, day, where, text))
    print("RESULT: {} items (today {}, next {} days)".format(
        len(items), today.isoformat(), args.days))


if __name__ == "__main__":
    main()
