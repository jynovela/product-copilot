---
type: metric
summary: Share of reminder recipients who mark a reminder as spam or ask to stop
updated: 2026-11-24
state: current
as_of: 2026-10-20
---

# Reminder complaint rate

## Definition

- Measures: whether the owner's customers object to reminders
- Formula: recipients who mark a reminder as spam or ask to stop / recipients who got a reminder (see [[2026-09-08-experiment-brief-invoice-reminders]])
- Data source: unknown
- Owner: Billing team
- Timing: leading; guardrail for [[invoice-reminders]]

## Known ways it misleads

- Customers who ignore reminders don't complain, so a low rate doesn't mean reminders are welcome.

## Baseline history

- 2026-10-13: 0.4% in the test's treatment group (see [[2026-10-20-experiment-results-invoice-reminders]])

## Definition changes

None.

## Contradictions

None.
