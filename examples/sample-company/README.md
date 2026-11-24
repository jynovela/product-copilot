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
| `stand-in/` | Tool exports that stand in for a live connector, for sync tests. Copied by hand, never by `setup.sh` | You, then the copilot |
| `seed/` | A wiki built from the sources in the current page format, plus its index lines and log entry | The copilot, in seeded test repos |
| `setup.sh` | Builds a fresh test repo outside this one | You |

Never let the copilot read `answer-key.md` or `expected/`. `setup.sh`
doesn't copy them.

`seed/` is one good result of ingesting all 18 sources, written by hand
against `answer-key.md`. It handles the traps the sources plant, but not
the chat script. Use it two ways: as a starting wiki for skills that need
one, and as a reference when you grade an ingest run.

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

   To test a skill that starts from a filled wiki, build the test repo with
   the seed instead:

   ```sh
   ./examples/sample-company/setup.sh --seeded
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

A seeded repo built on 2026-11-24 shows 8 "outdated" warnings: six
accounts known only from the 2026-09-15 CRM export, and two features no
source has mentioned since September. They're real staleness, useful for
sync and morning-brief tests.

## Keeping it current

The checklists for skills not built yet are drafts; revise each one when
its skill is written. When a template or page rule changes, update
`seed/` too, and check it with `./setup.sh --seeded` and the check
script.
