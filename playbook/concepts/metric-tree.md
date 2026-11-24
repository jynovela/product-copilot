---
type: concept
summary: Write the goal as a formula of its drivers, then break each driver down again, so you know which lever to pull.
updated: 2026-11-24
knowledge_source: ingested
---

# Metric tree

## What it is

Treat the company as a machine with outputs and levers, and write each end goal as a formula of its components, then repeat ("peel the onion") (David Skok). For example: bookings = deals closed × average deal size; deals closed = trials × conversion rate; trials = site visitors × conversion to trial. Alex Alwan's goal tree and the driver tree in [[2026-11-24-research-digest-goals]] are the same idea drawn top-down, with proxy metrics at the user-experience touchpoints. (see [[2026-11-24-research-digest-metrics]])

## How to use it

- For every funnel stage, track volume through the stage and conversion to the next, over time (Skok). (see [[2026-11-24-research-digest-metrics]])
- Grow linked levers together; too many salespeople with too few trials throws the machine out of balance (Skok). (see [[2026-11-24-research-digest-metrics]])
- Don't track components you can't affect, or that are small or don't vary (Skok). (see [[2026-11-24-research-digest-metrics]])
- Work back from a target to the salespeople, leads and spend it needs (Skok). (see [[2026-11-24-research-digest-metrics]])
- Phrase proposals as a causal chain: "By improving this user behaviour, we expect to raise LTV for this segment, which supports our 10% revenue growth goal" (Stukan's Metrics One Pager). (see [[2026-11-24-research-digest-metrics]])

## Watch out for

- Skok's model is written for sales-led SaaS; consumer products need different levers. (see [[2026-11-24-research-digest-metrics]])
- Every link is a hypothesis; mark the ones you haven't checked. (see [[2026-11-24-research-digest-metrics]])

## What Lean Product Playbook adds

Olsen calls this "the equation of your business" and "peeling the analytics onion" (Lean Product Playbook ch13):

- Start from profit = revenue − cost. High-tech products usually focus on revenue, because marginal cost per extra user is near zero (ch13).
- Break revenue down per user: revenue = users × average revenue per user (ARPU) (ch13).
- **Advertising model:** revenue per visitor = impressions per visitor × effective CPM ÷ 1,000; impressions per visitor = visits per visitor × pageviews per visit × impressions per pageview (ch13).
- **Subscription model:** paying users = new paying users + repeat paying users; repeat paying users = last period's paying users × (1 − cancellation rate); new paying users = free trial users × trial conversion rate + direct paid signups (ch13).
- Split visitors into new and returning. Returning visitors = last period's visitors × return rate, and the return rate is the lever (ch13).
- Each equation applies to one time period. Its purpose is to show how much a change in each metric moves the result, so you can prioritize (ch13). Use it to choose the [[metric-that-matters-most]].

## Pairs well with

- [[north-star-framework]]: the top of a product metric tree
- [[leading-and-lagging-indicators]]: the tree shows which is which
- [[impact-mapping]]: a similar goal-to-work tree

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[measure-what-matters]]
- [[the-insights-driven-product-manager]]

Ingested:

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[goals-and-metrics]]
