---
name: set-outcome
description: Help a team set the goals for a period (step 0 of the product loop). Reads how the last period's goals ended, proposes outcome-shaped goals tied to the strategy, and writes goal pages only once a person sets them. Use when the user asks to set, draft or review goals or OKRs, or when another skill needs a goal and none is active.
---

# set-outcome

You help a person decide what their team is trying to move next, and how
they'll know. You prepare; the person sets. A goal is a commitment, so it
never gets `copilot (unconfirmed)`, not even in a run without stopping.

Method comes from these pages in `playbook/concepts/`:
`outcomes-over-outputs`, `okrs`, `north-star-framework`, `impact-mapping`,
`kernel-of-good-strategy` and `primary-secondary-guardrail-metrics`. Open
one only when you need it. Playbook pages are advice, never evidence.

## Inputs

- The team (or "business" for company goals) and the period, such as
  "Mobile team, Q1 2027". If either is missing, ask once; for a period
  you can't infer, propose the next calendar quarter.
- Whether the user asked to run without stopping.

## Before you start

Read `rules/pages.md` and `templates/goal.md`. Read `templates/metric.md`
too if a goal may need a new metric.

## Steps

1. **Ground it.** Run `date +%F`. Read `wiki/ways-of-working.md`,
   `wiki/now.md` and the `## Strategy` and `## Current goals` sections of
   `wiki/overview.md`. Find the strategy page with `status: active`.
   Check three things and flag each that fails: its horizon covers the new
   period; its newest Reviews line (or Adopted date, if none) is under
   three months old; its Challenge and Where to play are filled in. With
   no active strategy, product goals can still hang off a business goal,
   and business goals get `Parent: none recorded`, flagged. Also find the
   business goals for the new period. If none exist, product goals get
   `Parent: none recorded`, flagged, and you ask who sets the business
   goals.
   **Output:** the strategy page and each flag, or "No strategy recorded".
2. **Close the last period.** Find every goal page for this team (and the
   business goals they hang off) whose period ended before the new one
   starts, plus any goal still `active`. For each, report: status and
   verdict, the last check-in against target, and what share of the way it
   got (`Inference:`, with the sum). Read verdicts by commitment: an
   aspirational goal near 70% isn't a failure; a committed goal below 100%
   is a miss. Flag:
   - a committed goal missed or replaced with no `goal` decision page
     (one is required; say it's missing, never write it yourself);
   - an output written as an outcome ("launch X by date");
   - more than one active product goal for one team, or more than five
     business goals;
   - a goal with no number, or a target with no Target from;
   - a goal past its period still marked `active`, or with no check-in
     in its last month. When no source gives its result, propose status
     `ended` (Verdict "ended: no result on record") in step 5; once a
     person agrees, it stops being flagged;
   - no goals recorded for this team in the period just before the new
     one;
   - a committed line inside an aspirational goal that was missed (it
     needs a `goal` decision page like any committed miss);
   - a feature that served the goal and was stopped or archived since.
   Don't change these pages here. A verdict or status a source supports
   goes into the proposed updates in step 5.
   **Output:** one line per goal, then the flags.
3. **Gather what the new goals can stand on.** From the wiki only: the
   strategy's Challenge, Focus areas, Bets and Won't do; parent business
   goals for the period; the top current problems and their Size; recent
   feature results and experiment outcomes; and metric pages with their
   newest Baseline history line. Note each metric's known ways to mislead
   and any two pages that define the same thing differently.
   **Output:** the inputs, one line each with its page.
4. **Draft two or three options.** Each option is one goal, or one goal
   set when the team owns business goals too. For each goal write, in the
   goal template's terms:
   - Outcome: one sentence naming a change in customer or business
     behaviour. Never a feature, a launch or a task. Work that should move
     it is not part of the goal (features point at goals).
   - Level, Kind (outcome, or learning when there is no metric or
     baseline yet), Serves, and Parent with why it moves the parent.
   - Primary metric: an existing metric page, or `new metric: needs a
     definition from <owner>`. Baseline: the newest sourced value, its
     date and source page. If none, say "no baseline" and prefer a
     learning goal.
   - Target: `direction only`, unless a source or the person gives a
     number. Never propose a number of your own, not even a "typical"
     lift. If the person later gives one, record its Target from.
   - One to three supporting metrics and the guardrails that must stay
     within a range, each tied to a metric page. A range may repeat one a
     person already set elsewhere (cite it); otherwise it's the person's
     to give. So is a learning goal's decide-by date.
   - Non-goals, and the strongest reason this option could be wrong.
   Keep one active product goal per team. Check each option against the
   strategy's Won't do and say where it would pull against it.
   Pick one option to recommend, marked `Inference:`, and say why in two
   lines. **Output:** the options, then the recommendation.
5. **Checkpoint: the person sets the goals.** Show steps 1 to 4 in one
   message (a working message: keep the field labels, and skip
   humanize-check, which is for documents) and ask the person to choose and to give, for each goal: the
   owner, who set it, committed or aspirational, and the target (a number
   with where it comes from, or direction only). List any goal page
   updates from step 2 (a status a source supports, a missing check-in)
   and ask for a yes. Wait for the answer.
   In a run without stopping, don't wait and don't write goal pages. File
   the options as an analysis page (step 6), report "No goal set: needs a
   person", and let any skill that follows use `direction only`.
   **Output:** the person's answer, or "Running without stopping".
6. **Write.** Save the person's answer as a chat note and source page
   with `workflows/record.md` steps 1 and 2 only (no
   Record report; log it under this skill's entry), so the goal can cite it.
   Then:
   - One goal page per goal set, from `templates/goal.md`, named
     `<outcome-words>-<yyyy>-<qn>.md` (or the period's own name).
     `status: active`. Set by names the person and cites the note.
     Owner is the team, with the person who keeps it true. Continues
     links the last period's goal it follows, if any.
   - A metric page for each new metric, only with a definition the person
     or a source gave.
   - The goal page updates the person approved in step 5.
   - If a goal replaces one mid-period, close the old one as `replaced`,
     link both ways, and say a `goal` decision page is required; write it
     only if the person names who decided and why.
   - In `wiki/overview.md`, the `## Current goals` links. Don't touch
     `wiki/now.md` unless the person asks.
   - Without stopping, write the options instead to
     `wiki/analyses/goal-options-<team>-<period>.md` from
     `templates/analysis.md`, and link it from the overview's
     `## Open questions`.
   Add every new page to `wiki/index.md`.
   If the person's answer also tells you something else to keep (a
   stopped feature, a new owner), don't fold it in here: after the report,
   offer to record it with `workflows/record.md`.
   **Output:** each path created or changed, one line each.
7. **Log and check.** Append `## [YYYY-MM-DD] set-outcome | <team>,
   <period>` to `wiki/log.md` with one line per page touched. Run
   `python3 tools/lint_wiki.py` until `RESULT: 0 errors`.
   **Output:** the final `RESULT` line.
8. **Report** with every heading. Write `None` under an empty one.

    ```text
    ## Set-outcome report: <team>, <period>
    ### Strategy check
    ### Last period
    ### Flags
    ### Options proposed
    ### Goals set (owner, set by, commitment, target and Target from)
    ### Pages created or changed
    ### Waiting on a person
    ### Lint result
    ```

## Never

- Write a goal page without a person named in Set by and an owner.
- Invent a target, a baseline or a metric definition.
- Write a `goal` decision page for a missed or replaced goal without the
  person who decided and their reason.
- Turn a feature or a launch into a goal.
