---
type: concept
summary: What it costs to win a customer, what the customer is worth, and how long it takes to earn the cost back.
updated: 2026-11-24
knowledge_source: ingested
---

# Unit economics: CAC, LTV and payback

## What it is

Customer acquisition cost (CAC) is sales and marketing spend ÷ new customers. Lifetime value (LTV, CLV) has several formulas: average purchase value × frequency × lifespan; average monthly revenue ÷ churn rate for subscriptions; or (revenue − cost to serve) per period × periods retained. CAC payback is CAC ÷ (new MRR × gross margin), or the months to recover CAC (NetSuite, Stukan). (see [[2026-11-24-research-digest-metrics]])

## How to use it

- Segment CAC by channel; a blended average hides channels that lose money (Gupta, de Haaff). (see [[2026-11-24-research-digest-metrics]])
- Compare LTV to CAC: $100 CAC with $80 LTV loses money on every customer (Stukan). (see [[2026-11-24-research-digest-metrics]])
- Track net revenue retention (NRR) alongside MRR; new customers can mask losses in MRR (Gainsight, HubSpot). (see [[2026-11-24-research-digest-metrics]])
- Know where growth is expected to come from: new regions, a new product line, expansion revenue (Stukan). (see [[2026-11-24-research-digest-metrics]])

## Watch out for

- "LTV at least 3× CAC" is an unsourced rule of thumb repeated by Dovetail, HubSpot and Gupta. (see [[2026-11-24-research-digest-metrics]])
- LTV is computed on revenue by some sources and on profit by others; say which. (see [[2026-11-24-research-digest-metrics]])
- HubSpot annualizes 6.4% monthly churn as about 52% with the wrong formula; correct is 1 − 0.936^12, about 55%. (see [[2026-11-24-research-digest-metrics]])

## What Lean Product Playbook adds

- Profit per customer = customer lifetime value (LTV) − customer acquisition cost (CAC). LTV here is profit before acquisition cost (Lean Product Playbook ch13).
- LTV = ARPU × average customer lifetime × gross margin; average lifetime = 1 ÷ churn rate, so LTV = ARPU × gross margin ÷ churn rate. A 5 percent monthly churn means a 20-month lifetime (ch13).
- The two levers on LTV are raising ARPU (prices, upsell, higher-priced products) and cutting churn (service, quality, continuing to meet needs) (ch13).
- CAC = sales and marketing costs ÷ new customers, but the actionable form is CAC = cost per acquisition (per prospect) ÷ prospect conversion rate. Lower CPA with cheaper channels or better ads; raise conversion with better landing pages (ch13).
- Skip discounted-cash-flow LTV models; the aim is actionable metrics, not precision (ch13).
- Olsen repeats the SaaS guideline that LTV:CAC should exceed 3, also without a source (ch13).
- Use this view once you have fit and are working toward profit (ch13).

## Pairs well with

- [[cohort-retention]]: the input LTV depends on
- [[aarrr-pirate-metrics]]: CAC at acquisition, LTV at revenue

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[venture-deals]]
- [[the-startup-owners-manual]]

Ingested:

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[goals-and-metrics]]
- [[pricing-and-packaging]]
