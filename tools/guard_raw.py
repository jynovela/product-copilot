#!/usr/bin/env python3
"""Stop an agent from changing a source file in raw/.

Claude Code runs this before every Edit or Write (see
.claude/settings.json). It reads the tool call as JSON on standard input.
Exit code 2 blocks the call and shows the message to the agent. Any other
outcome lets the call through.

Blocked: editing or overwriting a file that already exists under raw/.
Allowed: creating a new file under raw/ (the ingest and record workflows
save new sources there), and raw/README.md, which is documentation.

This covers the file tools only. A shell command can still change a raw
file; `python3 tools/lint_wiki.py` catches that afterwards by its hash.

Standard library only, Python 3.9+.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
RAW = os.path.join(ROOT, "raw")
ALLOWED = {os.path.join(RAW, "README.md")}


def main():
    try:
        call = json.load(sys.stdin)
    except ValueError:
        return 0
    if not isinstance(call, dict):
        return 0
    tool_input = call.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return 0
    if not os.path.isabs(path):
        path = os.path.join(call.get("cwd") or ROOT, path)
    path = os.path.realpath(path)
    inside = path.startswith(RAW + os.sep)
    if inside and path not in ALLOWED and os.path.exists(path):
        sys.stderr.write(
            "Blocked: {} is a source file. Sources in raw/ are never edited "
            "or overwritten (AGENTS.md, Never). Save a new file instead, or "
            "tell the person what needs to change.\n".format(
                os.path.relpath(path, ROOT)))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
