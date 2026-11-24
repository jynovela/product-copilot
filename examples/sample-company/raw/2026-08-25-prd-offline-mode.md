# PRD: Offline mode for the technician app

- Author: Priya Nair (Senior PM, Mobile)
- Date: 2026-08-25
- Status: approved for build by Dan Reyes on 2026-08-27
- Goal: Technicians rely on Crewline in the field (Q3 Mobile goal)

## Problem

Technicians lose signal in basements, crawl spaces and rural areas. The app
can't load job notes or close jobs without a connection. They fall back to
paper, the office re-types it, and invoices go out late.

Support tells me we get more than 300 offline tickets a quarter. The
Brightline HVAC interview describes the problem daily.

## Scope

- In: view today's and tomorrow's jobs offline, add notes and photos, mark
  parts used, close a job, capture a signature. Changes sync when the
  connection comes back.
- Out: creating new jobs offline, editing the schedule offline, and the
  Android tablet app. The tablet app is out because fewer than 5% of
  technicians use it.
- First slice: close a job offline with notes, then sync.

## Success metrics

Measured from the general availability date.

- Primary: offline sync errors per week down at least 50% from the August
  average within 6 weeks of general availability. Failure if down less than
  20%.
- Secondary: weekly active technicians as a share of paid seats up at least
  5 points from 41% within 8 weeks of general availability.
- Guardrail: app crash rate must stay within 0.5% of sessions.

Targets set by Priya and Dan from the August numbers.

## Launch

- Tier 1: announced to all customers by email and in the app.
- Invite-only beta from 2026-09-15 with 50 teams who reported offline
  problems.
- General availability planned for 2026-10-01, all plans.
- Support and sales briefed before general availability.

## Open questions

- How long can a job stay unsynced before conflicts get likely?
