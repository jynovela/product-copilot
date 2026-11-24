---
type: concept
summary: Turn company strategy into direction teams can act on: close Perri's knowledge, alignment and effects gaps by cascading vision, strategic intents, product initiatives and options, reviewed on a fixed cadence.
updated: 2026-11-24
knowledge_source: ingested
---

# Strategy deployment

Source note: this page comes from two secondary summaries of *Escaping the
Build Trap*, not the book text. Chapter numbers are the book's. Check
details against the book before quoting them.

## What it is

Perri uses Stephen Bungay's definition: strategy is a deployable
decision-making framework. It enables action toward desired outcomes, is constrained by current
capabilities, and fits the current context (Build Trap ch10). It is not a
detailed plan or a stakeholder wish list of features (ch10). **Strategy
deployment** is the act of telling the connected story of objectives and
outcomes at each level of the company, so each level can decide and act
(ch12). OKRs (Google), Hoshin Kanri (Toyota) and military mission command
are all forms of it (ch12).

A company needs two frameworks. The **operational framework** keeps
day-to-day work running. The **strategic framework** says how the company
reaches its vision through products and services. Companies often blur
the two; the strategic one matters most for products (ch12).

### The three strategic gaps

Treating strategy as a plan opens three gaps between plans, actions and
outcomes. Perri takes them from Bungay (ch11). Each has a tempting wrong fix:

| Gap | What it is | Wrong fix | Right fix |
| --- | --- | --- | --- |
| Knowledge | What leaders want to know versus what the company knows | Demand more detailed reports | Ask for just enough to decide; leaders state the strategic intent |
| Alignment | What people do versus what leaders want | Give more detailed instructions | Each level defines how it will meet the intent of the level above, and reports back |
| Effects | What we expect our actions to do versus what happens | Add more controls | Give teams freedom to adjust their actions toward the goal |

A common symptom: leaders say teams won't take ownership, and teams say
leaders keep handing them solutions. Both come from having no strategy
that enables action (ch11).

### Four levels

Perri says most product organizations need four levels of strategy
deployment (ch12):

1. **Vision:** where the company is going. Combine mission (why it exists)
   and vision (where it's going) into one statement of what the company
   does, why, and how it wins (ch13). Tell it as a story, then use the
   statement as a reminder (ch13).
2. **Strategic intents:** the few areas of focus that move the company
   toward the vision, reached over one to several years. They are
   business-level, such as entering a market or creating a revenue stream.
   One is usually enough for a small company and three are plenty for a
   large one (ch13). Leaders ask: "What is the most important thing we can
   do to reach our vision, based on where we are now?" (ch13).
3. **Product initiatives:** the major customer problems the product
   organization will solve to reach the intents (ch14). The VP of product
   works with PMs to pick them (ch14).
4. **Options:** the solutions and experiments teams try against an
   initiative, each with its own outcome goal (ch15).

Time frames narrow as you go down: executives think in years, middle
managers in years or quarters, teams in months or weeks (ch12).

## When to use

- Teams can't explain how their work connects to company goals.
- Leaders are asking for more status detail and more control.
- Annual planning produces a feature list that is stale by spring.
- Setting up OKRs or another goal system and choosing what each level
  owns.

## Steps

1. **Write the vision** as one statement plus the story behind it (ch13).
2. **Pick one to three strategic intents** from the current state of the
   business, not a wish list (ch13). Perri borrows Joshua Arnold's
   business value model, from his cost-of-delay work, to judge what value
   an intent creates (ch13).
3. **Write a product vision** for each product: why you are building it
   and the value for the customer. Keep it at the level of main
   capabilities, since a detailed one stifles growth (ch14). Amazon's
   press-release documents are one form; see [[working-backwards-pr-faq]].
4. **Set portfolio rules.** A CPO answers three questions: how the
   products work together as a system of value, what unique value each
   product line adds, and what values and guidelines govern new product
   bets (ch14).
5. **Choose product initiatives** as customer problems tied to an intent
   (ch14).
6. **Let teams set options** and run the [[product-kata]] against each
   initiative (ch15).
7. **Treat initiatives as bets.** Spotify's DIBBs, data, insights, beliefs
   and bets, frames work as a bet informed by the first three, which sets
   the right expectation that some will lose (ch12).
8. **Re-evaluate continuously, not yearly.** Tying budget and strategy to
   a yearly cycle hurts focus and follow-through. Review where you are and
   fund the next decisions (ch12, ch23).
9. **Organize teams around value streams**, meaning the whole flow that
   delivers value to a customer, not around features or technical
   components. Feature teams drift to output; component teams optimize
   their component instead of the goal (ch9).

### Review cadence

Visibility closes the knowledge gap. The more leaders can see, the more
they step back; hiding progress invites control (ch20). Perri's cadence
(ch20):

- **Quarterly business review:** executives review progress on strategic
  intents and financial outcomes such as revenue, churn and cost. The CPO
  reports how initiatives moved the intents. New intents can start here,
  but initiatives are not prioritized here.
- **Product initiative review:** quarterly, in the off months of the
  business review, for product, engineering and design leaders and PMs.
  Review options against initiatives, share experiment results, introduce
  and fund new initiatives.
- **Release review:** monthly, before release. Teams show what will ship
  and its success metrics. Only what will ship, not experiments.

**Roadmaps** explain strategy and the product's current stage, not a Gantt
chart. Each item shows its theme, hypothesis, goals and success metrics,
stage of development and key milestones (ch20). For the stages
(experiment, alpha, beta, general availability) see [[rollout-waves]].

## Good and bad signs

- Good: asked why they're doing their project, a PM and their leader give
  the same answer (ch11).
- Good: few strategic intents, and teams can name theirs.
- Bad: leadership passes down feature requests instead of outcomes, so
  teams can't connect their work to company results (ch11).
- Bad: a company of 5,000 people shipping about one feature a quarter
  because everyone works on too many things (ch13).

## Pitfalls

- A strategy document that is really a plan of features.
- A long list of intents. Focus comes from keeping the list small (ch13).
- Leaders who are not aligned at the top; the confusion flows down to every
  team (ch11).
- Treating autonomy as no direction. Autonomy without clear goals creates
  friction, not results (ch11).

## Contradictions

- [[product-strategy-canvas]] gives Perri's 2016 version: vision,
  challenge, target condition and current state (see
  [[2026-11-24-research-digest-strategy]]). The book summaries give four
  deployment levels instead: vision, strategic intent, product initiative
  and options. The canvas's challenge sits near the strategic intent and
  its target condition near an option goal. This is our mapping, not
  Perri's.
- [[okrs]] records that sources disagree on strict cascades, and Herbig
  says they push teams toward outputs. Perri sides with the loose version:
  each level sets its own "how" against the intent of the level above
  (ch11).

## Pairs well with

- [[kernel-of-good-strategy]]: test whether the strategy has a diagnosis
- [[okrs]]: one way to write goals at each level
- [[product-kata]]: what teams do with an option goal
- [[product-operations]]: who runs the cadence at scale
- [[cost-of-delay]]: valuing intents and initiatives

## From

- [[escaping-the-build-trap]] (from secondary summaries
  [[2020-11-17-swamy-seetharaman-escaping-the-build-trap-summary]] and
  [[bookey-escaping-the-build-trap-summary]]; `chN` = book chapter)

## Topics

- [[strategy-and-innovation]]
- [[goals-and-metrics]]
- [[product-teams-and-operating-model]]
