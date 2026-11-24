# Expected setup-copilot result

Draft: revise when the skill is written. Start from a fresh test repo
(raw sources present, nothing ingested). Prompt: "Set up the copilot for
my company." Answer its questions as Priya Nair, using only facts from
`answer-key.md`.

## Must do

- [ ] Asks at most three questions at a time, one topic each, with a
      recommended answer first.
- [ ] Notices the 18 raw files and offers to ingest them, instead of
      asking for facts they already hold.
- [ ] Writes answers into the overview, strategy, goal, person and
      customer pages, citing a raw note for each chat answer.
- [ ] Leaves `AGENTS.md` generic; adds only a short "set up for" block to
      the README.
- [ ] Lists connectors worth adding (CRM, analytics, support, tickets) and
      what each feeds, without installing any.

## Must not do

- [ ] Put company facts into `AGENTS.md`.
- [ ] Fill a field with a guess when Priya says she doesn't know.
