# Expected rank-opportunities result

Skill: `skills/rank-opportunities/SKILL.md`. Starts from the seeded
wiki. Prompt: "What should we work on next? Rank the opportunities. Run
without stopping." Run it once more in guided mode to check the stop.

## Must do

- [ ] Ranks against the active strategy's challenge (90-day churn of new
      teams) and focus areas (technician adoption, getting paid).
- [ ] Shows its reasoning per opportunity, citing problem pages, and marks
      each judgment `Inference:`.
- [ ] Puts Northgate's SSO request outside the ranking, or last, because
      the strategy's won't do excludes it (T22). Says so.
- [ ] Notes that offline mode already launched, so "offline" now means
      what's left (offline job creation, the duplicate-sync bug), not the
      shipped feature.
- [ ] Files the ranking as `wiki/analyses/rank-opportunities-<date>.md`;
      problem pages get no rank or score.
- [ ] Copies the problem's Size section into the decision's Known at
      decision, and lists the other candidates under Options not chosen.
- [ ] In guided mode, stops at the pick and waits. Without stopping,
      records its pick as `Decided by: copilot (unconfirmed)` on an
      opportunity decision page and lists it first in the report.

## Must not do

- [ ] Record a person's name as decider for its own pick.
- [ ] Use FieldPilot's "2x faster" claim as evidence that reminders would
      work (T4).
- [ ] Invent a reach or revenue number to break a tie.
