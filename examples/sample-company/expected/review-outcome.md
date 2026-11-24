# Expected review-outcome result

Skill: `skills/review-outcome/SKILL.md`. Prompt: "Review the outcome of
offline mode." Starts from the seeded wiki (both metrics exports are
ingested there). Guided: the run stops at the checkpoint (step 8).

## Must do

- [ ] Judges against the thresholds locked at launch on 2026-10-01, not
      new ones.
- [ ] Primary: met. August average 1,886.6 (Inference, sum shown); 943 or
      fewer reached in the week of 2026-10-12, inside the 6-week window.
- [ ] Secondary: met. 41.13% to 46.34% by the week of 2026-11-09.
- [ ] Guardrail: breached once, 0.6% in the week of 2026-10-12 (T18). The
      verdict says so; no pre-launch baseline exists.
- [ ] Evidence of cause: before/after only. Names JobHarbor's offline
      launch on 2026-10-07 as a confounder for any churn reading.
- [ ] Says the goal it served (Mobile KR2, aspirational 55%) ended Q3 at
      42.66%, about 12% of the way, and isn't the same window.
- [ ] Flags the missing launch decision for a tier 1 launch and the
      unset guardrail check date.
- [ ] Adoption check date (2026-11-26) not passed on a 2026-11-24 run:
      reads it as interim, and doesn't fill Verdict at final review.
- [ ] Gives two verdicts: result, and decision quality given what was
      known.
- [ ] Ends with an action from the shared list, not `scale` while the
      breach is unexplained, and asks a person to make the outcome
      decision (iterate/scale/kill reviews need a decision page with a
      named decider).

## Must not do

- [ ] Use the late-September ticket drop as evidence (T25).
- [ ] Record the outcome decision as decided by the copilot.
