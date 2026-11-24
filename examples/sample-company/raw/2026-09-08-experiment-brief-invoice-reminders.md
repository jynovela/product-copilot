# Experiment brief: automatic invoice reminders

- Owner: Tom Becker (PM, Billing)
- Analyst: Raj Patel
- Written: 2026-09-08
- Runs: 2026-09-15 to 2026-10-13 (4 weeks)

## Assumption we're testing

If Crewline sends payment reminders to the owner's customers automatically,
invoices get paid faster.

## Design

A/B test. Teams on Starter and Team plans that sent at least one invoice in
August are split 50/50 at random. Treatment teams get reminders turned on:
an email to their customer 3, 7 and 14 days after the invoice is sent, from
the business's name. Control teams see no change.

## Metric and decision rule

- Primary metric: median days from invoice sent to invoice paid, for
  invoices sent during the test.
- Ship if the treatment median is at least 3 days lower than control, with
  p < 0.05.
- Otherwise, don't ship as is. Re-scope and test again.
- Guardrail: complaint rate (the owner's customers who mark a reminder as
  spam or ask to stop) must stay within 1%.

Decision rule agreed by Tom and Dan on 2026-09-08. It doesn't change once
the test starts.

## Why 3 days

That is the change Tom thinks owners would notice, and it gets the billing
goal (19 to 14 days) more than halfway there.
