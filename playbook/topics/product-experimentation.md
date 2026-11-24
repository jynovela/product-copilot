---
type: topic
summary: Testing product ideas and changes: hypotheses, test types from fake doors to A/B tests, statistics, biases and what to do with results.
updated: 2026-11-24
knowledge_source: ingested
---

# Product experimentation

## What this covers

How to test whether an idea is worth building and whether a built change works: hypotheses, the ladder of test types, experiment design and statistics, the biases that fake results, and how to decide after a test. It condenses about 47 pieces from product, vendor, lab-science and peer-reviewed sources; the full detail is in [[2026-11-24-research-digest-experiments]].

In this wiki, each test of an assumption is an experiment page; its metrics and decision rule lock once it is running, and the outcome follows the rule.

## Core ideas

- Write the hypothesis, metrics and success criteria before the test, and don't change them during it (see [[2026-11-24-research-digest-experiments]]).
- Match the test to the question and the stage: cheap demand tests first, controlled experiments when traffic allows (see [[2026-11-24-research-digest-experiments]]).
- Use a randomized control for causal claims; everything else is directional (see [[2026-11-24-research-digest-experiments]]).
- A successful experiment is one that gives a clear, actionable read, whether or not it confirms the hypothesis (see [[2026-11-24-research-digest-experiments]]).
- An experiment informs a human decision; sources disagree on whether it should make it (see [[2026-11-24-research-digest-experiments]]).

## Books

- [[the-lean-startup]]: The Lean Startup
- [[designing-with-data]]: Designing with Data
- [[the-lean-product-playbook]]: The Lean Product Playbook
- [[how-to-lie-with-statistics]]: How to Lie with Statistics
- [[continuous-discovery-habits]]: Continuous Discovery Habits

## Concepts

- [[hypothesis-statement]]: the testable prediction
- [[experiment-design-doc]]: the one-page plan with the decision rule
- [[pretotyping]]: cheap demand tests before building
- [[fake-door-test]]: measure interest in something that doesn't exist yet
- [[concierge-and-wizard-of-oz]]: deliver the value by hand first
- [[minimum-viable-product]]: the smallest thing that tests the idea
- [[ab-testing]]: randomized controlled online experiments
- [[sample-size-and-power]]: significance, power, minimum detectable effect
- [[peeking-and-sequential-testing]]: when you may look at results
- [[staged-rollout]]: canary releases and feature flags
- [[primary-secondary-guardrail-metrics]]: what to measure
- [[statistical-traps]]: ways numbers mislead
- [[build-measure-learn]]: the loop experiments run inside
- [[mvp-test-matrix]]: the 2x2 of MVP tests
- [[metric-that-matters-most]]: improve one metric at a time with A/B tests
- [[product-kata]]: Perri's six questions from goal to learning, then explore, experiment and build until the goal is met

## Framework catalog

Section numbers point into [[2026-11-24-research-digest-experiments]].

### Processes (section 2.1)

| Process | Steps in short |
| ------- | -------------- |
| Product School, 6 steps | Goal, hypothesis, metrics and guardrails, design, run without peeking, analyse |
| Flagsmith, 5 steps | Hypothesis, metrics, sample size, run, analyse against pre-agreed criteria |
| Department of Product (Holmes) | Ideas backlog, if-then hypothesis, conduct, communicate, prioritize results like other work |
| Simon Cast's cycle | Plan, implement, monitor, act (compared with OODA) |
| Contentsquare, 6 steps | Goal from 5 components, hypothesis, 1 to 3 metrics, parameters, run, 5 post-test checks |
| Planio, 4 steps | Ask the right questions, 4-part hypothesis, conduct and monitor, communicate and act |
| Ben Smith, 4 steps | Hypothesis with null, minimal viable test, one success metric, decide and communicate |
| LaunchDarkly lifecycle and 6-stage checklist | Problem library to rollout; fix the audience percentage upfront |
| GrowthBook, 7 steps | Goal, metrics, baseline and variance, leading vs lagging, randomization, A/A test, duration |
| Statsig, 3 phases | Design document, monitoring, readout |
| DevCycle, 4 steps | PM brief, engineering setup, random rollout, 1 to 2 weeks minimum |
| Mastercard test and learn | Matched controls for business moves; pipeline scored on feasibility, impact, decision focus, fit |
| Google's four steps | Hypothesis, metric and action per outcome before launch, audience, respond |
| Longden's horse race | Smallest testable assumption, cheapest test, promising ideas earn bigger tests |
| Science processes | Scribbr, Six Sigma, Explorable, Bibikova, PLOS 10 simple rules |

### Test types, lightest to heaviest (section 2.3)

- Research and qualitative: customer interviews, surveys, usability tests, prototype tests, community building, click and funnel analysis, cohort analysis (see [[2026-11-24-research-digest-experiments]]).
- Demand tests (pretotypes): email, paid-ad and social campaigns, landing page, fake door, facade, Pinocchio, explainer video, pre-order, letter of intent, provincial launch, pop-up, infiltrator, crowdfunding (see [[2026-11-24-research-digest-experiments]]).
- Minimal products: piecemeal or mash-up, concierge, Wizard of Oz, single-feature product, minimum viable experiment (see [[2026-11-24-research-digest-experiments]]).
- Controlled online experiments: A/B, multivariate, funnel experiments, canary or staged rollout, beta programmes, feature flags, bandits and personalization, A/A tests, holdouts and backtests, pre/post (last resort), split URL tests (see [[2026-11-24-research-digest-experiments]]).
- Business and marketing experiments: test and learn with matched controls, synthetic control, analytical modelling; Google's Brand Lift, Conversion Lift, geo experiments and causal-impact analysis (see [[2026-11-24-research-digest-experiments]]).
- Scientific designs: completely randomized, randomized block, factorial, fractional factorial, response surface, split-plot, between vs within subjects, quasi-experiments (see [[2026-11-24-research-digest-experiments]]).
- ML experiments: model selection, feature engineering, hyperparameter tuning, data augmentation; one change at a time against a baseline (see [[2026-11-24-research-digest-experiments]]).

### Deciding when to test (sections 2.4, 2.5)

- Huryn's ladder: pretotypes, then minimal products, then prototypes, then production experiments (see [[2026-11-24-research-digest-experiments]]).
- Valerie Kroll's 10 situations where experiments add value, from stakeholder disagreement to piloting a third-party tool (see [[2026-11-24-research-digest-experiments]]).
- Megan Moore's four traits of high-impact experiments (high uncertainty, conflicting opinions, random exposure, measurable outcome) and four cases to skip (obvious fixes, low-impact changes, time-sensitive launches, no metric or too few users) (see [[2026-11-24-research-digest-experiments]]).
- If detecting a 1% lift would take four months, test a bigger change, a more sensitive metric, a narrower audience, or use another method (see [[2026-11-24-research-digest-experiments]]).

### Statistics and validity (section 2.6)

Sample size inputs, fixed-horizon vs sequential testing, health checks, Planio's four invalidators (overlapping tests, small audiences, stopping early, external events), ratio-metric traps, false-positive control, segmenting results, and the three design principles of randomization, blocking and replication (see [[2026-11-24-research-digest-experiments]]).

### Biases (section 2.7)

Anchoring, confirmation, default effect, bias blind spot, biased outlier removal, allocation, attrition, confounding, immortal time, recall, publication, self-selection, test-vs-control bias, survivorship, HiPPO. Questionable research practices: low power, pseudo-replication, repeated looks, p-hacking, selective reporting, HARKing. Remedies: preregistration, protocols, open data, independent analyst review (see [[2026-11-24-research-digest-experiments]]).

### After the test (section 2.8)

Decide ship, iterate, kill or re-scope; plan the action for every outcome before launch; Contentsquare's 5 post-test checks; Conversion.com's four-part review (data, hypothesis, execution, externalities); for a flat result ask whether the hypothesis, change, audience or metric was wrong; delete losing code and short-lived flags (see [[2026-11-24-research-digest-experiments]]).

### Principle lists and templates (sections 2.9 to 2.11)

Conversion.com's 9 principles; Product School's five ingredients; Planio's five components; Strategyzer's two levers for strong evidence (right participants, well-crafted artefact); Murray's practices for data teams; Ben Smith's checklist; Simon Cast's test-well rules; PostHog's six practices and launch checklist; LaunchDarkly's 9 practices; design docs from Product HQ, Statsig, DevCycle and Google; culture advice from Mixpanel, LaunchDarkly, Planio and Flagsmith (see [[2026-11-24-research-digest-experiments]]).

## Practices most sources agree on

Each appears in five or more independent sources (see [[2026-11-24-research-digest-experiments]]):

1. Write the hypothesis before the test.
2. Set metrics and success criteria before launch and don't change them.
3. One primary metric, plus guardrails and a few secondary metrics.
4. Use a randomized control group for causal claims.
5. Calculate sample size and duration upfront.
6. Don't stop early because a number looks good.
7. Run at least a full weekly cycle.
8. Change one thing at a time when you need to know the cause.
9. Check the setup before trusting results.
10. Treat negative and flat results as learning, and record them.
11. Keep a log of every experiment.
12. Match the method to the question and stage.
13. Tie every experiment to a goal.
14. Segment the results.
15. Pair numbers with qualitative evidence.
16. Avoid overlapping tests on the same users.
17. Log deviations from the plan.

## Contradictions

- What counts as an experiment: a controlled change with a control group (Product School, Flagsmith, Huryn) vs any structured test including interviews (Mind the Product, Longden) (see [[2026-11-24-research-digest-experiments]]).
- Qualitative first or A/B first: Rosemary King vs Terry Lee in the same Mind the Product article (see [[2026-11-24-research-digest-experiments]]).
- Peeking: never look vs sequential testing; compatible if chosen upfront (see [[2026-11-24-research-digest-experiments]]).
- How long to run: at least a week, 1 to 2 weeks, sample size over time, or 7 to 56 days tied to conversion lag (see [[2026-11-24-research-digest-experiments]]).
- How many metrics: one, 1 to 2, 2 to 3, or up to 3; Statsig groups guardrails inside "primary" (see [[2026-11-24-research-digest-experiments]]).
- Shipping without top-line significance: done at X on engagement metrics vs "if the launch criteria are not met, don't ship" (Statsig) (see [[2026-11-24-research-digest-experiments]]).
- Who decides: "implement the results no matter what" (Planio) vs data as one input to a human decision (Longden, Flagsmith, PMA) (see [[2026-11-24-research-digest-experiments]]).
- Small or bold changes: small reduces risk vs bold avoids local maxima (see [[2026-11-24-research-digest-experiments]]).
- Concierge vs Wizard of Oz: the same thing (Product School) vs different by whether users know (Huryn) (see [[2026-11-24-research-digest-experiments]]).
- Pre/post comparisons: counted as experimenting (Product School) vs directional only or not recommended (Planio, Google, GrowthBook) (see [[2026-11-24-research-digest-experiments]]).
- Significance as a gate: 95%, raised for high risk, vs report exact p-values and use p < 0.005 for novel claims (PLOS) (see [[2026-11-24-research-digest-experiments]]).
- Test everything vs test selectively (see [[2026-11-24-research-digest-experiments]]).

## Numbers to treat with care

"Only 10 to 30% of experiments produce a clear winner" is a GrowthBook claim; "for every experiment that succeeds, nearly 10 don't" is Thomke in HBR; "Booking.com runs over 1,000 A/B tests every day" is unsourced and likely wrong (usually reported as about 1,000 concurrent). Product School's "60% to 68%, a significant +8% lift" is +8 points, about +13% relative. The full flagged table is section 5 of the digest (see [[2026-11-24-research-digest-experiments]]).

## Questions to ask about your product

- Which experiment pages are running, and was each one's decision rule written before it started?
- Which assumptions behind our current bets have no experiment yet? Check problem and feature pages for untested claims.
- Do we have the traffic for an A/B test on this change, or should it be a fake door, concierge test or staged rollout?
- What will we do for each possible result, and who decides?
