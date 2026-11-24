---
type: experiment
summary: A/B test of automatic invoice reminders: 1.8 days faster to paid (p = 0.08), short of the 3-day rule; outcome not successful, re-scope
updated: 2026-11-24
status: done
---

# Invoice reminders A/B test

## Context

- Why now: getting paid is a strategy focus area and the Billing goal targets 14 days (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Owner: Tom Becker
- Evidence bar: strong evidence needed (because the rule asks for p < 0.05)

## Hypothesis

If Starter and Team teams get automatic reminders, then [[median-days-invoice-to-paid]] will fall by at least 3 days,
because owners stop relying on manual chasing.

- Would be proven wrong by: less than 3 days lower, or p of 0.05 or more (see [[2026-09-08-experiment-brief-invoice-reminders]])

## What it tests

- Assumption: automatic reminders make invoices get paid faster (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Risk: value
- Solution: [[invoice-reminders]]
- Problem: [[owners-wait-too-long-to-get-paid]]

## Method

- Type: A/B
- Why this type: random split gives evidence of cause
- Audience: [[small-field-service-owner]], Starter and Team teams that sent at least one invoice in August, split 50/50 at random (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Unit and control (A/B only): account (team), control sees no change
- Change tested: reminder emails 3, 7 and 14 days after an invoice, from the business's name
- Overlapping tests: none
- Setup check: none
- Planned length: 4 weeks, 2026-09-15 to 2026-10-13

## Metrics and decision rule

Set before the start. Never edited once status is running; to change it,
stop this experiment and start a new page.

- Primary (one decides): [[median-days-invoice-to-paid]], for invoices sent during the test, baseline 19 (see [[2026-07-01-okrs-2026-q3]]), normal variance not given, lagging
- Secondary (explain why): none
- Guardrails: [[reminder-complaint-rate]] must stay within 1%
- A/B only: significance level 0.05, minimum detectable effect 3 days, fixed length
- Stop early only if: not set
- Decision: at least 3 days lower with p < 0.05 -> ship; anything else -> re-scope and test again (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Target from: team guess (Tom Becker)

## Deviations

None.

## Result

- Primary: control 19.0 days (412 teams), treatment 17.2 days (409 teams); 1.8 days lower, p = 0.08 (see [[2026-10-20-experiment-results-invoice-reminders]])
- Secondary and guardrails: complaint rate 0.4%, within 1% (see [[2026-10-20-experiment-results-invoice-reminders]])
- Segments: Starter 2.6 days lower, Team 1.1; not sized for this comparison (see [[2026-10-20-experiment-results-invoice-reminders]])
- Setup checks: none run
- What people did or said: 39% of treatment teams turned reminders off at some point; reason not asked (see [[2026-10-20-experiment-results-invoice-reminders]])
- Outcome: not successful

## Learning and next step

- Inference: reminders may help, but by less than the 3 days the rule required; 4 weeks may be too short for late invoices to be paid.
- Next: the rule said re-scope and test again; Dan Reyes overrode it and ordered a November rollout: [[ship-invoice-reminders-despite-test]]

## Contradictions

None.
