---
type: feature
summary: Emails the owner's customers 3, 7 and 14 days after an invoice; tested in an A/B test that missed its rule, then ordered to roll out in November
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Invoice reminders

## What it does

Sends an email to the owner's customer 3, 7 and 14 days after an invoice is sent, from the business's name (see [[2026-09-08-experiment-brief-invoice-reminders]]).

## Status

planned (see [[2026-10-22-team-chat-reminders-override]], [[2026-11-17-metrics-weekly]])

- Plan: Starter and Team (see [[2026-10-22-team-chat-reminders-override]])

## Problems it addresses

- [[owners-wait-too-long-to-get-paid]]

## Scope

Locked once a `scope` decision approves it. A later change is a new
`scope` decision (action `re-scope`), not an edit.

- Approved by: not approved yet
- First slice: the tested version: reminders at 3, 7 and 14 days (see [[2026-09-08-experiment-brief-invoice-reminders]])
- In: not recorded beyond the tested version
- Out (non-goals): not recorded
- Later: none
- Constraints: rollout ordered for November (see [[2026-10-22-team-chat-reminders-override]])
- Open questions: why 39% of treatment teams turned reminders off (see [[2026-10-20-experiment-results-invoice-reminders]])

## Success metrics

Set before build. Locked at launch: after that, add dated Deviations lines
and judge results against the original thresholds.

- Goal it serves: [[owners-get-paid-faster-2026-q3]]
- Why this should move the goal: owners stop chasing payments by phone and get paid sooner (see [[2026-06-02-strategy-memo-2026-h2]])
- Owner: Tom Becker
- Primary (value; one decides): [[median-days-invoice-to-paid]]; Dan Reyes said "we'll watch the median after launch"; no threshold set (see [[2026-10-22-team-chat-reminders-override]])
  - Success if: not set
  - Failure if: not set
  - Target from: direction only
- Adoption (secondary): not set
- Guardrails: [[reminder-complaint-rate]] must stay within 1%, as in the test (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Segments to check: Starter vs Team, a hint from the test (see [[2026-10-20-experiment-results-invoice-reminders]])
- Evidence of cause: A/B [[invoice-reminders-ab-test]]
- Check dates: not set

## Launch

- Tier: not set
- Audience: everyone on Starter and Team (see [[2026-10-22-team-chat-reminders-override]])
- Rollout (dated, added as it happens):
  - 2026-09-15: A/B test with 409 treatment teams (see [[invoice-reminders-ab-test]])
- Launched: not yet; not rolled out as of the week of 2026-11-09 (see [[2026-11-17-metrics-weekly]])
- Announced: not announced
- Message: not recorded
- Teams briefed: not recorded
- Launch decision: [[ship-invoice-reminders-despite-test]]
- Launched with: none

## Deviations

None.

## Results at check dates

None yet.

## Feedback

- Mendez Plumbing would pay more for reminders sent from the business (see [[2026-08-19-interview-mendez-plumbing]])

## Contradictions

None.
