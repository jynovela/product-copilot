---
type: problem
summary: The accounting sync creates duplicate customers that teams fix by hand
updated: 2026-11-24
state: current
as_of: 2026-09-30
---

# Accounting sync duplicate customers

## Problem

The sync between Crewline and the team's accounting software sometimes creates the same customer more than once, and the office cleans it up by hand (see [[2026-08-12-interview-brightline-hvac]], [[2026-09-30-support-tickets-q3]]).

## Who has it

- [[small-field-service-owner]]

## Evidence

- Brightline HVAC fixes duplicate customers by hand once a week (see [[2026-08-12-interview-brightline-hvac]])
- 96 support tickets tagged invoice-sync in Q3; two examples describe duplicate customers after sync (see [[2026-09-30-support-tickets-q3]])

## Size

As of: 2026-09-30

Evidence strength (counted from Evidence above; own evidence and public evidence counted apart):

- Own: 2 sources; 1 named account (Brightline HVAC) plus 2 unnamed ticket examples; segments: [[small-field-service-owner]]
- Public: 0 sources
- First seen 2026-08-09, last seen 2026-09-30
- Kinds: interview, support ticket

Magnitude (each line: value, range or unknown, then its basis):

- Reach: unknown. 96 invoice-sync tickets in Q3; not all are about duplicates
  - Basis: measured for tickets (see [[2026-09-30-support-tickets-q3]])
- Frequency: weekly at Brightline HVAC
  - Basis: stated by source (see [[2026-08-12-interview-brightline-hvac]])
- Urgency: built a workaround
  - Basis: weekly manual cleanup (see [[2026-08-12-interview-brightline-hvac]])
- Cost to them: unknown
  - Basis: unknown
- Cost to us: 96 tickets in Q3, share about duplicates unknown
  - Basis: measured for tickets (see [[2026-09-30-support-tickets-q3]])

By segment: Same for all; accounting sync is on the Team plan (see [[2026-08-19-interview-mendez-plumbing]]).

Biggest unknown: how many invoice-sync tickets are duplicates; re-tagging one month of tickets would tell.

## Current workarounds

- Manual cleanup in the accounting software (see [[2026-08-12-interview-brightline-hvac]])

## Related features, experiments and decisions

- [[accounting-sync]]

## Contradictions

None.
