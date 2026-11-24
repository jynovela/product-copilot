---
type: feature
summary: Lets technicians view, update and close jobs with no signal and sync later; launched to all plans on 2026-10-01
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Offline mode

## What it does

Technicians can view today's and tomorrow's jobs, add notes and photos, mark parts used, close a job and capture a signature with no connection; changes sync when the connection returns (see [[2026-08-25-prd-offline-mode]]).

## Status

launched (see [[2026-10-06-metrics-weekly]])

- Plan: all plans (see [[2026-08-25-prd-offline-mode]])

## Problems it addresses

- [[technicians-lose-signal-in-the-field]]
- [[technicians-dont-adopt-the-mobile-app]]

## Scope

Locked once a `scope` decision approves it. A later change is a new
`scope` decision (action `re-scope`), not an edit.

- Approved by: [[approve-offline-mode-scope]]
- First slice: close a job offline with notes, then sync (see [[2026-08-25-prd-offline-mode]])
- In: view today's and tomorrow's jobs, add notes and photos, mark parts used, close a job, capture a signature, sync on reconnect (see [[2026-08-25-prd-offline-mode]])
- Out (non-goals): creating new jobs offline, editing the schedule offline, and the Android tablet app, used by fewer than 5% of technicians (see [[2026-08-25-prd-offline-mode]])
- Later: none
- Constraints: Q3 goal said launch by 2026-09-30 (see [[2026-07-01-okrs-2026-q3]])
- Open questions: how long a job can stay unsynced before conflicts get likely (see [[2026-08-25-prd-offline-mode]])

## Success metrics

Set before build. Locked at launch: after that, add dated Deviations lines
and judge results against the original thresholds.

- Goal it serves: [[technicians-rely-on-crewline-2026-q3]]
- Why this should move the goal: technicians who can work without signal keep using the app instead of paper (see [[2026-08-25-prd-offline-mode]])
- Owner: Priya Nair
- Primary (value; one decides): [[offline-sync-errors]], baseline 1,886.6 a week, the August average (Inference: mean of the five August weeks) (see [[2026-10-06-metrics-weekly]]), normal variance about 1,840 to 1,925 a week in August, leading
  - Success if: down at least 50% from the August average within 6 weeks of general availability (see [[2026-08-25-prd-offline-mode]])
  - Failure if: down less than 20% (see [[2026-08-25-prd-offline-mode]])
  - Target from: set by leadership (Priya Nair and Dan Reyes, from the August numbers)
- Adoption (secondary): [[weekly-active-technician-share]] up at least 5 points from 41% within 8 weeks of general availability (see [[2026-08-25-prd-offline-mode]])
- Guardrails: [[app-crash-rate]] must stay within 0.5% of sessions (see [[2026-08-25-prd-offline-mode]])
- Segments to check: not set
- Evidence of cause: before/after (directional)
- Check dates: guardrails not set; adoption 2026-11-26; value 2026-11-12; final review not set (Inference: 6 and 8 weeks after 2026-10-01)

## Launch

- Tier: 1 (announced widely) (see [[2026-08-25-prd-offline-mode]])
- Audience: everyone
- Rollout (dated, added as it happens):
  - 2026-09-15: invite-only beta with 50 teams who reported offline problems (see [[2026-10-06-metrics-weekly]], [[2026-08-25-prd-offline-mode]])
  - 2026-10-01: general availability (see [[2026-10-06-metrics-weekly]])
- Launched: 2026-10-01, the first day the target segment could use it without an invitation
- Announced: email and in-app planned; no record that it happened
- Message: not recorded
- Teams briefed: support and sales, planned before general availability; no record that it happened (see [[2026-08-25-prd-offline-mode]])
- Launch decision: none recorded. Inference: a tier 1 launch needs a decision page; the PRD's approval covered scope only, so the launch decision is missing.
- Launched with: none

## Deviations

None.

## Results at check dates

- 2026-11-12: [[offline-sync-errors]] 880 in the week of 2026-11-02 vs success 943 or fewer / failure above 1,509 (Inference: 50% and 80% of 1,886.6); first at or below 943 in the week of 2026-10-12 (940) (see [[2026-11-17-metrics-weekly]])
  - Segments: not measured
  - Other changes in that window: JobHarbor launched offline mode on all plans on 2026-10-07 (see [[jobharbor]])
  - What people did or said: a beta team said offline works in basements but a job closed offline showed up twice after sync (see [[2026-09-30-support-tickets-q3]])
- Week of 2026-11-09: [[weekly-active-technician-share]] 46.34% vs success 46.13% or more (Inference: 5,060 / 10,920; 41.13% + 5 points), ahead of the 2026-11-26 check date (see [[2026-11-17-metrics-weekly]])
- Guardrail: [[app-crash-rate]] 0.6% in the week of 2026-10-12, above 0.5%; 0.3% to 0.5% in the other five weeks. No crash data before 2026-10-05, so no pre-launch baseline (see [[2026-11-17-metrics-weekly]])
- Verdict at final review: not reviewed yet
- Next: none recorded

## Feedback

- Beta: works great in basements; one job closed offline showed up twice after sync (see [[2026-09-30-support-tickets-q3]])

## Contradictions

- Offline-sync tickets dropped in late September after the beta began, but beta teams were chosen from teams that complained, so the drop isn't evidence that offline mode worked (see [[2026-09-30-support-tickets-q3]]).
