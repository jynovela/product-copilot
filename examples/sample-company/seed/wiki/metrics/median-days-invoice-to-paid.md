---
type: metric
summary: Median days from an invoice being sent to it being paid
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Median days from invoice to paid

## Definition

- Measures: how fast owners get paid
- Formula: median of (paid date minus sent date) in days, for invoices paid that week, all teams (see [[2026-10-06-metrics-weekly]])
- Data source: analytics warehouse, weekly export (see [[2026-10-06-metrics-weekly]])
- Owner: Billing team (Tom Becker)
- Timing: lagging

## Known ways it misleads

- The weekly export counts invoices paid that week; the reminders test counted invoices sent during the test (see [[2026-09-08-experiment-brief-invoice-reminders]]). The two aren't directly comparable.
- Invoices never paid don't count.

## Baseline history

- 2026-07-01: 19, the Q3 baseline (see [[2026-07-01-okrs-2026-q3]])
- 2026-08-03 to 2026-09-28 weeks: 18 to 20; 18 in the week of 2026-09-28 (see [[2026-10-06-metrics-weekly]])
- 2026-10-05 to 2026-11-09 weeks: 18, 18, 18, 17, 17, 17 (see [[2026-11-17-metrics-weekly]])

## Definition changes

None.

## Contradictions

None.
