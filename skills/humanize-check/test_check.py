#!/usr/bin/env python3
"""Test check.py against references/examples.md.

Usage: python3 skills/humanize-check/test_check.py

Every "Before" must trigger the check named in its heading, and every
"After" must come back with no findings at all.
"""

import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check


def pairs():
    name = None
    with open(os.path.join(HERE, "references", "examples.md"), encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^### (\S+)", line)
            if m:
                name = m.group(1)
            m = re.match(r"^- (Before|After): (.*)$", line)
            if m and name:
                yield name, m.group(1), m.group(2)


def findings_for(text):
    fd, path = tempfile.mkstemp(suffix=".md")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    try:
        return check.check_file(path, "full")
    finally:
        os.remove(path)


def main():
    failures = 0
    count = 0
    for name, side, text in pairs():
        count += 1
        found = findings_for(text)
        names = {c for _, c, _ in found}
        if side == "Before" and name not in names:
            print("FAIL {} Before: expected '{}', got {}".format(name, name, sorted(names)))
            failures += 1
        if side == "After" and found:
            print("FAIL {} After: expected none, got {}".format(name, found))
            failures += 1
    print("RESULT: {} of {} examples passed".format(count - failures, count))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
