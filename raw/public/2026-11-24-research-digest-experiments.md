<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Experiments: research knowledge

Everything worth keeping from Juan's three batches of experimentation research
(pasted 2026-11-21 in the thread "Plan PM workflow steps for copilot skills").
Written for the person who turns this into playbook pages.

How to read it:

- Each claim ends with source codes in brackets, like `[GB, STATSIG]`. The codes
  are defined in section 7.
- **Vendor claim** marks a number or claim from a company that sells
  experimentation, analytics or feature-flag tools, with no independent source.
- **Unsourced** marks a number given with no source at all.
- **Inference:** marks my own reasoning, not something a source said.
- Skipped on purpose: the Google AI search summaries at the top of batches 1
  and 3, product pitches, and the lab time-management tips (off topic).
- Two sources were only partly available: Paweł Huryn's library is paywalled
  after section 3 `[HURYN]`, and Google's experimentation PDF was read through a
  summary, with its page-4 template lost as an image `[GOOGLE-PDF]`.

## Contents

1. Definitions and vocabulary
2. Frameworks, methods, models and lists
3. Practices most sources agree on
4. Conflicts between sources
5. Worked examples and numbers
6. Gaps: what the research doesn't cover well
7. Sources

---

## 1. Definitions and vocabulary

### Experiment, test, validation, research: the sources don't agree

| Term | Definition | Sources |
| ---- | ---------- | ------- |
| Product experimentation (narrow) | Expose a subset of real users to a controlled change, compare against a control, measure a pre-chosen metric. | `[PS, FLAG]` |
| Product experimentation (broad) | Any structured test of a belief, including interviews, landing pages, fake doors and data analysis. | `[LONGDEN, MTP-1, UP, PMA]` |
| Experimentation vs testing | Experimentation is the ongoing programme of hypotheses and iterations; a test is one contained activity inside it (an A/B test, a usability test, a QA check). | `[PS]` |
| Validation vs experimentation | Validation asks whether something is worth building at all (interviews, prototypes, fake doors, before code exists). Experimentation asks whether a built change works better than what it replaces. Treat them as one discovery loop. | `[FLAG]` |
| Research activities vs experiments | Interviews, analytics analysis and market research are "research activities", not validation experiments. Experiments validate hypotheses about value, usability, feasibility or viability. | `[HURYN]` |
| Generative vs evaluative experiments | Generative: qualitative, no fixed hypothesis, produces ideas (for example customer interviews). Evaluative: tests a hypothesis for a yes/no answer. | `[MTP-1]` |
| Confirmatory vs exploratory research | Confirmatory needs a defined hypothesis upfront; exploratory doesn't, but must be reported as exploratory. | `[PLOS]` |
| Feature experimentation | Running experiments on whole developed features (sign-up flow, referral programme, purchase funnel, pricing offers) with live users. | `[WINGIFY]` |
| Test and learn (business experimentation, controlled trials) | Compare a group that gets an initiative to a similar group that doesn't, often with matched (not random) controls, for business moves like pricing, loyalty, store changes. | `[MC]` |
| Experiment (science) | A structured test of cause and effect: manipulate an independent variable, measure a dependent variable, control the rest. | `[SCRIBBR, SIXSIGMA, EXPLORABLE]` |
| Experiment (ML) | A reproducible, tested hypothesis about a model, usually one small change against a baseline. | `[GML, MLEXP]` |
| Successful experiment | One that yields actionable insight, whether or not it confirms the hypothesis `[PS, MTP-CAST, CONV]`. Google: one that gives a clear, interpretable read, even if unexpected `[GOOGLE-PDF]`. Ben Smith: the only failures are inconclusive or badly run tests `[SMITH]`. | as listed |

### Hypothesis vocabulary

- **Hypothesis:** a testable statement that can be proven or disproven, a
  prediction about the relationship between two variables `[DOP]`; "a proposed
  explanation made on the basis of limited evidence as a starting point for
  further investigation" `[PLANIO]`.
- **Independent variable:** what you change (the part after "if").
  **Dependent variable:** what you measure (the part after "then").
  **Controlled variables:** what you hold constant `[DOP, MTP-CAST, EXPLORABLE]`.
- **Nuisance variable:** a factor you control or block but don't study
  `[SIXSIGMA]`. **Extraneous / confounding variable:** an uncontrolled factor
  that moves with the treatment and muddies cause `[SCRIBBR, SIXSIGMA]`.
- **Null hypothesis (H0):** the change and the outcome are unrelated. You never
  prove the hypothesis; you try to reject the null `[SMITH, SCRIBBR]`.
- **Falsifier:** the result that would prove the hypothesis wrong. If no result
  would change the roadmap, "you are decorating a decision already made" `[PHQ]`.

### Metric vocabulary

- **Primary metric:** the one metric that decides success `[GB, CSQ, SMITH]`.
  Statsig puts both goal metrics and guardrail metrics in its "primary" group
  `[STATSIG]` (see conflicts).
- **Secondary metrics:** context and explanation of why the primary moved, or
  complementary metrics that reveal cannibalization `[GB, STATSIG, PS]`.
- **Guardrail metrics:** must not get worse even if the primary improves
  (retention, error rates, support tickets, page performance, revenue per user,
  opt-outs) `[PHQ, CSQ, FLAG, PS]`.
- **Counter metrics:** PostHog's name for guardrails `[POSTHOG]`.
- **Monitoring metrics:** LaunchDarkly's term for metrics watched for harm
  `[LD-CHECK]`. **Trade-off metrics:** Ben Smith's term `[SMITH]`.
- **Leading vs lagging indicators:** leading move fast and suit short tests;
  lagging confirm long-term impact. Decide upfront which one decides success
  `[GB]`.
- **North Star metric:** the one ultimate goal metric experiments ladder up to,
  for example Airbnb's "nights booked" `[PLANIO, MURRAY]`.
- **Baseline:** current performance plus its normal variance `[GB, GML, MLEXP]`.
- **Minimum detectable effect (MDE):** the smallest change worth detecting or
  shipping `[CSQ, STATSIG, PHQ]`. For guardrails, the MDE is the largest
  regression you are willing to miss `[STATSIG]`.
- **Practical significance:** whether the lift is large enough to matter and
  pay for its maintenance, separate from statistical significance `[PHQ, SIXSIGMA]`.

### Statistics vocabulary

- **Statistical significance / significance level:** how confident you need to
  be before calling a result; 95% is the common convention `[CSQ, CONV]`. At
  95%, about 1 in 20 metrics with no real effect will look significant
  `[STATSIG, CONV]`.
- **Power:** the chance of detecting an effect if it exists, usually set at 80%
  or more `[GB, NC3RS, PLOS, MINITAB]`.
- **Type I error (false positive)** and **Type II error (false negative)**
  `[WINGIFY, SIXSIGMA, PLOS]`.
- **Confidence interval:** the uncertainty around the measured difference;
  if it doesn't cross zero, the difference is significant `[STATSIG]`.
- **Fixed-horizon vs sequential testing:** see section 2.6.
- **Allocation:** the share of users eligible for the experiment `[STATSIG]`.
- **Randomization unit:** user, account or session `[PHQ]`.
- **Sample ratio mismatch (SRM):** traffic split differently than planned; fix
  and rerun before judging `[CSQ]`. Also called "balanced exposures" `[STATSIG]`.
- **A/A test:** two identical variants to check the setup `[GB]`.
- **Peeking:** checking results early and stopping when a variant looks ahead;
  raises false wins `[CSQ, POSTHOG, PS]`.
- **Novelty effect / burn-in:** a short-term lift that fades as users adapt
  `[PHQ, PLANIO]`.
- **Replication vs pseudo-replication:** true replication applies the same
  treatment to more than one experimental unit; measuring one unit twice is
  pseudo-replication `[JMP, PLOS]`.
- **Quasi-experiment:** treatments not randomly assigned `[SCRIBBR]`.
- **Synthetic control:** a modelled control group built after the fact when no
  control existed `[MC]`.
- **Incrementality / lift:** in Google's ad context, whether the ad caused the
  action or it would have happened anyway `[GOOGLE-PDF]`.

### Other terms

- **HiPPO:** the highest-paid person's opinion overriding data
  `[FLAG, LD-SAVAGE, LD-MOORE, MTP-CAST]`.
- **Problem library:** LaunchDarkly's name for a backlog of untested ideas
  `[LD-MOORE]`. **Experiment backlog** `[DOP]`. **Question backlog** `[PLANIO]`.
- **Experiment log / archive:** a record of every experiment, result and action
  taken `[MTP-CAST, FLAG, DOP, GOOGLE-PDF]`.
- **Minimum viable experiment** `[CONV]` / **Minimal viable test (MVT)**
  `[SMITH]`: the simplest experiment that validates one part of an idea.
- **Local maximum:** optimizing small changes near the current design and
  missing a much better design elsewhere `[MTP-CAST, MURRAY]`.
- **LOFA:** "leap of faith assumption", the critical assumption to test first
  (quoted, not defined) `[LONGDEN]`.
- **Skin in the game:** evidence is stronger when the person gives something
  real (money, a signature, time) `[HURYN]`.
- **Artefact:** the thing you test with (landing page versions, an interview
  guide); not the same as the experiment `[STRAT]`.
- **Pretotyping:** cheap ways to test demand before building (named techniques
  in 2.3) `[HURYN]`.

---

## 2. Frameworks, methods, models and lists

### 2.1 End-to-end experiment processes

Most sources give a step list. They differ in length, not in substance.

| Process | Steps | Source |
| ------- | ----- | ------ |
| Product School 6-step framework | 1. Define a clear product goal grounded in data. 2. Build the hypothesis. 3. Choose 1 to 2 success metrics (they call them OKRs) plus guardrails. 4. Design parameters: type, segment, sample size, duration, variants, flags, tracking; end with a spec anyone can read. 5. Run: ramp from about 10% to 50/50 for risky tests, check mechanics not results, don't peek. 6. Analyse, check secondary and guardrail metrics, dig into why. | `[PS]` |
| Flagsmith 5-step | 1. Specific hypothesis (change, outcome, metric, reasoning). 2. Success and guardrail metrics. 3. Sample size. 4. Run controlled; don't read daily; sequential methods help. 5. Analyse against pre-agreed criteria; ship if guardrails held and the primary improved significantly, else document why. | `[FLAG]` |
| Department of Product (Rich Holmes) | 1. Ask questions and generate ideas (experiment backlog, stakeholders). 2. Create a testable "if then" hypothesis; prioritize by impact and evidence. 3. Conduct (A/B or multivariate; be bold). 4. Communicate findings and close the loop. 5. Prioritize results like any other backlog work. | `[DOP]` |
| Simon Cast's experimentation cycle | Plan, Implement, Monitor, Act; results feed planning, the backlog or development priority. Compares it to the OODA loop. | `[MTP-CAST]` |
| Userpilot | Collect data for insights; define the end goal (SMART); hypothesis; choose type and sample size; pick tools; run; analyse and interpret. | `[UP]` |
| Contentsquare 6-step | 1. Define a product goal using 5 components (problem, solution, benefit, users, data). 2. Hypothesis. 3. KPIs (1 to 3, with roles). 4. Parameters (significance level, MDE, sample, at least one week). 5. Run. 6. Review results and run 5 checks (2.8). | `[CSQ]` |
| Planio 4-step | 1. Ask the right questions (area and assumptions, sub-questions, dot vote, HMW statements, ethics check). 2. Testable hypothesis from 4 elements (business outcome / North Star, user group, user behaviour, feature). 3. Conduct and monitor; check validity. 4. Communicate and act (action plan, share, implement, celebrate). | `[PLANIO]` |
| Ben Smith 4-step | 1. Hypothesis (from a problem, one solution per problem, with null hypothesis). 2. Minimal viable test. 3. Analysis (one success metric). 4. Decide and communicate. | `[SMITH]` |
| LaunchDarkly experimentation lifecycle | 1. Keep a problem library. 2. Build with instrumentation. 3. Design with clear metrics. 4. Launch and monitor. 5. Present to stakeholders. 6. Roll out the winner. 7. Iterate. Run several experiments at different stages at once. | `[LD-MOORE]` |
| LaunchDarkly 6-stage checklist | 1. Discovery and hypothesis (standard requirements; success metric tied to hypothesis; agree the probability needed to call a winner). 2. Development targets (link flags to the programme; mock-ups). 3. Segmentation. 4. Metrics aligned to hypothesis (success plus monitoring). 5. Rollout strategy (fix audience percentage upfront; changing it means a new iteration; plan follow-ups; stop inconclusive tests). 6. Collect and evaluate (communicate broadly; inconclusive results are useful). | `[LD-CHECK]` |
| GrowthBook 7 steps | 1. Define the goal. 2. Primary, secondary and guardrail metrics. 3. Know the baseline and variance. 4. Leading vs lagging. 5. Population and randomization. 6. Validate setup (A/A). 7. Plan duration. Bonus: plan for all outcomes. | `[GB]` |
| Statsig 3 phases | 1. Design document (description, hypothesis, metrics, allocation, MDE, duration). 2. Monitoring (health checks, sequential check-ins, early-stop rules). 3. Readout (scorecard vs ship criteria, false-positive care, ratio metrics). | `[STATSIG]` |
| DevCycle 4 steps | 1. PM writes the experiment structure (hypothesis, description, audience, variations, metrics). 2. Engineering sets up variables, variations and events. 3. Rollout via random distribution. 4. Monitor and analyse (typically 1 to 2 weeks minimum). | `[DEVCYCLE]` |
| Mastercard test and learn, 6 steps | 1. Hypothesis. 2. Design and implement (minimize bias, isolate the test group). 3. Measure across all channels, before and after, test and control. 4. Roll out targeted. 5. Learn and repeat (pipeline scored on feasibility, economic impact, decision focus, strategic fit). 6. Build a culture (centre of excellence). | `[MC]` |
| Google's four steps | 1. Hatch your hypothesis (tied to a business goal). 2. Validate your victories (metric, significance threshold and action per outcome before launch). 3. Assign your audience (test and control). 4. Respond to results (adopt if expected; brainstorm and iterate if not). | `[GOOGLE-PDF]` |
| Jonny Longden's horse race | Break every idea into its smallest testable assumption; run the cheapest test; promising ideas earn a bigger, costlier test; weak ones are killed. Manage the pipeline as an "operating system", not a testing tool. | `[LONGDEN]` |
| Scribbr 5 steps (science) | 1. Define variables. 2. Write H0 and H1. 3. Design treatments (how widely and finely to vary). 4. Assign subjects (completely random vs randomized block; between vs within subjects). 5. Plan measurement. | `[SCRIBBR]` |
| Six Sigma 6 steps (science) | Define objectives; identify all variables (independent, dependent, nuisance); select design; set sample size and replication; execute and document; analyse for statistical and practical significance. | `[SIXSIGMA]` |
| Explorable (school science) | Research, problem, hypothesis, experiment, results, discussion and conclusion. | `[EXPLORABLE]` |
| Bibikova 8 steps (lab) | Define objective and controls; pick a method; write the protocol; get reagents ready; timeline (double your estimate); run; record everything, including deviations; analyse. | `[BIBIKOVA]` |
| PLOS 10 simple rules (research) | Planning: 1 specify the question, 2 write and register a protocol, 3 justify sample size, 4 data management plan, 5 reduce bias. Execution: 6 avoid questionable research practices, 7 be careful with significance, 8 make research open. Reporting: 9 report all findings, 10 follow reporting guidelines. | `[PLOS]` |

### 2.2 Hypothesis templates

| Template | Source |
| -------- | ------ |
| "We believe that doing X will impact Y because Z." | `[PS]` |
| "We believe that [changing X] for [users Y] will [impact Z] because [reason]." | `[PS]` |
| "We believe that [a solution] will [the change] for [audience segment] because [reason]." | `[CSQ]` |
| "If [change] then [outcome] because [reason]." Distil to two variables. | `[DOP, MTP-CAST]` |
| "If [segment] gets [change], then [metric] will [move] because [reason]", plus "what would falsify this". | `[PHQ]` |
| "We believe that… will result in… We'll know we've succeeded when…" | `[NOMAD]` |
| "By doing [X] to [Y], we expect [Z]." | `[DEVCYCLE]` |
| XYZ hypothesis: "At least X% of Y will do Z." For market-engagement tests. | `[HURYN]` |
| Problem statement + hypothesis + null hypothesis (example: "60% who start trial sign-up don't finish"; "fewer steps will raise completion"; H0 "step count doesn't affect completion"). | `[SMITH]` |
| Four building blocks: business outcome (North Star), user group, user behaviour, feature. | `[PLANIO]` |
| "If I change A, this results in B" (A = variable, B = success metric). | `[GOOGLE-PDF]` |
| Concrete outcome with size, for example "users in the new onboarding reach activation 10% more often". | `[GB]` |
| Hypothesis that names the expected chain: a tutorial video raises understanding, so successful interactions rise, support queries fall and churn (primary) drops. | `[POSTHOG]` |
| H0 / H1 pairs. | `[SCRIBBR]` |
| PICOT (population, intervention, comparator, outcome, time frame) for framing a research question. | `[PLOS]` |

Hypothesis quality tests named by sources:

- Someone else can read it and explain back what will change and what effect
  is expected `[MTP-CAST]`.
- Specific, measurable, rooted in rationale `[PS]`; specific, measurable,
  iterative `[DEVCYCLE]`.
- One hypothesis per experiment; split competing ones into separate
  experiments `[CONV]`. One problem, one hypothesis `[SMITH]`.
- States how much, not "wait and see" `[LD-GUIDE, GB]`.
- Comes from discovery, support themes, funnel gaps or sales objections, not
  brainstorm notes alone `[PHQ]`; from data `[CONV, UP]`.
- Prioritize hypotheses whose "because" clause is strongest `[MTP-CAST]`; by
  impact and supporting evidence `[DOP]`.
- Never change the hypothesis after the fact `[EXPLORABLE, CONV]`.

### 2.3 Catalogue of experiment types

Grouped from lightest to heaviest. "When" and "limits" are as the sources state.

#### Research and qualitative

- **Customer research interview.** The first experiment every PM should know;
  generative. Limits: measures what people say, so weaker evidence; strengthen
  it by asking about past behaviour, not future intent, and avoid leading
  questions `[MTP-1, STRAT]`. Huryn doesn't count it as an experiment `[HURYN]`.
- **Surveys and feedback forms / in-app surveys.** Direct feedback, open and
  closed questions; useful after a release or after an A/B test `[PMA, UP, CSQ]`.
- **Usability testing.** Watch users attempt tasks; explains the "why"; won't
  reach significance. Variants: moderated think-aloud, unmoderated recordings
  `[PS]`; card sorting, five-second test, lab testing, session replays `[UP]`.
- **Prototype / usability product experiments.** Test whether people understand
  and can use a design, especially new mental models (AI agents) `[PS]`.
- **Community building.** For a startup, a landing page or group to see who
  turns up is "your first experiment" `[MTP-1]`.
- **Click tracking (clickstream analysis), funnel testing (CRO), product usage
  analysis.** Observational analysis of behaviour `[UP, NOMAD]`.
- **Cohort analysis.** Group users by a shared trait (for example week of
  sign-up) to judge health. Do it right: compare new users per period; time-box
  actions (for example first 30 days) to separate cause from later effect;
  compare many features to avoid cherry-picking; show usage alongside
  retention lift. Avoid "people who do X retain more" claims `[MURRAY]`.

#### Demand and market tests (pretotypes)

From Huryn's library unless noted. All test value proposition, messaging and
often pricing; most need a landing page or traffic source.

- **Email campaign:** targeted email with a call to action `[HURYN]`.
- **Paid ads campaign:** also tests cost per click `[HURYN]`.
- **Social media campaign** `[HURYN]`.
- **Landing page:** describe the product, gather sign-ups, test willingness to
  pay; not necessarily a fake door unless it implies the product exists
  `[HURYN, PS, FLAG, PMA]`. Also used for "API appetite" tests `[DOP]`.
- **Fake door / painted door / smoke test / mock sale:** a button, menu item or
  page for something that doesn't exist; measure clicks; show "coming soon" or
  a waitlist; apologize or offer something if someone pays `[HURYN, PS, FLAG, UP,
  LD-KROLL]`. Use to separate must-have sales requests from nice-to-haves
  `[LD-KROLL]`.
- **Facade:** make an existing but limited product look more available or
  scaled (mostly physical products) `[HURYN]`.
- **Pinocchio / pretend to own:** use a non-working model yourself to see if
  you'd use it; tests only your own experience `[HURYN]`.
- **Explainer video** `[HURYN]`.
- **Pre-order:** collect money before it's built `[HURYN]`.
- **Letter of intent:** a signed, non-binding note of intent to buy; strong for
  B2B `[HURYN]`.
- **Provincial:** launch to a small group or place first (a pop-up) `[HURYN]`.
- **One-night stand / pop-up store:** offer a basic version for a limited time
  `[HURYN]`.
- **Infiltrator:** put your product in someone else's store or channel `[HURYN]`.
- **Crowdfunding:** caution, backers may not be your customers `[HURYN]`.

#### Minimal products

Deliver real value; costlier than pretotypes `[HURYN]`.

- **Piecemeal / impostor / mash-up:** stitch existing tools and no-code into a
  working product `[HURYN]`.
- **Concierge:** a manual, high-touch service; the customer knows it's manual
  `[HURYN]`. PS calls Wizard of Oz "concierge MVPs" `[PS]` (see conflicts).
- **Wizard of Oz:** looks automated, a human does the work; the user doesn't
  know `[HURYN, PS]`.
- **Single feature product:** mostly a go-to-market move, not a test `[HURYN]`.
- **MVP / minimum viable experiment:** the smallest thing that tests one part
  of the idea `[CONV, DOP, SMITH]`.

#### Controlled online experiments

- **A/B test (split test):** random split, one change, compare a metric. The
  "workhorse"; ideal for specific questions `[PS, FLAG, UP, PMA]`. Can include
  more than one variant against a control `[MTP-CAST]`. Limits: needs traffic;
  default use without fitting the question produces murky results `[FLAG]`.
- **Multivariate test (MVT):** several elements in combination, to find
  interactions. Needs more traffic and time; best for optimizing around a
  known peak; avoid on low traffic `[PS, FLAG, UP, MTP-CAST, MTP-1, GB]`.
- **Funnel experiments:** changes across several pages of a flow `[PLANIO]`.
- **Canary / incremental / staged rollout:** start with about 1 to 5% of
  traffic, watch errors, latency and key events, ramp up or roll back
  `[PS, FLAG]`. Before/after comparison per slice `[PS]`.
- **Beta programmes:** opt-in cohorts (employees, power users, accounts) in
  exchange for feedback `[PS, PMA]`.
- **Feature flags:** decouple deploy from release; target segments; kill
  switch. A foundation for running experiments safely `[WINGIFY, FLAG, PMA,
  LD-GUIDE]`. Remove experiment flags after the test `[LD-GUIDE]`.
- **Continuous personalization / bandits:** a model keeps adapting what each
  user sees (contextual bandits, reinforcement learning, multi-armed bandits);
  still needs control logic, guardrails and evaluation `[PS, WINGIFY, MURRAY]`.
- **A/A test:** see 2.6 `[GB]`.
- **Small test rollout first:** run at about 5% for a few days to catch bugs
  before the full experiment, because a broken launch can't be cleanly rerun
  `[POSTHOG]`.
- **Holdouts or backtests:** to check whether gains in a sensitive local metric
  ladder up to top-line metrics `[STATSIG]`.
- **Time-lapse / pre/post:** compare before and after a change. Not
  recommended; use only if you can't randomize `[PLANIO]`; directional only and
  rarely significant `[GOOGLE-PDF]`. One marketplace dropped it because it
  couldn't separate lift from seasonality `[GB]` (vendor claim).
- **Split URL tests:** route traffic to two URLs or URL parameters; needs
  engineering; firing action goals is harder than page-view goals
  `[MTP-CAST]`.

#### Business and marketing experiments

- **Test and learn with matched controls:** pair stores, branches, markets or
  customers with similar traits instead of randomizing; for big business moves
  `[MC]`.
- **Synthetic control:** model the missing control group after the fact `[MC]`.
- **Analytical modelling:** forecasting and regression generate hypotheses but
  don't measure cause `[MC]`.
- Mastercard's rule of thumb: A/B testing for digital interactions; test and
  learn for strategic initiatives (pricing, loyalty, marketing, operations);
  modelling for many quick scenarios or to support a test `[MC]`.
- **Google ad-measurement methods** `[GOOGLE-PDF]`:
  - A/B optimization: campaign experiments, ad variations, landing-page tests,
    bidding-strategy tests, video experiments.
  - Brand Lift: survey exposed vs eligible-but-unexposed users (recall,
    awareness, consideration, favourability, intent).
  - Conversion Lift: users who saw the ad vs eligible users shown another ad;
    needs minimum conversion volume; counts conversions in a 7 to 56 day window.
  - Geo experiments (GeoX): non-overlapping regions as test and control;
    heavy-up, go-dark or holdback; metrics such as incremental ROAS or cost per
    incremental acquisition.
  - Causal-impact / pre/post analysis: last resort.

#### Scientific design types

- **Completely randomized design:** treatments assigned at random; for
  homogeneous units `[SIXSIGMA, SCRIBBR]`.
- **Randomized block (stratified) design:** group by a shared trait (for
  example urban vs rural stores), then randomize within groups `[SIXSIGMA,
  SCRIBBR, JMP]`.
- **Factorial design:** two or more factors at once, including interactions;
  efficient `[SIXSIGMA, NC3RS, MINITAB]`.
- **Fractional factorial (Resolution V):** half or a quarter of the runs while
  still estimating main effects and two-way interactions `[MINITAB]`.
- **Response surface methodology:** optimize several inputs against one or more
  outputs `[SIXSIGMA]`.
- **Split-plot / strip-plot:** when a factor is hard to change (oven
  temperature), randomize with restrictions `[JMP]`.
- **Between-subjects vs within-subjects (repeated measures):** one treatment
  per subject vs every subject gets every treatment, with counterbalanced order
  `[SCRIBBR]`. Matched pairs within between-subjects designs `[SCRIBBR]`.
- **Quasi-experimental / observational study:** when random assignment is
  impossible or unethical `[SCRIBBR]`.

#### ML experiment types

- Model selection (same data, different models), feature engineering (same
  model, different features), hyperparameter tuning (grid search, random
  search, Bayesian optimization, Hyperband, genetic algorithms), data
  augmentation `[MLEXP]`.
- Make one small change at a time against a baseline; the winner becomes the
  new baseline; track neutral results too; noise comes from data shuffling,
  initialization, asynchronous training and small evaluation sets; rerun to
  confirm `[GML]`.

### 2.4 Matching the test to the stage

- Huryn's ladder: market-engagement tests (pretotypes) first, then minimal
  products, then feasibility and user prototypes, then experiments in
  production `[HURYN]`.
- Strategyzer: start with cheap, weak-evidence tests; move to costlier,
  stronger-evidence tests as signals improve; run more than one type
  `[STRAT]`.
- Longden: horse-race ideas through rising hurdles `[LONGDEN]`.
- Conversion.com: start with the minimum viable experiment, then scale
  `[CONV]`.
- Mind the Product (Rosemary King): start qualitative; move to quantitative
  only once you understand run length, segmentation and what false negatives
  and positives look like; learn metrics analysis in between `[MTP-1]`.
- Startups often lack traffic for significance, so test the value proposition,
  not button colours `[DOP]`.
- Low-traffic products: qualitative tests, fake doors, concierge, sequential
  rollouts instead of underpowered A/B tests `[PHQ]`; keep to simple A/B with few
  variations `[MTP-1, GB]`.
- Choose the method from the question, not the other way round. A fake door
  tells you in a week whether people notice a feature; a multivariate test
  would take a month `[FLAG]`. Start from the hypothesis, not "I want to run a
  fake door test" `[MTP-1]`.
- If detecting a 1% lift would take four months: choose a bigger expected
  effect, a more sensitive metric, a narrower high-intent audience, or a
  non-experiment method `[PHQ]`. If runtime is too long: test a bolder change,
  cut variations, or pick a more sensitive metric `[GB]`; raise allocation,
  raise the MDE, or change metrics `[STATSIG]`.

### 2.5 Deciding when to experiment (and when not to)

**LaunchDarkly / Valerie Kroll: 10 situations where experiments add value**
`[LD-KROLL]`:

1. Stakeholders disagree (use sparingly when build time is high).
2. Replicating another team's win.
3. UX research was inconclusive (research evidence is anecdotal or
   directional; it doesn't show business impact).
4. A sales-driven feature request (use a painted door).
5. An engineer's performance or stability improvement (hard to see in
   short-term business metrics).
6. A big gap between MVP and full build (prove value on an easy subset first).
7. Piloting a paid third-party tool before licensing it.
8. A leadership mandate you must follow but want to quantify.
9. Developing personas (test microcopy and tone).
10. A really big, disruptive idea.

**LaunchDarkly / Megan Moore: four traits of high-impact experiments**
`[LD-MOORE]`: high uncertainty (even about direction), conflicting opinions,
random audience and exposure, measurable outcomes.

**Four cases to skip** `[LD-MOORE]`: obvious improvements and bug fixes;
low-risk or low-impact changes (but context matters: navigation text can
matter, footer text rarely does); time-sensitive launches; no metric or too few
users (add measurement to the roadmap and park the idea).

**Others:**

- Don't test bug fixes, compliance or foundational work; test where
  uncertainty is high and being wrong is costly `[PHQ]`.
- Don't run experiments on broken experiences that need obvious fixes first
  `[PHQ]`.
- Not everything can be tested; strategy and judgment carry decisions
  experiments can't (a pricing change with legal implications, sunsetting a
  product line) `[PLANIO, FLAG]`.
- Prioritize funnel drop-offs, costly bets, disputed priorities, riskiest
  assumptions `[UP, PS]`.
- Without robust data tracking, testing "just makes you more confused"
  `[MTP-1]`.

### 2.6 Statistical design toolkit

**Sample size and power inputs:**

- Traffic, normal metric variance, smallest effect worth detecting `[GB]`.
- For two groups: the statistical test, significance level (often 5%), power
  (usually 80 to 90%), sidedness (usually two-sided), effect size of interest,
  and a standard-deviation estimate from a past experiment `[NC3RS]`.
- Baseline rate, MDE, weekly traffic and stop rules, written down beforehand
  `[PHQ]`.
- Run sample-size calculations under several assumptions and take the largest;
  adjust for missing data; consult a statistician early `[PLOS]`.
- Alternative: size for a desired confidence-interval width (precision) rather
  than for a significance test `[PLOS]`.
- Small samples don't just miss effects: when a small study does find a
  significant result, it tends to overestimate the effect ("small-study
  effect") `[PLOS]`.
- Rules of thumb quoted: social science often uses 30+ participants; in a
  25-company B2B market, testing with half your customers would be great
  `[STRAT]`. At least 1,000 visitors per landing-page variation `[SIXSIGMA]`
  (unsourced). Three replicates is not a magic number `[LABDESIGN]`.
- Tools named: VWO calculator `[MTP-CAST]`, ExperimentCalculator.com `[SMITH]`,
  GrowthBook power calculator (80% power) `[GB]`, PostHog running-time
  calculator `[POSTHOG]`, G*Power, statpages.info, NC3Rs EDA `[NC3RS]`, R
  "pwr", SampleSizeR `[PLOS]`.

**Duration:**

- Fixed-horizon testing: set the sample upfront, read once; most power;
  checking early inflates false positives `[GB]`.
- Sequential testing: look as often as you like; costs wider intervals and less
  power, but can stop clear winners or losers sooner `[GB]`. PostHog's version
  gives "always-valid" p-values; still plan the sample `[POSTHOG]`. Statsig
  suggests check-ins at days 1, 3 and 7, then weekly or every two weeks, for
  regressions and to confirm the new experience is live `[STATSIG]`.
- Set the readout window upfront, for example "first 14 full days"
  `[STATSIG]`.
- Cover at least a full weekly cycle; extend over holidays and unusual periods
  `[PS, CSQ, MTP-CAST, LD-GUIDE]`.

**Monitoring and validity:**

- Health checks: balanced exposures and metrics data joined to exposures
  `[STATSIG]`; logging working, no rise in crashes, session replays look right,
  split ratio as expected `[POSTHOG]`.
- PostHog checklist: before launch (goal metric, hypothesis, secondary metrics,
  counter metrics, duration from sample size, only eligible users, QA both
  variants); 24 to 48 hours after (assignment volumes, logging ratios, crashes);
  at the end (validate hypothesis, document and share, deploy the winner and
  delete losing code) `[POSTHOG]`.
- Only include affected users: filter out ineligible users before checking the
  flag (for example people who already completed onboarding) `[POSTHOG, GB]`.
- Randomize as close to the experience as possible; keep assignment across
  sessions; use a true control `[GB]`.
- Keep sample sizes balanced; skewed cohorts skew results `[LD-GUIDE]`.
- Don't change the control during the test `[MTP-CAST]`.
- Ignore periods of transient traffic (a PR spike) and use data from either
  side `[MTP-CAST]`.
- Planio's four invalidators: overlapping tests contaminate each other; small
  audiences let outliers dominate; stopping early; external events
  (competitor launches, a pandemic) `[PLANIO]`.
- When a bug harms users: stop, fix, restart (re-randomizes). If only logging
  broke: keep it live, fix logging, reset the duration from the fix date
  `[STATSIG]`.
- Changing the audience percentage mid-test means a new iteration `[LD-CHECK]`.

**Reading results:**

- Compare against the ship criteria in the design doc; if trade-offs appear,
  use a pre-agreed rule such as "up to 1% loss in subscriptions is acceptable
  per 1% gain in purchased items" `[STATSIG]`.
- Controlling false positives: use 98% intervals for metrics not expected to
  move; doubt significant results with no logical explanation; treat
  unexplained gains and losses the same way `[STATSIG]`.
- Ratio metrics can mislead: purchases per visit up 4% while sessions fell 10%
  and purchases fell 6% (Statsig's illustration) `[STATSIG]`.
- Multiple testing corrections exist and are debated `[GB, PLOS]`.
- Report exact p-values and read them gradually, not as pass/fail at 0.05; a
  p-value near 0.05 has only about a 50% chance of replicating; novel claims
  may need p < 0.005 `[PLOS]`.
- "No evidence of impact" is not "proof of no impact" `[PHQ]`; absence of
  evidence is not evidence of absence `[PLOS]`.
- Frequentist vs Bayesian: some situations never have enough traffic for a
  frequentist approach `[LD-MOORE]`.
- Look at related metrics: more new subscribers but more cancellations may mean
  fewer total subscribers `[LD-GUIDE]`.
- Check data and segments: device, new vs returning, traffic source `[CSQ]`;
  browser, country, URL parameters, time, day, visitor type, keywords, device,
  OS `[MTP-CAST]`; mobile vs desktop is the most common slice `[LD-MOORE]`.
  Segmenting found target-market conversion lower than the average, hidden by
  other markets `[MTP-CAST]`.
- Report descriptive statistics and uncertainty (means, standard deviations,
  confidence intervals) `[NC3RS]`.
- GRADE is the most established framework for rating certainty of evidence
  `[PLOS]`.

**Scientific design principles:**

- Three basic principles: randomization (reduces bias), blocking (controls
  nuisance variation), replication (estimates experimental error) `[JMP]`.
- Five pillars: randomization, replication, control (positive and negative
  controls), blocking, sample size `[SIXSIGMA]`.
- NC3Rs key elements: unbiased (random allocation, random order, blinding),
  adequately powered, range of applicability (include both sexes, strains,
  sites), simple (pilot first; don't change plans mid-way without documenting
  why), report uncertainty `[NC3RS]`.
- Minitab DOE tips: exploratory runs to find the variable space; spread control
  (centre-point) runs to check stability; Pareto analysis to pick the problem;
  widen input ranges to gain power; fractionate (Resolution V); add replicates;
  use quantitative responses instead of defect counts; study all variables of
  interest `[MINITAB]`.
- Vary one variable at a time unless using a factorial design `[LABDESIGN,
  SIXSIGMA]`.

### 2.7 Bias catalogue

| Bias | What it is | Prevention | Source |
| ---- | ---------- | ---------- | ------ |
| Anchoring | Over-relying on the first information | Awareness | `[LD-GUIDE]` |
| Confirmation | Seeking what confirms your belief | Pre-set criteria; analyst review | `[LD-GUIDE, CANDU, LONGDEN]` |
| Default effect | Favouring the default option | Awareness | `[LD-GUIDE]` |
| Bias blind spot | Believing you're less biased than others | Awareness | `[LD-GUIDE]` |
| Biased outlier removal | Dropping data that doesn't fit the story | Rules set beforehand | `[LD-GUIDE]` |
| Allocation | Systematic differences in who gets the treatment | Random allocation with concealment | `[PLOS]` |
| Attrition | Uneven dropouts | Retention efforts | `[PLOS]` |
| Confounding | A third variable drives both | Randomization; else restriction, matching, stratification, propensity scores | `[PLOS, SCRIBBR, JMP]` |
| Immortal time | Exposure requires surviving a period | Assign at time zero | `[PLOS]` |
| Information / recall | Differences in how data is collected | Standardized, blinded, objective measures | `[PLOS]` |
| Publication / file drawer | Only striking results get reported | Protocols, registration, report all results | `[PLOS]` |
| Self-selection | Participants choose themselves (loyalty programmes) | Matched controls | `[MC]` |
| Natural test vs control bias | Groups differ before the test | Precise control matching | `[MC]` |
| Sampling, survivorship | Unrepresentative sample | Representative sampling | `[SCRIBBR]` |
| HiPPO | Senior opinion overrides data | Leadership commits before results | `[FLAG, LD-SAVAGE]` |
| Senior-management involvement | Leads to bolder tests but can undermine cause-and-effect learning (cites an HBS study) | Awareness | `[LD-SAVAGE]` |

**Questionable research practices** `[PLOS]`: low power, pseudo-replication,
repeated inspection of data, p-hacking, selective reporting, HARKing
(hypothesizing after results are known). Product equivalents: hypotheses written
after results, metric fishing, underpowered tests treated as gospel, ignoring
guardrails `[PHQ]`; "result shopping" `[PS]`; collecting data until you get the
result you want `[SIXSIGMA]`; "spin" on secondary outcomes when the primary is
null `[PLOS]`.

**Remedies named:** preregistration and registered reports; study protocols
with population, sample size, inclusion/exclusion, design, data handling and
planned analysis; open data and code; reporting guidelines (CONSORT for
randomized trials, SPIRIT for protocols, STROBE, PRISMA, ARRIVE, STARD/TRIPOD)
`[PLOS]`. Analysts independently review experiments before a winner is declared
(Flo Health) `[MTP-1]`. Document your biases `[MTP-1]`.

### 2.8 After the test: decisions and learning

- **Decision options:** ship, iterate, kill, or re-scope `[PHQ]`. Expected
  result: adopt; unexpected: brainstorm why and iterate `[GOOGLE-PDF]`.
  Confirmed: roll out to the segment; disproved: don't `[CSQ]`.
- **Plan for every outcome before launch:** cheap features may ship on
  directional evidence; costly ones need strong evidence; neutral results
  still teach `[GB]`. Know what you'll do with each result: dig deeper, run a
  bigger test, or run a validation test `[PLANIO]`. Map the action per outcome
  `[GOOGLE-PDF]`.
- **You can still launch on a neutral result** `[LD-GUIDE]`. If results are
  similar, the risk of switching is probably too high; if identical, don't
  change `[CANDU]`.
- **Contentsquare's 5 post-test checks:** ran correctly (split, tracking, full
  length); primary vs guardrails; segments; behaviour per variant (heatmaps,
  replays); record inconclusive results `[CSQ]`.
- **Conversion.com's four-part review** of any result: was the data read
  correctly; was the hypothesis actually proven or disproven; was the execution
  the best possible; did external factors skew it `[CONV]`.
- **When a test is flat, ask:** was the hypothesis wrong, the change too weak,
  the audience wrong, or the metric insensitive `[PHQ]`.
- **When it wins:** does it generalize beyond the segment, and will quality
  hold at full scale `[PHQ]`.
- **Retrospective questions:** success? why or why not? questions raised and
  answered? what did we learn? launch or not? `[LD-GUIDE]`.
- **Anomalous results** (perpendicular to the hypothesis, for example one
  country converting 50% better for no clear reason) deserve their own
  questions `[MTP-CAST]`.
- **Closing the loop:** what do results mean for development priority, and why
  did we get them `[MTP-CAST]`. Don't jump a winner to the top of the backlog;
  prioritize it like any work `[DOP]`. Explore beyond the hypothesis `[MC]`.
- **An experiment informs a human decision; it doesn't make it** `[LONGDEN,
  FLAG]`. Contrast: "implement the results no matter what" `[PLANIO]` (see
  conflicts).
- **Communicate:** a few data points and a graph or two `[DOP]`; share evidence
  and trade-offs, not just scores; share failures `[MIX, LD-GUIDE]`.
- **Delete losing variant code and short-lived flags** `[POSTHOG, LD-GUIDE]`.

### 2.9 Principle lists

**Conversion.com's 9 experimentation principles** `[CONV]`:

1. Challenge assumptions, beliefs and doctrine.
2. Always start with data.
3. Experiment early and often.
4. One provable hypothesis per experiment.
5. Define the success metric and criteria in advance.
6. Start with the minimum viable experiment, then iterate.
7. Evaluate the data, hypothesis, execution and externalities separately.
8. Measure the value of experimentation in impact and insight.
9. Use statistical significance to minimize risk (raise the bar above 95% for
   high-risk tests such as pricing strategy).

**Product School's five ingredients of a successful experiment** `[PS]`: clear
purpose and hypothesis; relevant success metrics; robust design (control,
sample size, duration); data-driven, unbiased decisions; focus on user impact;
plus an iterative mindset.

**Planio's five components of a good experiment** `[PLANIO]`: problem, users
(audience size), benefit (and trade-offs), feature, data (North Star metric and
how much). Contentsquare uses the same five for defining the goal `[CSQ]`.
Planio's three purposes of an experiment: inform a decision, reduce uncertainty
about an assumption, understand and improve performance `[PLANIO]`.

**Strategyzer: two levers for strong evidence** `[STRAT]`:

- Right participants: a precise segment, representative of it, large enough;
  use screener questions.
- Well-crafted artefact: designed to test the hypothesis, not a smaller version
  of the product (that adds too many variables).
- Evidence strength: what people do (A/B) beats what they say (interviews), but
  design can weaken a strong method or strengthen a weak one.

**Murray's experiment-design practices for data teams** `[MURRAY]`: lead with
behavioural hypotheses, not feature variations; translate hypotheses into
independent experiment attributes; pick consecutive A/B tests or multivariate
deliberately; avoid local maxima; "if we can't measure it, we can't launch it";
define outcome metrics and segments before launch.

**Ben Smith's hypothesis checklist** `[SMITH]`: start from a problem (not from
what's easy to build or measure); one solution per problem; test aggressively
(gentle tests end inconclusive); value (1 to 2% vs 50 to 200%); measurable
(Google Analytics may miss about 5% of traffic, unsourced); trade-off metrics;
null hypothesis; find the one underlying assumption that must be true (use 5
Whys); work in themes so experiments build on each other.

**Simon Cast's "test well" rules** `[MTP-CAST]`: don't change the control;
discount transient traffic; segment; run at least a week; reports exist only to
drive the next action; negative results can matter more than positive ones;
keep an experiment log (name, where, what, variants, dates, result, action).

**PostHog's six best practices** `[POSTHOG]`: clear hypothesis; only affected
users; smallest reasonable change (but too small slows you down); test the
experiment with a small rollout; predetermine duration; use a launch checklist.

**LaunchDarkly mega-guide, 9 best practices** `[LD-GUIDE]`: culture
(question results, ideas from everyone); define success as a specific metric
moved by a specific amount; look at complementary metrics and balanced sample
sizes; segmentation (cover usage days, account for multi-visit journeys);
recognize bias; retrospective; plan experiments with flags; empower others with
controls; remove experiment flags.

**Wingify feature-experimentation practices** `[WINGIFY]`: culture; team
effort; make it easy; realistic goals tied to a roadmap; learn from failure;
choose metrics; target the right audience; run long enough (sample size matters
more than time); use feature flags.

**Digital Nomad's principles** `[NOMAD]`: hypothesis-driven, segmented testing,
randomized control groups, significance, documentation; tips: clear
objectives, prioritize, iterate, cross-functional work, incremental changes.

**PMA best practices** `[PMA]`: start small, be patient, analyse and iterate,
stay user-centric, diversify methods (qual and quant), combine data with
intuition.

**Experiment-design one-pager (Product HQ)** `[PHQ]`: context and evidence;
hypothesis; audience and exclusion rules; variant description; primary metric
and window; guardrails; duration and power notes; QA checklist; decision rule;
after the test: result, interpretation, next action, open questions. Also a
decision owner.

**Statsig design document** `[STATSIG]`: description; hypothesis; primary
metrics (goals and guardrails); secondary metrics; allocation; MDE per primary
metric; duration from power analysis (take the longest); analysis window.

**DevCycle experiment brief** `[DEVCYCLE]`: hypothesis, description and
location, target audience, variations, mock-ups, metrics (with direction of
improvement).

**Google's template contents** `[GOOGLE-PDF]`: hypothesis, success metrics,
design and execution method; keep a central pipeline or log with standardized
past results for benchmarking.

**Study protocol (science)** `[PLOS]`: research question and hypothesis,
population, target sample size, inclusion and exclusion criteria, design, data
collection, processing and planned statistical analyses.

**Experimental procedure (school science)** `[SCIFAIR]`: amounts and measures,
the variable and how it changes, the control, how change is measured, diagrams;
repeated trials.

### 2.10 Prioritizing experiment ideas

- Impact vs effort; link to OKRs; for hypotheses, impact and evidence `[DOP]`.
- Dot voting (3 to 5 dots each, multiple votes allowed) after brainstorming
  questions and sub-questions (why, who, what, where, when, which, how many,
  how, how long, do, are, will, have, should, is), then "How might we"
  statements and an ethics gut check `[PLANIO]`.
- Mastercard's pipeline criteria: feasibility, economic impact, decision focus,
  strategic fit `[MC]`.
- Fix problems earlier in the journey first, so later tests get more users
  `[SMITH]`.
- The PM makes the final prioritization call; stakeholders feed the backlog
  `[DOP]`.
- Prioritization is managing ideas through validation hurdles by evidence
  `[LONGDEN]`.
- Start with small, well-defined experiments for quick wins, then grow
  `[UP, LD-SAVAGE]`.

### 2.11 Culture and operating model

- Leadership buy-in; psychological safety; accessible data; a structured
  process `[MIX]`.
- Mixpanel's 5 steps: experimentation as a core value; structured process;
  tools; fast feedback loops; reward experimentation (including in performance
  reviews). Challenges: resistance (highlight quick wins), unclear success
  metrics, fear of failure `[MIX]`.
- LaunchDarkly's 5 tips: clear goals (including programme goals such as
  experiments per month and time from experiment to shipping); data-first
  mindset; rigorous process (start simple, then policies on audience size,
  run-time, validity, reproducibility); cross-functional teams with authority;
  infrastructure `[LD-SAVAGE]`.
- Planio's 7 culture steps: curiosity; a company-wide North Star; hire
  data-minded people; humanize data; tools you trust; be a role model; know
  when you can't experiment `[PLANIO]`.
- Flagsmith: document every experiment; engineers own guardrails and rollout
  speed; agree which flows a rollout may touch; same tools and process for all;
  small frequent tests beat big rare ones; check infrastructure can isolate
  concurrent experiments ("blast radius") before scaling `[FLAG]`.
- Data teams: embed analysts once the platform is mature, keep a core; use
  standard platforms; self-serve data has costs; clickstream data loses value
  fast `[MURRAY]`.
- Experimentation "isn't a separate team; it is product management" `[LONGDEN]`.
- Don't punish failed experiments, or teams run safe, boring tests `[FLAG, PHQ]`.
- Inconclusive results hurt early momentum; early conclusive wins build the
  habit `[SMITH]`.
- Statistical approach and dashboards should be consistent across experiments
  so they can be compared `[LD-MOORE, FLAG]`.

---

## 3. Practices most sources agree on

These appear in five or more independent sources each.

1. **Write the hypothesis before the test**, naming the change, the expected
   outcome, the metric and the reason `[PS, FLAG, DOP, PHQ, CSQ, CONV, GB,
   MTP-CAST, GOOGLE-PDF, POSTHOG]`.
2. **Set metrics and success criteria before launch**, and don't change them
   during the test `[PS, FLAG, CONV, CSQ, STATSIG, GOOGLE-PDF, PLOS, PHQ]`.
3. **One primary metric, plus guardrails** that must not regress, plus a few
   secondary metrics for context `[GB, STATSIG, PHQ, CSQ, PS, FLAG, POSTHOG]`.
4. **Use a randomized control group** for causal claims `[PS, FLAG, MTP-CAST,
   NOMAD, LD-MOORE, SCRIBBR, NC3RS, JMP]`.
5. **Calculate sample size and duration upfront**; underpowered tests produce
   false results `[FLAG, GB, STATSIG, POSTHOG, NC3RS, PLOS, CSQ]`.
6. **Don't stop early because a number looks good** (peeking) `[PS, CSQ,
   POSTHOG, PHQ, PLANIO, CANDU, SIXSIGMA, GOOGLE-PDF]`.
7. **Run at least a full weekly cycle** and avoid unusual periods `[PS, CSQ,
   MTP-CAST, LD-GUIDE, CANDU]` (with nuance in section 4).
8. **Change one thing at a time** when you need to know the cause, or admit
   you're testing a package `[PHQ, MTP-CAST, CANDU, POSTHOG, STRAT, EXPLORABLE,
   LABDESIGN]`.
9. **Check the setup** (tracking, assignment, split ratio) before trusting
   results `[PS, GB, STATSIG, POSTHOG, CSQ, PHQ]`.
10. **Treat negative and flat results as learning**, and record them
    `[PS, FLAG, MTP-CAST, CONV, CSQ, MIX, GB, PLOS]`.
11. **Keep a log or archive of every experiment** so nobody repeats one
    `[MTP-CAST, FLAG, DOP, CSQ, GOOGLE-PDF, NOMAD, GML, MLEXP]`.
12. **Match the method to the question and stage**: lightweight tests early or
    on low traffic, A/B tests when volume allows `[FLAG, PHQ, MTP-1, HURYN,
    STRAT, DOP]`.
13. **Tie every experiment to a goal**, not testing for its own sake `[DOP,
    MTP-CAST, PS, GOOGLE-PDF, CSQ, WINGIFY]`.
14. **Segment the results** to find where effects differ `[MTP-CAST, CSQ,
    LD-MOORE, LD-GUIDE, PS]`.
15. **Pair numbers with qualitative evidence** to learn why `[CSQ, PS, CANDU,
    PMA]`.
16. **Avoid overlapping tests on the same users**, or manage them as
    mutually exclusive layers `[PLANIO, GOOGLE-PDF, SMITH, STATSIG, MC]`.
17. **Log deviations** from the plan `[NC3RS, BIBIKOVA, SIXSIGMA, PLOS]`.

---

## 4. Conflicts between sources

1. **What counts as an experiment.** Narrow: a controlled change with a
   control group `[PS, FLAG]`; Huryn excludes interviews as "research
   activities" `[HURYN]`. Broad: interviews are the first experiment
   `[MTP-1]`; landing pages, interviews and data analysis count `[LONGDEN]`.
   Flagsmith splits the field into validation (pre-build) and experimentation
   (post-build) `[FLAG]`.
2. **Qualitative first or A/B first.** Rosemary King: don't run A/B tests
   until you're good at qualitative ones. Terry Lee, same article: every PM
   should know A/B, split and fake-door tests, and "you could probably achieve
   almost anything with an A/B test" `[MTP-1]`. Longden quotes a practitioner
   who prioritizes A/B testing even for early ideas, and another who leans on
   qualitative methods `[LONGDEN]`.
3. **Peeking.** Never look before the planned end `[PS, CSQ, PLANIO, CANDU]`
   vs sequential testing lets you look as often as you like at a power cost
   `[GB, POSTHOG, STATSIG, FLAG]`. Compatible if the method is chosen upfront.
4. **How long to run.** At least a week `[PS, CSQ, MTP-CAST]`; 1 to 2 weeks
   minimum `[DEVCYCLE]`; sample size matters more than time `[WINGIFY]`;
   Google ties windows to conversion lag, 7 to 56 days, and excludes a 1 to 2
   week ramp-up in pre/post tests `[GOOGLE-PDF]`; Airbnb learned to run longer
   in a complex ecosystem `[MIX]`.
5. **Number of metrics.** One success metric `[SMITH, GB]`; one primary or a
   small set of 2 to 3 `[PS]`; 1 to 2 ideal `[PS, FLAG]`; up to 3 KPIs, more
   invites cherry-picking `[CSQ]`; a few allowed, "not too many" `[GOOGLE-PDF]`.
   Statsig groups guardrails inside "primary", while others keep guardrails
   separate `[STATSIG]` vs `[GB, CSQ]`.
6. **Shipping without top-line significance.** At X, teams sometimes shipped on
   positive engagement metrics when daily active users showed no harm but no
   significant gain `[GB]` vs "if the launch criteria are not met, don't ship"
   `[STATSIG]` and "beware experimenting without significance, it's not much
   better than guessing" `[CONV]`. Ben Smith: in small tests, the metric moving
   in the right direction can be enough `[SMITH]`.
7. **Who decides.** Data decides: "implement the results no matter what"
   `[PLANIO]`; "data trumps opinion" `[PS, PLANIO]`. Humans decide with data as
   one input `[LONGDEN, FLAG, PMA]`; Stephen Watts: A/B tests give "data, not
   definitive answers" `[LONGDEN]`.
8. **Small or bold changes.** Small, incremental changes reduce risk `[NOMAD,
   MIX, PMA, LD-SAVAGE]` vs be bold to avoid local maxima; small tests produce
   1 to 2% gains `[DOP, MTP-CAST, SMITH, MURRAY]`. PostHog: as small as
   reasonable, but too small slows you down `[POSTHOG]`.
9. **Concierge vs Wizard of Oz.** Product School treats them as the same
   ("Wizard of Oz… (concierge MVPs)") `[PS]`; Huryn separates them by whether
   the user knows a human is doing the work `[HURYN]`.
10. **Pre/post comparisons.** Product School counts before/after per rollout
    slice as experimenting `[PS]`; Planio says it's usually not recommended
    `[PLANIO]`; Google says directional only `[GOOGLE-PDF]`; a GrowthBook
    customer abandoned it for seasonality reasons `[GB]`.
11. **Significance as a gate.** 95% as convention, raise for high risk
    `[CONV, CSQ]` vs don't dichotomize at 0.05, report exact p-values, use
    p < 0.005 for novel claims `[PLOS]`; "a tool, not a religion" `[PHQ]`.
12. **Test everything vs test selectively.** Treat every meaningful change as
    an experiment `[PS]`; "everything you build is an experiment" `[DOP]`;
    aim for more experiments per month `[LD-SAVAGE]` vs value over volume,
    skip four kinds of change `[LD-MOORE]`; teams that get the most value run
    better tests, not more `[GB]`; Simon Cast and Holmes warn against vanity
    experimentation `[DOP]`.
13. **Settling disagreements by test.** A good use `[LD-KROLL, LD-MOORE]`, but
    "use sparingly" when build time is significant `[LD-KROLL]`.
14. **Multivariate gives more insight.** "Usually more detailed insights than
    A/B" `[UP]` vs needs much more traffic and best only for optimizing near a
    peak `[MTP-CAST, MTP-1, GB]`.

---

## 5. Worked examples and numbers

| Example or number | Who published it | Flag |
| ----------------- | ---------------- | ---- |
| Netflix tests artwork for titles to raise engagement; thousands of A/B tests a year | Batch-1 unattributed guide | Unsourced in the guide. General knowledge: Netflix's artwork testing is documented on its tech blog. |
| Booking.com runs "over 1,000 A/B tests every day" | Batch-1 unattributed guide | Unsourced; likely wrong. General knowledge: usually reported as about 1,000 concurrent experiments. Confidence: medium. |
| Etsy: a more prominent "Add to Cart" colour raised add-to-cart rates | Batch-1 unattributed guide | Unsourced; I can't confirm it. |
| Amazon, Booking.com, Facebook, Google and Microsoft run tens of thousands of experiments a year; most companies run less than "a few dozen" a year (Stefan Thomke, HBS) | LaunchDarkly (Savage) | Vendor article citing Thomke |
| "For every experiment that succeeds, nearly 10 don't" (Thomke, HBR) | Planio | Quoted from HBR |
| Only 10 to 30% of experiments produce a clear winner | GrowthBook | Vendor claim |
| Jeff Bezos: success is "a function of how many experiments" Amazon runs | Product School | Quote, no citation given |
| Spotify runs more than 250 tests a year | Mixpanel | Vendor claim citing Spotify's blog |
| Airbnb learned to run experiments longer; North Star is "nights booked" | Mixpanel; Planio | Vendor articles |
| Google's "41 shades of blue" test called "seriously flawed" | Shane Murray | Practitioner opinion |
| Marissa Mayer "allegedly" tested shades of blue | Department of Product | Hedged by the source |
| Dow Jones A/B tested AI summaries (half saw them), "not trying to confirm hopes and dreams" | Product School (ProductCon talk) | Course seller relaying a talk; no result given |
| Onboarding example: completion 60% to 68%, "a significant +8% lift" | Product School | Illustrative. Inference: 60 to 68% is +8 percentage points, about +13% relative; the source mislabels it. |
| "Only 40% of new users complete onboarding; those who don't have 50% higher 30-day churn" | Product School | Illustrative |
| Canary releases start at 1 to 5% of traffic | Product School | Practitioner guidance |
| 97% of PMs say AI helps them decide faster (General Assembly survey) | Flagsmith | Vendor citing a survey |
| PeerIndex: moving buttons did little; radically different layouts gave a 200% conversion improvement; one country converted 50% better for no clear reason | Simon Cast (Mind the Product, 2012) | Practitioner's own case |
| DPG Media moved digital subscriptions into the mobile hero spot after heatmaps; "a resounding success" (no number) | Contentsquare | Vendor case study |
| Canyon Bicycles cut analysis time by 94% | Contentsquare | Vendor claim |
| 5,000 monthly onboarding users vs a decision from 40 sessions is risky | Contentsquare | Illustrative |
| X (Twitter): DAU too slow to move; teams shipped on engagement metrics when DAU harm was ruled out | GrowthBook | Practitioner account on a vendor blog |
| toom moved from partial to 100% traffic, cutting time to confidence | GrowthBook | Vendor case |
| A European marketplace dropped before/after analysis because of seasonality | GrowthBook | Vendor case |
| Dropbox and Khan Academy use tight hypotheses / careful metrics | GrowthBook | Vendor case mentions, no numbers |
| 4 vs 3 items per row, 100% allocation, 2 weeks, 14-day window from day 2 | Statsig | Illustrative design doc |
| Purchases per visit +4% while sessions -10% and purchases -6% | Statsig | Illustrative |
| "Up to 1% regression in subscriptions acceptable per 1% lift in purchased items" | Statsig | Example trade-off rule |
| Mastercard research: 44% of business initiatives fail to break even; 45% of campaigns carry natural test vs control bias | Mastercard | Vendor claim |
| Smart ATMs: $17M annual profit improvement from targeted rollout | Mastercard | Vendor case |
| Telecom retention offers: 3.3% churn decrease (synthetic control) | Mastercard | Vendor case |
| QSR promotion: +1.3% sales per customer; shorter promotions with bigger discounts worked best | Mastercard | Vendor case |
| Apparel remodel: 3.6% lift didn't cover cost; targeted rollout gave $9M NPV in year one | Mastercard | Vendor case |
| 159 billion anonymized transactions behind Mastercard insights | Mastercard | Vendor claim |
| 88% of retailers believe experimentation will be important | Planio | Unsourced |
| Ritual increased its experimentation rate | LaunchDarkly (Savage) | Vendor link, no number |
| GoDaddy built an experimentation culture with Mixpanel | Mixpanel | Vendor testimonial |
| Upwell Labs founder placed product pretotypes in an IKEA store, posing as staff | Huryn | Practitioner anecdote |
| Hotel digital keys: pilot on easy card-key systems across brands first | LaunchDarkly (Kroll) | Illustrative |
| Parking app: preload spots within 0.5 miles; over half of users book the same location | LaunchDarkly (Kroll) | Illustrative |
| Testing Klarna or Happy Returns before an annual contract | LaunchDarkly (Kroll) | Illustrative |
| Google Analytics captures at best 95% of traffic | Ben Smith | Unsourced |
| "60% of people who start trial sign-up don't complete" | Ben Smith | Illustrative |
| Conversion lift: conversions with CPA over $20 need bigger budgets; 40+ day lag needs upper-funnel metrics | Google PDF | Vendor guidance |
| Stacked tests: a prospecting test during a remarketing holdback puts about 30% of prospecting users in the holdback | Google PDF | Vendor illustration |
| Social science rule of thumb: 30+ participants | Strategyzer | General rule, unsourced |
| 96% of PubMed records report at least one significant p-value; positive studies 4 times more likely to be published | PLOS (citing studies) | Peer-reviewed, cited |
| A p-value near 0.05 has about a 50% chance of replicating | PLOS (citing studies) | Peer-reviewed, cited |
| EQUATOR lists 468 reporting guidelines | PLOS | Cited |
| Six Sigma programmes "documented billions" in savings | Six Sigma training site | Unsourced, course seller |
| Factorial tomato yields; coating hardness at three temperatures; urban vs rural store blocking | Six Sigma training site | Illustrative |
| Blood-pressure trial with 200 random participants | Six Sigma training site | Illustrative |
| School science examples (mould and temperature; paper towel absorbency) | Explorable | Illustrative |
| MMR-autism recall bias; Oscar winners' "longer survival" from immortal time bias | PLOS | Cited examples |

---

## 6. Gaps: what the research doesn't cover well

Inference: my reading of what's thin, for the playbook author.

- Discovery experiments get a paragraph each; nearly all the rigour is about
  online A/B tests. The playbook's existing `mom-test-interviews`,
  `design-sprint` and `minimum-viable-product` pages fill some of this.
- No source gives a worked sample-size calculation; all point to calculators.
- Interaction effects between concurrent experiments are mentioned but not
  explained beyond "use layers" `[STATSIG]` and "avoid overlap".
- Network effects and two-sided marketplaces (where control and test users
  affect each other) are only hinted at via Airbnb running longer `[MIX]`.
- Ethics gets one line: a gut check for manipulation `[PLANIO]`, and PLOS's
  pointer to research ethics `[PLOS]`.
- About 18 of 47 pieces are from vendors selling experimentation, analytics or
  flag tools; their method advice matches independent sources, but their
  framing leans toward "test more, buy a platform".

---

## 7. Sources

Kinds: **practitioner** (individual writing from experience), **vendor**
(sells a related tool), **course seller** (sells training or certification),
**consultancy**, **editorial** (publication with editors), **educational**,
**research** (peer-reviewed or research body).

### Batch 1 (pasted inline in the thread)

| Code | Author, publisher, title | Kind | Date | Substantive? |
| ---- | ------------------------ | ---- | ---- | ------------ |
| — | Google AI search summary with numbered links | AI summary | — | Skipped |
| B1-GUIDE | Unattributed, "Product Experimentation: How to Design, Implement, and Learn from Experiments" | Unknown | Not shown | Thin: principles, A/B, MVT, interviews, usability; source of the Netflix, Booking.com and Etsy claims |

### Batch 2 (uploaded file, about 20 pieces)

| Code | Author, publisher, title | Kind | Date | Substantive? |
| ---- | ------------------------ | ---- | ---- | ------------ |
| PS | Carlos Gonzalez de Villaumbrosia, Product School, "The Product Experimentation Playbook for AI PMs" | Course seller | 2025-12-30 | Yes: 8 types, 6-step framework; AI section is promotional |
| LONGDEN | Jonny Longden (Speero), LinkedIn, "How to (Properly) Integrate Experimentation into Product Management" | Consultancy | 2025-04-30 | Yes: horse-race model, operating system |
| FLAG | Asaph Kotzin, Flagsmith, "Product Experimentation: Why Most Teams Get the Foundation Wrong" | Vendor | Not shown | Yes: validation vs experimentation, 5 steps, infrastructure |
| DOP | Rich Holmes, Department of Product, "How to Design Experiments for Your Product" | Practitioner newsletter | Not shown | Yes: process, prioritization, idea table |
| UP | Userpilot Team, "Product Experimentation Guide for Product Managers" | Vendor | Not shown | Partly: types list |
| PHQ | Product HQ, "Experiment design for product managers" | Course seller | Not shown | Yes: strongest single design guide |
| LD-KROLL | Valerie Kroll (facts & feelings), LaunchDarkly blog, "When does experimentation add value?" | Vendor blog | Not shown | Yes: 10 scenarios |
| NOMAD | "Digital Nomad in Product management", Medium, "Best Practices for Product-led Growth Experimentation" | Practitioner | 2023-06-15 | Thin; recommends Thomke's *Experimentation Works* |
| LD-CHECK | Unattributed 6-stage feature-flag experiment checklist (Inference: likely LaunchDarkly, from its terms) | Vendor (inferred) | Not shown | Partly |
| MIX | Mixpanel Team, "How to create a culture of experimentation in product teams" | Vendor | 2025-03-28 | Culture only |
| MTP-1 | Eira Hayward, Mind the Product, "Experimentation for product teams: Part 1" (Rosemary King; Terry Lee, Flo Health) | Editorial | 2022-03-21 | Yes: generative vs evaluative, conflicts |
| PLANIO | Planio, "How to Build a Culture of Product Experimentation (And Run Better Experiments!)" | Vendor | Not shown | Yes: question-to-hypothesis method, invalidators |
| PMA | Srinath Kotela, Product Marketing Alliance, "Evolving with the market: experimentation in B2C product marketing" | Practitioner community | 2023-11-15 | Thin |
| HURYN | Paweł Huryn, The Product Compass, "Testing Product Ideas: The Ultimate Validation Experiments Library" | Practitioner newsletter | 2023-10-21 | Yes: 18 named techniques; sections 4 to 7 paywalled |
| WINGIFY | Léo Wiel, Wingify (VWO), "Feature Experimentation Best Practices" | Vendor | 2022-04-29 | Thin |
| MURRAY | Shane Murray, "Meaningful Product Experimentation: 5 Impactful Data Projects" (publisher not shown) | Practitioner | Not shown | Yes: cohort analysis, data-team view |
| CSQ | Contentsquare, "Product experimentation framework" | Vendor | 2022-04-27, updated 2026-11-17 | Yes: 6 steps, 5 checks, mistakes |
| DEVCYCLE | DevCycle docs, "Product-Led Experimentation in DevCycle" | Vendor docs | Not shown | Partly: brief template, roles |
| LD-SAVAGE | Cameron Savage, LaunchDarkly, "5 Tips for Fostering a Culture of Product Experimentation" | Vendor | Not shown | Culture; cites Thomke and an HBS study |
| MTP-CAST | Simon Cast (ProdPad co-founder), Mind the Product, "Everything a product manager needs to know about experiments" | Practitioner | 2012-08-20 | Yes: cycle, local maximum, segmentation, log |

### Batch 3 (uploaded file, about 27 pieces)

| Code | Author, publisher, title | Kind | Date | Substantive? |
| ---- | ------------------------ | ---- | ---- | ------------ |
| — | Google AI search summary with numbered links | AI summary | — | Skipped |
| LD-GUIDE | LaunchDarkly, "30 Feature Flagging Best Practices Mega Guide", chapter "9 best practices for experimentation" | Vendor | Not shown | Yes: bias list, segmentation |
| GB | GrowthBook, "Experimentation Design Best Practices: 7 Steps to Improving Your Experiments" (author ex-Facebook and X; name not shown) | Vendor | 2025-12-22 | Yes: baseline, leading/lagging, A/A, sequential |
| STATSIG | Statsig, "Product experimentation best practices" | Vendor | 2024-07-10 | Yes: design doc, MDE, monitoring, readout |
| STRAT | Tendayi Viki and Franziska Beeler, Strategyzer, "Designing strong experiments" | Course seller / consultancy | 2019-08-01 | Yes: evidence strength |
| POSTHOG | PostHog docs, "Experiments & A/B testing best practices" | Vendor docs | Not shown | Yes: launch checklist |
| MINITAB | Minitab Blog Editor, "8 Expert Tips for Excellent Designed Experiments (DOE)" | Vendor | 2016-11-02 | Yes, for industrial DOE |
| NC3RS | NC3Rs, "Key elements of a well-designed experiment" | Research body | Not shown | Yes: power inputs, bias |
| LABTIME | Unattributed, "How to Plan Experiments and Manage Your Time in the Lab" | Educational | Not shown | Off topic, skipped |
| TRANSONIC | Astrid Haegens, Transonic, "Top 7 Factors for Good Experimental Practice" | Vendor (lab equipment) | 2021-03-05 | Mostly animal-lab specific |
| MC | Mastercard, "The essential guide to business experimentation" | Vendor | 2024-04-15, updated 2026-10-27 | Yes: test and learn, synthetic control |
| CANDU | Jonathan Anderson, Candu, "Experimentation Best Practices" | Vendor | 2024-07-16 | Thin |
| BIBIKOVA | Elena Bibikova, "8 Steps to More Successful Experiments" (publisher not shown) | Educational (lab) | Updated 2023-02-07 | Thin for product work |
| SIXSIGMA | Lean Six Sigma training site, "A Comprehensive Guide to Experimental Design Principles" | Course seller | 2026-04-19 | Yes: five pillars, design types |
| CONV | Kyle Hearnshaw, Conversion.com, "Introducing: The 9 experimentation principles" (quotes Lukas Vermeer, Ron Kohavi, Rand Fishkin) | Consultancy | 2018-07-11 | Yes |
| JMP | "Key Principles of Experimental Design" (Inference: JMP, from its e-course mention) | Vendor (stats software) | Not shown | Yes: randomization, blocking, replication, pseudo-replication |
| LABDESIGN | "Experimental Design Considerations" (lab research article series; publisher not shown) | Educational | Not shown | Thin |
| LD-MOORE | Megan Moore, LaunchDarkly, "How to design, prioritize, and run high-impact experiments" | Vendor | Not shown | Yes: when to and not to test |
| SCIFAIR | "Tips for designing your own experiments" (school science guide; publisher not shown) | Educational | Not shown | Thin |
| SMITH | Ben Smith (Boardable), "Best Practices in Product Experimentation" | Practitioner | 2022-01-17 (written 2020-05) | Yes |
| GML | "Experiments" page of an ML project guide (Inference: Google developers) | Educational | Not shown | ML only |
| EXPLORABLE | Martyn Shuttleworth, Explorable.com, "How to Conduct Science Experiments" | Educational | 2008-03-19 | Thin |
| MLEXP | "Machine learning experiments: approaches and best practices" (publisher not shown) | Unknown | 2024-08-12 | ML only |
| PLOS | Schwab et al., "Ten simple rules for good research practice", *PLOS Computational Biology* (PMC9223329) | Research (peer-reviewed) | 2022 | Yes: strongest source on bias and significance |
| SCRIBBR | Rebecca Bevans, Scribbr, "Guide to Experimental Design" | Educational | 2019-12-03, revised 2023-06-21 | Yes: design types |
| GOOGLE-PDF | Google / Think with Google, "Paving the path to proven success: Your playbook on experimentation" (read via summary; page-4 template not extracted) | Vendor (ad platform) | Not shown (likely about 2021) | Partly: ad-measurement methods |

Books named in the research: Stefan Thomke, *Experimentation Works* `[NOMAD,
PLANIO, LD-SAVAGE]`; Eric Ries, *The Lean Startup* `[MTP-1]`. Other resources
named: Kromatic website `[MTP-1]`; Reforge courses `[SMITH]`; Oxford
Catalogue of Bias, GRADE, EQUATOR, OSF `[PLOS]`; Alberto Savoia's pretotyping
techniques (named as "pretotyping techniques") `[HURYN]`.
