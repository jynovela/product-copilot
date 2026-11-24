#!/usr/bin/env python3
"""Test guard_raw.py on a small made-up copilot.

Usage: python3 tools/test_guard_raw.py

Each test copies the script into a temp folder with one raw file, sends it
a tool call as JSON and checks the exit code. Standard library only,
Python 3.9+.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def run(root, payload):
    """Send one tool call to the script in root. Return (exit code, stderr)."""
    done = subprocess.run(
        [sys.executable, os.path.join(root, "tools", "guard_raw.py")],
        input=payload, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True)
    return done.returncode, done.stderr


def call(root, path, tool="Edit", key="file_path", cwd=None):
    body = {"tool_name": tool, "tool_input": {key: path}}
    if cwd:
        body["cwd"] = cwd
    return run(root, json.dumps(body))


def main():
    root = os.path.realpath(tempfile.mkdtemp(prefix="guard-test-"))
    try:
        for folder in ("tools", "raw/pasted", "wiki"):
            os.makedirs(os.path.join(root, folder))
        shutil.copy(os.path.join(HERE, "guard_raw.py"), os.path.join(root, "tools"))
        for name in ("raw/2026-11-03-call-acme.md", "raw/README.md",
                     "wiki/overview.md"):
            with open(os.path.join(root, name), "w", encoding="utf-8") as f:
                f.write("x\n")
        source = os.path.join(root, "raw", "2026-11-03-call-acme.md")

        # name, (exit code, stderr), expected exit code
        cases = [
            ("editing a source is blocked", call(root, source), 2),
            ("overwriting a source is blocked", call(root, source, "Write"), 2),
            ("a relative path is resolved from cwd",
             call(root, "raw/2026-11-03-call-acme.md", cwd=root), 2),
            ("a path with .. in it is still blocked",
             call(root, os.path.join(root, "wiki", "..", "raw",
                                     "2026-11-03-call-acme.md")), 2),
            ("a new file in raw/ is allowed",
             call(root, os.path.join(root, "raw", "pasted", "new.md"), "Write"), 0),
            ("raw/README.md is allowed",
             call(root, os.path.join(root, "raw", "README.md")), 0),
            ("a wiki page is allowed",
             call(root, os.path.join(root, "wiki", "overview.md")), 0),
            ("a call with no file path is allowed",
             run(root, json.dumps({"tool_name": "Bash",
                                   "tool_input": {"command": "ls"}})), 0),
            ("input that isn't JSON is allowed", run(root, "not json"), 0),
        ]
        passed = 0
        for name, (code, err), expected in cases:
            ok = code == expected and (expected != 2 or "Blocked:" in err)
            if ok:
                passed += 1
            else:
                print("FAIL {}: exit {} (expected {}), stderr: {}".format(
                    name, code, expected, err.strip()))
        print("RESULT: {} of {} checks passed".format(passed, len(cases)))
        return 0 if passed == len(cases) else 1
    finally:
        shutil.rmtree(root)


if __name__ == "__main__":
    sys.exit(main())
