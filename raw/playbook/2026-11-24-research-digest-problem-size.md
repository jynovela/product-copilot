<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Research knowledge: problem framing and problem sizing

As of 2026-11-24. Written from Juan's research batch for the problem-size gap
(upload `36e1cc05-2ee5-4407-a96b-a037ee50e51e`, received 2026-11-23, about 25
pieces). All text below is a paraphrase unless quoted. Each claim names the
source it came from by its short tag; the full list is in section 6.

Labels used:

- **Vendor**: the publisher sells a product or course related to the claim.
  Treat it as a source, not as fact.
- **Unsourced**: the piece gives a number or story without a checkable source.
- **General knowledge**: added by Claude from memory, not from the batch.
- **Inference**: Claude's own reasoning.

The AI search summary at the top of the batch was read for orientation only.
None of its claims are cited here, because AI search answers are not sources.

How the batch splits: about half the pieces are about writing a problem
statement or about the PM process in general. Only about ten say anything
specific about sizing. See section 6 for which ones mattered.

## 0. What the design took from this (short)

The copilot design that came out of this batch is in the plan doc section
"Gap research: problem size". In short: problem pages get a `## Size` section
that keeps **evidence strength** (counted by the copilot) apart from
**magnitude** (reach, frequency, urgency, cost to them, cost to us). Each
magnitude line has a basis (`measured`, `stated by source`,
`team guess (<who>)`, `inference`) or says `unknown`. Ranges are allowed.
Urgency is a behavior ladder. The size is copied and locked on the decision
page when an opportunity is chosen. No RICE scores and no market size on
problem pages. The rest of this file is the wider knowledge, including what
the design did not use.

## 1. Frameworks, methods, models and lists

### 1.1 Problem statement formats

Every source here agrees on one rule: a problem statement describes a
situation and never names a solution. Formats differ in which parts they
require.

| Format | Parts | Source(s) |
| --- | --- | --- |
| Current state / consequence / ideal state | What happens now; the gap or cost it causes; what good looks like | Hermanto |
| 5W problem framing canvas | Who faces it, what it is, where it happens, when it arises, why it is worth solving | Hermanto; Stewart (adds "How"); ProdPad ("5 Ws and H", the H is how it is handled today) |
| Gap / Orientation / Impact / Significance | Gap: what's wrong versus what should happen. Orientation: when, where, how it was found. Impact: measurable effects. Significance: why it matters to the organization | Morelli (Harvard GSE); Miro uses the same four with Importance in place of Significance and maps them to the 5 Ws |
| Stanford d.school point-of-view formula | "[Stakeholder] needs a way to [need, as a verb] because [insight]" | Abraham |
| Persona / problem / situation / impact sentence | "[Persona] struggles with [problem] when [situation], which leads to [impact]" | ProdPad (Vendor) |
| Five-part anatomy | The problem, who is affected, context, impact on user and business, desired outcome | Stewart |
| Five components | Problem, context (including existing solutions and their limits), scope (what you won't solve), measurability, impact | ProductPlan (Vendor) |
| Problem statement template | Current situation (with data), affected users (who, how many, which segment), impact (quantified), root cause (labeled hypothesis), success looks like (a measurable outcome) | noirbook |
| Problem document | What is the problem, who are we solving it for, why now, how it links to strategic goals, how we would validate it's solved | Goetzmann |
| WHO / WHEN / WHY / HOW | Who has it, when it occurs, why it appears, how it makes them feel, then rewritten as a "How might we" question | Piteiu-Apostol (LogRocket, Vendor) |
| SCQA | Situation, Complication, Question, Answer; a storytelling frame for stakeholders | ProdPad |
| Business case format | Stresses commercial impact: market size, cost, urgency | Stewart |
| JTBD format | "When I [situation], I want to [motivation], so I can [outcome]" | Stewart; ProdPad |
| SMART as a check | Specific, Measurable, Achievable, Relevant, Time-bound, used as a final filter on the statement | Stewart; Smalley mentions SMART for KPIs |

Quality tests the sources give for a statement:

- If it has only one obvious solution, it is too narrow (Trivedi). Naming a
  channel ("a better app") is already a solution (Hermanto).
- Too broad is also a failure: "users are dissatisfied" is useless; narrow it
  to which users, with what, compared to what (noirbook; Morelli).
- Usually one to three sentences. If it needs a page, root-cause analysis or
  solution ideas have crept in (Miro; Stewart).
- d.school list of what a good statement does: focuses, inspires, gives
  criteria for judging ideas, lets the team decide on its own, isn't "all
  things to all people", is discrete not broad (Abraham, citing d.school).
- The statement is a living document and gets revised as you learn
  (ProductPlan; Miro; ProdPad; Brereton; Torres).
- Miro gives an "output" for each of its 5 steps: one problem sentence plus
  2 to 3 data points; context points and constraints; 2 to 5 root-cause
  hypotheses ordered by evidence; an outcome statement with proxy signals;
  1 to 3 solution directions plus what to validate next.

### 1.2 Root cause and decomposition methods

| Method | What it does | Limits noted | Source(s) |
| --- | --- | --- | --- |
| 5 Whys | Ask "why" about each answer, usually about five times, until you reach a cause you can't explain further | Can push you to one cause when several contribute; use it to make hypotheses and check them with data (noirbook) | Barrows; Morelli; Miro; noirbook; Creately |
| Logic tree / issue tree | Break a problem into mutually exclusive, collectively exhaustive (MECE) possible causes | — | Barrows (Harvard); Verma (McKinsey method) |
| Symptoms versus root cause | Symptoms are what you see; diagnosis needs the full set of symptoms together, like a medical diagnosis | — | Morelli |
| Recurring versus situational test | A symptom seen across classes, people and times points to a systemic cause; a one-off may be temporary | — | Morelli |
| Affinity mapping | Group raw research notes to find patterns; use interview data, not opinion | Messy and slow | Torres; Miro |
| Journey mapping / funnel analysis | Find where in a flow the problem shows up | — | Miro; Creately |
| Empathy map | Four boxes: what the user thinks, feels, does, says | — | Hermanto |
| Diverge and converge | Each person defines the problem alone, then the group compares and picks or merges | — | Hermanto; Goetzmann (double diamond) |
| Map your own perspective first | Each teammate maps one recent real experience alone, then shares; then customer research; then synthesize and test the shared map | Without this, your own beliefs bias how you hear customers | Torres |
| Reframing | Restate the problem to find a better one (slow elevator becomes "waiting is boring") | — | Trivedi (citing an HBR article); noirbook (Slack example) |
| McKinsey-style 8 steps | Define, break down (MECE), prioritize issues, hypothesize, test with data, synthesize, develop SMART solutions, implement with feedback | Case results in the piece are unsourced | Verma |
| Barrows 4 steps | Define (reframe with others), decompose (logic tree), analyze (collect data per cause, 5 Whys), act (try a fix and recheck) | — | Barrows |

### 1.3 Ways to classify a problem

**Awareness and urgency categories (Blank, as told by Trivedi).**

- Latent: they have the problem but don't know it. Needs years of education
  or marketing before it sells.
- Passive: they know but aren't trying to fix it. Bundling with something
  bought often, or riding a trend, helps.
- Active: they are looking for a fix but it isn't burning. Long sales
  cycles; buyers care about price and quality.
- Urgent: "ass on fire". They'll buy if you're there, but big urgent problems
  usually already have competitors; without distribution you must be 10x
  better.
- Imaginary (Trivedi's addition): the problem doesn't exist but people
  believe it does. The fix is usually communication, not product.
- Problems move between categories over time; a shock such as a pandemic can
  make a latent problem urgent overnight.

General knowledge, not verified: Blank's own ladder in *The Four Steps to the
Epiphany* has five steps: has a problem, knows it, is actively looking, has
cobbled together a workaround, has or can get budget. The design's Urgency
line follows this five-step version because each step can be observed.

**Painkiller, vitamin, candy** (Trivedi). All three can be big businesses, but
positioning must match: a painkiller sold as a vitamin won't sell, and a
vitamin sold as a painkiller invites lawsuits.

**Problems, needs and wants** (Trivedi). Problems are a subset of needs and
wants. "Value add" features without a real problem tend to help few users for
a short time.

**Reframing questions for a feature request** (Trivedi): is it an incentive
problem, an expectations problem, an attitude problem (inertia), a brand
perception problem, a misinformation problem (they believe competitors do it
better), or a problem caused by another of your own solutions?

**Well-structured versus ill-structured problems** (Torres, citing David
Jonassen). Well-structured: known start, known goal, fixed rules, one right
answer. Ill-structured: several solutions, each with pros and cons for
different people. PM work is mostly ill-structured, and skill at the first
kind doesn't transfer to the second. Jonassen's definition: a problem only
exists when there is a "felt need" to close a gap.

**Four types of problems** (Smalley, Lean Enterprise Institute):

1. Troubleshooting: fix an abnormal condition fast and return to standard
   (put out the fire). Toyota uses a 4C routine: concern, cause,
   countermeasure, check.
2. Gap from standard: structured root-cause work with goal, analysis,
   countermeasures, checks and follow-up (find what caused the fire).
3. Target state: continuous improvement (kaizen) to a new, better standard.
4. Open-ended innovation: pursue a vision beyond current levels.

Smalley maps Heifetz's technical problems to types 1 and 2 and adaptive ones
to types 3 and 4. His wider point: no single method (5 Whys, Six Sigma, 8D,
A3, DMAIC) fits every problem.

**Annie Schugart's problem evaluation framework** (used to judge companies or
big features):

- Basics: size of the problem (how many, how deeply, how often; measure size
  and frequency together as a ratio); hacks or existing solutions (including
  low-tech workarounds that may be good enough); riskiest risks (regulation,
  closed industries, cost to solve).
- Differentiators: exponentiality (is it a wedge into bigger markets, like
  Amazon starting with books); expandability (does it apply to other
  industries; the frisbee started as pie tins); unique market hooks such as
  regulation that gives an unfair advantage.
- Ethics and mission: potential for future harm; mission alignment.
- Her footnote: you can pick frequent smaller problems (Uber) or rarer bigger
  ones (Airbnb).

### 1.4 Sizing a problem

**Dimensions the sources name.**

| Dimension | What sources say | Source(s) |
| --- | --- | --- |
| Reach | How many users or accounts have it; a segment, not "everyone" | Trivedi; noirbook; Goetzmann; Belitsky; Schugart |
| Frequency | How often it happens | Schugart; ProdPad; Creately |
| Depth, severity or intensity | How painful; "the more severe the pain, the more valuable the solution" | ProdPad; Schugart ("how deeply"); Goetzmann |
| Cost to the user | Time, money or "life" saved | Trivedi; Stewart |
| Cost to the business | Revenue, retention, activation, support load | noirbook; Stewart; Miro |
| Existing solutions and workarounds | What people do today, including nothing | Schugart; noirbook (opportunity canvas); ProductPlan |
| Self-discoverability | How likely users are to find a change on their own; Trivedi uses it as a proxy for impact | Trivedi |

**Ways to get the numbers.**

- Instrumented product: pull the real count of affected users. Not
  instrumented but has users: dig through other data. New product: Trivedi
  says guess (would 80% or 20% of users find it useful?) and write the number
  down in the PRD or ticket.
- Evidence channels: support tickets, product analytics, QA, sales calls,
  user feedback, people closest to the problem (support, success, design,
  engineering). Aim for "the right problem, not just the most vocal one"
  (Miro; Creately says check which issues come up most often and frustrate
  most).
- Proxies when data is missing: a similar past feature's adoption, another
  team's click-through on the same surface, historic traffic growth
  (Belitsky).
- What customers pay today, directly or indirectly, to work around the
  problem (Productboard prompt).

**Opportunity canvas** (noirbook). Fields: problem (evidence-based), users
affected (who and how many), current alternatives, strategic fit, estimated
impact (quantified), estimated effort (T-shirt size), confidence level
(high, medium, low for each line), and "what would change your mind?".

**Opportunity sizing against one North Star metric** (Belitsky, Built In).
This sizes solution ideas, not problems.

1. Pick one North Star metric for all ideas, so they can be compared.
   Common choices she lists: revenue, enrollments, activation, referrals,
   engagement, user satisfaction (feedback score or NPS). She says
   e-commerce often uses revenue per session; top of funnel uses
   enrollments, activation or referrals; SaaS uses engagement or
   satisfaction.
2. Write each idea as: "By [project], [what will happen], leading to [effect
   on the North Star]".
3. Collect baseline numbers (monthly active users, sessions, revenue,
   clicks).
4. Model with proxies where you don't know (see above).
5. Keep a shared "book" (spreadsheet) of all ideas with their sizes and show
   it to stakeholders to explain the order.

She stresses that sizing is directional, "not a financial report, a thesis or
a promise".

**Internal or platform friction formula** (from the AI summary, credited to
noirbook): hours lost per week × loaded cost per person × number of people ×
52 weeks. The formula was not in the noirbook text included in the batch, so
treat it as unverified. Inference: it is a standard cost-of-time calculation
and fits the "Cost to them" line.

### 1.5 Market sizing

**TAM, SAM, SOM** (noirbook; Olafioye; Productboard prompt).

- TAM, total addressable market: revenue if you had 100% share; the
  theoretical ceiling.
- SAM, serviceable addressable (or available) market: the part your model,
  pricing, geography and capabilities can serve.
- SOM, serviceable obtainable market: the part you can realistically win in
  one to three years given competition and sales capacity. noirbook: "the
  number that should drive resource allocation".

**Top-down versus bottom-up.**

- Top-down starts from an industry figure and narrows by filters. Fast and
  good for the big picture; often too optimistic; investors distrust it
  without bottom-up support (Olafioye).
- Bottom-up builds from real units: number of companies that fit your
  profile × share with the problem × price × realistic capture. More
  credible (noirbook; Olafioye; Productboard).

**Productboard market sizing prompt** (Vendor; written as an AI prompt).

- Inputs: the problem and for whom; the buyer (may differ from the user);
  what customers pay today; pricing model; third-party data; customer and
  sales data (win rates, deal sizes, cycle length); competitor claims and
  revenue; beachhead market; expansion path.
- Phase 1, bottom-up: define the ideal customer, count them (method and
  confidence level), model beachhead revenue (count × average contract value
  × capture rate), then SAM by expansion layers (geography, segments, seats,
  adjacent problems, platform), given as a range, then TAM with caveats.
- Phase 2, three sanity tests: the revenue math (does your plan imply your
  claimed market?); competitor revenue (competitor revenue ÷ their share);
  budget reality (buyer's annual spend in the category × number of buyers).
- Phase 3, attractiveness beyond size: growth rate, timing (what changed),
  penetration (low means education needed, high means displacing someone),
  buyer psychology (want or need, pain intensity), competitive intensity.
- Red flags: never present a percentage of a huge market as your
  opportunity; never cite analyst reports without saying why they apply;
  always show bottom-up math.

**Fermi estimation** (noirbook). Break an unknowable number into smaller
guessable parts and multiply. noirbook claims errors "tend to cancel out" and
that it gives the right order of magnitude in minutes. Use for quick sizing
or to sanity-check a detailed analysis.

**Why market sizing matters, per Olafioye:** investor trust, choosing which
segments and problems to focus on, pricing and revenue planning, and
go-to-market precision. Market sizing should be revisited as data comes in.

### 1.6 Prioritization tools mentioned alongside sizing

These are covered in more depth in existing playbook concept pages
(`rice-scoring`, `value-vs-effort-matrix`, `kano-model`), so only the batch's
own points are kept here.

- Impact / effort matrix (noirbook; Creately): quick wins (high impact, low
  effort), strategic bets (high, high), fill-ins (low, low), time sinks (low
  impact, high effort; "where feature requests from loud customers often
  land"). noirbook warns teams overestimate impact on ideas they love; see
  the unsourced 2 to 3x claim in section 5.
- RICE, MoSCoW, Kano (Creately; pmo365): named and described in one line
  each. No new detail.
- Eisenhower matrix for issues (Verma).

### 1.7 When to frame and size formally

noirbook's guidance:

- Use formal framing for work over two weeks of engineering, a new market or
  product direction, disagreement about what to build, justifying resources
  to leadership, or an ambiguous problem with several plausible causes.
- Skip it for a well-understood problem with a validated solution and small
  effort, a known bug, iterating on a feature with clear success metrics, or
  a team with strong recent shared context.
- Solo PM or early team: the problem statement template plus a quick Fermi
  estimate, written in 30 minutes, not 3 days.
- One-way doors (irreversible: new market, platform migration, multi-year
  partnership, sunsetting) need rigorous framing and sizing; two-way doors
  need light experiments. (noirbook credits Jeff Bezos for the distinction.)

**Scope hammering** (noirbook): write the maximal version, cut to the
smallest version that delivers value, then sequence the cut pieces into
independently shippable phases. Basecamp is its example.

### 1.8 Estimating well (applies to size estimates too)

From Mountain Goat Software (Mike Cohn's company; Vendor: sells training).
Written for story points, but the advice carries over to any team estimate.

1. Agree which of five kinds of estimate you give: single most likely, ideal
   case (about a 10% chance), median (50/50, his recommendation), risk-averse
   (about 90% chance of beating it), worst case.
2. Estimate relatively, by analogy to known items.
3. Stay within one order of magnitude (about 1 to 10); build up gradually
   for bigger items, or split them.
4. Avoid false precision: use buckets (powers of two, or Fibonacci 1, 2, 3,
   5, 8, 13); when torn between two buckets, round up.
5. Triangulate against one smaller and one larger item.
6. Avoid anchoring (even saying "these are all small" skews estimates).
7. Don't settle disputes by picking the middle value (central tendency
   bias); let the high and low estimators argue first.

The opposite view, Kyle Evans: teams get stuck in cycles of estimating and
re-estimating; delivering value quiets demands for estimates better than
better guesses do.

### 1.9 Research planning and bias (from the problem-space pieces)

Piteiu-Apostol (LogRocket, Vendor) gives a research plan template: goal,
questions, participants (specific), number of participants, timeframe,
methods, success measure. Her worked example: a French bank studying Gen Z
and Millennial customers' carbon footprint, with an 800-response survey sent
to 1,500 customers, 10 to 15 interviews, one month, success at 500 responses
and 10 interviews. She recommends story-based interviews ("tell me about the
last time you...") and recording them.

Her bias table:

| Bias | Description | How to reduce it |
| --- | --- | --- |
| Confirmation | Seeking what confirms existing beliefs | Non-leading questions; aim to uncover, not confirm; adequate sample |
| Friendliness | Agreeing to keep things pleasant | Short sessions; a neutral interviewer |
| Social desirability | Answering to look good | Don't ask "how do you like X"; confidentiality; forced ranking; 1-on-1 |
| Hawthorne effect | Acting differently when watched | Anonymous testing; a non-threatening setting |

She also cites Bain's 30 consumer Elements of Value (functional, emotional,
life-changing, social impact) and the B2B Elements of Value (table stakes,
functional, ease of doing business, individual, inspirational).

## 2. Definitions and vocabulary

| Term | Definition(s) | Where sources differ |
| --- | --- | --- |
| Problem | A gap between the current and desired state (Barrows; Hermanto; Miro). Jonassen via Torres adds that it is only a problem if there is a "felt need" to close it. | Barrows says a problem need not be unpleasant, just a variance. Trivedi treats problems as a subset of needs and wants. |
| Problem statement | A short, evidence-based description of who has a problem, what it is and why it matters, without a solution (Stewart; Miro; ProdPad; Brereton). | Some include a desired outcome or success measure (noirbook; ProductPlan; Stewart); Hermanto notes some statements in practice include a solution, which most others reject. |
| Problem framing | Deciding what question you're answering before building answers (noirbook); a discovery process to understand and define a problem (Hermanto). | — |
| Problem space versus solution space | Explore the problem through research before ideating; the double diamond (Goetzmann; Piteiu-Apostol). | — |
| Opportunity sizing | Assessing how big the prize is once a problem is defined (noirbook); estimating the metric lift of an idea relative to other ideas (Belitsky). | noirbook sizes problems and markets; Belitsky sizes solution ideas against a North Star metric. |
| Market sizing | Estimating potential demand and the revenue it could bring (Olafioye). | — |
| TAM / SAM / SOM | See 1.5. | SAM is "serviceable addressable" in noirbook and "serviceable available" in Olafioye. Same idea. |
| Root cause versus symptom | Symptom: an observable effect. Root cause: the reason behind it, which when fixed gives a lasting result (Morelli). | — |
| Latent / passive / active / urgent | See 1.3. | Trivedi's four steps versus Blank's original five (General knowledge, unverified). |

## 3. Practices most sources agree on

1. Define the problem before discussing solutions, and write it down
   separately from any solution (nearly every piece; Goetzmann says keep the
   problem document separate so you don't fit the problem to the solution).
2. Base it on evidence from several channels, not on opinion or the loudest
   request (Miro; ProdPad; Stewart; Creately; noirbook).
3. Name a specific segment, not "everyone" (Trivedi; noirbook; Morelli).
4. Size by how many, how often and how badly, plus the cost to user and
   business (Schugart; Trivedi; ProdPad; Stewart; noirbook; Goetzmann).
5. Dig for root causes; treat the first answer as a hypothesis (Morelli;
   Barrows; Miro; noirbook).
6. Frame it with others (design, engineering, customer-facing teams) to align
   and catch blind spots (Hermanto; Goetzmann; Miro; Torres; Brereton).
7. Treat the statement and the sizing as living; revise as evidence arrives
   (ProductPlan; Miro; ProdPad; Torres; Olafioye).
8. Prefer bottom-up sizing to top-down (noirbook; Olafioye; Productboard).
9. Aim for order of magnitude, not false precision (noirbook "sizing
   theater"; Mountain Goat buckets; Belitsky "directional").
10. Write down assumptions and how sure you are (noirbook confidence per
    line; Productboard confidence level; Belitsky proxies).

## 4. Conflicts between sources

1. **Score or compare.** Torres (2016) says scoring ideas in a spreadsheet
   (business impact, request count, build time) treats an ill-structured
   problem as if a formula could solve it. Belitsky says a data-driven
   sizing spreadsheet against one North Star is "the best way" to rank and
   to stop "anyone with an opinion" hijacking the roadmap. They partly talk
   about different things: Belitsky sizes solution ideas. General knowledge:
   Torres's later book *Continuous Discovery Habits* (2021) uses opportunity
   sizing (how many customers, how often) as one input when comparing
   opportunities, without a formula.
2. **Guess or leave blank.** Trivedi: for a new product, guess (80% or 20%)
   because having a number written down matters. Miro and ProdPad: evidence,
   not guesses or "assumptions dressed as facts". noirbook: estimate but rate
   your confidence.
3. **Top-down market sizing.** Productboard: top-down ("the market is $50B")
   is useless. Olafioye: fine as a framing tool if checked bottom-up.
   noirbook: TAM is for investors, not prioritization; SOM drives resources.
   Olafioye says TAM helps judge whether an opportunity is worth strategic
   investment.
4. **Does severity equal value?** ProdPad: more severe pain means a more
   valuable solution. Trivedi: urgent problems are usually already served by
   competitors, and latent ones don't sell without years of education; how
   people act on the problem matters more than how much it hurts.
5. **Blank's ladder.** Trivedi's four categories versus Blank's five-step
   ladder (General knowledge, unverified; check the book).
6. **Do Fermi errors cancel out?** noirbook claims errors "tend to cancel
   out". The same piece warns against "sizing theater", and Mountain Goat
   says people estimate well only within one order of magnitude. Inference:
   errors cancel only when independent and unbiased; teams that like an idea
   tend to push every input the same way, which noirbook itself notes.
7. **Estimate more or less.** Mountain Goat: estimate better with seven
   techniques. Evans: estimation cycles can replace delivering value. Radford
   (Product School): multiply every engineering estimate by 4 (Unsourced).
8. **How much to plan up front.** noirbook: frame formally for one-way doors
   and skip for small two-way ones. Hermanto: frame "as early as possible" for
   every problem. Inference: these fit if early framing for small work is
   light.

## 5. Worked examples and numbers

| Example or number | Publisher | Flag |
| --- | --- | --- |
| Bottom-up example: 50,000 companies fit the profile, 30% have the problem, $12K average contract a year, close 5% in year one = $9M | noirbook | Illustration |
| TAM example $7.5B project management software; SAM $800M remote-first tech in North America; SOM 2% in 18 months = $16M ARR | noirbook | Illustration; figures not sourced |
| Fermi example: ~30M US businesses, 40% B2B, 60% use SaaS, 15% with 10 to 500 staff, 20% have the problem, 10% pay $200+/month = 21,600 companies, about $52M a year | noirbook | Illustration; input percentages are guesses |
| Problem statement example: "43% of new users abandon onboarding at step 3"; free-plan first-time users about 12,000/month; success = completion from 57% to 75% | noirbook | Illustration |
| "Admins spend 40 minutes per day on repetitive individual actions" as a reframed problem behind "bulk actions" | noirbook | Illustration |
| Slack framed the problem as knowledge workers spending 28% of the week on email | noirbook | Unsourced; the 28% figure is commonly credited to McKinsey (General knowledge); the story reads as told after the fact |
| Dropbox's early sizing was a Fermi estimate | noirbook | Unsourced story |
| Teams over-promise impact by 2 to 3x; apply a correction factor | noirbook | Unsourced |
| Top-down example: 6.5B smartphone users × 12% in Africa × 85% Android × 30% urban 18 to 30 = 198.9M users; at $2/month = $4.77B a year at 100% capture | Olafioye | Illustration; share figures not sourced except a Statista link for 6.5B |
| Bottom-up example: Lagos pilot reaches 10,000, converts 500 (5%); 2M Android users aged 18 to 30 in Lagos × 5% = 100,000 users; at $5/month = $6M a year | Olafioye | Illustration |
| Loyalty carousel card: other teams' carousel CTR about 3%; similar feature saw 20% enrollment; traffic grows 2.5% a month; model gives 469 enrollments for a past quarter and 2,545 new users the next year | Belitsky | Worked example; the tables behind it were images not included in the batch |
| Driver attendance case: client estimated about 10% overpayment; the real problem was "Am I overpaying?"; a report solved it at about 20x less effort than a new system | Trivedi | Anecdote |
| Onboarding completion 42% versus a 70% activation threshold; 38% completion; integration tickets up 27% last quarter; engineers spend nearly 50% of sprint capacity on legacy defects | Miro | Vendor; illustrations |
| WebMD Medscape saw 60% more product improvements a quarter and a 10% engagement lift after moving discovery into Miro | Miro | Vendor case study |
| Industry examples: 48-hour transaction delay with 15% more complaints; 3-week appointment waits with 25% lower satisfaction; 30% claim rejection rate; 10% network reliability drop; 15% more food waste | ProductPlan | Vendor; "inspired by customers", not real data |
| 27% of product teams say roadmaps get thrown off by lack of discovery (2026 State of Product Management report); only 5.7% use a structured prioritization framework | Stewart | Unsourced in the text; likely vendor survey |
| "Over 80% of new product initiatives fail" | Dan Olsen, quoted by Stewart | Unsourced |
| 85% of executives say their companies are poor at problem diagnosis | Barrows | Unsourced in the text |
| Knowledge workers spend three hours on admin and meetings per hour of strategic work; 93% have collaboration problems | Miro "Momentum at Work" | Vendor survey |
| Multiply every engineering estimate by 4 | Radford (Product School) | Unsourced rule of thumb |
| About 60% of founders and half of PM candidates describe a solution when asked for the problem | Trivedi | Personal observation |

## 6. Sources

Short tag, then author, publisher, kind and date where shown. "Substantive"
means it added sizing or framing knowledge beyond generic advice.

| Tag | Author / publisher | Title | Kind | Date | Substantive? |
| --- | --- | --- | --- | --- | --- |
| noirbook | noirbook.org (author not shown) | Problem Framing & Opportunity Sizing | Practitioner reference site | Not shown | Yes, the most useful piece: templates, canvas, TAM/SAM/SOM, Fermi, pitfalls, when to frame |
| Schugart | Annie Schugart, annieschugart.tech | How to measure a problem | Practitioner blog | Not shown | Yes: problem evaluation framework, size and frequency as a ratio |
| Trivedi | Ujjwal Trivedi, Medium (The Startup) | Product Management Is the Art of Problems (Not Solving) | Practitioner blog | 2020-08-08 | Yes: problem categories, reframing questions, measuring reach and impact |
| Belitsky | Olivia Belitsky, Built In | Opportunity Sizing for New Product Managers: A Guide | Practitioner article | 2022-03-09 | Yes: North Star sizing method, proxies |
| Productboard | Productboard | Market Opportunity Sizing (prompt library) | Vendor (AI prompt) | Not shown | Yes: bottom-up method and sanity tests |
| Olafioye | Seyifunmi Olafioye, The Product Notebook (Substack) | Market Sizing 101: A Guide for Product Managers | Practitioner newsletter, inspired by a Treford course | 2025-04-27 | Yes: TAM/SAM/SOM, top-down and bottom-up examples |
| Torres | Teresa Torres, Product Talk | Product Managers, Level Up Your Problem-Solving Skills | Practitioner blog (promotes her course) | 2016-01-06 | Yes: ill-structured problems, against formula scoring |
| ProdPad | Megan Saker, ProdPad | The Product Management Problem Statement: How to Get it Right | Vendor blog | 2025-06-19 | Partly: frequency and severity, templates |
| Miro | Miro | How to write a problem statement | Vendor guide | Not shown | Partly: evidence channels, 5 steps with outputs |
| Stewart | Rebecca Stewart and Janardhana Siddhartha Saladi (publisher not named; quotes Dan Olsen) | How to craft more effective product problem statements | Practitioner or vendor article | 2026-07-27 | Partly: anatomy, frameworks list |
| ProductPlan | ProductPlan | Guide to writing an effective problem statement | Vendor blog | Not shown | Partly: components including scope and measurability |
| Mountain Goat | Mike Cohn, Mountain Goat Software | 7 Ways to Get the Best Estimates of Story Size | Vendor (training) blog | Updated 2024-06-24 | Yes, for estimation practice |
| Morelli | Dr. Katherine E. Morelli, Harvard Graduate School of Education | How to Focus Your Problem Statement | University writing guide | 2024 | Partly: gap/orientation/impact/significance, symptoms versus root cause |
| Barrows | Ed Barrows (Babson / Harvard-affiliated, publisher not named) | Four steps to improved problem solving | Academic practitioner article | Not shown | Partly: define, decompose, analyze, act |
| Hermanto | Alvin Hermanto, Medium | Problem Framing: What it is and How to Write a Problem Statement | Practitioner blog | 2021-04-26 | Partly: 5W canvas, current/consequence/ideal |
| Abraham | Marc Abraham, marcabraham.com | My Product Management Toolkit (4): Problem Statements | Practitioner blog | 2016-02-07 | Partly: d.school formula and characteristics |
| Goetzmann | Jens-Fabian Goetzmann (RevenueCat) | PM 101: Define the Problem Before the Solution | Practitioner blog | 2019-05-12 | Partly: problem document fields |
| Piteiu-Apostol | Raluca Piteiu-Apostol, LogRocket blog | An overview of the problem space | Vendor blog | 2024-06-11 | Partly: research plan, bias table |
| Verma | Rohit Verma, Medium | Unraveling McKinsey's Approach | Practitioner blog | 2023-12-09 | Little: 8 steps; case figures unsourced |
| Smalley | Art Smalley, Lean Enterprise Institute | Standardize Your Problem-Solving Approach? Why One Size Does Not Fit All | Nonprofit institute Q&A (promotes his book) | 2019-01-30 | Little for sizing: four types of problems |
| Brereton | Jake Brereton (page carries a Dotwork ad) | Solving the Product Problem Statement | Vendor-hosted article | 2023-02-25 | Little: generic |
| Evans | Kyle Evans, Medium | 7 Ways to Elevate Product Thinking | Practitioner blog | 2018-12-11 | Little: value over estimates |
| Radford | Dan Zirkelbach / Fred Radford, Product School | Solving Product Management Problems with 8×8's PM | Course seller AMA | 2023-01-09 | Little: "multiply estimates by 4" |
| pmo365 | Laith Adel, pmo365 | The Guide to Effective Product Management | Vendor blog | 2021-07-06 | No: generic process |
| Creately | Amanda Athuraliya, Creately | 7-Step Product Management Process | Vendor guide | Updated 2026-08-19 | No, except the support-ticket advice |
| AI summary | Search assistant answer at the top of the batch | — | AI search answer | — | Not cited |

Pieces that were mostly off-topic for sizing: pmo365, Creately, Smalley,
Barrows, Evans, Radford and Brereton. They are kept above for completeness.
