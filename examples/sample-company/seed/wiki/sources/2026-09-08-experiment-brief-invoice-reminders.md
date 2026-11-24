---
type: source
summary: Tom Becker's A/B test plan for automatic invoice reminders with a fixed decision rule: ship only if at least 3 days faster with p < 0.05
updated: 2026-11-24
raw: raw/2026-09-08-experiment-brief-invoice-reminders.md
raw_sha256: 34f13fd3d81c51eaae3ed0980ffe375ac565bf1278704adf032bc0af4bcd40f6
---

# Experiment brief: automatic invoice reminders

- **Kind:** other
- **Evidence:** own (from the team or its customers)
- **URL:** none
- **Date of source:** 2026-09-08
- **From:** Tom Becker, PM, Billing; analyst Raj Patel

## Summary

Tom Becker plans a 4-week A/B test (2026-09-15 to 2026-10-13) of automatic reminders sent 3, 7 and 14 days after an invoice, for Starter and Team teams that invoiced in August, split 50/50. Primary metric: median days from invoice sent to paid. Rule: ship if treatment is at least 3 days lower with p < 0.05; otherwise re-scope and test again. Guardrail: complaint rate must stay within 1%. Tom and Dan agreed the rule on 2026-09-08.

## Key points

- Decision rule: at least 3 days lower with p < 0.05, else re-scope, see [[invoice-reminders-ab-test]]
- Guardrail: complaint rate must stay within 1%, see [[reminder-complaint-rate]]
- 3 days chosen as noticeable to owners and more than halfway to the billing goal, see [[owners-get-paid-faster-2026-q3]]

## Quotes

None.

## Pages this source feeds

- [[invoice-reminders-ab-test]]
- [[invoice-reminders]]
- [[median-days-invoice-to-paid]]
- [[reminder-complaint-rate]]
- [[owners-wait-too-long-to-get-paid]]
- [[tom-becker]]
- [[raj-patel]]
