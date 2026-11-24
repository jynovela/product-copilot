---
type: concept
summary: Five layers of product-market fit (target customer, underserved needs, value proposition, feature set, UX), the six-step process that climbs them, and how to iterate or pivot.
updated: 2026-11-24
knowledge_source: ingested
---

# Product-market fit pyramid

## What it is

Product-market fit means your product meets real customer needs better than
the alternatives, so it creates significant customer value (Lean Product
Playbook ch1). Olsen keeps it separate from a working revenue model or a
cheap acquisition channel: you must create value before you can capture it,
and calling fit "profitable" blurs the idea (ch1).

The pyramid breaks fit into five layers, each resting on the one below
(ch1):

| Layer | Section | Space |
| ----- | ------- | ----- |
| 5. User experience (UX) | Product | Solution |
| 4. Feature set | Product | Solution |
| 3. Value proposition | Product | Problem |
| 2. Underserved needs | Market | Problem |
| 1. Target customer | Market | Problem |

- The **market** is all the existing and potential customers who share a
  need or set of related needs, whatever solution they use today (ch1).
- **Underserved needs** are the ones current solutions don't meet well.
  Avoid markets where customers are very happy with what they have (ch1).
- The **value proposition** is the set of needs you aim to meet, and how you
  will be better than the alternatives. This is product strategy (ch1).
- The **feature set** is the functionality, each feature built for a need;
  the **UX** is what brings it to life for the user (ch1).

Fit is how well the top three layers satisfy the bottom two, judged by the
target customers against the other products they could use (ch1). The value
proposition is the problem-space layer you control most: you can choose
customers and needs but not change them (ch2). See
[[problem-vs-solution-space]].

## When to use

- Building a new product, a v2, or a redesign.
- Adding a feature: treat it as a "minimum viable feature" and run the same
  steps (ch1).
- Feedback is poor and you need to find which assumption is wrong (ch10).

## Steps

The Lean Product Process climbs the pyramid from the bottom (ch1):

1. Determine your target customer ([[target-customer-and-personas]]).
2. Identify underserved needs ([[customer-benefits]],
   [[opportunity-scoring]]).
3. Define your value proposition ([[value-proposition-grid]]).
4. Specify your MVP feature set ([[mvp-feature-set]]).
5. Create your MVP prototype ([[mvp-test-matrix]], [[ux-design-iceberg]]).
6. Test your MVP with customers ([[moderated-user-testing]]).

Steps 1 to 3 are mostly for a new product. After v1, you keep looping
through steps 4 to 6 (ch1). The process works as a checklist: any
assumption you don't make explicitly, you make implicitly (ch1).

### Iterate: hypothesize, design, test, learn

Olsen relabels build-measure-learn (ch10):

1. **Hypothesize.** Start from problem-space hypotheses; you need them to
   know what to build.
2. **Design.** Make the cheapest artifact that tests them. It doesn't have
   to be built; clickable wireframes count.
3. **Test.** Show it to customers. Qualitative results count as measuring.
4. **Learn.** Draw lessons, then revise the hypotheses and go round again.

Your speed is set by how fast you design and test, since learning and
hypothesizing are quick (ch10).

For each finding, name the pyramid layer it belongs to and fix the lowest
layer first. A UX fix is cheap. A wrong value-proposition assumption forces
changes to the feature set and the UX above it (ch10).

### Track progress across waves

After each test wave, count how many users raised each issue, as a
percentage, grouped by feature set, UX and messaging (ch10). Progress looks
like issues dropping to zero, new issues getting smaller and fewer, and
median value and ease-of-use ratings rising (ch10). Then move up in
fidelity: wireframes, then mockups, then the live product. Test the live
product again, since what people do beats what they say they'd do (ch10).

### Persevere or pivot

A pivot changes a main hypothesis, such as the target customer or the
value proposition's differentiators. A UX tweak is not a pivot (ch10).

1. If several waves bring no gain, stop and list every possible cause.
2. Map each cause to a pyramid layer. Start at the bottom and work up until
   you find the wrong hypothesis. Iterating on UX can't fix a wrong target
   customer (ch10).
3. Consider pivoting when target customers stay lukewarm, or no customer
   type is very excited about the MVP (ch10).
4. Look for the pivot in your test results: a minor part of the value
   proposition that resonates most, or a submarket that loves one aspect
   (ch10).
5. Weigh the time and money left. Startups and internal projects both have
   limits (ch10).

Picture each opportunity as a mountain: measure your rate of climb per
wave, try other paths when it slows, then look for a taller mountain
(ch10).

## Good and bad signs

- Good: each hypothesis is written down and tied to a layer.
- Good: issues fall wave over wave and ratings climb (ch10).
- Bad: the team can't name the target customer or the differentiators.
- Bad: endless UX tweaks while feedback stays lukewarm.

## Pitfalls

- Starting at the feature layer without a clear target customer.
- Pivoting at every rough patch ("shiny object syndrome"). Three pivots can
  leave you facing the opposite way (ch10).
- Never stepping back, and banging your head against the same wall (ch10).
- Testing design artifacts long past the point of learning, or launching
  before you've validated enough. There is no fixed rule for "enough"
  (ch10).
- Salvaging the old build after a pivot in the lower layers. Rebuild on the
  new foundation instead (ch14).

## Contradictions

- [[build-measure-learn]] (Lean Startup) starts the loop with "build" and
  measures with metrics. Olsen starts with "hypothesize", says "design"
  need not mean building, and counts qualitative tests as measuring (ch10).
- Olsen defines fit as customer value alone. Some growth sources, such as
  [[a-dozen-lessons-on-growth]], tie it to retention and economics. Olsen
  treats those as business metrics to optimize after fit (ch1, ch13).

## Pairs well with

- [[four-product-risks]]: value and usability risk map to the middle and top
  layers
- [[product-market-fit-measures]]: how to tell when you have fit
- [[cohort-retention]]: the best fit signal after launch

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)
- [[a-dozen-lessons-on-growth]]

## Topics

- [[discovery-and-customer-insight]]
- [[startups-and-business-building]]
