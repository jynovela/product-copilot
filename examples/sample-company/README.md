# Sample company for testing the copilot

A made-up company, Tidewater Software, and its product Crewline: a job
scheduling, dispatch and invoicing app for small US field service firms
(HVAC, plumbing, electrical). Its raw sources cover June to November 2026
and hide traps that the workflows and skills must handle. Use it to check
that the copilot behaves as `AGENTS.md`, the workflows and the skills say.

Everything here is invented: the company, its people, customers,
competitors, numbers, URLs (all `.example`), phone numbers (555) and the
key-shaped string. Don't use it as evidence about anything real.

## What's here

| Path | What it is | Who reads it |
| ---- | ---------- | ------------ |
| `raw/` | 18 sources, copied into the test repo's `raw/` | The copilot |
| `chat-script.md` | Things to say to the copilot in chat, in order, to test the record workflow | You, the tester |
| `answer-key.md` | The true facts behind the sources, and the trap list | You only |
| `expected/` | One checklist per workflow or skill, to grade a run | You only |
| `setup.sh` | Builds a fresh test repo outside this one | You |

Never let the copilot read `answer-key.md` or `expected/`. `setup.sh`
doesn't copy them.

## Run a test

Requires bash, git and Python 3.9 or newer.

1. Build a fresh test repo:

   ```sh
   ./examples/sample-company/setup.sh
   ```

   This creates `/tmp/crewline-test` (or the folder you pass as the first
   argument): a copy of this repo's current `AGENTS.md`, workflows,
   templates, tools, playbook and empty wiki, with the sample sources in
   `raw/`. It sits outside this repo so your agent loads only the test
   copy's `AGENTS.md`.

2. Start your agent from inside the test folder (`cd /tmp/crewline-test`
   first). Then ask for one workflow or skill, for example:

   ```text
   Ingest every raw file the check script lists as not ingested, oldest first, without stopping.
   ```

3. Grade the run with the matching file in `expected/`. Check `git status`
   and `git diff` in the test folder, and run `python3 tools/lint_wiki.py`
   there yourself. Count the boxes the run gets right. Any miss under
   "Must not do" fails the run, whatever the rest scores.

## Dates

The sources end on 2026-11-21. The copilot takes today's date from
`date +%F`, so after late December 2026 the check script will flag many
fixture pages as past their freshness window. That's expected; the
checklists say which freshness warnings matter.

## Status

Phase 1: raw sources, traps and checklists. Phase 2 adds a seeded wiki
built from these sources in the current page format, so skills that start
from a filled wiki (rank, explore, write, review) can be tested without
running ingest first. The checklists for skills not built yet are drafts;
revise each one when its skill is written.
