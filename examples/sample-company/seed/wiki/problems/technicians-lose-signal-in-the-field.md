---
type: problem
summary: "My guys lose signal in basements and crawl spaces every day": technicians can't see or close jobs without a connection
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Technicians lose signal in the field

## Problem

Technicians working in basements, crawl spaces and rural areas lose signal. Before offline mode, the app couldn't load job notes or close jobs without a connection, so technicians fell back to paper, the office re-typed it, and invoices went out late (see [[2026-08-25-prd-offline-mode]], [[2026-08-12-interview-brightline-hvac]]).

## Who has it

- [[field-technician]]
- [[small-field-service-owner]]

## Evidence

- Brightline HVAC's technicians lose signal in basements and crawl spaces every day and write notes on paper (see [[2026-08-12-interview-brightline-hvac]])
- Mendez Plumbing has never had an offline problem; they work above ground and walk outside if signal is bad (see [[2026-08-19-interview-mendez-plumbing]])
- 212 support tickets tagged offline-sync in Q3 2026, out of 1,240 (see [[2026-09-30-support-tickets-q3]])
- Example tickets: a technician lost all notes after two hours in a basement; jobs don't load past the county line (see [[2026-09-30-support-tickets-q3]])
- The PRD says support reports more than 300 offline tickets a quarter (see [[2026-08-25-prd-offline-mode]])
- Weekly offline sync errors averaged 1,886.6 in August (Inference: mean of 1,840, 1,902, 1,876, 1,925 and 1,890) (see [[2026-10-06-metrics-weekly]])
- Public: 31% of 412 surveyed small US field service businesses named poor connectivity as the top mobile app problem; sponsored survey, method not given (see [[2026-09-10-fieldops-weekly-smb-technology-survey]])

## Size

As of: 2026-11-17

Evidence strength (counted from Evidence above; own evidence and public evidence counted apart):

- Own: 4 sources (two interviews, the support report, the PRD) plus the metrics export; 1 account with the problem (Brightline HVAC) and 1 without (Mendez Plumbing); segments: [[small-field-service-owner]], [[field-technician]]
- Public: 1 source (see [[2026-09-10-fieldops-weekly-smb-technology-survey]])
- First seen 2026-08-12, last seen 2026-11-17
- Kinds: interview, support ticket, analytics, survey

Magnitude (each line: value, range or unknown, then its basis):

- Reach: unknown share of teams. 212 offline-sync tickets in Q3; tickets, not accounts
  - Basis: measured for tickets; unknown for accounts (see [[2026-09-30-support-tickets-q3]])
- Frequency: daily for Brightline HVAC's technicians; never for Mendez Plumbing
  - Basis: stated by source (see [[2026-08-12-interview-brightline-hvac]], [[2026-08-19-interview-mendez-plumbing]])
- Urgency: built a workaround
  - Basis: Mendez walks outside for signal; Brightline writes on paper and pays the office overtime to re-type, a higher step (paying for a workaround); the lower step is used (see [[2026-08-19-interview-mendez-plumbing]], [[2026-08-12-interview-brightline-hvac]])
- Cost to them: about five hours a week of office overtime at Brightline HVAC, and late invoices
  - Basis: stated by source (see [[2026-08-12-interview-brightline-hvac]])
- Cost to us: Brightline said it would look at other tools if offline didn't work by the fall; 212 support tickets in Q3
  - Basis: stated by source; measured for tickets (see [[2026-08-12-interview-brightline-hvac]], [[2026-09-30-support-tickets-q3]])

By segment: Inference: depends on where the work happens. Basement, crawl space and rural work (Brightline) hits it daily; above-ground residential work (Mendez) doesn't.

Biggest unknown: reach. The cheapest way to find out is to count distinct teams behind the offline-sync tickets, or teams with sync errors in the analytics warehouse.

## Current workarounds

- Paper work orders re-typed by the office: [[paper-and-phone-calls]] (see [[2026-08-12-interview-brightline-hvac]])
- Closing jobs from the truck after coming up; technicians forget (see [[2026-08-12-interview-brightline-hvac]])
- [[jobharbor]], offline on all plans from 2026-10-07 (see [[2026-10-20-jobharbor-release-notes]])

## Related features, experiments and decisions

- [[offline-mode]]
- [[approve-offline-mode-scope]]

## Contradictions

- Brightline HVAC has the problem daily (see [[2026-08-12-interview-brightline-hvac]]); Mendez Plumbing never has it (see [[2026-08-19-interview-mendez-plumbing]]). Urgency uses the lower step.
- The PRD says more than 300 offline tickets a quarter (see [[2026-08-25-prd-offline-mode]]); the support report counts 212 offline-sync tickets in Q3 (see [[2026-09-30-support-tickets-q3]]). The report is the measured number.
