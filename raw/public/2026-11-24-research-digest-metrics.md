<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Success metrics: research knowledge

What this is: everything important from Juan's two research batches on success metrics (uploaded 2026-11-21, about 39 articles), written in my own words so the raw pages aren't needed. Short quotes are marked. It was written for the product-copilot playbook. The design decisions drawn from it (feature page fields, the `metric` page type) live in the plan doc, "PM workflow plan for product-copilot skills", section "Gap research: success metrics".

How to read the citations: each claim names its source by a short key in square brackets, for example [Siegel]. Section 6 lists every key with author, publisher, kind and date. **Vendor** means the publisher sells a tool, course or consulting service related to the topic. **Unsourced** means the source gives a number or example with no reference.

Left out on purpose: salary and career-pay content (for example Gupta's comp figures), generic self-help, tool how-to steps (Semrush, Vitally and Jira screens), an AI search summary at the top of batch 2 (it cites other pieces and isn't a source), and one piece on a PM's personal success [Fejzullahu] that isn't about product metrics.

Not covered here: the experiments research. It was done in the thread "Plan PM workflow steps for copilot skills".

---

## 1. Frameworks, methods, models and lists

### 1.1 Feature success metrics method (primary, secondary, guardrail)

- **What:** a method for proving whether one feature delivered its intended result, "while also not wreaking havoc elsewhere in the product" [Siegel].
- **How it works:**
  1. *Define three kinds of metric.*
     - **Primary (value indicator):** did the feature solve the problem it was built for? Example: for a bulk-edit feature built to save time, the primary metric is time saved, not whether people used it.
     - **Secondary (usage indicator):** adoption and engagement, such as the share of target users who engage, time to first use, and return usage. Useful but not sufficient.
     - **Guardrail ("don't break stuff"):** things the feature must not harm, such as conversion rate, page load time, support ticket volume, or the cloud bill.
  2. *Define success before measuring.* For each metric, set a **success threshold** (the minimum improvement that counts as success, such as "at least 25% reduction in time-to-completion") and a **failure threshold** (the point where you intervene, such as "conversion dropped by 5% against an expected 0% change"). "Not successful" isn't "failure": a feature with less impact than hoped may still be worth keeping, while one that made things worse may need to be removed.
  3. *Build measurement before the feature:* tracking and logging, dashboards, a pre-launch baseline, and alerts for bad trends.
  4. *Plan the check-ins before launch.* Default schedule: baseline before launch; daily guardrail checks in week 1; weekly reviews of value and adoption in weeks 2 to 4; monthly checks in months 2 to 3; a full analysis against the original goals at quarter end.
- **Ownership:** the PM owns the feature's success metrics. They make sure the right metrics are tracked, actually monitored, and acted on.
- **Alignment chain:** feature success metrics roll up to team OKRs, which roll up to the company North Star.
- **Best practices listed:** measure value, not just what's easy (usage); automate collection, though manual beats none at early-stage companies; set success and failure thresholds up front; use feature flags so rollback is easy; actually come back and check (teams often write metrics into specs and never revisit them); beware correlation vs causation when several teams ship into the same area.
- **When:** any feature launch.
- **Limits:** one short glossary page from a product-tool vendor (Momentum). No evidence offered for the schedule.
- **Sources:** [Siegel].

### 1.2 Five steps to define a success metric (Hustle Badger)

- **Definition used:** a success metric is "the single best quantifiable measure" of how the product is doing over time. It sits alongside a qualitative objective (example: objective "grow our user base", success metric MAU). There are team success metrics (over a quarter or year) and feature success metrics; they're often the same, but a feature can have a more specific one if it's a known driver of the team metric [HustleBadger].
- **Why useful:** clarifies the objective, tracks performance against a baseline, gives a common currency for prioritizing, and shows what drives success [HustleBadger].
- **Core idea:** businesses are valued on one or two headline financial metrics (revenue, profit or EBITDA, ARR for SaaS, GMV for marketplaces). These are *lagging*: slow to move and mixed with other teams' impact. You need a *leading* metric that is responsive but still a direct driver of the lagging one [HustleBadger].
- **The five steps (names only; the detail is behind a paywall):**
  1. Business metric.
  2. Mechanism.
  3. Definition, considering correlation, position in the funnel, time period, absolute vs relative, aggregate vs individual, and the overall result.
  4. Check that it is intuitive, measurable, actionable, and something you can influence.
  5. Iterate.
- **Traps named:** focusing on vanity metrics, treating the metric as the goal, using noisy metrics, failing to move the metric.
- **Limits:** only the outline is visible in the paste. Also points to a "Product Metrics Cheat sheet" spreadsheet, not included.
- **Sources:** [HustleBadger].

### 1.3 Two questions, plus good and bad metric traits (Giannakopoulos)

- **The two questions:**
  1. "Why do people (or I) bother doing this thing?" Answer honestly. "Because it's awesome" doesn't count, and the real answer may be uncomfortable, such as "people sign up for the free trial grab".
  2. "What do people need to do to [answer to question 1]?" The answer gives the intermediate steps, and those steps are what you measure.
- **Turning steps into metrics:** don't map one step to one metric mechanically. Think wider; for example, support tickets from people who can't find feature X measure discoverability.
- **A good metric is:** measurable (not a blended "awesomeness factor"), impactful (connected to a step), actionable (you know what to do when it moves), readable (others understand it and its place in the bigger picture), and relevant (closely tied to what you measure, and it won't get dropped later).
- **A bad metric is:**
  - *Partial:* covers a small part of the story, so a rise means something but a fall may mean nothing. Example: time to click a button.
  - *Vanity-based:* unrelated to the overall goal, such as social presence not tied to visits.
  - *Telling the wrong story:* sound data, wrong reading. Examples: survivorship bias in WW2 aircraft armor, and designing cockpit seats for an "average" pilot who doesn't exist.
  - *Focused on validation:* built to prove a preset view. Check it by asking "What value of this metric will prove that we were wrong?"
- **Cadence:** "as often as it makes sane sense". Weekly is ideal but hard to keep up; monthly is realistic.
- **Targets:** set goals (KPIs) only after monitoring the metric for a while. A goal set at the start is arbitrary; if one is unavoidable, treat it as a best guess and adjust as data comes in.
- **Limits:** personal practitioner essay; no data.
- **Sources:** [Giannakopoulos].

### 1.4 "Company as a machine": decompose the goal into levers (Skok)

- **What:** treat the company as a machine with outputs and levers. Good metrics expose how the machine works, so management knows which lever to pull [Skok].
- **How:** start from the end goals (profit, growth, cash flow) and work backwards by writing each as a formula of its components, then repeat ("peel the onion"):
  - Profit (EBITDA) = Revenue − Cost of Goods Sold − Expenses
  - Bookings = Number of deals closed × Average deal size
  - Reseller revenue = Productive resellers × Average productivity per reseller
  - Deals closed = Productive salespeople × Average productivity per salesperson, and also = Trials × Conversion rate
  - Trials = Site visitors × Conversion rate to trial
  - Visitors = Normal traffic + for each campaign (target audience × conversion rate to visitor)
- **Balance warning:** grow linked levers together. Too many salespeople with too few trials, or the reverse, throws the machine out of balance.
- **Funnel tracking:** for every funnel stage track two numbers: volume through the stage and conversion to the next stage (campaigns → visitors → trials → closed deals, plus overall visitor-to-deal conversion). Track each over time to see trends early.
- **Inside-sales example:** individual performance = deals closed × average deal size. Deals closed breaks into calls made, call-back rate, call-to-demo rate and demo-to-close rate; each one points to a specific fix (peer pressure, voicemail training, value-prop training, demo training).
- **Funnel-wide metrics:** CAC, CAC by lead source, ROI by lead source (cost, conversion and lifetime value per source).
- **What not to track:** prioritize components with the biggest effect; don't track what you can't affect; skip items that are small or don't vary.
- **Bad vs good board meeting:** a weak team blames "a tough market"; a strong team peels back the layers to the real cause (for example, new Facebook ads converting worse to trial) and knows exactly how much traffic it must add.
- **Work back from a target:** from a bookings target you can compute the salespeople, leads and campaign spend needed.
- **Limits:** written for sales-led and SaaS companies; the example is illustrative.
- **Sources:** [Skok].

### 1.5 Building less-flawed metrics (Manheim, peer-reviewed)

- **Problem statement:** metrics distort the systems they measure. Campbell's law and Goodhart's law, as paraphrased by Hoskin: "every measure which becomes a target becomes a bad measure" [Manheim].
- **Four causes of metric failure:**
  1. *Task-appropriate data is hard to find.* "Easy to measure is rarely the same as important". Example: the h-index was designed around the data that happened to be available.
  2. *Imperfect correlation, which collapses at the extremes.* Height correlates with basketball skill, but the tallest people aren't the best players. Correlation also isn't transitive: tall people and coordinated people both do better at basketball, but very tall people tend to be less coordinated.
  3. *Using non-causal correlates as incentives creates perverse effects.* Example: grading students on the number of questions they ask rewards useless questions.
  4. *The goal is unknown, incoherent, or conflicting.* Examples: a committee with different values; education's mixed goals, where GPA correlates poorly with long-term outcomes.
- **Desiderata (properties in tension with each other):** cost, availability, immediacy, simplicity, fairness, trust, non-corruptibility.
- **Design considerations:**
  - *Coherence:* if goals are fuzzy, no metric captures them. "Strategy surrogation" is when managers forget that a measure is a proxy and treat it as the goal.
  - *Causal forethought:* use a theory of change. Example: rewarding attendance may just put sleeping students in seats.
  - *Structured discussion and compromise:* for conflicting goals; satisfice (Herbert Simon). Costly.
  - *Pre-gaming:* imagine how the metric will be gamed, like a pre-mortem, and design against it, but don't dictate methods so tightly that you stifle better approaches.
  - *Monitoring behaviors:* set checkpoints, because metrics drift. Example: overzealous sales show up later as lower repeat sales.
  - Effort spent on metric design should match the stakes.
- **Metric features and strategies:**
  - *New data sources:* novelty briefly resists gaming.
  - *Diversification:* several measures triangulate a goal.
  - *Aggregation:* a composite eases evaluation but hides detail and adds complexity.
  - *Secret metrics:* participants can't game what they don't know; secrecy degrades over time and hurts fairness.
  - *Post hoc specification:* choose the metric after the actions; risks unfairness and corruption.
  - *Randomization:* random weights make gaming harder but feel unfair.
  - *Soft metrics:* human judgment and peer review.
  - *Limiting maximization:* set a standard to meet instead of a number to maximize. Caution: a limit tends to become the target, as with flight duty times.
  - *Abandoning metrics:* when the perverse effects outweigh the benefit; consider measuring for diagnosis rather than reward.
- **Six-step design process:**
  1. Understand the system: scope, what the metrics are for, its causal structure (logic model), stakeholders.
  2. Identify goals: immediate and longer-term.
  3. Identify which desiderata matter.
  4. Brainstorm measures: outcomes, data sources, what's easy, how measures relate to outcomes, what's not captured.
  5. Consider and plan: how measures become metrics, whether for diagnosis or incentives, soft metrics to triangulate, avoiding a reward/punish split, pre-mortems.
  6. Plan revisits: a set date or interval plus triggers for an unscheduled review.
- **Limits:** focused on incentive systems (academia, policy, employees), less on product features.
- **Sources:** [Manheim]. Related points in [12Char], [LSA] (Wells Fargo), [Gupta] (counter-metrics).

### 1.6 Measure-Perform-Review-Adapt (Balanced Scorecard Institute)

- **What:** the institute's framework for developing and running a KPI system [BSI].
- **Pre-measurement:**
  - *Launch:* leadership engagement, explaining why to measure, teams and roles, process, automation, performance culture.
  - *Articulate strategic intent* with a goal framework (Balanced Scorecard, SMART, MBO, OKRs, WIGs). "If you don't know what you are trying to accomplish, it is too early for KPIs."
- **Measure:**
  1. Identify objectives (qualitative, continuous-improvement outcomes) and their intended results (unambiguous).
  2. Find alternative measures: a direct measure of the result first; if none, indirect measures built from a hypothesis of correlation or contribution, using a logic model, cause-effect analysis, or process flow analysis.
  3. Select measures by scoring options on strength and data availability. A good measure answers users' key questions, informs decisions, is valid, encourages good behavior, and avoids undue data burden or side effects.
  4. Document each one in a **Performance Measure Data Definition Table**, so it's calculated the same way every period.
- **Perform** (usually quarterly):
  - *Set targets and thresholds:* the target is the desired level for a period; thresholds are the upper and lower limits around it, which set the green, yellow and red points.
  - *Implement improvement initiatives:* a short list of experiments, not a long project list.
- **Review:** collect and visualize trends; analyze each action's effect against targets and thresholds.
- **Adapt:** were the strategies effective and assumptions valid? This can lead to re-forecasting targets, new initiatives, or recalibrating strategy. The framework borrows agile's assumption that you can't know everything at the start.
- **Limits:** consulting firm's own method, wrapped in a sales pitch.
- **Sources:** [BSI].

### 1.7 Twelve characteristics of effective performance metrics

Source has no author in the paste; it reads like a BI/data-warehousing guide [12Char].

1. **Strategic:** start from the goals and work backwards; all the metrics together tell the strategy's story.
2. **Simple:** people know what's measured, how it's calculated, the target, the incentives, and how to affect it. Composite indexes are hard to act on. (Quote from an energy services director about teaching technicians how the repeat-call metric works.)
3. **Owned:** every metric has an accountable owner, sometimes two to encourage teamwork.
4. **Actionable:** when it falls, people know what to do. "Sales of a specific segment are falling" is more actionable than "sales are falling". People need the authority to act.
5. **Timely:** updated often enough to intervene in time.
6. **Referenceable:** users can see its metadata: owner, last update, calculation, source systems.
7. **Accurate:** clean source data. Example of a misleading formula: revenue per worker rises with inflation even if nobody got more productive. Survey and absenteeism measures of satisfaction are both flawed.
8. **Correlated:** check that the metric actually drives the outcome you want; refresh it.
9. **Game-proof:** "Users always look for loopholes in your metrics." Example: one company hires a research firm to audit customer surveys.
10. **Aligned:** metrics don't undermine each other ("sub-optimization").
11. **Standardized:** agreed definitions of terms like sales, profit and customer, so dashboards roll up.
12. **Relevant:** metrics have a life cycle; they energize at first, then lose impact and need refreshing or retiring.

### 1.8 SMART criteria

- **What:** Specific, Measurable, Achievable (or Attainable), Relevant, Time-bound [Semrush] [Asana] [Atlassian] [NetSuite] [Passio] [Spider].
- **Variants:**
  - [Semrush] uses it for KPIs and adds an example ("reduce support response times by 20% within three months").
  - [Atlassian]'s example: bad KPI "respond to customers faster"; good KPI "answer all customer messages within 2 hours during business hours by June 30".
  - [Spider] adds "Actionable" and drops "Specific" for KPI criteria.
  - [Passio] lists SMARTs as individual-employee goals alongside "Big 3s" (each team's top three priorities, with a share of time) and "EOS Rocks" (quarterly goals in the Entrepreneurial Operating System).
- **Limits:** a checklist for wording a goal; it says nothing about whether the metric is causal or gameable [Manheim].

### 1.9 KPIs vs OKRs, and a combined framework

- **The distinction:**
  - [LogRocket]: KPIs are barometers of baseline health (business as usual); OKRs set ambitious, outcome-oriented goals to drive change where KPIs show a gap.
  - [Atlassian]: KPIs are ongoing vital signs that stay stable; OKRs are aspirational stretch goals for transformation (example: KPI tracks market share; OKR is "expand into three new markets in six months").
  - [Rego]: KPIs and OKRs both look forward, while "performance metrics" describe today.
- **LogRocket's seven-step combined framework** (customer service example):
  1. Define objectives aligned with company goals.
  2. Define KPIs reflecting them (CSAT, first response time, resolution time, share handled manually).
  3. Find areas to improve from the KPI data and dig into causes.
  4. Set OKRs (for example "improve first response time by 50% within a timeframe").
  5. Define initiatives (automation, triage, SLAs, templates).
  6. Prioritize by impact and feasibility, treating them as hypotheses.
  7. Test, monitor the KPIs, and repeat.
- **Sources:** [LogRocket] [Atlassian] [Rego].

### 1.10 Ways to classify metrics

Each source slices metrics differently. All of them, listed so the playbook can map between them:

- **Input / output / outcome / process** [Semrush]:
  - *Input:* resources and effort, such as marketing spend or hours worked.
  - *Output:* direct results, such as units made or sales volume.
  - *Outcome:* broader effect, such as a CSAT rise after a new service strategy.
  - *Process:* efficiency of stages, such as response time or issues resolved per hour.
- **Input / output (product sense)** [Atlassian comments]: input metrics are what the team controls and moves (for example first-time-user-experience completion); output metrics are driven by inputs (for example DAU).
- **Leading / lagging:** leading predicts, lagging confirms. Almost every source uses it [Asana] [LSA] [Monday] [Atlassian] [Rego] [NetSuite] [HustleBadger] [ProductSpace]. Examples:
  - Pipeline volume vs quarterly revenue [Asana].
  - Burning 750 extra calories a day vs losing 15 pounds [LSA].
  - Risk register updates, velocity trends, backlog growth and stakeholder engagement vs budget variance, CSAT, ROI and on-time completion [Monday].
  - Trial signups vs MRR [ProductSpace].
  - The same metric can be lagging for one function and leading for another: recruiting metrics lag for HR but lead for the business [NetSuite].
- **Quantitative / qualitative** [Atlassian] [Rego] [NetSuite]:
  - [Rego]: qualitative metrics "tell a story and don't involve numbers" (feedback, surveys); they answer why.
  - [NetSuite]: qualitative metrics are numeric scores of judgments (CSAT, NPS, brand value).
- **Objective / subjective** [HBS] (Robert Simons): objective measures can be independently verified; subjective ones need judgment (for example employee engagement) and work only when employees trust managers to apply them fairly.
- **Primary / secondary** [ProductSpace]: primary metrics tie directly to strategic goals; secondary ones explain what drives them. This axis is about *importance*, while leading/lagging is about *timing*, so a metric can be any combination. In [Siegel], "secondary" means usage indicators specifically.
- **Guardrail / counter-metric:** a metric that must not get worse while you push the primary [Siegel] [Gupta] [ProductSchool].
- **Business / process / investment / agile** [Rego]:
  - *Business-based:* for leadership; ROI, payback, profitability, market share, NPS, benefits realized vs planned.
  - *Process-based:* PMO view; schedule, financial, risk, resource management.
  - *Investment-based:* health of one investment, to continue or stop it; percent complete, budget variance, burn rate.
  - *Agile:* throughput, lead time, defect trend, epic lead time ratio, turnaround time.
- **Measure / metric / KPI** [Spider]:
  - *Measure:* a single raw data point or the system that produces it.
  - *Metric:* measures over time, with context and often a goal or benchmark; the number of visitors today is a measure, conversion rate is a metric.
  - *KPI:* the vital few metrics tied to strategic goals.
- **Seven types of performance metric** [NetSuite]: business, financial, operational, sales, project management, marketing, employee (formulas in 1.24).
- **By team** [Asana]: general business, marketing, customer success, sales, developer, HR (lists in 1.25).
- **Three product KPI categories** [Atlassian16]: business performance, customer and user engagement, product development (lists in 1.21).
- **Four product KPI categories** [Wrike]: business performance, product usage, product development, product quality. Measurement types: activity (a count), outcome (progress on a result), project (progress of work), target (a deadline-bound amount).
- **Metrics pyramid** [Gupta]: business metrics at the top (MRR, LTV, profitability; for executives), product metrics in the middle (retention, conversion, North Star; owned by the PM), engagement metrics at the bottom (DAU, session length, feature adoption; the daily levers). Assumes a causal chain: engagement drives product success, which drives business results.
- **By stage of product life:**
  - [ProductSpace]: early = acquisition, activation, engagement; growth = retention, conversion; mature = monetization, efficiency, reducing churn.
  - [ProductSchool]: early = TTFV, goal completion, cohort retention, North Star; growth/mature = expansion, usage diversity, adoption velocity, stickiness.
  - [Gainsight]: hyper-growth = CAC and time to value; mature SaaS = stickiness and retention.
- **By stakeholder** [ProductSpace]: executives look at revenue, growth and market share; marketing at acquisition, conversion and traffic sources; engineering at performance, bugs and uptime; customer success at churn, retention and CSAT.

### 1.11 North Star Metric

- **What:** the single metric that best captures the core value the product delivers to customers [Gupta] [ProductSchool] [ProductSpace].
- **Criteria:**
  - [Gupta]: measures customer value (only rises when users get real value), reflects product strategy, is a leading indicator of revenue (if it rises while revenue is flat, monetization is broken), and isn't a vanity metric.
  - [ProductSpace]: reflects long-term growth, aligns with user value, drives strategic decisions.
- **Examples, all unsourced and repeated across sources:**
  - Airbnb nights booked; Spotify minutes streamed; Slack messages sent per team [ProductSpace] [ProductSchool].
  - Slack's is "teams that send over 2,000 messages" [Gupta].
  - By business model [Gupta]:
    - SaaS: weekly active teams completing the core action (Asana: tasks completed per week).
    - Marketplace: successful transactions (Airbnb nights booked).
    - E-commerce: weekly repeat purchasers (Amazon Prime items delivered).
    - Media: time spent (YouTube watch time).
    - Social: daily active users sending a message (early Facebook: users with 7 friends in 10 days).
- **Stress test** [Gupta]: ask key stakeholders "If we could only improve one number for the next 12 months…" and see whether they agree.
- **Chain** [Siegel]: feature success metrics → team OKRs → North Star.
- **"Magic metric"** [Holmes]: a metric your own analysis has shown drives your most important goals; close in spirit to a North Star.
- **Limits:** a single number invites gaming and tunnel vision; pair it with counter-metrics (see 4.1).

### 1.12 AARRR ("pirate metrics")

- **Stages and metrics** [Gupta]:
  - *Acquisition:* key metric CAC = total sales and marketing spend ÷ new customers. Segment it by channel, because a blended average hides channels that lose money.
  - *Activation:* the "aha" moment. Find the user actions that correlate with long-term retention. Examples: Dropbox's one file in one folder on one device; Facebook's friends early on. Metrics: onboarding completion, time to the first key action, share hitting the aha moment in the first session.
  - *Retention:* cohort analysis by signup week or month. A curve that flattens means product-market fit. For early-stage B2B SaaS, "even a 10-15% flat retention curve" means a core group loves it (unsourced).
  - *Referral:* K-factor = invites sent per user × invite conversion rate. Above 1.0 is viral and rare; 0.2 to 0.4 can still cut CAC noticeably (unsourced).
  - *Revenue:* LTV and LTV:CAC; LTV should be at least 3× CAC (unsourced rule of thumb, repeated by [Dovetail] and [HubSpot]).
- **Variants:**
  - Acquisition → Activation → Conversion → Engagement → Revenue → Retention [Atlassian comments].
  - Subscription lifecycle of acquisition, engagement, referral, retention [Holmes].
  - [ProductSpace] groups its 15 metrics as acquisition, conversion, engagement, retention, revenue (see 1.18).

### 1.13 HEART (Google)

- **Categories** [Gupta]:
  - *Happiness:* NPS, CSAT (good for one feature or support interaction), app store ratings.
  - *Engagement:* depth of use. Session length alone can mislead, since a long session can mean confusion.
  - *Adoption:* people trying a new feature for the first time. Example: share of active users who applied a new photo filter in the first week.
  - *Retention:* habit and stickiness.
  - *Task success:* task completion rate, time on task, error rate.
- **Positioning:** a counterweight to growth-only AARRR. "AARRR is your telescope, HEART is your microscope": use AARRR to spot a leak in the funnel, HEART to see why users drop off.
- **Sources:** [Gupta]. HEART is already a playbook concept (`heart-framework`).

### 1.14 Goal Tree (with OKRs)

- **What:** a visual tree with the ultimate goal at the top and sub-goals, metrics and initiatives branching below [Alwan].
- **Steps:**
  1. Envision the product's future: the problem and the long-term impact.
  2. Set objectives as stepping stones.
  3. Pick key results: the tangible metrics for each objective.
  4. Find **proxy metrics**: touchpoints in the user experience that move the key metrics, each with its own metric. These are the indirect indicators that tell you what to work on next.
- **After building the tree:**
  1. Add initiatives under the objectives.
  2. Prioritize initiatives by value.
  3. Generate opportunity hypotheses (specific features) under each.
  4. Prioritize those by value and effort.
  5. Validate before building.
  6. Monitor; use segmentation, cohorts and workflow analysis.
- **Story:** used by the author's product strategy team at FOX (FOX Sports, FOX NOW, FOX Nation) to fix misalignment.
- **Limits:** "Salesforce uses goal trees" is asserted without a source. Author runs a consultancy (PRODUCT360).
- **Sources:** [Alwan].

### 1.15 Metrics One Pager

- **What:** a page with business metrics on top and product metrics (acquisition, activation, engagement, retention) underneath, showing how they link [Stukan].
- **Method:** map how your initiatives connect to business metrics; precision matters less than being able to tell the story. Phrase proposals as a causal chain, for example: "By improving this specific user behaviour, we expect to increase the Lifetime Value of this customer segment, which supports our 10% annual revenue growth goal."
- **Sources:** [Stukan].

### 1.16 Balanced scorecard

- **What:** combines the financial perspective with customer, internal process, and learning and growth perspectives, so intangible assets (research capability, brand loyalty, customer relationships) get measured [HBS] (Simons). The four perspectives are listed in [NetSuite]'s FAQ.
- **Used by:**
  - Data and analytics leaders, at enterprise, department and team level [IIA].
  - [BSI] as one way to articulate strategy.
  - [LSA] as "balanced measurement": financial, customer, employee, operational, innovation.
- **Already in the playbook** as a related idea under OKRs and strategy.

### 1.17 Diagnostic control systems and the profit plan (Simons)

- **Diagnostic control systems:** information systems managers use to monitor outcomes and correct negative performance, such as performance scorecards, project monitoring, HR systems and standard cost accounting [HBS].
- **Profit plan:** the expected revenue and expenses for a period, laid out as an income statement. It holds managers accountable for revenue, expense and profit targets.
- **Simons' three questions:** does the business make enough profit to cover costs and reinvest? Does it generate enough cash to stay solvent through the year? Does it return enough to investors?
- **Non-financial goals:** quality, customer satisfaction, engagement and ethics feed the financial results. Tom Polen (Becton Dickinson): "we'll never sacrifice a quality goal for a financial goal."
- **Sources:** [HBS].

### 1.18 Funnel metrics with formulas (The Product Space, 15 metrics)

All from [ProductSpace]:

- **Acquisition:**
  - CAC = marketing and sales spend ÷ new customers.
  - Traffic sources: the channel mix.
  - Sign-up rate = sign-ups ÷ visitors × 100.
- **Conversion:**
  - Activation rate = activated users ÷ new sign-ups × 100, where "activated" means doing a key action that shows core value.
  - Time to value: sign-up to first key action, averaged over a cohort.
  - Drop-off rate = users who abandon a step ÷ users who enter it × 100.
- **Engagement:**
  - DAU and MAU, and stickiness = DAU ÷ MAU.
  - Session length = total session time ÷ number of sessions.
  - Feature adoption rate = users who used the feature ÷ total users × 100.
- **Retention:**
  - Churn = customers lost ÷ customers at the start × 100.
  - Retention = (customers at end − new customers) ÷ customers at start × 100.
  - NPS = % promoters − % detractors.
- **Revenue:**
  - MRR = sum of recurring revenue from active subscriptions in a month.
  - ARPU = revenue ÷ users.
  - CLTV = average purchase value × purchase frequency × customer lifespan.
- **Bonus:** CSAT (average rating on a 1 to 5 scale); bug or issue rate (reports per week or month, compared with usage).
- **Advice:** cross-reference metrics (high acquisition with low retention suggests onboarding problems); revisit metrics as the product evolves.

### 1.19 Metrics by product type (Holmes, Department of Product)

Holmes' stance: the value of metrics is discovery, such as finding out the product can't sustain itself beyond six months, or that an API earns more than display ads. Dashboards used to look clever don't build good products. The lists below are inspiration, not essentials [Holmes].

- **General:**
  - NPS: "How likely are you to recommend…?" on 0 to 10; promoters 9 to 10, detractors 0 to 6; NPS = % promoters − % detractors. The result is a number, not a percentage. Review monthly or quarterly and ask low scorers why.
  - Revenue.
  - Actions: the product-specific action tied to its value, counted over a period.
  - Magic metric: the one your own analysis shows drives your key goals.
  - MRR: slice it by dimensions such as plan or company size.
  - Churn: % of customers who stop, usually monthly.
  - Cost per acquisition: compare it with LTV.
  - Virality or referrals: % who refer someone.
  - LTV.
- **E-commerce:**
  - Orders; average order value.
  - Cart abandonment (filled a cart, didn't reach checkout); checkout abandonment (reached checkout, didn't buy).
  - Product searches.
  - Average shipping cost (when does delivery cost kill the sale?).
  - Repeat customers (% with at least one past order).
  - Revenue; visits; visit-to-sale conversion (split by category on large sites).
  - Shipping time.
  - CPA (if average order is $50 and CPA is $80, look at LTV); LTV.
  - Mailing list effectiveness (open, click and sales conversion).
  - Virality.
- **API products:**
  - API calls (proves use; borderline vanity).
  - Failure rate.
  - Actions per month (sending a text, booking a room); better than raw calls.
  - Revenue tied to calls or actions.
  - Support tickets caused by API problems.
  - Uptime and downtime.
  - Client retention month on month.
  - Number of external customers.
- **Content sites** (usually ad-funded on CPM):
  - Ad click-through rate; ad CPM (cost per thousand impressions).
  - New vs returning visits.
  - Bounce rate (useful per landing page, not site-wide).
  - Pages per user.
  - % of users who share content (matters only if growth relies on virality).
  - Most-viewed content.
  - Email subscriber rate.
  - Revenue per visit.
- **Subscription / SaaS** (lifecycle: acquisition, engagement, referral, retention):
  - CPA (should be below LTV).
  - Leads (defined by you); visit-to-lead %; visit-to-subscription %.
  - Subscriber LTV.
  - Package breakdown (also shows bundling options).
  - Churn: example, 100 subscribers in month 1 and 95 of them in month 2 means 5% churn; retention is the opposite.
  - Actions per month.
  - % activations ("activate" defined per product, for example converting from trial).
  - % active users ("active" defined by you; spot lapsed users before they cancel).
  - MRR.
- **Mobile apps:**
  - Downloads; activations; uninstalls.
  - DAU; MAU.
  - Session length (higher usually better, but an app that anticipates needs may have short sessions).
  - Session interval (time between opens; shows stickiness).
  - Store ratings.
  - In-app purchases.
- **Lead generation:**
  - Leads-to-customers ratio (low means poorly qualified leads or a product that doesn't fit; ask them why).
  - Bounce rate per landing page; visit-to-lead %.
  - Lead form abandonment.
  - Content downloads.
  - Qualified leads (definition evolves through experiments); qualified visit %.
  - Email subscriber rate; email unsubscribe rate.
  - Dwell time (averages distorted by tabs left open; dig deeper).

### 1.20 Product School's 13 product success metrics

From [ProductSchool], a course seller. Definitions are reasonable; the stage mapping is in 1.10.

1. **Time to first value (TTFV):** first value event time − signup time. Example: sign up 2:00 PM, first design 2:15 PM, TTFV 15 minutes.
2. **Feature adoption depth:** users actively using key, high-value features ÷ active users × 100. Example: 25% vs 80% using a reporting dashboard tell different stories.
3. **Retention by cohort:** users retained in a period ÷ cohort size at start × 100. Example: 100 January signups with 30 active in April gives 30% three-month retention. Cut by signup date, channel, onboarding path or plan.
4. **Customer expansion rate:** (end revenue − start revenue) ÷ start revenue × 100 for the same customers. Example: $100K to $130K is 30%.
5. **Product usage diversity:** average features used per user, or % using three or more core features.
6. **North Star Metric:** see 1.11.
7. **Adoption velocity:** % of active users using a new feature within 7, 14 or 30 days of launch. Slow adoption may mean poor discoverability, unclear value or usability problems.
8. **Support ticket volume per active user.** Example: 500 tickets from 5,000 users is 0.1. A counterbalance to engagement metrics.
9. **Referral rate:** % of users who refer at least one new user. Example: 200 of 5,000 is 4%.
10. **Goal completion rate:** successful completions ÷ attempts.
11. **Stickiness (DAU/MAU).** Example: 6,000 ÷ 24,000 is 25%.
12. **Product-qualified leads (PQLs):** users whose behavior shows they're sales-ready (finished onboarding, invited teammates, integrated tools).
13. **User sentiment by feature:** targeted surveys, feedback tagging, qualitative analysis.

How to choose [ProductSchool]:

- Pick 3 to 5 metrics for current priorities and review them quarterly.
- Ask "what decisions will this metric help us make?"
- Map metrics to business goals: expansion revenue points to expansion rate and PQLs; a retention push points to cohort analysis and sentiment.
- Involve the cross-functional team, and pair numbers with qualitative insight.
- Traps: activity instead of outcomes (clicks vs task completion); over-focusing on acquisition when churn is the problem; relying on one metric such as DAU; setting targets without knowing what success looks like.
- Beyond metrics: define success collaboratively and early, close the feedback loop, value momentum over milestones, and keep the team clear on goals.

### 1.21 Product management KPI lists from vendors

- **Atlassian, 16 KPIs** [Atlassian16]:
  - *Business:* gross revenue, net revenue, gross margin, net margin.
  - *Customer and engagement:* conversion rate, retention rate, CAC, CLV, NPS, ARPU, churn, customer satisfaction.
  - *Development:* time to market, defect density (defects ÷ codebase size), feature adoption rate, team velocity.
  - Review cadence: weekly or monthly early on, quarterly or annually as the product matures; critical KPIs more often than supporting ones.
- **Productboard, 11 KPIs** [Productboard]: product adoption, satisfaction and engagement, time to market, retention, conversion (free or trial to paid), revenue and lifetime profitability (growth, ARPU, gross margin), feature adoption, competitive analysis (share, perception), quality and error report rate, execution against the roadmap, portfolio expansion.
  - *How to choose:* define objectives, identify relevant metrics, prioritize impact, check measurability and data, set specific realistic targets, involve stakeholders, keep it actionable, review.
  - *How to track:* measurement methods, a reporting system, tracking frequency, an owner per KPI, regular review, adapt, communicate.
- **Wrike** [Wrike]:
  - Build five to six KPIs across business performance, usage, development and quality.
  - Four-step structure: (1) outline the measurement (activity, outcome, project or target); (2) describe the outcome as a specific number by a date, in the same unit as the measurement; (3) state the data source; (4) set tracking frequency, monthly or quarterly.
  - Example KPIs:
    - "Increase NPS by 20%".
    - "Gain two places on Gartner's Quadrant".
    - "Improve customer count for a feature by 45% by February 2022".
    - "Reduce time to onboard new users by 28% by next quarter".
    - "Gain 2,200 new users for the reports feature in six months".
    - "99% on-time deliveries".
    - "Resource utilization above 90%".
    - "Fewer than 200 monthly support tickets".
    - "Defect rate under 2%".
  - Error to flag: the article says NPS "includes the percentage of users adopting the new feature", which is wrong; NPS is a single recommendation question.
- **Gainsight, 10 metrics** [Gainsight]:
  - *Product-level:* user retention (users, not accounts; B2B accounts have many users), time to value (identify the value milestone first; enterprise products may take months), DAU/WAU/MAU (pick the interval that fits usage: daily for email, monthly for travel booking), customer effort score (a leading indicator of retention), stickiness (more important as a product matures), adoption rate (feature adoption as a proxy for product adoption).
  - *Business-level:* CAC (product-led conversion lowers it; track trial-to-paid), churn (example: 500 customers to 460 in a quarter is 8%; B2B usually annual renewals, consumer monthly), NRR (revenue change from existing customers including upgrades, downgrades and churn, excluding new customers; MRR can hide dissatisfaction because new customers mask losses), NPS, CSAT.
  - Advice: keep it simple, start from goals, segment users.
- **Aha!, 15 SaaS metrics** [deHaaff]:
  - *Marketing:* monthly unique visitors; CAC (example: $1,000 campaign bringing 10 customers is $100 each; segment by source); organic vs paid traffic.
  - *Customer success:* conversion rate to customer (trial or lead to paid); support tickets created (a rise can mean more users or a usability problem); first response time; time to close a ticket; churn (customers and revenue; plan for a "healthy" amount, since some customers always cancel).
  - *Business operations:* active users; new MRR (new customers only); add-on MRR (expansion from existing customers); total new MRR (net of add-on and churn; high new MRR with low total new MRR means you lose as many as you add); ARR = MRR × 12; ACV; LTV = average monthly revenue × average lifetime in months.
  - Example: paying $4,000 CAC is sensible when ACV is above $16,000, since you'd recover it in the first quarter.
  - Vendor note: written by Aha!'s CEO, with claims about Aha!'s own growth.
- **Plugseal, 7 metrics** [Plugseal]: CAC, CLV, NPS, MRR (paying users × ARPU), churn, engagement, CSAT (share of 4 to 5 ratings). Tips include benchmarking against industry standards.

### 1.22 Customer success metrics (account health)

Off-topic for single features but common in the batch; useful for the wiki's customer pages.

- **Dovetail, 10 metrics** [Dovetail]:
  - Churn = churned ÷ customers at start × 100. Example: 10 of 100 is 10%.
  - LTV: subscription = average monthly revenue ÷ churn rate; non-subscription = average purchase value × purchase frequency × engagement time.
  - CAC = sales and marketing spend ÷ new customers.
  - Retention = (end − new) ÷ start.
  - Customer retention cost = retention program cost ÷ active customers.
  - Customer health score: custom indicators (usage frequency, support tickets); there's no universal "good" score.
  - CSAT = positive responses ÷ responses × 100. Example: 70 of 100 is 70%. Survey at several journey points (after support, before renewal, 24 hours after purchase).
  - MRR = average revenue per customer × active customers. Example: 10 × $100 is $10,000.
  - Customer effort score (agreement with "it was easy to…" on 1 to 10).
  - NPS, surveyed 7 to 30 days after use, then ask why.
  - Errors to flag: its MRR growth formula is written backwards ((previous − current) ÷ previous), and it gives the NPS scale as 1 to 10.
- **HubSpot, 15 metrics** [HubSpot]:
  1. Health score: weighted blend, "typically 40% usage, 30% support health, 30% business results", in green, yellow and red bands that drive expansion, enablement or save plays.
  2. NPS on 0 to 10 with passives 7 to 8.
  3. Qualitative feedback coded into themes.
  4. Churn: exclude new customers from the denominator. Example: 64 of 1,000 is 6.4% monthly. Its annualized figure, written as "(1 − 0.936)^12 ≈ 52%", has the wrong formula; correct is 1 − 0.936^12 ≈ 55%.
  5. MRR = customers × ARPU, plus expansion and contraction MRR. Example: 1,000 × $750 is $750K; +$25K upsell − $10K downgrade is +$15K net new.
  6. CLV (non-SaaS formula; SaaS = MRR ÷ churn). Example: $1,000 ÷ 5% is $20,000.
  7. Customer retention cost; "healthy" CRC:CLV under 1:3.
  8. Customer effort score on 1 to 7 ("target > 5.0").
  9. First contact resolution ("benchmark 75 to 85%").
  10. CSAT as share of 4 to 5 star responses ("target 80 to 90%").
  11. Renewal rate ("healthy SaaS > 90%").
  12. Product usage rate (% of accounts meeting weekly usage thresholds).
  13. Time on platform.
  14. Active users by license type and tenure.
  15. Free trial conversion = paid ÷ trials × 100.

### 1.23 Product quality and engineering metrics

- **Xray, six product quality metrics** [Xray]:
  1. Defect rate, linked to feature area and timing (late defects can delay releases).
  2. Test automation measured by functional coverage, not code coverage.
  3. Mean time to green: how long a failed build takes to go green; the same idea applies to incident SLAs.
  4. Speed of development (productivity, an indirect influence on quality).
  5. Defect rate relative to automated tests (are the tests catching defects?).
  6. Quality of acceptance criteria.
  - Warnings: separate product metrics from productivity metrics, and avoid team-comparison vanity metrics (velocity per team, commits per person). Publish numbers with a narrative; defect counts mean little until tied to components.
  - Inspired by DORA. Vendor (test management tool).
- **DORA metrics** [LogRocket]: lead time for changes (commit to production) and deployment frequency. The paste names only these two of the four.
- **ITSM metrics** [ServiceNow]:
  - *Incidents:* mean time to resolution, self-solve %, call deflection, first call resolution, volume trends.
  - *Changes:* success rate, lead time.
  - *Problems:* resolution time, age of open problems.
  - *Requests:* fulfillment time, CSAT.
  - Value measurement: ROI, cost savings, productivity gains, service quality.
  - Vendor.
- **Agile metrics:** throughput, lead time, cumulative defect trend, epic lead time ratio, turnaround time [Rego]. Time to market, defect density, velocity [Atlassian16]. Velocity should not be the only measure [MondayAgile].

### 1.24 Project and operational performance formulas

- **Project management KPIs** [Monday]:
  - *Schedule:* on-time completion = on-time ÷ total × 100; schedule variance (SV) = EV − PV; cycle time = end − start; milestone rate = met ÷ total × 100.
  - *Budget:* budget variance = actual − budgeted; cost performance index (CPI) = EV ÷ AC; ROI = (benefits − costs) ÷ costs × 100; earned value (EV) = % complete × budget at completion.
  - *Quality:* CSAT, defect density = defects ÷ module size, deliverable quality score.
  - *Resources:* utilization = productive ÷ available hours × 100, productivity index, employee satisfaction.
  - *Strategic:* benefits realization = actual ÷ projected benefits × 100.
  - Before locking a KPI, ask: does it relate to a strategic goal? Can it be collected automatically? Do we know how to fix it if it drops? Will sharing it motivate the right behavior?
- **Seven types, with formulas** [NetSuite]:
  - *Business:* gross revenue; ROI; employee turnover; COGS; customer satisfaction rate; revenue vs forecast variance.
  - *Financial:* net income; net profit margin; operating cash flow ratio; debt-to-equity; accounts receivable turnover; days sales outstanding = 365 ÷ AR turnover.
  - *Operational:* production downtime and its cost; throughput; on-time delivery; RMA rate; mean time to repair = maintenance time ÷ repairs; first-time fix rate; SLA compliance.
  - *Sales:* quote-to-close; month-over-month growth; lead-to-sale; CLV; CAC.
  - *Project:* planned value; earned value; resource capacity; CPI; schedule variance.
  - *Marketing:* cost per lead; CTR; lead conversion; CAC payback = CAC ÷ (new MRR × gross margin).
  - *Employee:* payroll-to-revenue; productivity rate; error rate; satisfaction; turnover.
  - Worked examples are in 5.

### 1.25 Metrics by team (Asana) and "seven common success metrics" (Indeed)

- **By team** [Asana]:
  - *General:* gross margin, ROI, productivity (output ÷ input), customer count, recurring revenue.
  - *Marketing:* daily traffic, new users, email open rate, leads.
  - *Customer success:* NPS, retention, churn, feedback, average lifetime, CLV.
  - *Sales:* qualified leads, lead-to-customer conversion, CAC ("as close to zero as possible"), new customers.
  - *Developer:* uptime, bug response time, DAU (a big gap between customers and DAU suggests low value), cycle time, throughput.
  - *HR:* employee satisfaction, retention, feedback.
  - Advice: 5 to 10 metrics per team; balance leading and lagging; review quarterly.
  - Mistakes: vanity metrics, too many, not tied to goals, inconsistent calculation, not acting, not updating.
- **Seven common success metrics** [Indeed]: profit; customer interactions (enquiries, sales and complaints tracked separately, because enquiries rising without sales means a conversion problem); capacity utilization ("realistic 80 to 85%", unsourced); revenue-to-outgoings ratio; marketing engagement; CAC; website traffic.

### 1.26 Internal product KPIs (Pendo)

Five metrics for PMs of employee-facing tools [Pendo]:

1. **Application adoption:** DAU, WAU, MAU, and subgroups with low adoption. Cites McKinsey that successful CEOs care about adoption as much as strategy (secondhand).
2. **Support deflection:** measure baseline ticket volume first, deploy in-app help, then compare the new level against the baseline.
3. **Segmented application NPS:** weight scores by how often people use the tool.
4. **Workflow productivity:** average time to complete business-critical workflows; shows both productivity and process design.
5. **Feature sprawl:** feature count overall or per user in homegrown apps. Example: JLL suspected unused features in its MarketSphere app.

Vendor (digital adoption platform).

### 1.27 AI product metrics (Gupta)

From [Gupta]:

- **Precision:** of the items the model flagged, how many were right.
- **Recall:** of the items it should have caught, how many it caught.
- **F1:** the harmonic mean of precision and recall. Which matters more depends on the use: medical diagnosis wants high recall; a recommender wants high precision.
- **Inference latency:** report percentiles (p50, p90, p99), not averages.
- **Cost per prediction** (per 1,000).
- **Model drift:** performance decay over time; alert and retrain.
- **Human-in-the-loop rate:** how often a person must fix the AI.
- **AI acceptance rate:** share of suggestions accepted without edits; a proxy for trust.

[Stukan] adds AI and data accuracy as business-critical "trust" metrics.

### 1.28 Building a metric in a customer success tool (Vitally docs)

A concrete model of how tools define a metric [Vitally]:

- **Structure:** a numerator (event counts, users doing an event, average, sum, unique, min or max of an event property; or trait values) and an optional denominator, over a rolling window of 7, 14, 30 or 90 days, or custom up to 90.
- **Examples:** % of an account's users doing an event in the last 30 days; % of licenses used; change in a trait over time.
- **History:** not calculated retroactively; values are cached daily. **Editing a metric applies only from that day forward; older values aren't recomputed, and some types can't be rebuilt at all.**
- **Lesson:** every definition change needs a dated note, because history before it isn't comparable.

Vendor documentation.

### 1.29 How-to-choose checklists from other sources

- **Purdue blog:** start with your "why" (the business why and the audience why), form a hypothesis, then set a goal, a primary metric, a "bonus" metric and supporting KPIs.
  - Their case: goal "increase website traffic from search"; primary metric pageviews from organic search; bonus metric new users; KPIs total ranking keywords, non-branded ranking keywords, ranking posts.
  - Goals change as the program matures (next focus: lead generation).
  - Tech shifts such as AI search summaries change which metrics make sense.
  - Source: [Purdue].
- **LSA Global, 10 steps:**
  1. Define strategic success before metrics.
  2. Focus on the critical few.
  3. Balanced measurement.
  4. Leading and lagging.
  5. Design rewards carefully.
  6. Involve stakeholders early.
  7. Data quality and credibility.
  8. Review regularly.
  9. Embed metrics in daily operations.
  10. Dashboards.
  - Uses Wells Fargo as the cautionary tale: aggressive cross-selling targets led employees to open about 3.5 million unauthorized accounts.
  - Source: [LSA].
- **Rego Consulting:** questions to ask:
  - What matters to the organization and the industry?
  - Where does the data come from, and can you get it consistently?
  - What's the baseline? The target? The frequency?
  - Can you make decisions from it?
  - Other advice: keep it simple; don't tie metrics to salaries; look at the whole story (profit up while NPS falls signals long-term risk); plan communication with a RACI; manage change; retire metrics that are inaccurate, never reviewed, or not actionable; review at least quarterly.
  - Source: [Rego].
- **Spider Strategies, seven-step aligned system:**
  1. Define goals.
  2. Pick KPIs (1 to 5 per department).
  3. Choose supporting metrics.
  4. Establish measures (data sources).
  5. Set targets: how much, by when, who owns it (example: 10% year-over-year revenue growth by Q4, owned by the sales VP).
  6. Monitor regularly.
  7. Optimize.
  - Also: note any methodology changes.
  - Source: [Spider].
- **Semrush:** for KPIs, identify core goals, engage stakeholders (including customers), and link each goal to KPIs. For metrics: start with the objective, use industry benchmarks, pilot a new metric for a month before adopting it, keep it simple, avoid vanity metrics, balance types, know your audience, review quarterly. Source: [Semrush].
- **MAP Consulting:** align, be specific, involve stakeholders, be actionable, review; set targets, collection methods, daily integration, regular reporting, accountability. Mostly sales copy. Source: [MAP].
- **Atlassian KPI guide:** traits: aligned, defined and measurable, actionable, time-bound, accessible to owners. Pros and cons, including gaming and number fixation. Source: [Atlassian].
- **PassioHR:** tailor KPIs to the industry (retail sales per square foot, SaaS MRR); individual KPIs as SMARTs, Big 3s and EOS Rocks. Source: [Passio].
- **Miki:** success metrics must trace directly to the feature's expected benefit. Don't claim indirect metrics as success metrics. Not every feature aims at revenue, engagement or retention; internal or data-gathering features still need a traceable metric. Source: [Miki].
- **Atlassian community comments** (unnamed practitioners replying to a question):
  - Think in input and output metrics, and work back from the business goal.
  - Set metrics during discovery as hypotheses, not fixed targets, but define success before building.
  - Change metrics when data shows they're wrong, though changing is painful; review quarterly.
  - Ask "if this metric improves, will it meaningfully affect business goals?"
  - When the business link is unclear, use leading indicators that historically correlate with long-term results.
  - Source: [Atlassian comments].

### 1.30 Business metrics for PMs (Stukan)

From [Stukan]:

- **Company financial goals:** increase annual revenue by X%, grow MRR, grow ARPU or ARPC, reduce operating costs, increase profitability (gross profit = direct costs such as development and hosting; operating profit also includes sales, marketing and finance). The PM's job is to know *where* the growth or savings are expected to come from: new regions, a new product line, expansion revenue from premium add-ons, and so on.
- **Commercial efficiency:**
  - CAC (better onboarding conversion lowers it).
  - LTV (engagement raises it).
  - LTV:CAC (example: $100 CAC with $80 LTV loses money on every customer).
  - Payback period (months to recover CAC; 18 months means 18 months underwater).
  - Retention and churn.
- **Industry-critical metrics** that cap everything else: platform uptime and latency for API products; fraud and compliance in fintech and insurance ("a 10% increase in revenue means nothing if fraud losses increase by 20%"); AI accuracy; data accuracy.

### 1.31 Data and analytics leaders' success metrics (IIA)

From podcast interviews with chief data and analytics officers [IIA]:

- **Four categories:**
  1. *Business value:* "Business outcomes. Period."; share of work aligned to a strategic pillar; ROI goals; leader testimonials to tell a fuller story.
  2. *Customer problems:* satisfaction of teams served; NPS; ideas coming from end users.
  3. *Analytic operations:* adoption of recommendations, reuse, backlog, training, behavior change, ethics.
  4. *Team talent and engagement.*
- **Mars's ratios:** questions answered per unit time (Q/T) and per dollar (Q/$).
- **Cigna's rule:** "If there's not a number next to it, we should question why we are doing it."
- **Survey claim:** 71% of data executives say leadership expects revenue growth from data science (Wakefield Research, cited).

Author is IIA's VP of marketing.

### 1.32 Strategy and performance measurement (HBS Online)

- Objective and subjective measures; diagnostic controls; profit plan; non-financial goals; intangible assets via the balanced scorecard [HBS].
- Cites Seagate: businesses act on 32% of their data.
- Cites Gallup: engagement raises profitability by up to 23%.
- Course marketing for "Strategy Execution".

---

## 2. Definitions and vocabulary

Where sources disagree, the alternatives are listed and the disagreement is marked.

- **Metric.**
  - A quantitative data point for monitoring a specific activity, as opposed to an overarching goal [Semrush].
  - An umbrella term for any measurement; a KPI is one kind [Rego].
  - A measure examined over time, with context [Spider].
  - A specific number teams use to track success, detect risk and set goals [Wrike].
  - Mostly compatible: "metric" is the general term.
- **Measure.** A single raw data point, or the tool that generates it [Spider]. [BSI] uses "measure" for what others call a metric. Manheim uses "measure" for the underlying quantity, and "metric" once it's used to evaluate or reward [Manheim].
- **KPI** (the definitions conflict):
  - A *goal* with a target and deadline, such as "rank top 10 within six months" [Semrush] [Wrike].
  - The vital few *most important metrics* tied to strategy [Spider] [NetSuite] [Atlassian].
  - *Forward-looking* metrics about where you want to be, vs performance metrics about where you are [Rego].
  - *Health barometers* for business as usual, vs OKRs for change [LogRocket] [Atlassian].
  - The same thing as a success metric [Asana] [Alwan] [Passio].
  - "Metrics report the past. KPIs shape what happens next." [Monday]
  - Targets set on metrics after monitoring them [Giannakopoulos].
  - (The product-copilot wiki dropped the term on 2026-11-21 and uses "metric" plus "target".)
- **Success metric.**
  - A measurement that proves whether a *feature* delivered its intended result [Siegel].
  - "The single best quantifiable measure" of a strategy, product or feature over time [HustleBadger].
  - A quantifiable measure of whether a business strategy works; same as KPI [Asana].
  - Measurable parameters for progress and effectiveness [LogRocket].
  - Measurable outcomes showing a company's progress toward objectives [Indeed].
- **OKR:** an objective plus measurable key results; ambitious, aimed at change [LogRocket] [Atlassian]. [Alwan] combines OKRs with goal trees.
- **Leading vs lagging:** leading predicts future results; lagging confirms past results. Agreed by all; examples in 1.10. [NetSuite] notes most metrics are lagging, and that lagging ones are easiest to collect.
- **Primary, secondary, guardrail:**
  - Primary = proof of value; secondary = usage; guardrail = must not break [Siegel].
  - Primary = tied to strategic goals; secondary = explains drivers [ProductSpace].
  - Guardrail = counter-metric [Gupta].
  - Slightly different meanings of "secondary".
- **Counter-metric:** a metric you watch so pushing the primary doesn't cause harm. Examples: conversion vs return rate; support tickets vs CSAT; ad clicks vs retention [Gupta].
- **Vanity metric:** looks impressive but doesn't inform decisions or tie to goals; examples include page views, likes, total signups, downloads [Semrush] [Asana] [Giannakopoulos] [Gupta] [ProductSchool]. [Xray] extends it to team-comparison productivity metrics. [Holmes] calls raw API calls borderline vanity.
- **Proxy metric:** an indirect indicator at a user-experience touchpoint that moves a key result [Alwan]. [BSI] calls these indirect measures, chosen on a hypothesis of correlation or contribution.
- **Magic metric:** the metric your own analysis shows drives your most important goals [Holmes].
- **North Star Metric:** the one metric that best captures the core value delivered (see 1.11).
- **Baseline:** pre-change data to compare against, collected before launch [Siegel]; historical averages or industry benchmarks [NetSuite]; one of Rego's must-answer questions [Rego].
- **Target vs threshold:**
  - Target = the desired level for a period; thresholds = upper and lower limits around it that set green, yellow and red [BSI].
  - Success threshold and failure threshold per metric [Siegel].
  - A target says how much, by when, and who owns it [Spider].
- **Benchmark:**
  - An external comparison point (industry averages, competitors) [Semrush] [NetSuite] [Plugseal].
  - Your own past metrics used as a reference [Asana].
  - One of the traits of an effective metric [Spider].
- **Activation:** a user doing the key action that shows they've experienced core value; defined per product [Holmes] [ProductSpace] [Gupta].
- **Stickiness:** DAU ÷ MAU [Gainsight] [ProductSchool] [ProductSpace].
  - "Above 20% is often" considered good [Gupta] (sentence cut off in the paste).
  - "> 0.4 for collaboration tools, WAU/MAU > 0.6 for CRM" [HubSpot].
  - Both unsourced.
- **Churn and retention** (the formulas differ):
  - Churn = lost ÷ customers at start [ProductSpace] [Dovetail] [HubSpot] [Plugseal]. [HubSpot] says to exclude new customers from the denominator. [deHaaff] divides customers lost in a month by the prior month's total.
  - Retention = (end − new) ÷ start [ProductSpace] [Dovetail].
  - Retention = active users ÷ total users for a period [Wrike]. This differs from the above.
  - User retention vs customer (account) retention differ in B2B [Gainsight].
  - Revenue churn matters more than customer churn in software [deHaaff].
- **NPS** (scale disagreement):
  - 0 to 10 scale; promoters 9 to 10, passives 7 to 8, detractors 0 to 6; score = % promoters − % detractors, ranging −100 to +100. Correct per [Holmes] [HubSpot] [Atlassian16] [Plugseal] [Gupta].
  - [Dovetail] and [Gainsight] say "1 to 10", a likely error.
  - [Asana] calls NPS "sometimes referred to as a customer satisfaction score", which conflates two different metrics.
  - [Holmes]: NPS isn't a percentage.
  - NPS is a registered trademark of Bain, Reichheld and Satmetrix [HubSpot].
- **CSAT:** "How satisfied are you with…?"
  - Usually reported as the share of positive (4 to 5 of 5) answers [HubSpot] [Dovetail] [Plugseal] [NetSuite].
  - Sometimes reported as the average score [ProductSpace] [Gainsight].
  - NPS measures loyalty; CSAT measures satisfaction [Gainsight].
- **Customer effort score (CES)** (scales differ):
  - 1 to 7, the average, with higher meaning easier [HubSpot].
  - Agreement on 1 to 10 [Dovetail].
  - A Likert scale from very easy to very difficult [Gainsight].
- **LTV / CLV / CLTV** (formulas differ):
  - Average purchase value × frequency × lifespan [ProductSpace] [Plugseal] [HubSpot] [Dovetail] [NetSuite].
  - Average monthly revenue ÷ churn rate, for subscriptions [Dovetail] [HubSpot].
  - Average revenue per month × average lifetime in months [deHaaff].
  - Revenue vs profit basis also varies: "profit" [Asana]; "net revenue" [deHaaff]; "revenue" [Atlassian16].
- **MRR:** recurring revenue in a month.
  - Variants: new MRR, add-on (expansion) MRR, contraction MRR, total new MRR [deHaaff] [HubSpot].
  - ARR = MRR × 12; ACV = annual contract value [deHaaff].
- **NRR (net revenue retention):** revenue change from existing customers (upgrades, downgrades, churn), excluding new customers. It shows health that MRR can hide [Gainsight] [HubSpot].
- **CAC:** sales and marketing cost ÷ new customers. [Gainsight] includes sales salaries. CPA (cost per acquisition) is used as a synonym [Holmes].
- **CAC payback:** CAC ÷ (new MRR × gross margin) [NetSuite]; months to recover CAC [Stukan].
- **Time to value (TTV) / time to first value (TTFV):** time from signup or purchase to the first value event [ProductSchool] [ProductSpace] [Gainsight]. Requires defining the value milestone first [Gainsight].
- **Feature adoption rate:** users who used the feature ÷ total users [ProductSpace] [Atlassian16]. Related terms: adoption *depth* (use of key, high-value features), adoption *velocity* (% within 7, 14 or 30 days) [ProductSchool], and adoption as first-time use in a week [Gupta].
- **Customer health score:** a weighted composite of usage, support and outcomes in color bands [HubSpot]; no universal standard [Dovetail].
- **Product-qualified lead (PQL):** a user whose behavior signals sales readiness [ProductSchool].
- **K-factor:** invites per user × invite conversion [Gupta].
- **Goodhart's law and Campbell's law:** when a measure becomes a target it stops being a good measure, as people optimize the number instead of the goal [Manheim].
- **Strategy surrogation:** treating the proxy measure as if it were the goal [Manheim].
- **Sub-optimization:** metrics that undermine each other [12Char].

---

## 3. Practices most sources agree on

1. **Start from the goal, then choose metrics.** [Skok] [BSI] [Manheim] [HustleBadger] [Giannakopoulos] [Semrush] [Asana] [Spider] [LSA] [Monday] [Purdue] [Productboard] [Atlassian comments]. BSI: "If you don't know what you are trying to accomplish, it is too early for KPIs."
2. **Keep to a few metrics.** [Asana] (5 to 10 per team) [Spider] (1 to 5 per department) [ProductSchool] (3 to 5) [Wrike] (5 to 6) [Semrush] [LogRocket] [LSA] [Monday] [Atlassian]. LogRocket and Monday also warn against too few.
3. **Balance leading and lagging.** [Asana] [LSA] [Monday] [Rego] [NetSuite] [HustleBadger] [Productboard] [ProductSpace].
4. **Avoid vanity metrics; measure outcomes, not activity.** [Semrush] [Asana] [Giannakopoulos] [Siegel] [Gupta] [ProductSchool] [Xray] [ProductSpace].
5. **Metrics must be actionable:** you know what to do when one moves, and you can influence it. [12Char] [Giannakopoulos] [HustleBadger] [Monday] [Rego] [Spider] [Skok] [ProductSchool].
6. **Define each metric once and keep the calculation consistent; note changes.** [12Char] [BSI] [Asana] [Spider] [Atlassian] [Vitally].
7. **Get a baseline before setting a target.** [Siegel] [NetSuite] [Rego] [Pendo] [Giannakopoulos].
8. **Give each metric an owner.** [12Char] [Siegel] [Spider] [Productboard].
9. **Review metrics on a schedule and retire stale ones.** Quarterly is most common [Asana] [Semrush] [Rego] [BSI] [ProductSchool] [Atlassian comments] [LSA] [Manheim] [12Char].
10. **Pair numbers with qualitative evidence.** [ProductSchool] [Alwan] [HubSpot] [Rego] [Plugseal] [LogRocket] (warns against over-relying on data) [Atlassian] (number fixation).
11. **Watch for gaming and unintended effects.** [Manheim] [12Char] [LSA] [Atlassian] [Gupta] [Rego].
12. **Segment; don't trust averages.** [Gupta] [Gainsight] [Pendo] [HustleBadger] [12Char] (segment-level data is more actionable) [deHaaff] (CAC by source).
13. **Data quality matters; automate collection where possible.** [12Char] [LSA] [LogRocket] [Siegel] [Atlassian16] [ServiceNow] [Monday].
14. **Tell the story behind the numbers.** [Xray] [Giannakopoulos] [Stukan] [Gupta] [Rego] [IIA].

---

## 4. Conflicts between sources

1. **One number vs many.**
   - For one: [HustleBadger] ("single best" metric), North Star advocates [Gupta] [ProductSchool] [ProductSpace], [LSA] ("pick the one or two that matter most").
   - Against: [Manheim] (diversify, because any single metric gets gamed), [Gupta] again ("optimizing for a single metric… is a fast-track to building a product people hate"), [Plugseal] and [Rego] ("no single metric provides the full picture").
   - Common resolution: one primary metric plus counter-metrics.
2. **When to set the target.**
   - Before launch: [Siegel] (thresholds before launch), [Asana] (before the initiative starts), [ProductSchool] (before you build), [Atlassian comments] (in discovery, as hypotheses).
   - After observing: [Giannakopoulos] (only after monitoring a while; an early target is a guess to adjust).
3. **Tie targets to rewards?**
   - Yes: [NetSuite] ("most effective when paired with meaningful rewards and consequences"), [12Char] (embed in job descriptions and reviews).
   - No or careful: [Rego] (don't tie to salaries; it discourages honest reporting), [LSA] (aggressive compensation links distort behavior; Wells Fargo), [Manheim] (incentives cause gaming).
4. **Benchmarks as a target source.**
   - For: [Semrush] (match or beat competitors), [NetSuite], [Spider], [Plugseal], [Atlassian16] ("benchmarking against industry").
   - Against or cautious: [Giannakopoulos] and [Manheim] imply your own baseline and causal reasoning; [Dovetail] says a "good" churn depends on industry (2 to 8% typical, 25% in some) and chasing an unrealistic one is counterproductive.
5. **What a KPI is.** Seven incompatible definitions; see section 2.
6. **Is adoption a success metric?**
   - Yes: [Atlassian16] and [Productboard] (feature adoption rate as a KPI), [ProductSchool] (adoption depth and velocity), [Asana] (DAU), [Pendo] (app adoption).
   - Only secondary: [Siegel] (usage doesn't prove value). [Gupta] ranks adoption below retention.
7. **Secret or after-the-fact metrics vs metrics fixed in advance.**
   - [Manheim] lists secret metrics and post hoc specification as anti-gaming tools for incentive systems.
   - [Siegel] fixes thresholds in advance so results can't be explained away afterwards.
   - The context differs: rewarding people vs judging a feature.
8. **Are qualitative inputs metrics?**
   - Yes: [Rego] ("qualitative metrics tell a story and don't involve numbers"), [Atlassian] ("qualitative KPIs", CSAT), [HubSpot] (qualitative feedback as metric 3).
   - Only as numeric judgments: [NetSuite] (qualitative = scored judgments).
   - Not metrics: [Giannakopoulos] and [HustleBadger] (must be quantifiable).
9. **Review cadence.** Weekly to monthly [Giannakopoulos]; weekly or monthly early, quarterly or annually when mature [Atlassian16]; quarterly [BSI] [Asana] [Rego] [ProductSchool]; staged per feature [Siegel]; monthly or quarterly [Wrike]; "as often as it makes sane sense" [Giannakopoulos]. Mostly a difference of level (metric set vs feature check vs company review).
10. **Direct metric vs link to business metrics.**
    - [Miki]: only direct metrics count as a feature's success metrics; don't claim indirect benefits.
    - [Stukan], [Alwan] and [Gupta]: tie every feature up the chain to a business metric.
    - Compatible if the direct metric decides and the business link is stated as a hypothesis.
11. **Which metrics depend on product stage.**
    - Early = activation and time to value, later = retention and expansion [ProductSchool] [ProductSpace] [Gainsight].
    - [Gupta]: track retention from day one because "you can't fake" it.
12. **Changing metrics.**
    - Change them when they stop fitting [Rego] [Asana] [Semrush] [LSA] [Atlassian comments].
    - But changing breaks trend comparability [Asana] [Spider] [Vitally], and is painful [Atlassian comments].
13. **Number of KPIs:** 1 to 5 [Spider]; 3 to 5 [ProductSchool]; 5 to 6 [Wrike]; 5 to 10 per team [Asana]; "critical few" [LSA]. None cite evidence.
14. **Is revenue a goal?** [Skok] leaves revenue out of the end goals (profit, growth, cash flow) and treats it as a component. [Indeed] says any company with more revenue is "by definition" having a successful period. [Stukan] and [HustleBadger] treat revenue as a headline metric.

---

## 5. Worked examples and numbers, with provenance

Flags: **[vendor]** = the publisher sells a related product or service; **[unsourced]** = no reference given; **[error]** = the math or definition is wrong.

**Illustrations (made-up numbers, fine as teaching examples):**

- Bulk-edit feature: primary metric is time saved, not usage. Success "≥25% less time to completion"; failure "conversion −5% vs expected 0%" [Siegel] [vendor].
- Fasting analogy: losing 15 lb is lagging, burning 750 extra calories a day is leading [LSA].
- Fasting and app sign-up examples for the two-question method [Giannakopoulos].
- Funnel decomposition and the Facebook-ads conversion story [Skok].
- Churn: 100 subscribers to 95 is 5% [Holmes]; 10 of 100 is 10% [Dovetail]; 500 to 460 in a quarter is 8% [Gainsight]; 64 of 1,000 is 6.4% monthly [HubSpot].
- HubSpot annualizes 6.4% monthly churn as "(1 − 0.936)^12 ≈ 52%" [HubSpot] [error]. The correct calculation is 1 − 0.936^12 ≈ 55%.
- LTV: $1,000 MRR ÷ 5% churn is $20,000 [HubSpot]. $50 × 3 visits a month × 24 months is $3,600 [HubSpot].
- CAC: $1,000 campaign bringing 10 customers is $100 each [deHaaff]. $4,000 CAC is fine if ACV is above $16,000 (recovered in a quarter) [deHaaff] [vendor].
- LTV:CAC: $100 CAC vs $80 LTV loses money per customer [Stukan].
- Ecommerce: $50 average order vs $80 CPA, so check LTV [Holmes].
- TTFV: signup 2:00 PM to first design 2:15 PM is 15 minutes; dashboard adoption 25% vs 80%; January cohort 30 of 100 still active in April is 30% retention; expansion $100K to $130K is 30%; 500 tickets from 5,000 users is 0.1 per user; referrals 200 of 5,000 is 4%; DAU 6,000 ÷ MAU 24,000 is 25% [ProductSchool] [vendor].
- MRR: 10 × $100 is $10,000 [Dovetail]; 1,000 × $750 is $750K, with +$25K upsell and −$10K downgrades giving +$15K net new [HubSpot].
- CSAT: 70 of 100 positive is 70% [Dovetail]; 40 of 50 is 80% [HubSpot].
- Spam filter: precision vs recall trade-off [Gupta].
- Retail COGS: $5M opening inventory + $15M purchases − $4M closing = $16M, up about 23% from $13M two years earlier [NetSuite] [vendor].
- Capacity planning: 260 − 11 − 10 − 5 = 234 working days; (234 × 8) − (2 × 8) − (50 × 2) = 1,756 hours per person; × 9 people = 15,804 hours against a 20,000-hour contract, so 4,196 hours short and at least three more hires [NetSuite] [vendor].
- Downtime: 450 hours × $150,000 per hour = $67.5M; MTTR = 450 × 60 ÷ 1,100 incidents = 24.5 minutes; a $10M saving needs about 66.6 fewer hours, which is about 3.6 minutes less MTTR per incident [NetSuite] [vendor].
- Revenue per worker rises with inflation even with no productivity change [12Char].
- Teacher who grades on number of questions asked; class attendance rewarded while students sleep; h-index built from available data; height vs basketball skill [Manheim].
- Starbucks closed hundreds of stores weak on three KPIs: profitability, barista satisfaction, customer experience ("Project Bloom") [LSA] [unsourced].
- Adidas America moved its KPIs from financial metrics to NPS [MAP] [unsourced].
- JLL found unused features in its MarketSphere app [Pendo] [vendor].
- FOX product strategy team used goal trees [Alwan]. "Salesforce's goal tree" [Alwan] [unsourced].
- Purdue blog results in 2024: 460+ ranking keywords, 105 ranking posts, 92% non-branded, 4,742+ pageviews, 70% from new users [Purdue]. Self-reported, with no baseline.
- Wells Fargo: about 3.5 million unauthorized accounts opened to hit cross-sell targets [LSA]. This is a well-documented public case; LSA's account is fine as an illustration.

**Benchmarks and targets (use as context only, never as a target without a cited primary source):**

- LTV ≥ 3× CAC [Dovetail] [HubSpot] [Gupta] [unsourced rule of thumb].
- Retention around 85%; professional services 84%; hospitality and travel 55% [Dovetail] [vendor] [unsourced].
- Churn usually 2 to 8%, up to 25% in finance or cable TV [Dovetail] [vendor] [unsourced].
- CSAT 75 to 85% "good", above 90% hard [Dovetail]; target 80 to 90% [HubSpot]. [vendor] [unsourced]
- NPS above 0 OK, above 50 excellent, above 70 rare [Dovetail] [vendor] [unsourced].
- MRR growth 10 to 20% "good" [Dovetail] [vendor] [unsourced]; Dovetail's growth formula is also inverted [error].
- CES target above 5.0 on a 1 to 7 scale [HubSpot]; first contact resolution 75 to 85% [HubSpot]; renewal rate above 90% [HubSpot]; CRC:CLV under 1:3 [HubSpot]. [vendor] [unsourced]
- NRR: top quartile 115 to 120% vs median 106% [HubSpot], citing Gainsight and Wudpecker blogs [vendor]. HubSpot also says NRR above 110% "proves" customer success drives growth [vendor].
- Trial conversion: low-touch B2B 15 to 25%, enterprise 8 to 15%, consumer 2 to 5%; 20% is a "solid baseline" [HubSpot], citing First Page Sage [vendor].
- DAU/MAU above 0.4 for collaboration tools, WAU/MAU above 0.6 for CRM; 60 to 80% of accounts hitting weekly thresholds; sessions of 15 to 45 minutes for productivity tools and 5 to 15 for transactional apps [HubSpot], partly citing Databox [vendor].
- "Regular, purposeful sessions mean 25% higher renewals"; "5% lift [in trial conversion] = 25% ARR growth" [HubSpot] [vendor] [unsourced].
- Stickiness above 20% "often" good [Gupta] [unsourced].
- Flat retention of 10 to 15% shows product-market fit for early B2B SaaS; K-factor of 0.2 to 0.4 helps [Gupta] [unsourced].
- Capacity utilization realistic at 80 to 85% [Indeed] [unsourced].
- Selling to an existing customer is about 4× more likely than to a new one [Dovetail] [unsourced].
- 58% of marketers chasing more aggressive KPI targets in 2024 [NetSuite] [unsourced in the paste].
- Gallup: 21% of employees strongly agree their metrics are within their control; fewer than one in three say managers involve them in goal setting; about one in five feel their performance is managed in a motivating way [NetSuite], citing Gallup.
- Gallup: engagement raises profitability by up to 23% [HBS], citing Gallup.
- Seagate: businesses act on 32% of their data [HBS], citing Seagate's 2020 report.
- 71% of data executives say leadership expects revenue growth from data science [IIA], citing Wakefield Research for Domino.
- Nearly 60% of product leaders say business acumen will be the most critical PM skill [Stukan], citing Productboard's own report [vendor].
- "85% of Fortune 100 companies choose Asana" [Asana] [vendor].

**Uncited statistics (don't use as fact):**

- [MAP] [vendor] [unsourced]:
  - 31% higher success with KPI-deviation protocols.
  - 23% better goal attainment from KPI training.
  - 19% productivity gain from frontline metric use.
  - 23% from feedback mechanisms.
  - Change initiatives monitored by KPIs succeed 51% of the time vs 13%.
  - "Eight times more likely to succeed".
  - 66.67% of employees burn out during change.
  - A diagnostic built on data from "15,000 companies and 170,000 leaders".
- "Research from Harvard Business Review consistently shows…" and "Bain research shows…" with no reference [LSA] [vendor] [unsourced].

---

## 6. Sources

Kind: **practitioner** = individual writing from experience; **vendor** = company selling a related tool, course or service; **research** = peer-reviewed or academic. "Substantive" means it adds ideas beyond generic lists.

**Batch 1** (Juan, 2026-11-21, about 22 pieces):

| Key | Title | Author / publisher | Kind | Date | Substantive? |
|---|---|---|---|---|---|
| [Xray] | 6 key metrics to determine product quality | Mariana Santos / Xray (getxray.app) | vendor | 2022-08-23 | Some (quality metrics) |
| [Semrush] | KPIs vs. Metrics: The Key Differences for Business Success | Hava Salsi / Semrush | vendor | 2024-02-19 | Some (input/output/outcome/process) |
| [Asana] | Success metrics examples: How to choose KPIs by team | Sarah Laoyan / Asana | vendor | 2026-02-06 | Lists |
| [Purdue] | Measuring content success (Graduate Programs Blog case) | Purdue Daniels School marketing team blog | practitioner (institution) | 2025-06-19 | Some (why → hypothesis → metrics) |
| [LSA] | Strategy Success Metrics: 10 Steps for Better Strategy Design | LSA Global | vendor (consulting) | not shown | Some (Wells Fargo); uncited research claims |
| [12Char] | 12 Characteristics of Effective Metrics | not shown in the paste | unknown (BI guide) | not shown | Yes |
| [Giannakopoulos] | Defining and Tracking Success: Crafting Meaningful Metrics | Mike Giannakopoulos / Medium | practitioner | 2024-01-21 | Yes |
| [Vitally] | Success Metrics (help doc) | Ethan Patrick / Vitally | vendor docs | not shown | Some (forward-only edits) |
| [LogRocket] | A guide to success metrics | Dr. Marina Stojanovski / LogRocket blog | practitioner on vendor blog | 2024-04-23 | Some (KPI + OKR framework) |
| [HustleBadger] | Choosing the right success metrics | Ed Biden / Hustle Badger | practitioner (paid newsletter) | updated 2025-06-30 | Yes (outline only; paywalled) |
| [Monday] | KPIs for project management: essential metrics and trends | Ben Kazinik / monday.com | vendor | 2026-01-23 | Formulas |
| [Atlassian] | What are key performance indicators (KPIs)? | Atlassian | vendor | not shown | Lists |
| [Skok] | Designing Metrics for Success | David Skok / For Entrepreneurs | practitioner (investor) | not shown | Yes |
| [MAP] | Master KPIs and Metrics for Organizational Success | MAP Consulting | vendor (consulting) | not shown | No (sales copy, uncited stats) |
| [Rego] | Metrics: What They Are, Why They Matter, and Best Practices | Rego Consulting (LinkedIn) | vendor (consulting) | 2025-08-21 | Some |
| [NetSuite] | Performance Metrics: Definition, Types & Examples | Lisa Schwarz / Oracle NetSuite | vendor | 2024-05-29 | Formulas, worked examples |
| [BSI] | How to Develop KPIs / Performance Measures (MPRA) | Balanced Scorecard Institute (kpi.org) | vendor (consulting) | not shown | Yes |
| [Manheim] | Building less-flawed metrics | David Manheim / Patterns (Cell Press), PMC10591122 | research | 2023 | Yes (strongest) |
| [IIA] | The Most Revealing Success Metrics for High-Performing Data and Analytics Leaders | Jason Larson / International Institute for Analytics | vendor (marketing VP) | 2022-06-06 | Some |
| [Indeed] | 7 common metrics for success | Indeed Editorial Team (UK) | content site | updated 2025-11-27 | Little |
| [HBS] | How to Measure Your Business Performance | Kate Gibson / HBS Online | course seller | 2023-11-14 | Some (Simons) |
| [Dovetail] | 10 customer success metrics that deserve your attention | Dovetail (reviewed by Miroslav Damyanov) | vendor | 2023-02-21 | Lists, benchmarks |
| [Passio] | How to Develop Key Success Metrics to Move Your Company Forward | Roger Hays / PassioHR | vendor (PEO) | 2024-11-11 | Little |
| [Siegel] | Success Metrics (glossary) | Avi Siegel / Momentum (gainmomentum.ai) | vendor (product tool), practitioner author | not shown | Yes (most feature-specific) |
| [HubSpot] | The 15 customer success metrics that actually matter in 2026 | Clint Fontanella / HubSpot | vendor | updated 2026-08-31 | Lists, benchmarks, one math error |
| [ServiceNow] | Measuring Success with ServiceNow | ServiceNow community (employee) | vendor | 2024-07-01 | Little |
| [Spider] | KPIs vs. Metrics vs. Measures | Scott O'Reilly / Spider Strategies | vendor | 2023-09-11 | Some (hierarchy, targets) |

**Batch 2** (Juan, 2026-11-21, about 17 pieces):

| Key | Title | Author / publisher | Kind | Date | Substantive? |
|---|---|---|---|---|---|
| [Holmes] | Metrics that Matter to Product Managers | Rich Holmes / Department of Product | practitioner (sells a product intelligence tool) | not shown | Lists by product type |
| [Stukan] | A Product Manager's Guide To Business Metrics | Corinna Stukan / Insights Driven PM (Substack) | practitioner | 2026-01-25 | Yes |
| [Miki] | Defining success metrics as a product manager | Brian Miki / Medium | practitioner | 2023-12-11 | Yes (short) |
| [Atlassian16] | 16 product management KPIs and how to track them | Atlassian | vendor | not shown | Lists |
| [Atlassian comments] | Practitioner replies on the same page | unnamed commenters | practitioner | not shown | Some |
| [Alwan] | How Successful Product Managers Set and Crush Their Metrics | Alex Alwan / PRODUCT360 | practitioner (consultancy) | 2022-01-27 | Yes (Goal Tree) |
| [ProductSchool] | Product Success: 13 Metrics That Measure What Matters | Product School (CEO byline) | course seller | 2025-06-10 | Yes (selection advice) |
| [Gainsight] | The Essential Guide to Product Management Metrics | Gainsight | vendor | updated 2026-10-20 | Some |
| [MondayAgile] | Agile product management: 15 practices | Ben Kazinik / monday.com | vendor | 2025-11-12 | Little |
| [Plugseal] | Metrics for Product Success: Essential Tips | Plugseal Innovation Services (LinkedIn) | vendor | 2024-07-08 | Little |
| [ProductSpace] | 15 Most Important Metrics for Product Managers to Track | Senior PM at Google / The Product Space | course seller | not shown | Some (formulas, axes) |
| [Pendo] | 5 KPIs for internal product managers to track | Nat Brown / Pendo | vendor | 2024-03-07 | Some |
| [Fejzullahu] | Self-Evaluation: Setting Metrics for Your Success as a Product Manager | Stina Fejzullahu / Product Breaks | practitioner | 2024-04-03 | Off topic (excluded) |
| [Wrike] | Product Management Metrics and KPIs Explained | Alex Zhezherau / Wrike | vendor | not shown | Some (KPI structure) |
| [Productboard] | Product Management KPIs Every Business Should Track | Productboard | vendor | 2024-07-20 | Lists |
| [deHaaff] | 15 KPI Metrics Every Software Product Manager Should Know | Brian de Haaff / Aha! | vendor (CEO) | not shown | SaaS metric definitions |
| [Gupta] | Mastering Metrics for Product Managers in 2026 | Aakash Gupta / aakashg.com | practitioner (newsletter) | 2026-04-03 | Yes (AARRR, HEART, AI metrics, counter-metrics); salary content excluded |
| (excluded) | AI search summary at the top of batch 2 | unknown | AI summary | — | Not a source |
