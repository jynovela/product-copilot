---
type: metric
summary: Teams active in a week; the Q3 goals and the metrics export define it differently
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Active teams

## Definition

- Measures: teams using Crewline in a week
- Formula: teams where at least one technician logged in to the mobile app that week (see [[2026-10-06-metrics-weekly]])
- Data source: analytics warehouse, weekly export (see [[2026-10-06-metrics-weekly]])
- Owner: unknown
- Timing: leading

## Known ways it misleads

- Two definitions are in use (see Contradictions). Numbers labelled "active teams" may not measure the same thing.

## Baseline history

- 2026-08-03 week: 902 (see [[2026-10-06-metrics-weekly]])
- 2026-09-28 week: 944 (see [[2026-10-06-metrics-weekly]])
- 2026-11-09 week: 981 (see [[2026-11-17-metrics-weekly]])

## Definition changes

None recorded.

## Contradictions

- The Q3 goals define an active team as one that scheduled at least one job in the week (see [[2026-07-01-okrs-2026-q3]]); the metrics exports count teams where a technician logged in to the mobile app (see [[2026-10-06-metrics-weekly]]). This page uses the export's definition because its numbers use it; which one the company means is unconfirmed.
