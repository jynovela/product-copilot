---
name: review-outcome
description: Review whether a launched feature worked (step 8 of the product loop). Judges results against the thresholds locked at launch, reports every guardrail, weighs evidence of cause, proposes an action, and asks a person to make the outcome decision. Use when the user asks whether a feature worked, for a post-launch review, or when a feature's check date has passed.
---

# review-outcome

You judge a launched feature against what the team said success would
look like before it launched, not against what looks good now. You
report the result, the evidence that the feature caused it, and how good
the decision was given what was known then. You propose the next action;
a person makes the call.

Method comes from these pages in `playbook/concepts/`: `resulting`,
`statistical-traps`, `primary-secondary-guardrail-metrics`,
`north-star-framework` and `heart-framework`. Open one only when you need
it. Playbook pages are advice, never evidence.

## Inputs

- One feature page in `wiki/features/`. If the user names it loosely,
  find the page and confirm it in your first output.
- Whether the user asked to run without stopping.

## Entry check

Stop and say what's missing, with the step that would fix it, when:

- the feature has no Launched date (it isn't launched; an invite-only beta
  doesn't count);
- Success metrics has no primary metric with a Success if or Failure if
  threshold. Never write thresholds after launch. Offer a descriptive
  before/after instead, clearly labeled "no thresholds were set", with
  verdict `inconclusive`;
- no ingested source has a value for the primary metric after the
  Launched date. Ask for the export to be put in `raw/` and ingested.

## Before you start

Read `rules/pages.md`, `templates/feature.md`, `templates/decision.md`
and `templates/analysis.md`.

## Steps

1. **Fix the yardstick.** Run `date +%F`. Read `wiki/ways-of-working.md`
   and `wiki/now.md`. From the feature page copy, as written, the
   Success metrics (goal served, primary with baseline and Success if and
   Failure if, adoption, guardrails, segments, Evidence of cause, check
   dates), the Launched date and every Deviations line. In a git repo,
   run `git log -p --follow -- wiki/features/<feature>.md` and flag any
   change to Success metrics after the Launched date that has no
   Deviations line. If the history starts after launch, compare the
   section with the source pages it cites instead, and say so. Judge
   against the original wording, always: if a later Results line on the
   page uses a different baseline, use the locked one and flag the drift.
   Read each metric's page for its definition, known ways it misleads and
   definition changes in the window.
   **Output:** the locked yardstick, the check dates and which have
   passed, and any flag.
2. **Read every metric against it.** Find the newest values in source
   pages (`grep -l "\[\[<metric>\]\]" wiki/sources/`, then read the source
   page; open the raw file only for a value you must sum). For each of
   primary, adoption and each guardrail write: the value, its week or
   date, the threshold, and met, not met or not due yet. Show every sum or
   average as `Inference:` with the arithmetic. Respect the window: a
   threshold "within 6 weeks of launch" is read inside that window, and a
   weekly reading counts only if its week ends inside it. Say whether the
   threshold was reached once or held after it was reached. A check date
   that hasn't passed gets an interim reading, labeled so.
   **Output:** one line per metric.
3. **Report every guardrail breach.** Check every week or reading after
   launch, not only the latest. A breach in any one of them is reported
   with its date and value, even when the primary metric succeeded and
   even when later readings are back within range. A guardrail given as
   one number ("must stay within 0.5%") is a limit in the bad direction:
   a ceiling for crashes or churn, a floor for retention. Say whether a
   pre-launch baseline exists for the guardrail; if not, say the breach
   can't be tied to the launch or cleared of it.
   **Output:** each breach, or "No guardrail breached", with readings.
4. **Weigh the evidence of cause.** Use the locked Evidence of cause: A/B
   supports cause; a staged rollout supports it partly; before/after is
   directional only. Then list what else changed in the window: other
   launches, competitor moves, price changes, campaigns, seasonality,
   definition changes (search `wiki/log.md`, decision, competitor and
   feature pages by date). Name any evidence the wiki already marks as
   unusable (for example a cohort chosen from complainers, noted in
   Contradictions) and don't use it. Check segments if the yardstick
   lists them; an unsized segment cut is a hint, never a finding.
   **Output:** the strength of the cause evidence in one line, then each
   confounder with its page.
5. **Read the goal it served.** Open the goal page. Say how the goal ended
   or stands (read by its commitment), and whether its period matches the
   feature's measurement window. A feature can succeed while its goal
   misses, and the reverse. If no goal is active now, say the feature
   serves no current goal. **Output:** two or three lines.
6. **Give two verdicts.**
   - Result: `succeeded`, `not successful`, `failed` or `inconclusive`,
     following the primary metric's thresholds. Below success but above
     failure is `not successful`. If a guardrail was breached, the verdict
     line says so in the same sentence, like "succeeded, but the crash
     rate guardrail was breached once (0.6% in the week of 2026-10-12)".
   - Decision quality: given only what was known at the scope and launch
     decisions, was the call sound? Separate luck from judgment: a good
     result doesn't prove a good decision, nor a bad one a bad decision.
     Note missing pieces that were knowable then (no launch decision, no
     guardrail baseline, no check dates).
   Both are `Inference:` until a person confirms them.
   **Output:** both verdicts with their reasons.
7. **Propose the action.** Pick from `ship`, `scale`, `iterate`,
   `re-scope`, `delay` or `kill`, usually `iterate`, `scale` or `kill`,
   marked `Inference:`, with two lines of why. Don't propose `scale` while
   a guardrail breach is unexplained; propose finding its cause first.
   Name the next question to investigate and the problem page it belongs
   to (it feeds synthesize-problems or rank-opportunities).
   **Output:** the action, why, and the next question.
8. **Checkpoint: a person decides.** Show steps 1 to 7 in one message (a
   working message: skip humanize-check, which is for documents).
   Ask the feature's Owner (or the person who made its scope or launch
   decision) to make the outcome decision: the action, and whether they
   agree with both verdicts. Wait for the answer. In a run without
   stopping, don't wait and don't decide: write everything except the
   decision, and put `Needs an outcome decision from <owner>` first in
   the report.
   **Output:** the person's answer, or "Running without stopping".
9. **Write.**
   - `wiki/analyses/outcome-review-<feature>-<YYYY-MM-DD>.md` from
     `templates/analysis.md`, with steps 1 to 7.
   - Feature page, `## Results at check dates`: add new dated lines for
     readings not already there; never edit an earlier line. Fill
     `Verdict at final review` only when the final review date has passed
     or the person says this is the final review; otherwise leave it and
     add an interim line. Set `Next` once a decision exists.
   - Each metric page: add new values to `## Baseline history`.
   - The problem page: one dated Evidence line if the result changes what
     we know about the problem, citing the source.
   - After the person decides: save their answer as a chat note and
     source page with `workflows/record.md` steps 1 and 2 only (no
     Record report; log it under this skill's entry). Write an
     `outcome-review` decision page (kind block: Reviews and Verdict)
     with Decided by the person, Options not chosen ("Do nothing" first),
     Expected result, Revisit when and Watch (write `not recorded` for
     any field the person didn't give, and list it in the report); add a
     dated Reviews line with both verdicts to the scope decision and to
     the launch decision, if one exists. Never record
     the outcome decision as decided by the copilot.
   Add every new page to `wiki/index.md`.
   If the person's answer also tells you something else to keep (a
   stopped feature, a new owner), don't fold it in here: after the report,
   offer to record it with `workflows/record.md`.
   **Output:** each path created or changed, one line each.
10. **Log and check.** Append `## [YYYY-MM-DD] review-outcome |
    <feature>` to `wiki/log.md`, one line per page touched. Run
    `python3 tools/lint_wiki.py` until `RESULT: 0 errors`.
    **Output:** the final `RESULT` line.
11. **Report** with every heading. Write `None` under an empty one.

    ```text
    ## Review-outcome report: <feature>
    ### Waiting on a person
    ### Yardstick locked at launch
    ### Results against it
    ### Guardrails
    ### Evidence of cause and confounders
    ### Goal it served
    ### Verdicts (result, decision quality)
    ### Proposed action and next question
    ### Pages created or changed
    ### Lint result
    ```

## Never

- Change a threshold, a check date or a metric definition to fit the
  result, or judge against numbers set after launch.
- Leave a guardrail breach out of the verdict because the primary metric
  succeeded.
- Use evidence the wiki marks as biased or unusable.
- Record an outcome decision with `copilot (unconfirmed)` or no decider.
