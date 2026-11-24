---
type: problem
summary: "If Crewline sent the reminders for me, I'd pay more for it": owners wait weeks for invoices to be paid and chase them by phone
updated: 2026-11-24
state: current
as_of: 2026-11-17
---

# Owners wait too long to get paid

## Problem

Customers of field service firms pay invoices late. Owners track unpaid invoices themselves and chase them by phone, which takes time and delays cash (see [[2026-08-19-interview-mendez-plumbing]]).

## Who has it

- [[small-field-service-owner]]

## Evidence

- At Mendez Plumbing about a third of invoices sit unpaid more than 30 days; the owner tracks them in his own spreadsheet and they phone late payers every Friday (see [[2026-08-19-interview-mendez-plumbing]])
- Median days from invoice sent to paid was 19 at the start of Q3 and 17 in November, all teams (see [[2026-07-01-okrs-2026-q3]], [[2026-11-17-metrics-weekly]])
- Support examples: an owner asking how to send a reminder for an unpaid invoice; another asking for automatic late fees (see [[2026-09-30-support-tickets-q3]])
- 230 billing-question tickets in Q3; Lena Park estimates "maybe a third" are about chasing unpaid invoices, untagged (see [[2026-09-30-support-tickets-q3]])
- Reminders cut the median by 1.8 days in an A/B test, p = 0.08 (see [[2026-10-20-experiment-results-invoice-reminders]])
- Public: a survey says the median small field service business waits 22 days to be paid and 48% would pay more for software that gets them paid faster (see [[2026-09-10-fieldops-weekly-smb-technology-survey]])

## Size

As of: 2026-11-17

Evidence strength (counted from Evidence above; own evidence and public evidence counted apart):

- Own: 5 sources (interview, support report, Q3 goals, metrics export, experiment results); 1 account (Mendez Plumbing); segments: [[small-field-service-owner]]
- Public: 1 source (see [[2026-09-10-fieldops-weekly-smb-technology-survey]])
- First seen 2026-07-01, last seen 2026-11-17
- Kinds: interview, support ticket, analytics, survey

Magnitude (each line: value, range or unknown, then its basis):

- Reach: unknown share of teams. About 77 billing questions in Q3 may be about chasing payments (Inference: a third of 230)
  - Basis: team guess (Lena Park) (see [[2026-09-30-support-tickets-q3]])
- Frequency: weekly chasing at Mendez Plumbing; about a third of its invoices go past 30 days
  - Basis: stated by source (see [[2026-08-19-interview-mendez-plumbing]])
- Urgency: built a workaround
  - Basis: Mendez built a spreadsheet and phones late payers weekly; says he'd pay more for reminders (see [[2026-08-19-interview-mendez-plumbing]])
- Cost to them: delayed cash; median 17 to 19 days from invoice to paid
  - Basis: measured (see [[2026-10-06-metrics-weekly]], [[2026-11-17-metrics-weekly]])
- Cost to us: unknown
  - Basis: unknown

By segment: Same for all on record. The reminders test hinted Starter teams gain more than Team teams (2.6 vs 1.1 days), but it wasn't sized for that (see [[2026-10-20-experiment-results-invoice-reminders]]).

Biggest unknown: reach. Tagging billing questions about unpaid invoices for one month would size it cheaply.

## Current workarounds

- Owner's own spreadsheet and Friday phone calls (see [[2026-08-19-interview-mendez-plumbing]])
- Resending the whole invoice (see [[2026-09-30-support-tickets-q3]])
- [[fieldpilot]] includes automatic payment reminders on its Crew plan (see [[2026-10-14-fieldpilot-pricing-page]])

## Related features, experiments and decisions

- [[invoice-reminders]]
- [[invoice-reminders-ab-test]]
- [[ship-invoice-reminders-despite-test]]
- [[owners-get-paid-faster-2026-q3]]

## Contradictions

None.
