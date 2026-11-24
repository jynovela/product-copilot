#!/usr/bin/env python3
"""Test lint_wiki.py on a small made-up copilot.

Usage: python3 tools/test_lint_wiki.py

Each test builds a tiny valid copilot in a temp folder, breaks one thing,
runs the check script there and looks for the expected line. Standard
library only, Python 3.9+.
"""

import datetime
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()

RAW_CALL = """# Call with Acme

> "Exports take me two hours
> every Friday."

Ana said they'd pay for a faster export.
"""
RAW_LIST = "# Reading list\n\nA list that recommends one book.\n"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def base():
    """Return {path: text} for a copilot that passes with no errors."""
    return {
        "AGENTS.md": "# AGENTS.md\n\n| Asks | `skills/demo/SKILL.md` |\n",
        "skills/demo/SKILL.md": "---\nname: demo\n---\n",
        ".claude/skills/demo/SKILL.md": "---\nname: demo\n---\n",
        "raw/2026-11-03-call-acme.md": RAW_CALL,
        "raw/playbook/reading-list.md": RAW_LIST,
        "wiki/index.md": "# Index\n\n- [[overview]]: picture\n"
                         "- [[2026-11-03-call-acme]]: call\n"
                         "- [[slow-export]]: problem\n- [[acme]]: account\n"
                         "- [[ops-lead]]: customer\n",
        "wiki/log.md": "# Log\n\n## [2026-11-03] ingest | Call with Acme\n",
        "wiki/overview.md": "# Overview\n\n- [[slow-export]]\n- [[acme]]\n"
                            "- [[ops-lead]]\n",
        "wiki/sources/2026-11-03-call-acme.md":
            "---\ntype: source\nsummary: call\nupdated: 2026-11-03\n"
            "raw: raw/2026-11-03-call-acme.md\nraw_sha256: {}\n---\n\n"
            "# Call\n\n## Quotes\n\n"
            '- "Exports take me two hours every Friday."\n\n'
            "## Pages this source feeds\n\n- [[slow-export]]\n".format(sha(RAW_CALL)),
        "wiki/problems/slow-export.md":
            "---\ntype: problem\nsummary: problem\nupdated: {0}\n"
            "state: current\nas_of: {0}\n---\n\n# Slow export\n\n"
            "## Evidence\n\n"
            "- Exports take two hours a week\n"
            "  (see [[2026-11-03-call-acme]])\n\n"
            "## Size\n\nAs of: {0}\n".format(TODAY),
        "wiki/accounts/acme.md":
            "---\ntype: account\nsummary: account\nupdated: {0}\n"
            "state: current\nas_of: {0}\nstatus: active\n---\n\n# Acme\n\n"
            "- Segment: [[ops-lead]]\n"
            "- Status: active, as of 2026-11-03 "
            "(see [[2026-11-03-call-acme]])\n".format(TODAY),
        "wiki/customers/ops-lead.md":
            "---\ntype: customer\nsummary: customer\nupdated: {0}\n"
            "state: current\nas_of: {0}\n---\n\n# Ops lead\n\n"
            "- Runs exports (see [[2026-11-03-call-acme]])\n"
            "- Has [[slow-export]] at [[acme]]\n".format(TODAY),
        "playbook/playbook-index.md": "# Playbook index\n\n- [[reading-list]]: list\n"
                                      "- [[some-book]]: book\n",
        "playbook/playbook-log.md": "# Playbook log\n\n"
                                    "## [2026-11-20] ingest | Reading list\n",
        "playbook/sources/reading-list.md":
            "---\ntype: source\nsummary: list\nupdated: 2026-11-20\n"
            "raw: raw/playbook/reading-list.md\nraw_sha256: {}\n---\n\n"
            "# Reading list\n\n- Recommends [[some-book]]\n".format(sha(RAW_LIST)),
        "playbook/books/some-book.md":
            "---\ntype: book\nsummary: book\nupdated: 2026-11-20\n"
            "knowledge_source: model-memory\n---\n\n# Some book\n\n"
            "- **On the list:** [[reading-list]]\n\n"
            "General knowledge: a point from memory.\n",
    }


def run(files, remove=()):
    """Write files to a temp copilot, run the check there, return its output."""
    root = tempfile.mkdtemp(prefix="lint-test-")
    try:
        os.makedirs(os.path.join(root, "tools"))
        shutil.copy(os.path.join(HERE, "lint_wiki.py"), os.path.join(root, "tools"))
        for path, text in files.items():
            if path in remove:
                continue
            full = os.path.join(root, path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as f:
                f.write(text)
        done = subprocess.run(
            [sys.executable, os.path.join(root, "tools", "lint_wiki.py")],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        return done.stdout
    finally:
        shutil.rmtree(root)


def edit(path, old, new):
    files = base()
    assert old in files[path], "test setup: {!r} not in {}".format(old, path)
    files[path] = files[path].replace(old, new)
    return files


def with_file(path, text):
    files = base()
    files[path] = text
    return files


CALL = "wiki/sources/2026-11-03-call-acme.md"
PROBLEM = "wiki/problems/slow-export.md"
ACCOUNT = "wiki/accounts/acme.md"
BOOK = "playbook/books/some-book.md"

# name, files, files to leave out, text the output must contain
CASES = [
    # The base quote sits on two wrapped block-quote lines in the raw file.
    ("a valid copilot passes", base(), (), "RESULT: 0 errors, 0 warnings"),
    ("a quote that isn't in the raw file",
     edit(CALL, "two hours every Friday", "three hours every Friday"), (),
     "ERROR quote " + CALL),
    ("a quote with a gap matches both halves",
     edit(CALL, "Exports take me two hours every Friday.",
          "Exports take me ... every Friday."), (),
     "RESULT: 0 errors"),
    ("a changed raw file",
     with_file("raw/2026-11-03-call-acme.md", RAW_CALL + "edited\n"), (),
     "ERROR raw-changed " + CALL),
    ("a missing raw file is a warning, not an error",
     base(), ("raw/2026-11-03-call-acme.md",),
     "WARN  raw-missing " + CALL),
    ("a missing raw file leaves no errors",
     base(), ("raw/2026-11-03-call-acme.md",), "RESULT: 0 errors, 1 warnings"),
    ("a raw file nobody ingested",
     with_file("raw/2026-11-04-notes.md", "notes\n"), (),
     "WARN  not-ingested raw/2026-11-04-notes.md"),
    ("an Evidence line with no source",
     edit(PROBLEM, "\n  (see [[2026-11-03-call-acme]])\n\n## Size",
          "\n- Cited (see [[2026-11-03-call-acme]])\n\n## Size"), (),
     "ERROR uncited " + PROBLEM),
    ("a page that cites nothing",
     edit(PROBLEM, "(see [[2026-11-03-call-acme]])", "(see [[ops-lead]])"), (),
     "ERROR no-citation " + PROBLEM),
    ("a wiki page that cites only a playbook source",
     edit(PROBLEM, "(see [[2026-11-03-call-acme]])", "(see [[reading-list]])"), (),
     "ERROR no-citation " + PROBLEM),
    ("a broken link",
     edit(PROBLEM, "## Size", "See [[no-such-page]].\n\n## Size"), (),
     "ERROR broken-link " + PROBLEM),
    ("a page missing from the index",
     edit("wiki/index.md", "- [[slow-export]]: problem\n", ""), (),
     "ERROR not-in-index " + PROBLEM),
    ("a page nothing links to",
     with_file("wiki/customers/lonely.md",
               "---\ntype: customer\nsummary: s\nupdated: {0}\nstate: current\n"
               "as_of: {0}\n---\n\n- x (see [[2026-11-03-call-acme]])\n".format(TODAY)),
     (), "ERROR orphan wiki/customers/lonely.md"),
    ("a type that doesn't match its folder",
     edit(PROBLEM, "type: problem", "type: feature"), (),
     "ERROR frontmatter " + PROBLEM),
    ("a missing frontmatter field",
     edit(PROBLEM, "summary: problem\n", ""), (),
     "ERROR frontmatter " + PROBLEM),
    ("a stale page gets an outdated warning",
     edit(PROBLEM, "as_of: " + TODAY, "as_of: 2020-01-01"), (),
     "WARN  outdated " + PROBLEM),
    ("an archived page with no Archived line",
     edit(PROBLEM, "state: current", "state: archived"), (),
     "ERROR archived " + PROBLEM),
    ("an account whose two statuses differ",
     edit(ACCOUNT, "- Status: active", "- Status: churned"), (),
     "ERROR account-status " + ACCOUNT),
    ("an account status outside the list",
     edit(ACCOUNT, "status: active\n---", "status: happy\n---"), (),
     "ERROR frontmatter " + ACCOUNT),
    ("a memory-only book without the General knowledge marker",
     edit(BOOK, "General knowledge: ", ""), (),
     "ERROR provenance " + BOOK),
    ("a bad log heading",
     edit("wiki/log.md", "] ingest | Call", "] Ingested Call"), (),
     "ERROR log-format wiki/log.md"),
    ("a bad playbook log heading",
     edit("playbook/playbook-log.md", "] ingest | Reading", "] added Reading"), (),
     "ERROR log-format playbook/playbook-log.md"),
    ("two pages with the same file name",
     with_file("wiki/customers/slow-export.md", "x\n"), (),
     "ERROR duplicate-slug"),
    ("a decision the copilot may not make",
     with_file("wiki/decisions/raise-price.md",
               "---\ntype: decision\nsummary: s\nupdated: {}\nkind: pricing\n---\n\n"
               "- Decided by: copilot (unconfirmed)\n"
               "- x (see [[2026-11-03-call-acme]])\n".format(TODAY)),
     (), "ERROR decision wiki/decisions/raise-price.md"),
    ("a skill with no AGENTS.md row",
     with_file("skills/other/SKILL.md", "---\nname: other\n---\n"), (),
     "ERROR skill skills/other/SKILL.md"),
    ("a document with a bad name",
     with_file("documents/prd.md", "---\ntype: document\n---\n"), (),
     "ERROR document documents/prd.md"),
    ("an old review-queue line",
     with_file("wiki/review-queue.md",
               "# Review queue\n\n- [2020-01-01] change | from: x | confirm: y\n"),
     (), "WARN  review-queue wiki/review-queue.md"),
]


def main():
    passed = 0
    for name, files, remove, expected in CASES:
        output = run(files, remove)
        if expected in output:
            passed += 1
        else:
            print("FAIL {}: expected '{}' in:\n{}".format(name, expected, output))
    print("RESULT: {} of {} checks passed".format(passed, len(CASES)))
    return 0 if passed == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
