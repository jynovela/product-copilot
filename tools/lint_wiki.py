#!/usr/bin/env python3
"""Mechanical health check for the product wiki.

Usage:
    python3 tools/lint_wiki.py               # check the wiki
    python3 tools/lint_wiki.py --hash FILE   # print the sha256 of a raw file

Standard library only. Works on Python 3.9+.

Each problem is printed on its own line:
    ERROR <check> <file>: <message>
    WARN  <check> <file>: <message>
The last line is always:
    RESULT: <n> errors, <m> warnings
Exit code is 1 if there are errors, else 0.
"""

import datetime
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PLAYBOOK = ROOT / "playbook"
RAW = ROOT / "raw"
DOCUMENTS = ROOT / "documents"

# layer -> {folder name -> required value of the "type" field}
LAYERS = {
    WIKI: {
        "sources": "source",
        "customers": "customer",
        "accounts": "account",
        "problems": "problem",
        "features": "feature",
        "people": "person",
        "competitors": "competitor",
        "decisions": "decision",
        "experiments": "experiment",
        "metrics": "metric",
        "goals": "goal",
        "strategies": "strategy",
        "analyses": "analysis",
    },
    PLAYBOOK: {
        "books": "book",
        "topics": "topic",
        "concepts": "concept",
        "essays": "essay",
    },
}
# layer -> its index page; pages in a layer must be listed in its index
INDEXES = {WIKI: "index", PLAYBOOK: "playbook-index"}
SPECIAL_PAGES = {"index", "log", "overview", "playbook-index", "reading-paths",
                 "newsletters-and-podcasts", "now", "ways-of-working",
                 "review-queue"}
# page types whose claims must cite at least one source page
MUST_CITE = {"customer", "account", "problem", "feature", "competitor", "decision", "book",
             "essay", "experiment", "metric", "goal", "strategy", "person"}
# page types that must link to at least one book or essay page
MUST_LINK_BOOK = {"topic", "concept"}
# page types that must say where their knowledge came from
KNOWLEDGE_TYPES = {"book", "essay", "topic", "concept"}
KNOWLEDGE_SOURCES = {"model-memory", "ingested"}
MEMORY_MARKER = "General knowledge:"
REQUIRED_FIELDS = ["type", "summary", "updated"]
SOURCE_FIELDS = ["raw", "raw_sha256"]
RAW_IGNORED = {"README.md", ".gitkeep", ".DS_Store"}
# page type -> {frontmatter field -> allowed values}; these fields are required
ENUM_FIELDS = {
    "experiment": {"status": {"planned", "running", "done", "stopped"}},
    "goal": {"level": {"business", "product"},
             "commitment": {"committed", "aspirational"},
             "status": {"active", "met", "missed", "dropped", "replaced"}},
    "strategy": {"status": {"draft", "active", "replaced"}},
    "account": {"status": {"prospect", "trial", "active", "at-risk", "churned"}},
    "decision": {"kind": {"opportunity", "scope", "launch", "outcome-review",
                          "pricing", "strategy", "goal", "other"}},
}
# page types with state and as_of -> freshness window in days. A current
# page whose as_of is older than its window is flagged as outdated.
FRESHNESS_DAYS = {"account": 30, "feature": 30, "problem": 90, "competitor": 90,
                  "customer": 180, "person": 180, "analysis": 180, "metric": 365}
STATES = {"current", "archived"}
ARCHIVED_RE = re.compile(r"^- Archived: \d{4}-\d{2}-\d{2}, \S", re.M)
WAYS_OF_WORKING_MAX_LINES = 100
REVIEW_QUEUE_MAX_DAYS = 14
QUEUE_LINE_RE = re.compile(r"^- \[(\d{4}-\d{2}-\d{2})\]", re.M)
MONTH_RE = re.compile(r"^- Month: (\d{4})-(\d{2})\s*$", re.M)
# page type -> frontmatter fields that hold "YYYY-MM-DD to YYYY-MM-DD"
PERIOD_FIELDS = {"goal": "period", "strategy": "horizon"}
PERIOD_RE = re.compile(r"^\d{4}-\d{2}-\d{2} to \d{4}-\d{2}-\d{2}$")

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LOG_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (ingest|query|lint|search|record) \| \S.*$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DOC_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*\.md$")
DOC_STATUS = {"draft", "final"}
# decision kinds the copilot may pick itself in a run without stopping
UNCONFIRMED_KINDS = {"opportunity", "scope"}
UNCONFIRMED_RE = re.compile(r"^- Decided by:\s*copilot \(unconfirmed\)", re.M)
# Files every session loads. Keep their total small so the model isn't
# distracted by rules that don't apply to the task. Lower this as the
# always-loaded files shrink.
CONTEXT_FILES = ["AGENTS.md", "CLAUDE.md"]
CONTEXT_BUDGET = 8000  # bytes, roughly 2,000 tokens

TODAY = datetime.date.today()
errors = []
warnings = []


def error(check, path, msg):
    errors.append("ERROR {} {}: {}".format(check, rel(path), msg))


def warn(check, path, msg):
    warnings.append("WARN  {} {}: {}".format(check, rel(path), msg))


def rel(path):
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(text):
    """Return (fields, body). fields is None if there is no frontmatter."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fields = {}
            for line in lines[1:i]:
                if ":" in line and not line.startswith((" ", "\t", "#")):
                    key, value = line.split(":", 1)
                    fields[key.strip()] = value.strip().strip('"').strip("'")
            return fields, "\n".join(lines[i + 1:])
    return None, text


def parse_date(text):
    """Return a date for YYYY-MM-DD, or None if it is not a real date."""
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def strip_code(text):
    """Remove fenced and inline code so example links are not checked."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--hash":
        print(sha256(sys.argv[2]))
        return 0
    if len(sys.argv) != 1:
        print(__doc__)
        return 2

    pages = {}  # slug -> dict(path, fields, body, links)
    paths = []
    for layer in LAYERS:
        if layer.is_dir():
            paths.extend(sorted(layer.rglob("*.md")))
    for path in paths:
        slug = path.stem
        if slug in pages:
            error("duplicate-slug", path,
                  "same file name as {}".format(rel(pages[slug]["path"])))
            continue
        if not SLUG_RE.match(slug):
            error("bad-slug", path,
                  "file name must be lowercase-words-with-dashes")
        text = path.read_text(encoding="utf-8")
        fields, body = parse_frontmatter(text)
        pages[slug] = {
            "path": path,
            "fields": fields,
            "body": body,
            "links": set(LINK_RE.findall(strip_code(body))),
        }

    for name in ("index", "log", "overview"):
        if name not in pages:
            error("missing-page", WIKI / (name + ".md"), "required page is missing")
    if PLAYBOOK.is_dir() and "playbook-index" not in pages:
        error("missing-page", PLAYBOOK / "playbook-index.md", "required page is missing")

    # frontmatter and folder checks
    for slug, page in pages.items():
        path, fields = page["path"], page["fields"]
        if slug in SPECIAL_PAGES:
            continue
        folder = path.parent.name
        layer = path.parent.parent
        page["layer"] = layer
        if layer not in LAYERS or folder not in LAYERS[layer]:
            allowed = ["{}/{}/".format(l.name, f) for l in LAYERS for f in LAYERS[l]]
            error("bad-folder", path, "pages must live in one of: " + ", ".join(allowed))
            continue
        FOLDER_TYPES = LAYERS[layer]
        if fields is None:
            error("frontmatter", path, "missing --- frontmatter block at top of file")
            continue
        required = REQUIRED_FIELDS + (SOURCE_FIELDS if folder == "sources" else [])
        for key in required:
            if not fields.get(key):
                error("frontmatter", path, "missing field '{}'".format(key))
        if fields.get("type") and fields["type"] != FOLDER_TYPES[folder]:
            error("frontmatter", path, "type is '{}' but folder {}/ needs '{}'".format(
                fields["type"], folder, FOLDER_TYPES[folder]))
        if fields.get("updated") and not DATE_RE.match(fields["updated"]):
            error("frontmatter", path, "updated must be YYYY-MM-DD")
        for key, allowed in ENUM_FIELDS.get(fields.get("type"), {}).items():
            if fields.get(key) not in allowed:
                error("frontmatter", path, "{} must be one of: {}".format(
                    key, ", ".join(sorted(allowed))))
        period_key = PERIOD_FIELDS.get(fields.get("type"))
        if period_key and not PERIOD_RE.match(fields.get(period_key, "")):
            error("frontmatter", path,
                  "{} must look like 'YYYY-MM-DD to YYYY-MM-DD'".format(period_key))
        window = FRESHNESS_DAYS.get(fields.get("type"))
        if window:
            state, as_of = fields.get("state"), fields.get("as_of", "")
            if state not in STATES:
                error("frontmatter", path, "state must be one of: archived, current")
            checked = parse_date(as_of) if DATE_RE.match(as_of) else None
            if checked is None:
                error("frontmatter", path, "as_of must be a date, YYYY-MM-DD")
            elif state == "current":
                age = (TODAY - checked).days
                if age > window:
                    warn("outdated", path, "facts last checked {} days ago; "
                         "{} pages are checked every {} days".format(
                             age, fields["type"], window))
            if state == "archived" and not ARCHIVED_RE.search(page["body"]):
                error("archived", path, "add '- Archived: YYYY-MM-DD, <why> "
                      "(see [[page]])'")
        if fields.get("type") == "decision":
            replaces = re.search(r"^- Replaces: \[\[", page["body"], re.M)
            reopened = re.search(r"^- Reopened because[^:\n]*:[ \t]*\S", page["body"], re.M)
            if replaces and not reopened:
                error("decision", path, "it replaces a decision, so fill in "
                      "'Reopened because' with the new information")
            if UNCONFIRMED_RE.search(page["body"]):
                if fields.get("kind") not in UNCONFIRMED_KINDS:
                    error("decision", path, "the copilot may only pick an "
                          "opportunity or a scope; a person must decide this one")
                else:
                    warn("unconfirmed", path, "decided by the copilot; ask a "
                         "person to confirm it")
        if fields.get("type") in KNOWLEDGE_TYPES:
            ks = fields.get("knowledge_source")
            if ks not in KNOWLEDGE_SOURCES:
                error("frontmatter", path,
                      "knowledge_source must be one of: " + ", ".join(sorted(KNOWLEDGE_SOURCES)))
            elif ks == "model-memory" and MEMORY_MARKER not in page["body"]:
                error("provenance", path, "knowledge_source is model-memory, so mark "
                      "those claims with '{}'".format(MEMORY_MARKER))

    # at most one active strategy
    active = [p["path"] for p in pages.values()
              if (p["fields"] or {}).get("type") == "strategy"
              and (p["fields"] or {}).get("status") == "active"]
    if len(active) > 1:
        for path in active:
            error("strategy", path, "only one strategy page may be active")

    # source pages point at real, unchanged raw files
    ingested = set()
    for slug, page in pages.items():
        fields = page["fields"] or {}
        if page["path"].parent.name != "sources" or not fields.get("raw"):
            continue
        raw_path = (ROOT / fields["raw"]).resolve()
        ingested.add(raw_path)
        if RAW.resolve() not in raw_path.parents:
            error("raw-path", page["path"], "raw must be a path under raw/")
        elif not raw_path.is_file():
            error("raw-missing", page["path"], "raw file not found: " + fields["raw"])
        elif fields.get("raw_sha256") and sha256(raw_path) != fields["raw_sha256"]:
            error("raw-changed", page["path"],
                  "{} changed since ingest; raw files must never be edited".format(
                      fields["raw"]))

    # links
    inbound = {slug: set() for slug in pages}
    for slug, page in pages.items():
        for target in page["links"]:
            target = target.strip()
            if target not in pages:
                error("broken-link", page["path"], "[[{}]] has no page".format(target))
            elif slug not in ("index", "log", "playbook-index") and target != slug:
                inbound[target].add(slug)

    for slug, page in pages.items():
        if slug in SPECIAL_PAGES:
            continue
        if not inbound[slug]:
            error("orphan", page["path"],
                  "no other page links here (index pages and log.md do not count)")
        layer = page.get("layer")
        if layer in INDEXES:
            index = INDEXES[layer]
            if slug not in pages.get(index, {}).get("links", set()):
                error("not-in-index", page["path"], "add [[{}]] to {}/{}.md".format(
                    slug, layer.name, index))
        ptype = (page["fields"] or {}).get("type")
        if ptype in MUST_LINK_BOOK:
            books = [t for t in page["links"]
                     if t in pages and pages[t]["path"].parent.name in ("books", "essays")]
            if not books:
                error("no-book", page["path"], "link at least one book or essay page")
        if ptype in MUST_CITE:
            cited = [t for t in page["links"]
                     if t in pages and pages[t]["path"].parent.name == "sources"]
            if not cited:
                error("no-citation", page["path"],
                      "cite at least one source page, e.g. [[some-source]]")

    # log format
    if "log" in pages:
        for n, line in enumerate(pages["log"]["path"].read_text(
                encoding="utf-8").split("\n"), 1):
            if line.startswith("## ") and not LOG_RE.match(line):
                error("log-format", pages["log"]["path"],
                      "line {} must look like '## [YYYY-MM-DD] ingest | Title'".format(n))

    # files saved by the research skills say where they came from
    public = RAW / "public"
    if public.is_dir():
        for path in sorted(public.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if re.search(r"^- Fetched:", text, re.M) and not re.search(
                    r"^- URL: \S", text, re.M):
                warn("raw-url", path, "fetched by a research skill but has no URL line")

    # raw files nobody has ingested yet
    if RAW.is_dir():
        for path in sorted(RAW.rglob("*")):
            if path.is_file() and path.name not in RAW_IGNORED \
                    and "assets" not in path.relative_to(RAW).parts \
                    and path.resolve() not in ingested:
                warn("not-ingested", path, "no source page points at this file")

    # the short pages read every session stay short and current
    if "ways-of-working" in pages:
        n = len(pages["ways-of-working"]["path"].read_text(
            encoding="utf-8").split("\n"))
        if n > WAYS_OF_WORKING_MAX_LINES:
            warn("too-long", pages["ways-of-working"]["path"],
                 "{} lines; keep it under {}".format(n, WAYS_OF_WORKING_MAX_LINES))
    if "now" in pages:
        month = MONTH_RE.search(pages["now"]["body"])
        if month and (int(month.group(1)), int(month.group(2))) < (TODAY.year, TODAY.month):
            warn("outdated", pages["now"]["path"], "Month is past; replace it "
                 "with this month's focus")
    if "review-queue" in pages:
        for day in QUEUE_LINE_RE.findall(pages["review-queue"]["body"]):
            queued = parse_date(day)
            if queued and (TODAY - queued).days > REVIEW_QUEUE_MAX_DAYS:
                age = (TODAY - queued).days
                warn("review-queue", pages["review-queue"]["path"],
                     "a change from {} has waited {} days; ask who should "
                     "confirm it".format(day, age))

    # documents written for people
    if DOCUMENTS.is_dir():
        for path in sorted(DOCUMENTS.rglob("*.md")):
            if path.name == "README.md":
                continue
            if not DOC_NAME_RE.match(path.name):
                error("document", path, "name must be "
                      "YYYY-MM-DD-<doc type>-<short-title>.md")
            text = path.read_text(encoding="utf-8")
            fields, body = parse_frontmatter(text)
            if fields is None:
                error("document", path, "missing --- frontmatter block at top of file")
                continue
            if fields.get("type") != "document":
                error("document", path, "type must be 'document'")
            if not SLUG_RE.match(fields.get("doc_type", "")):
                error("document", path, "doc_type must be lowercase-words-with-dashes")
            if not DATE_RE.match(fields.get("date", "")):
                error("document", path, "date must be YYYY-MM-DD")
            if fields.get("status") not in DOC_STATUS:
                error("document", path, "status must be one of: draft, final")
            if not re.search(r"^## Built from\s*$", body, re.M):
                error("document", path, "add a '## Built from' section")
            for target in LINK_RE.findall(strip_code(body)):
                if target.strip() not in pages:
                    warn("document-link", path,
                         "[[{}]] no longer has a page".format(target.strip()))

    # size of the files every session loads
    loaded = [ROOT / name for name in CONTEXT_FILES if (ROOT / name).is_file()]
    size = sum(p.stat().st_size for p in loaded)
    if size > CONTEXT_BUDGET:
        warn("context-budget", ROOT / CONTEXT_FILES[0],
             "{} and {} together are {} bytes; keep them under {}. Move "
             "detail into files read only when needed".format(
                 CONTEXT_FILES[0], CONTEXT_FILES[1], size, CONTEXT_BUDGET))

    for line in errors + warnings:
        print(line)
    print("RESULT: {} errors, {} warnings".format(len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
