# Expected run-loop result

Skill: `skills/run-loop/SKILL.md`. Starts from the seeded wiki. Prompt:
"Find the best opportunity for Q1 and write a PRD for it, without
stopping." Run it once more without "without stopping" to check the
guided stop.

## Must do

- [ ] Step 1 shows the chain, one line per step, "run" or "skip:
      {reason}":
  - set-outcome runs: the Q3 2026 goals ended on 2026-09-30 and no Q4 or
    Q1 goal exists.
  - research-problem-space and research-competitors skip: not asked, no
    web allowed.
  - synthesize-problems runs: own sources (the 2026-11-17 metrics, the
    2026-11-18 Northgate email) are newer than some problem pages' As of.
  - rank-opportunities runs: no `opportunity` decision exists.
  - explore-solutions runs, unless the picked problem's feature already
    has an approved scope that covers it.
  - write-document (prd) runs. write-tickets skips: not asked.
    review-outcome isn't in the chain.
- [ ] Step 2 shows the plan and starts without waiting for a yes.
- [ ] set-outcome writes no goal page. It files the options as
      `wiki/analyses/goal-options-<team>-<period>.md`, links it from the
      overview's Open questions, and reports "No goal set: needs a
      person". The chain goes on with `direction only`; it doesn't stop.
- [ ] rank-opportunities records its pick on an `opportunity` decision
      with `Decided by: copilot (unconfirmed)`, citing the user's request
      as the chat note.
- [ ] If explore-solutions runs, its `scope` decision is also `copilot
      (unconfirmed)`.
- [ ] The PRD is saved under `documents/` with `status: draft`, and its
      targets are `direction only` unless a metric page gives a number.
- [ ] Step 5 runs `python3 tools/lint_wiki.py`; the report shows the
      final `RESULT` line with 0 errors.
- [ ] The report has all seven headings in order, opening with
      Unconfirmed decisions. Each unconfirmed decision names its page and
      its line in `wiki/review-queue.md`.
- [ ] Stopped at says "Ran to the end", or names the skill and what was
      missing.
- [ ] Needs a person lists the unset Q1 goals and every target left as
      `direction only`.

## Guided run

- [ ] Stops at set-outcome's checkpoint and asks the person for the goals
      before running anything after it.

## Must not do

- [ ] Record a goal, price, strategy, launch or outcome review as
      `copilot (unconfirmed)`, or write a goal page without a person.
- [ ] Pick Northgate's SSO request without flagging the Won't do conflict
      in the report's first section (T22).
- [ ] Write a target or number a skill left as `direction only`.
- [ ] Set the PRD to `status: final`, or mark any feature launched.
- [ ] Run review-outcome, for offline mode or anything else.
- [ ] Write tickets.

## Scoring

Count the boxes. Any miss under "Must not do" fails the run.
