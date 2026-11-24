---
type: metric
summary: Share of mobile app sessions that crashed, tracked weekly from 2026-10-05
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# App crash rate

## Definition

- Measures: mobile app stability
- Formula: crashed sessions / all mobile app sessions, over one week (see [[2026-11-17-metrics-weekly]])
- Data source: analytics warehouse, weekly export (see [[2026-11-17-metrics-weekly]])
- Owner: unknown
- Timing: leading; guardrail for [[offline-mode]]

## Known ways it misleads

- No data before 2026-10-05, so there's no pre-launch baseline for offline mode.

## Baseline history

- 2026-10-05 to 2026-11-09 weeks: 0.4%, 0.6%, 0.5%, 0.4%, 0.4%, 0.3% (see [[2026-11-17-metrics-weekly]])

## Definition changes

- 2026-10-05: first tracked. No values before this date.

## Contradictions

None.
