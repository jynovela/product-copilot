---
type: concept
summary: Reach an outcome goal with Perri's Product Kata: six questions from goal to learning, then problem exploration, build-to-learn solution experiments with a pass-or-fail ask, and building until the goal is met.
updated: 2026-11-24
knowledge_source: ingested
---

# Product kata

Source note: this page comes from two secondary summaries of *Escaping the
Build Trap*, not the book text. Chapter numbers are the book's. Check
details against the book before quoting them.

## What it is

Melissa Perri's process for getting from a goal to the right solution. It
adapts Toyota's Improvement Kata, documented by Mike Rother: set a target
condition, find the obstacle in the way, plan, experiment, check the
result, and act on it in the next round (Build Trap ch12). The Product
Kata keeps the team in love with the problem rather than a solution, and
the team keeps iterating until it reaches the outcome (ch15).

The direction comes from the level above: the vision, a strategic intent
or a product initiative (ch15). See [[strategy-deployment]]. The current
state is where the outcome measures stand today. An **option goal** is the
next outcome the team must reach to move the initiative forward (ch15).

The six questions (ch15):

1. What is the goal?
2. Where are we now in relation to it?
3. What is the biggest problem or obstacle in the way?
4. How will we try to solve it?
5. What do we expect to happen? (the hypothesis)
6. What actually happened, and what did we learn?

The answer to question 6 feeds question 2 of the next round.

## When to use

- A team has an outcome goal and needs to decide what to build.
- A team is jumping from a goal straight to a feature.
- Reviewing a team's work: the six questions make a simple status
  format.

## Steps

### 1. Understand the direction and set metrics

Pick metrics that show product and business health (ch16). Avoid vanity
metrics; adding a time frame makes a count actionable ("more users than
last month, and what did we change?") (ch16). Output measures such as
features shipped or story points are productivity metrics, not product
metrics (ch16). Perri's favorite frameworks are [[aarrr-pirate-metrics]]
and [[heart-framework]] (ch16). Retention is lagging, so steer by leading
measures such as activation, happiness and engagement (ch16). See
[[leading-and-lagging-indicators]].

### 2. Explore the problem

- Talk to customers. Analytics show what happens, not the whole story
  (ch17).
- Problem research is generative: its job is to find the problem worth
  solving, through interviews, observation, surveys and feedback (ch17).
- Find the pain point and its root cause. Ask, for example, "What is the
  biggest problem standing in the way of you finishing?" (ch17). See
  [[five-whys]].
- Don't define the problem as a missing feature (ch17).
- Kill bad ideas before the team gets attached to them (ch17).

### 3. Explore solutions: build to learn

Companies confuse building to learn with building to earn. Experiments
build to learn: they test a hypothesis as fast as possible and are not
meant to last (ch18). The point of an MVP is the learning, at the least
effort (ch18).

Three solution experiments (ch18):

- **Concierge:** deliver the result by hand; the customer knows. Fast, no
  code, tight feedback, but doesn't scale.
- **Wizard of Oz:** looks like a real product, run by hand behind the
  scenes. Reaches more people; can be combined with an A/B test.
- **Concept test:** show a landing page, wireframe, prototype or video and
  ask how it would or wouldn't solve the problem. On its own it is
  generative.

To make a concept test evaluative, set a pass-or-fail **ask**: something
the customer gives up, such as a commitment, money or time (ch18). A
landing page's email signup is an ask. See [[concierge-and-wizard-of-oz]]
and [[fake-door-test]].

Skip A/B tests when you are still unsure of the solution direction or
lack the traffic for significance; use concept tests then (ch18).

Plan how each experiment ends ("close the loop"), and tell participating
customers why you're testing, when and how it ends, and what comes next
(ch18). Apply the same rigor to internal tools (ch18).

### 4. Build and optimize

- Don't invent solutions for things outside your core value proposition.
  Copy the known best practice, measure it, and iterate. Save effort for
  what makes or breaks the value proposition (ch15).
- Align on the vision with a **North Star document**: the problem, the
  proposed solution, the factors that matter for success and the expected
  outcomes. It gives context, not an action plan, and evolves as you
  learn (ch19). Break down the work with a [[story-map]] (ch19).
- Order releases with [[cost-of-delay]]: weigh the value a scope captures
  against the time it takes to ship (ch19).
- **Done means the goal is met,** not that version 1 shipped (ch19).

Then return to question 2.

## Good and bad signs

- Good: the team can say which kata question it is on and which tools fit
  that stage (ch15).
- Good: few features, many killed ideas. Fewer features mean less
  complexity and less feature fatigue (ch15).
- Bad: the team starts with a solution and works backward to a problem.
- Bad: experiments that keep running as half-products with no end.

## Pitfalls

- Treating a generative concept test as proof of demand. Without an ask
  it doesn't pass or fail.
- Running A/B tests too early or on too little traffic (ch18).
- Over-designing parts that aren't core (ch15).
- Shipping version 1 and moving on. "Version 2 is the biggest lie in
  software development" (Jeff Gothelf, quoted in ch19).

## Contradictions

- [[product-strategy-canvas]] describes the 2016 version, where the kata
  runs against a target condition set with managers (see
  [[2026-11-24-research-digest-strategy]]). The book summaries call the
  team's goal an option goal. Same loop, different labels.
- [[minimum-viable-product]] records Olsen's usage: an MVP is a real
  product customers find viable, and cheap checks are "MVP tests" (Lean
  Product Playbook ch7). Perri treats the MVP as the least effort needed to
  learn (ch18), which is the Lean Startup sense.

## Pairs well with

- [[strategy-deployment]]: where the goal comes from
- [[opportunity-solution-tree]]: mapping options under an outcome
- [[minimum-viable-product]]: the least effort that tests an assumption
- [[kill-criteria]]: deciding in advance when to stop

## From

- [[escaping-the-build-trap]] (from secondary summaries
  [[2020-11-17-swamy-seetharaman-escaping-the-build-trap-summary]] and
  [[bookey-escaping-the-build-trap-summary]]; `chN` = book chapter)

## Topics

- [[product-experimentation]]
- [[discovery-and-customer-insight]]
- [[goals-and-metrics]]
