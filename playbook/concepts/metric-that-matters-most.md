---
type: concept
summary: After launch, pick the one AARRR metric with the best return right now (usually retention, then conversion, then acquisition) and improve it with Olsen's Lean Product Analytics Process.
updated: 2026-11-24
knowledge_source: ingested
---

# Metric that matters most

## What it is

At any moment, one of the five AARRR macro-metrics (acquisition,
activation, retention, revenue, referral) offers the best return on effort
for improving the business. Olsen calls it the **metric that matters most**
(MTMM) (Lean Product Playbook ch13). It changes over time because of
diminishing returns: the easy wins go first, and after enough progress
another metric offers more (ch13).

The **Lean Product Analytics Process** is the loop for improving it (ch14):

1. Define your key metrics.
2. Measure a baseline for each.
3. Estimate each metric's upside potential.
4. Select the MTMM.
5. Brainstorm improvement ideas and estimate the effect of each.
6. Pick the highest-ROI idea, then design and build it.
7. Test it, ideally with an A/B test.
8. Learn, then go back to step 5. When ideas for this metric run out,
   return to step 3.

## When to use

- After launch, once you have users and analytics (ch13).
- The team disagrees about whether to work on growth, conversion or
  retention.
- A metric has stopped improving despite effort.

## Steps

### 1. Define the metrics

Track two or three micro-metrics under each macro-metric (ch13). Olsen's
"conversion" (prospect becomes customer) is a narrower version of
McClure's "activation" (ch13). Prefer normalized ratios, such as the share
of users who send invites, over raw counts that rise and fall with the size
of the user base (ch14). Break the top-level goal into drivers with the
equation of your business; see [[metric-tree]].

### 2. Choose the MTMM, usually in this order

- **Retention first.** It is the metric closest to product-market fit.
  Until customers keep using the product, spending on acquisition or
  conversion has little effect and takes time from what matters (ch13).
- **Conversion next.** With fit shown, get more of the people who arrive to
  sign up, so later acquisition spend pays off better (ch13).
- **Then acquisition.** Try new channels, segments, messages, prices and
  promotions as small experiments, and scale the ones that work (ch13).
- **Revenue before acquisition** if acquisition is paid and expensive.
  Knowing what each customer brings in lets you spend on acquisition with
  confidence. If acquisition is free, such as viral or organic, work on it
  separately from revenue (ch13).

### 3. Estimate upside potential

Picture each metric on a diminishing-returns curve of value against
effort. A metric you haven't worked on is often on the steep part; one
you've already optimized is on the flat part. Rare "silver bullets" give
big gains for little effort (ch14). When you can't estimate returns, use
upside potential: (maximum possible value − current value) ÷ current value
(ch14). A conversion rate at 85 percent can rise at most 18 percent; a
share at 15 percent can rise about 570 percent (ch14). Also prefer metrics
you can move without changing people's behavior: it's easier to get
people who already do something to do more of it than to convert people
who've chosen not to (ch14).

### 4. Run the improvement loop

- Write each idea as a hypothesis with a number: "a mobile-optimized
  registration page will lift conversion from 20 to 30 percent" (ch14).
- Estimate effort and rank by ROI ([[mvp-feature-set]]) (ch14).
- Build the smallest chunk that tests the idea, such as one email provider
  first (ch14).
- Use an A/B test. A before-and-after comparison works only if the metric
  has been stable, and is riskier (ch14). Use trailing seven-day averages
  to smooth weekday swings (ch14).
- A miss still teaches you something for better hypotheses (ch14).

### Viral loops

For viral products, map the loop from active users to invites to signups,
and track each step as a ratio. Multiplying the ratios gives the viral
coefficient. Above 1, each user brings more than one new user; below 1 but
high, such as 0.4, is still large free growth (ch14). No product stays
viral for long, because the pool of prospects shrinks (ch14).

## A/B testing in this process

- Significance rises with bigger differences and bigger samples. Close
  results need very large samples (ch7, ch14).
- **Throttling:** release a major change to a small share of users, check
  that target metrics improve and others don't get worse, then ramp up
  (ch14).
- **Avoid a local maximum.** Testing 41 shades of a button won't find the
  better page layout. Cast a wide net for ideas (ch14).
- **You can't A/B test your way to fit.** Launching an MVP and optimizing it
  will most likely lead to an inferior local maximum. Target customer,
  needs and value proposition need qualitative work: qualitative defines
  the product, quantitative optimizes it (ch14).

## Good and bad signs

- Good: the team can name the MTMM and why it beats the others now.
- Good: dashboards show every metric over time with a baseline (ch14).
- Bad: buying traffic while retention curves fall toward zero.
- Bad: the analytics data hasn't been checked against what you meant to
  track. Instrumenting takes real work (ch14).

## Pitfalls

- Optimizing one metric past diminishing returns (ch13).
- Tracking raw counts instead of ratios (ch14).
- Testing only small variations of one design (ch14).
- Skipping qualitative research once A/B testing is available (ch14).

## Contradictions

- [[aarrr-pirate-metrics]] notes that Reforge calls the stages too siloed
  (see [[2020-05-07-built-in-aarrr-metrics]]). Olsen focuses on one stage at
  a time, but checks that other key metrics don't get materially worse
  before rolling a change out (ch14).
- [[north-star-framework]] keeps one metric for the long run. Olsen's MTMM
  moves on purpose as returns diminish (ch13).

## Pairs well with

- [[product-market-fit-measures]]: retention as the first MTMM
- [[ab-testing]]: running the tests well
- [[unit-economics]]: when revenue comes before acquisition
- [[ice-scoring]]: another way to rank growth ideas

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[goals-and-metrics]]
- [[product-experimentation]]
