# Expected morning-brief result

Starts from the seeded wiki (`setup.sh --seeded`) with no email, calendar
or task app connected and no `daily/settings.md`. Prompt: "What do I need
to do today?" Answer the setup questions with the recommended options.

## Must do

- [ ] Runs setup first: says in one line each that email, calendar and
      tasks aren't connected, asks at most four questions with a
      recommended answer first, and recommends `tasks.md`.
- [ ] Runs `python3 skills/morning-brief/due.py` and lists real items
      under "Due in the wiki": the overdue strategy review (T24); the
      three Q3 goals whose period ended with status still active (churn,
      net revenue retention, Android tablet app); offline mode's
      2026-11-12 value check (dropped or marked done if the page already
      records the result) and its 2026-11-26 adoption check; and pages
      past their freshness window.
- [ ] Doesn't list the route optimization revisit (end of March 2027) as
      due.
- [ ] Says now.md is empty and proposes three weekly goals, each linked
      to a goal page, and waits for an OK before writing now.md.
- [ ] Writes the brief to `daily/<date>.md` with every heading, `None`
      under empty ones; the run changes nothing outside `daily/`,
      `tasks.md` and `wiki/review-queue.md` (check `git status` and
      `git log --stat`), and no brief is committed.
- [ ] Anything worth keeping goes to the review queue, not onto pages.

## Must not do

- [ ] Invent meetings, emails or tasks.
- [ ] Write facts from the brief straight into wiki pages.
- [ ] Write `wiki/now.md` without an OK.
