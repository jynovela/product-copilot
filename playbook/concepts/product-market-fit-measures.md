---
type: concept
summary: Tell whether you have product-market fit: pick research methods with Rohrer's attitudinal-behavioral grid, then use the Sean Ellis 40 percent test, NPS trends and, above all, the three parameters of the retention curve.
updated: 2026-11-24
knowledge_source: ingested
---

# Product-market fit measures

## What it is

Before launch you rely on qualitative research with prospective customers.
After launch, analytics and A/B tests add measurement at scale (Lean
Product Playbook ch13). This page covers how to choose a learning method
and which numbers show fit. Fit is defined in the
[[product-market-fit-pyramid]].

### Choosing a method: Rohrer's grid

Christian Rohrer's framework sorts research on two axes (ch13):

| | Qualitative | Quantitative |
| --- | --- | --- |
| **Behavioral** (what people do) | Usability tests | Analytics, A/B tests |
| **Attitudinal** (what people say) | User interviews | Surveys |

Qualitative tells you **why**; quantitative tells you **how many**. Olsen
calls them "Oprah versus Spock" (ch13). The usual order is qualitative
first, to learn which questions and answers matter, then quantitative, to
count them (ch13). For a v1, Oprah matters most; after launch, Spock helps
you optimize (ch13). Rohrer's full version adds a third dimension, context
of use: natural, scripted, or not using the product (ch13).

## When to use

- Deciding whether to invest in growth. Olsen and Sean Ellis both say don't
  grow until you have fit (ch13).
- Choosing between an interview, a survey, a usability test or analytics.
- Tracking whether each release improves fit.

## Steps

1. **Pick the method that fits the question.** Use behavioral data for
   questions about what people will do. A smoke test answers "would you use
   it?" more reliably than a survey (ch13).
2. **Run the Sean Ellis test once you have users.** Ask "How would you feel
   if you could no longer use [product]?": very disappointed, somewhat
   disappointed, not disappointed, or no longer use it. Products where 40
   percent or more say "very disappointed" tend to have fit; the threshold
   varies by category (ch13). Send it to a random sample of people who have
   used the product at least twice and recently, and follow up with "Please
   help us understand why you selected this answer" (ch13).
3. **Track NPS over time.** One NPS wave is only somewhat useful. The value
   is in the trend, which should rise as fit improves, and in an open "why"
   question. NPS reflects overall sentiment, so it also flags support or
   service problems (ch13). See [[net-promoter-score]].
4. **Build retention curves.** Retention rate is active customers divided
   by total customers, plotted against days, weeks or months since signup,
   not calendar dates (ch13). Read three parameters (ch13):
   - **Initial drop-off:** the share who never come back after day 1.
   - **Rate of descent:** how fast the curve falls after that.
   - **Terminal value:** where it flattens, if it does. A curve that falls
     to zero loses everyone.
   Stronger fit means a lower drop-off, a slower descent and a higher
   terminal value. Terminal value matters most: it is the share of people
   who tried the product and still use it in the long run (ch13).
5. **Compare cohorts.** Plot one curve per signup month. Fit is improving
   when newer cohorts flatten higher (ch13). Keep five curves or fewer on a
   chart, since cohort data is noisy (ch13).
6. **Split new from returning users.** Active-user growth can hide poor
   retention behind heavy acquisition. Retention rate is a pure measure of
   fit; returning-user counts mix in acquisition and conversion (ch13).

## Why retention is the best fit metric

Asked to pick one metric to measure fit, people suggest revenue or user
growth. Those can be the metric that matters most for a business, but
retention rate measures fit itself: people who value a product keep using
it (ch13). Olsen calls it the single best measure of fit (ch13).

## Surveys: what they can and can't do

- Good for simple questions people can answer from what they know:
  importance and satisfaction, feelings about your product and brand,
  perception against competitors, and repeated tracking surveys (ch13).
- Bad for predicting behavior. Asking a thousand people how likely they'd be
  to use "a new, easy-to-use photo-sharing app" gives them eight words to go
  on (ch13).
- Attitudinal answers often don't match behavior (ch13).
- Results change with question and answer wording, so survey design takes
  skill (ch13).
- Moderated tests inflate intent: nine of ten users saying they'd click
  doesn't mean a 90 percent conversion rate. Use an A/B test to measure the
  real effect (ch13).

## Good and bad signs

- Good: newer cohorts retain better than older ones (ch13).
- Good: every fit survey includes an open "why".
- Bad: fit judged by total active users or signups alone (ch13).
- Bad: a survey asks people to predict use of a product they've never seen
  (ch13).

## Pitfalls

- Spending on acquisition or conversion before retention shows fit (ch13).
- Reading a single NPS number without a trend or benchmark (ch13).
- Surveying the wrong users for the Ellis test, such as one-time visitors
  (ch13).

## Contradictions

- The vendor sources on [[net-promoter-score]] say NPS measures loyalty,
  while CSAT measures satisfaction (see
  [[2026-11-24-research-digest-metrics]]). Olsen calls NPS an attitudinal
  measure of satisfaction and a proxy for fit (ch13). Both agree it is
  attitudinal, so check it against retention.

## Pairs well with

- [[cohort-retention]]: building cohort tables
- [[metric-that-matters-most]]: what to improve after fit
- [[moderated-user-testing]]: the qualitative behavioral quadrant

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[goals-and-metrics]]
- [[startups-and-business-building]]
- [[discovery-and-customer-insight]]
