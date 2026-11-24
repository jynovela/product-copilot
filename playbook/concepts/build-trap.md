---
type: concept
summary: Spot and escape the build trap, where success is measured by features shipped instead of value created; diagnose it with Perri's six questions and fix goals, rewards, safety and budgets.
updated: 2026-11-24
knowledge_source: ingested
---

# Build trap

Source note: this page comes from two secondary summaries of *Escaping the
Build Trap*, not the book text. Chapter numbers are the book's. Check
details against the book before quoting them.

## What it is

A company is in the build trap when it measures success by output, such as
features shipped, specs written or story points done, instead of outcomes,
the value those things create (Build Trap ch1). The company ships a lot,
but adoption is poor, features are orphaned, and nobody can say whether
any of it worked (ch1).

Perri frames value as an exchange. Customers get a need or want met, and
in return the business gets money, data, knowledge or other value (ch1).
Customer needs keep shifting with their communities and the technology
around them, which the business can't control. The business can control
its own constraints: its people, processes, policies, strategy and culture
(ch2). The build trap is a business constraint that blocks the exchange.

Three terms that companies blur (ch3):

- A **product** is a vehicle for value. It delivers value again and again
  without something new being built each time. Shipping is the first step
  of its life, not the end.
- A **service** delivers value through human labor.
- A **project** is a bounded piece of work with a set output and end date.
  Managing product work as a series of projects leads straight to the trap.

A **product-led** organization optimizes for business outcomes, aligns
product strategy to them, and then picks the work most likely to grow its
products into sustainable drivers of growth (ch4). Perri contrasts it with
sales-led, visionary-led and technology-led companies (ch4).

## When to use

- The roadmap is a list of features with dates and no goals.
- The team ships steadily but revenue, retention or adoption don't move.
- Leaders ask for more features while every team chases a different
  output metric.
- You are deciding whether to join a company, or checking your own.

## Steps

### 1. Diagnose with the six questions

Perri's appendix gives six questions to ask a product manager (Build Trap
appendix):

1. **Who came up with the last feature you built?** A healthy answer is
   puzzled: "our team did". Management sets goals; the team finds how to
   reach them. Ideas from above should be the exception, and a team that
   can't say why it is building something is a red flag.
2. **What was the last product or idea you killed?** "We never kill
   anything" points to features promised to customers in advance,
   use-it-or-lose-it budgets, or no safe way to push back on management.
3. **When did you last talk with customers?** Being kept away from
   customers is a bad sign; the job should require it.
4. **What is your goal?** No clear goal, or a goal about shipping dates,
   means the organization manages output.
5. **What are you working on?** Strong PMs talk about the problems they
   are solving more than the features they are shipping.
6. **What are your product managers like?** PMs seen as dictators, or as
   order-takers beaten down by stakeholders, both signal an unhealthy
   function.

Also ask of the last thing you shipped: how do you know it succeeded, did
it meet a real need, and did anyone go back and iterate on it (ch1)?

### 2. Separate what you know from what you don't

List facts, then known unknowns: questions you can name, such as
assumptions to test or data to gather. Resolve them with research and
experiments before building (ch5). Unknown unknowns can only be shrunk by
exploring. Treat gut feel ("I just know this is right") with caution
(ch5).

### 3. Change the system, not just the roadmap

- **Goals and strategy:** set outcome goals at every level and let the
  next level decide how. See [[strategy-deployment]].
- **Process:** run each goal through the [[product-kata]].
- **Definition of done:** a feature is done when it reaches its goal, not
  when version 1 ships. Moving on without measuring is how teams stay
  trapped (ch19).
- **Rewards:** reward people for outcomes, learning about users and
  finding good opportunities, not for output (ch21).
- **Safety:** let teams try odd ideas and fail early, small and cheap.
  The costly failure is the slow one, where products ship and are never
  measured for years (ch22). Release to small alpha and beta groups first
  to bound the risk (ch22).
- **Budgets:** fund work by portfolio and stage. Fund known work to build,
  set money aside for discovery, and increase funding as opportunities
  are validated, instead of fixing everything in a yearly plan (ch23).
- **Leadership:** the change starts with the CEO. Leaders who say they
  want outcomes but still count features shipped are the main reason
  transitions fail (ch20, ch25).

## Good and bad signs

- Good: teams can name the outcome their work serves and its current
  value.
- Good: the company kills ideas early and often (ch25).
- Good: teams go back and iterate on what they shipped.
- Bad: everything is priority zero, and each team optimizes its own output
  (ch1).
- Bad: developers are praised for code volume, designers for pixel
  polish, and PMs for long specs and big backlogs (Build Trap intro).
- Bad: building feature parity with a competitor without checking whether
  anyone uses that feature (ch1).

## Pitfalls

- Treating the trap as a team problem when the cause is goals, rewards or
  budgets set above the team.
- Swapping feature counts for vanity metrics. See [[vanity-metrics]].
- Expecting results within a quarter. Companies stuck in the trap are not
  patient enough for outcomes to emerge (ch20).

## Pairs well with

- [[outcomes-over-outputs]]: writing goals as outcomes
- [[strategy-deployment]]: setting direction so teams can act
- [[product-kata]]: the process for reaching each goal
- [[pm-archetypes]]: bad PM patterns that keep a company trapped
- [[kill-criteria]]: deciding in advance when to stop

## From

- [[escaping-the-build-trap]] (from secondary summaries
  [[2020-11-17-swamy-seetharaman-escaping-the-build-trap-summary]] and
  [[bookey-escaping-the-build-trap-summary]]; `chN` = book chapter)

Inference: these books cover related ground.

- [[product-roadmaps-relaunched]]
- [[lean-vs-agile-vs-design-thinking]]
- [[lean-ux]]

## Topics

- [[strategy-and-innovation]]
- [[product-teams-and-operating-model]]
