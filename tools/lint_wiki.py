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

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

# folder name -> required value of the "type" field
FOLDER_TYPES = {
    "sources": "source",
    "customers": "customer",
    "problems": "problem",
    "features": "feature",
    "competitors": "competitor",
    "decisions": "decision",
    "analyses": "analysis",
}
SPECIAL_PAGES = {"index", "log", "overview"}
# page types whose claims must cite at least one source page
MUST_CITE = {"customer", "problem", "feature", "competitor", "decision"}
REQUIRED_FIELDS = ["type", "summary", "updated"]
SOURCE_FIELDS = ["raw", "raw_sha256"]
RAW_IGNORED = {"README.md", ".gitkeep", ".DS_Store"}

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LOG_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (ingest|query|lint) \| \S.*$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

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
    for path in sorted(WIKI.rglob("*.md")):
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

    for name in SPECIAL_PAGES:
        if name not in pages:
            error("missing-page", WIKI / (name + ".md"), "required page is missing")

    # frontmatter and folder checks
    for slug, page in pages.items():
        path, fields = page["path"], page["fields"]
        if slug in SPECIAL_PAGES:
            continue
        folder = path.parent.name
        if path.parent.parent != WIKI or folder not in FOLDER_TYPES:
            error("bad-folder", path,
                  "pages must live in one of: wiki/" + ", wiki/".join(FOLDER_TYPES))
            continue
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
            elif slug not in ("index", "log") and target != slug:
                inbound[target].add(slug)

    for slug, page in pages.items():
        if slug in SPECIAL_PAGES:
            continue
        if not inbound[slug]:
            error("orphan", page["path"],
                  "no other page links here (index.md and log.md do not count)")
        if slug not in pages.get("index", {}).get("links", set()):
            error("not-in-index", page["path"], "add [[{}]] to wiki/index.md".format(slug))
        ptype = (page["fields"] or {}).get("type")
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

    # raw files nobody has ingested yet
    if RAW.is_dir():
        for path in sorted(RAW.rglob("*")):
            if path.is_file() and path.name not in RAW_IGNORED \
                    and "assets" not in path.relative_to(RAW).parts \
                    and path.resolve() not in ingested:
                warn("not-ingested", path, "no source page points at this file")

    for line in errors + warnings:
        print(line)
    print("RESULT: {} errors, {} warnings".format(len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
