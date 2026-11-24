---
type: concept
summary: Group users by when they started and track how many are still active over time; a flattening curve signals product-market fit.
updated: 2026-11-24
knowledge_source: ingested
---

# Cohort retention

## What it is

Group users by a shared start, such as signup week, and track the share still active in each later period. Retention by cohort = users retained in a period ÷ cohort size × 100; 100 January signups with 30 active in April is 30% three-month retention (Product School). A curve that flattens means a core group keeps using the product (Gupta). (see [[2026-11-24-research-digest-metrics]])

## How to use it

- Cut cohorts by signup date, channel, onboarding path or plan (Product School). (see [[2026-11-24-research-digest-metrics]])
- Time-box actions (for example first 30 days) to separate cause from later effect, and compare many features to avoid cherry-picking (Murray; see [[2026-11-24-research-digest-experiments]]).
- Count users, not accounts, in B2B, where accounts have many users (Gainsight). (see [[2026-11-24-research-digest-metrics]])
- Track it from day one, because retention "can't be faked" (Gupta). (see [[2026-11-24-research-digest-metrics]])

## Watch out for

- Avoid "people who do X retain more" claims; that is correlation (Murray; see [[2026-11-24-research-digest-experiments]]).
- Retention formulas differ between sources: (end − new) ÷ start vs active ÷ total users. Define it once. (see [[2026-11-24-research-digest-metrics]])

## What Lean Product Playbook adds

- Measure by relative days since signup, not calendar dates (Lean Product Playbook ch13).
- Read three parameters of each curve: initial drop-off (who never returns after day 1), rate of descent, and terminal value (where it flattens). Better fit means lower drop-off, slower descent and a higher terminal value; terminal value matters most (ch13).
- Initial drop-off varies by category; mobile apps drop steeply because people forget them without a trigger such as a notification (ch13).
- Store cohorts as a table: one row per signup month, initial users, then active users by months since signup. Divide by initial users to get each cell's retention rate (ch13).
- Fit is improving when each newer cohort's curve sits higher. Keep five or fewer curves on one chart (ch13).
- Olsen calls retention rate the single best measure of product-market fit (ch13). See [[product-market-fit-measures]].

## Pairs well with

- [[unit-economics]]: retention drives LTV
- [[product-market-fit-pyramid]]: a flat curve is the usual fit signal

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[product-analytics-for-dummies]]
- [[the-lean-startup]]

Ingested:

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[goals-and-metrics]]
