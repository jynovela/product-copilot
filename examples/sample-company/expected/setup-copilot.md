# Expected setup-copilot result

Start from a fresh test repo (`setup.sh`, raw sources present, nothing
ingested). Prompt: "Set up the copilot for my company." Answer its
questions as Priya Nair, using only facts from `answer-key.md`. When it
asks about something the answer key doesn't give (for example the plans'
technician limits), say "I don't know".

## Must do

- [ ] Notices the 18 raw files and offers to ingest them before asking
      anything they already answer.
- [ ] Shows a table of topics as known, partly known or empty, and asks
      only about the gaps.
- [ ] Asks at most three questions at a time, one topic each, with a
      recommended answer or draft first.
- [ ] Saves each round of answers as a note in `raw/notes/` and writes
      them into the overview, goal, person, customer or ways-of-working
      pages, citing the note.
- [ ] Adds only a `## Set up for` section to `README.md`.
- [ ] Says once that sources are committed and the repository must be
      private, without waiting for an answer.
- [ ] `git diff --stat <first commit> -- AGENTS.md CLAUDE.md rules
      workflows templates skills tools` prints nothing.
- [ ] Lists connectors worth adding (CRM, tickets, support, analytics,
      email and calendar) and what each feeds, without installing any.
- [ ] Ends with the setup report, every heading present, and lint at
      `RESULT: 0 errors`.

## Must not do

- [ ] Put company facts into `AGENTS.md` or any generic file.
- [ ] Fill a field with a guess when Priya says she doesn't know.
- [ ] Ask for a fact the ingested sources already hold.
