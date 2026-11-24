---
type: metric
summary: Failed syncs reported by the mobile app each week
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Offline sync errors

## Definition

- Measures: how often the mobile app fails to sync
- Formula: count of failed syncs reported by the mobile app, over one week (see [[2026-10-06-metrics-weekly]])
- Data source: analytics warehouse, weekly export (see [[2026-10-06-metrics-weekly]])
- Owner: Priya Nair
- Timing: leading; drives [[weekly-active-technician-share]] because failed syncs push technicians back to paper (see [[2026-08-25-prd-offline-mode]])

## Known ways it misleads

- It's a raw count, not a rate: it moves with the number of technicians and jobs.
- Inference: a sync that never starts because the app is closed may not count as a failure.

## Baseline history

- 2026-08-03 to 2026-08-31 weeks: 1,840, 1,902, 1,876, 1,925, 1,890; average 1,886.6 (Inference) (see [[2026-10-06-metrics-weekly]])
- 2026-09-07 to 2026-09-28 weeks: 1,950, 1,810, 1,650, 1,580; invite-only beta from 2026-09-15 (see [[2026-10-06-metrics-weekly]])
- 2026-10-05 to 2026-11-09 weeks: 1,120, 940, 910, 925, 880, 860; general availability 2026-10-01 (see [[2026-11-17-metrics-weekly]])

## Definition changes

None.

## Contradictions

None.
