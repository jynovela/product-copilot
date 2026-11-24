# Results: automatic invoice reminders test

- Analyst: Raj Patel
- Date: 2026-10-20
- Test: 2026-09-15 to 2026-10-13, as planned in Tom's brief of 2026-09-08

## Who was in it

| Group | Teams | Invoices sent during test |
| ----- | ----- | ------------------------- |
| Control | 412 | 9,830 |
| Treatment | 409 | 9,615 |

## Primary metric

Median days from invoice sent to invoice paid.

| Group | Median days |
| ----- | ----------- |
| Control | 19.0 |
| Treatment | 17.2 |

Difference: 1.8 days lower in treatment. p = 0.08.

## Guardrail

Complaint rate in treatment: 0.4% of the owners' customers who got a
reminder.

## Other things we saw

- 61% of treatment teams left reminders on for the whole test; 39% turned
  them off at some point. We didn't ask why.
- Starter teams improved more than Team plan teams (2.6 days vs 1.1 days),
  but the test wasn't sized to compare plans, so treat that as a hint.
- 4 weeks may be too short. Invoices sent in the last week had little time
  to be paid.

## Readout

The result didn't meet the ship threshold in the decision rule (at least 3
days, p < 0.05).
