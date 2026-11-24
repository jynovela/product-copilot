---
name: explore-solutions
description: For one chosen problem, generate several solution options, name each option's riskiest assumption, plan the cheapest test that could kill it, and propose a first-slice scope (steps 4 and 5 of the product loop). Use when the user asks how to solve a problem, what to build for it, what to test, or to scope a solution.
---

# explore-solutions

You turn one problem into a few real options, find what would have to be
true for each, and plan how to find out cheaply. Then you propose a scope
for the option the person picks. A list of solutions without assumptions
is the build trap, so every option gets one.

Method comes from these pages in `playbook/concepts/`:
`opportunity-solution-tree`, `four-product-risks`, `working-backwards-pr-faq`,
`minimum-viable-product`, `fake-door-test`, `ab-testing`, `premortem`,
`story-map` and `outcomes-over-outputs`. Open one only when you need it.
Playbook pages are advice, never evidence.

## Inputs

- One problem page in `wiki/problems/`, usually the opportunity a person
  picked. If the user names a problem loosely, find the page and confirm
  it in your first output. If none exists, stop and say so: the problem
  needs a page first (ingest, record or synthesize-problems).
- Whether the user asked to run without stopping.

## Before you start

Read `rules/pages.md`, and `templates/analysis.md`,
`templates/feature.md`, `templates/experiment.md` and
`templates/decision.md`.

## Steps

1. **Ground it.** Run `date +%F`. Read `wiki/ways-of-working.md` and
   `wiki/now.md`. Read the problem page and the source pages behind its
   strongest claims. Then find, with `grep -l "\[\[<problem>\]\]"
   wiki/`:
   - the `opportunity` decision that picked it, and the goal it serves
     (flag if no decision exists, or if the goal is closed and no current
     one replaces it; continue anyway, using the newest goal as context).
     If the user says who picked it, offer to record that decision with
     `workflows/record.md` after the report;
   - the active strategy's Focus areas, Bets and Won't do;
   - every feature that addresses it, with Status, Scope and results;
   - every experiment on it, with its decision rule, Result, Outcome and
     Deviations;
   - decisions that affect it, especially any that overrode an
     experiment's rule or are still being carried out;
   - competitor offers for it, as "they say" claims.
   **Output:** the problem in one line, the goal it serves, then
   "What we already know": one line per item with its page.
2. **State the constraints in flight.** List what the options must fit:
   work already decided or rolling out, locked scopes, strategy Won't do
   lines, and dates. A decision a person made stands even if you'd argue
   with it; build on it, and say plainly where the evidence pulls against
   it. Read experiment results by their rule, not by their best-looking
   number:
   - A segment difference from a test not sized for it is a hint to test,
     never a finding.
   - A short test, a high opt-out or turn-off rate, or a missing setup
     check limits what the result can say. Name the limit.
   **Output:** the constraints, one line each with its page.
3. **Generate options.** Write at least three options that differ in kind,
   not three versions of one feature. Change to product, to process,
   to pricing or policy, or to what you tell customers all count.
   Include "let what's in flight land, then measure" as a baseline option
   when something is in flight, and say what it costs to wait. Tie each
   option to the evidence that suggests it (a quote, a ticket, a
   competitor offer, an experiment hint), or mark it `Inference:`. Flag
   any option that conflicts with the strategy's Won't do.
   **Output:** the options, two or three lines each.
4. **Find each option's riskiest assumption.** For each option, list its
   assumptions under the four risks: value (will they want it), usability
   (can they use it), feasibility (can we build it) and viability (does it
   work for the business, including legal and support). Pick the riskiest:
   the one that would sink the option and has the least evidence. Say what
   evidence exists for it today, with pages.
   **Output:** one line per option: riskiest assumption, risk type,
   evidence today.
5. **Plan the cheapest test for each.** For each riskiest assumption pick
   a method from the experiment template's Type list, the cheapest one
   that could prove it wrong. Give the audience and how many (a playbook
   rule of thumb, marked `General knowledge:`, or `to be set by
   <owner>`), the length,
   the metric (an existing metric page, or a definition the person must
   give), and what result kills the option. Write kill and pass thresholds
   as `to be set by <owner>` unless a source gives a number or the
   threshold is plain arithmetic on a sourced baseline the person already
   committed to; never set one yourself. Note overlap with any running
   test or rollout on the same customers.
   **Output:** one test per option.
6. **Recommend and premortem.** Recommend which option or options to test
   first, and which one to scope now if any is ready, marked `Inference:`.
   Run a short premortem on the recommendation: it failed a year from now;
   list the three likeliest reasons, each with the page that makes it
   plausible.
   **Output:** the recommendation and the premortem.
7. **Draft the scope** for the option you'd scope now (skip if none is
   ready, and say why), in the feature template's terms: First slice (the
   smallest version that tests the riskiest assumption), In, Out
   (non-goals, with why), Later, Constraints (from step 2), and Open
   questions. Draft Success metrics too: Goal it serves; Primary metric
   with its sourced baseline; Target from `direction only` unless a
   source gives a target (cite who set it, for example a goal's target
   set by leadership); guardrails; Evidence of cause.
   **Output:** the draft scope and success metrics.
8. **Checkpoint: the person picks.** Show steps 3 to 7 in one message (a
   working message: keep the field labels, and skip humanize-check, which
   is for documents) and
   ask the person to choose: which tests to plan, and whether to approve
   the scope (and who approves it). Wait for the answer.
   In a run without stopping, don't wait: pick the recommended option,
   scope and tests yourself. Your scope pick counts as approved for step
   9, with `Decided by: copilot (unconfirmed)`, listed first in the
   report and added to `wiki/review-queue.md`. Your tests count as chosen
   and are written as `planned`, never `running`. Set no target. The
   user's request to run without stopping is the chat note you save and
   cite.
   **Output:** the person's answer, or "Running without stopping".
9. **Write.**
   - Always: `wiki/analyses/solutions-<problem>.md` from
     `templates/analysis.md`, holding the options, assumptions, tests,
     recommendation and premortem. Link it, and every new feature,
     experiment or decision page, from the problem page's `## Related
     features, experiments and decisions`.
   - For each option the person chose (or the one you picked without
     stopping): a feature page with Status `idea`, or update the existing
     feature page. Its Scope gets the draft from step 7 with `Approved
     by: not approved yet`, unless the scope is approved now; then its
     Status is `planned`.
   - For each test the person chose: an experiment page with
     `status: planned`, its rule thresholds as the person gave them or
     `to be set by <owner>`.
   - If the scope was approved: a `scope` decision page (kind block:
     Feature) with Decided by the person, or `copilot (unconfirmed)`
     without stopping. Fill Options not chosen from step 3 ("Do nothing"
     first), Revisit when (a signal, by a date the owner sets if no
     source gives one), and Watch. Then set `Approved by` on the
     feature's Scope. Save the person's answer first as a chat note and
     source page with `workflows/record.md` steps 1 and 2 only (no
     Record report; log it under this skill's entry), and cite it.
   Never edit a locked section: an experiment's rule once running, a
   launched feature's Success metrics, an approved Scope, a decision above
   Reviews. A change to an approved scope is a new `scope` decision
   (action `re-scope`). Add every new page to `wiki/index.md`.
   If the person's answer also tells you something else to keep (a
   stopped feature, a new owner), don't fold it in here: after the report,
   offer to record it with `workflows/record.md`.
   **Output:** each path created or changed, one line each.
10. **Log and check.** Append `## [YYYY-MM-DD] explore-solutions |
    <problem>` to `wiki/log.md`, one line per page touched. Run
    `python3 tools/lint_wiki.py` until `RESULT: 0 errors`.
    **Output:** the final `RESULT` line.
11. **Report** with every heading. Write `None` under an empty one.

    ```text
    ## Explore-solutions report: <problem>
    ### Unconfirmed picks
    ### What we already know
    ### Constraints in flight
    ### Options, riskiest assumptions and tests
    ### Recommendation and premortem
    ### Scope proposed
    ### Pages created or changed
    ### Waiting on a person
    ### Lint result
    ```

## Never

- Present a segment difference, an unsized cut or a result that missed
  its rule as proof.
- Set a target, a threshold or a price. Targets stay `direction only`
  unless a source gives one.
- Ignore a decision a person made, or edit a locked section to fit a new
  option.
- Write a decision page with no decider. Without stopping, the only
  decider you may write is `copilot (unconfirmed)`, and only for a scope.
