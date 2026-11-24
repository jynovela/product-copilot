---
type: concept
summary: Write customer needs as precise benefits ("reduce my audit risk"), test each in discovery interviews, and organize them with benefit ladders and needs hierarchies.
updated: 2026-11-24
knowledge_source: ingested
---

# Customer benefits

## What it is

Olsen uses "needs" and "customer benefits" for the same thing: whatever
customers want or value (Lean Product Playbook ch4). He drops the split
between needs, wants and desires, since importance is measured separately
(ch4). User goals, user stories and pain points all fit under the same
umbrella; a pain point is a need that isn't met well (ch4).

Needs can be stated, unarticulated (the customer has it but doesn't say it),
or unknown (they don't know they value it until asked or shown something
new) (ch4). Needs are like onions: each layer has a more detailed one
beneath it (ch4). Benefits are the second layer of the
[[product-market-fit-pyramid]].

## When to use

- After choosing a target customer, before designing anything.
- Writing requirements, user stories or a value proposition.
- A feature list exists but nobody can say what each feature does for the
  customer.

## Steps

### 1. Write benefits, not features

A team that lists features instead of benefits has started in solution
space (ch4). Write each benefit so that it (ch4):

- Speaks from the customer's view, using "I" and "my".
- Starts with a verb: help, check, reduce, maximize.
- Where possible, increases something wanted or decreases something
  unwanted, such as "reduce the time it takes me to enter my tax
  information". This makes the gain measurable.

A good user story follows "As a [type of user], I want to [do something],
so that I can [benefit]" (ch4).

### 2. Peel the onion

Break a broad need into detailed benefits. "Prepare my taxes" splits into
checking accuracy, reducing audit risk, saving entry time, saving filing
time and maximizing deductions (ch4). Defining the problem space precisely
is the team's job, not the customer's (ch4). Olsen agrees with Ulwick that a
single job can have 50 to 150 or more desired outcomes (ch4).

### 3. Test each benefit in a discovery interview

Treat each benefit as a hypothesis: "target customer X would find benefit Y
valuable" (ch4). One-on-one, in-person interviews work best. For each
benefit statement, ask (ch4):

1. What does this statement mean to you? (checks it is clear)
2. How might this help you?
3. If a product delivered this, how valuable would it be? (no, low,
   medium, high or very high value)
4. For high value: why? For low value: why not?

The reasons are what you're after; they show how customers think (ch4).
Expect different customers to use different words for the same idea, and
to speak at different levels of detail (ch4). Listen closely, repeat back
what you heard, and probe (ch4).

### 4. Build benefit ladders

Keep asking "why is that important to you?" until no new answer comes. Each
answer climbs a rung, from detailed benefits to higher ones, and ladders
converge at the top (ch4). The six tax benefits climb to three: feel
confident, save time, save money (ch4). This is similar to the five whys
(ch4).

### 5. Map the hierarchies

Some needs only matter once another is met, as in Maslow's hierarchy (ch4).
Olsen's hierarchy of web user needs, bottom to top (ch4):

1. **Available:** the product is up when the user wants it.
2. **Fast:** response time is good enough.
3. **Works:** it does what it should, without bugs.
4. **Features:** the functionality.
5. **UX:** how easy and enjoyable it is to use.

Teams love working on the top two layers, but lower layers come first
(ch4). Your position changes: a new feature can add bugs, load the database
or spike traffic, so "dip down" to fix lower layers when they slip (ch4).

### 6. Prioritize

Rate each benefit's importance and current satisfaction, and go after the
important, poorly served ones. See [[opportunity-scoring]].

## Good and bad signs

- Good: every requirement traces to a benefit with a verb and a direction.
- Good: interview notes record why customers value a benefit, not only a
  rating.
- Bad: "benefits" that name screens, buttons or technologies.
- Bad: a few vague, high-level objectives stand in for the problem space
  (ch4).

## Pitfalls

- Expecting customers to describe the problem space well. They are better
  at saying what they like and dislike about a solution (ch4).
- Stopping at the first layer of the onion (ch4).
- Shipping features while the product is slow or down. Users won't value
  features until lower needs are met (ch4).
- Relying on the "voice of the customer" word for word. Customers are often
  vague, so the team must define benefits precisely (ch4).

## Contradictions

- [[jobs-to-be-done]] (Competing Against Luck) says a job is not a need: needs
  are too abstract to explain why someone buys, and the circumstance is
  what matters. Olsen treats jobs, needs, user stories and pain points as
  the same kind of thing (ch2, ch4). Olsen's precise benefits are close to
  Ulwick's desired outcomes, not to Christensen's jobs.
- [[mom-test-interviews]] says never ask people whether they'd value or use
  something, because opinions about the future are unreliable. Olsen's
  discovery script asks exactly that: "how valuable would that be to you?"
  (ch4). Use his ratings as a rough first sort, ask for the reasons, and
  check them against past behavior and later tests.

## Pairs well with

- [[problem-vs-solution-space]]: benefits are the problem space
- [[mom-test-interviews]]: ask about past behavior, not hypotheticals
- [[five-whys]]: the same questioning pattern as laddering

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[discovery-and-customer-insight]]
