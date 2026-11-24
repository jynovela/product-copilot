#!/usr/bin/env python3
"""Test due.py on a small made-up wiki.

Usage: python3 skills/morning-brief/test_due.py
"""

import datetime
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import due

PAGES = {
    "wiki/features/export.md": """---
type: feature
state: current
---
## Success metrics
- Check dates: value 2026-11-20; adoption 2026-11-28; final 2027-01-15
## Results at check dates
- Week of 2026-11-09: review shows 40% (see [[2026-11-10-metrics]])
""",
    "wiki/decisions/old.md": """---
type: decision
---
## Revisit when
- If churn rises (by 2026-11-01), then review (see [[2026-10-01-memo]])
""",
    "wiki/features/gone.md": """---
type: feature
state: archived
---
- Check dates: value 2026-11-01
""",
    "wiki/goals/q3.md": """---
type: goal
status: active
period: 2026-07-01 to 2026-09-30
---
""",
    "wiki/goals/q4.md": """---
type: goal
status: active
period: 2026-10-01 to 2026-12-31
---
## Check-ins
- 2026-10-20: 41%, confidence medium
""",
    "wiki/goals/q4-done.md": """---
type: goal
status: met
period: 2026-10-01 to 2026-12-31
---
""",
    "wiki/strategies/s.md": """---
type: strategy
status: active
---
- Adopted: 2026-05-28 by someone
## Reviews
None recorded.
""",
    "wiki/review-queue.md": """# Review queue
## Waiting
- [2026-11-01] Mark Acme churned | from: [[crm]] | confirm: Sam
""",
    "wiki/sources/2026-11-10-metrics.md": """---
type: source
---
- Check dates: 2026-11-01
""",
}

EXPECTED = {
    ("OVERDUE", "2026-11-20", "wiki/features/export.md"),
    ("SOON", "2026-11-28", "wiki/features/export.md"),
    ("OVERDUE", "2026-11-01", "wiki/decisions/old.md"),
    ("GOAL", "2026-09-30", "wiki/goals/q3.md"),
    ("GOAL", "2026-10-20", "wiki/goals/q4.md"),
    ("STRATEGY", "2026-05-28", "wiki/strategies/s.md"),
    ("QUEUE", "2026-11-01", "wiki/review-queue.md"),
}


def main():
    with tempfile.TemporaryDirectory() as root:
        for rel, text in PAGES.items():
            path = os.path.join(root, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        items = due.collect(root, datetime.date(2026, 11, 24), 7, with_lint=False)
    got = {(kind, day, rel) for kind, day, rel, _, _ in items}
    failures = 0
    for item in sorted(EXPECTED - got):
        print("FAIL missing: {}".format(item))
        failures += 1
    for item in sorted(got - EXPECTED):
        print("FAIL unexpected: {}".format(item))
        failures += 1
    if failures:
        print("RESULT: {} failures".format(failures))
    else:
        print("RESULT: {} of {} checks passed".format(len(EXPECTED), len(EXPECTED)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
