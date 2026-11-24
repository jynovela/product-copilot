<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Decision making: knowledge from research batch 1

Everything worth keeping from Juan's decision-making research batch (sent 2026-11-23 CT, about 37 web pieces), for turning into playbook pages. Written 2026-11-24 by the thread "Research decision making for product-copilot". The design findings (decision page fields) are in the plan doc section "Gap research: decision making"; this file holds the general knowledge.

How to read it:

- Claims are paraphrased. Each ends with source keys in brackets, such as [Bain]. The keys are listed in section 6.
- **Vendor** marks a source that sells a product or service related to the claim. Treat its claims as marketing until another source backs them.
- **From memory** marks something I added that no source in the batch says. Verify before using as fact.
- Left out: generic self-help with no reusable method (trust your gut, be brave, sleep on it), course pitches, and an AI search summary that was in the file (it's an AI answer, not a source).

## 1. Frameworks, models and methods

### 1.1 Decision processes (the steps of a decision)

**Seven-step decision process.** Identify the decision; gather information; identify alternatives; weigh the evidence; choose; take action; review the decision and its consequences. If the review shows the need wasn't met, repeat steps. Step 4 asks you to imagine carrying each alternative to the end and rank them by your own values. [UMass] Atlassian uses the same seven steps and adds a tool and a trap for each: 5 whys and problem framing to identify (trap: decision fatigue); mind mapping and a project poster to gather (trap: information bias); six thinking hats and brainwriting to find alternatives (trap: groupthink); SWOT and a trade-off analysis to weigh (trap: "extinction by instinct", deciding just to be done); DACI or a vote to choose (trap: analysis paralysis); a stakeholder communication plan plus goals, signals and measures to act (trap: self-doubt); a 4 Ls retrospective to review (trap: hindsight bias). It says the full process is overkill for small choices. [Atlassian-process, vendor] Business News Daily gives a five-step version: identify the goal, gather information, evaluate options, choose, evaluate the decision in the short and long term. [BND] Atlassian's second piece walks the seven steps through choosing a new hire. [Atlassian-guide, vendor]

- When: a consequential choice with time to think. Limits: generic; says nothing about who decides.

**Six-step product decision cycle (Naik).** Identify the problem precisely (not "engagement is low" but "daily active users dropped 22% after the onboarding redesign"); gather qualitative and quantitative input; list alternatives, always including do nothing, tweak what exists, and build something new; choose (use a premortem); implement with owners, a timeline and success metrics; review what worked, what failed, and what to change. [Naik]

**Ten-step decision framework (Cheesecake Labs).** Describe the issue; align with company goals and product strategy; map stakeholders; learn their concerns (interviews, surveys, focus groups); research the market; ask outside opinions; explore risks; evaluate outcomes with scenario analysis; check resources; analyze constraints (regulation, dependencies, policy). [Cheesecake, vendor: agency]

**SPADE (Gokul Rajaram, at Square).** For hard decisions that must be made quickly, not everyday ones.

- Setting: what exactly is being decided, when it must be decided and why now. Abraham adds the value metric affected. [Zeda, Abraham]
- People: three roles. Responsible: makes the decision and is accountable for it (Rajaram treats the two as the same). Approver: vetoes the quality of the decision process, not the decision itself. Consultants: give input. Rajaram says most companies rely on consensus for hard calls and that this doesn't work. [Zeda]
- Alternatives: feasible, diverse and comprehensive options, beyond the obvious binary. [Zeda, Abraham]
- Decide: consultants vote privately first, to avoid groupthink; the responsible person decides. [Zeda] Abraham's version says decide "based on data and voting, if required". [Abraham]
- Explain: communicate the decision and its reasons. [Zeda, Abraham]

Abraham's piece doesn't name Rajaram; Zeda does. [Abraham, Zeda]

**Bain's What, Who, How, When (part of "Five Steps to Better Decisions").** To fix one decision: clarify the What (frame it well; Ford's Alan Mulally reframed taking bailout money from yes/no into "what strategy best maximizes long-term value", which surfaced alternatives such as fixing operations, a merger or Chapter 11). Determine the Who (decision roles, using RAPID). Understand the How (consensus, vote or one person; how information flows; agree criteria in advance; present more than one real alternative). Make the When explicit (timetables and deadlines, so action follows quickly and "the hurdle to reopen the decision is high"). [Bain]

**Bain's five steps to better decisions (organizational).** 1 Score the organization on decision quality, speed, yield (execution) and effort, by surveys, interviews and data. 2 Focus on critical decisions using "decision architecture": list decisions per business process and screen them by value at stake (value of one decision times how often it's made, so frequent small operating decisions count) and by how much management attention they need, ending with the top 20 to 30 critical decisions; diagnose a broken one with a "decision X-ray". 3 Make decisions work (What, Who, How, When). 4 Build an organization that supports decisions (for example, put the best people in the jobs with most impact on critical decisions). 5 Embed decision capabilities. Its warnings: don't start what you won't finish; apply the tools to hard decisions, not only easy ones; don't fudge people issues; cut bureaucracy, and don't assign RAPID roles unless the decision's value justifies it. [Bain, vendor: consultancy that owns RAPID]

**Outcome-based product management (Torres, 2015).** 1 Map the challenge visually (customer journey, sales flow, system architecture). 2 Find points of intervention using performance data on each part (where do people drop off?); "the most important decision a product manager makes is where to invest resources". 3 Source ideas for that one point of intervention, from the whole organization; companies have too many ideas but consider too few when deciding. 4 Rank ideas by expected impact on that challenge alone and pick the top two or three, instead of spreadsheets with half a dozen criteria. 5 Test assumptions: list what must be true for each idea, collect evidence, run experiments only as needed. Then invest or "jump" to another idea or back to sourcing, and keep monitoring whether the point of intervention has moved. [Torres]

**Data-driven decision making (IBM).** Defined as using data and analysis "instead of intuition". Six steps: define objectives; identify, prepare and collect data; organize and explore; analyze; draw conclusions; implement and evaluate. Challenges: data quality, silos, data illiteracy, over-reliance on historical data, confirmation bias in analysis, security. Four kinds of analysis: descriptive (what happened), diagnostic (why), predictive (what will happen), prescriptive (what to do). [IBM, vendor] Momentum's version: define a North Star metric, instrument everything early, combine quantitative with qualitative, make data accessible. [Momentum, vendor]

**Decision-Making PreAmble and Decision Classification Grid (Walker).** The PreAmble is a pause before debate to agree what is being decided, how it's framed, the assumptions, and what the process should achieve. Teams that debate options first end up "solving different problems, revisiting assumptions, or negotiating authority". The grid classifies a decision on two axes, purpose (strategic or operational) and reversibility, and the class sets how much deliberation, participation and authority it gets. Three questions before a decision: awareness (whose tendencies dominate), practices (which assumptions to examine), design (who participates, who has authority, which process). Walker also sells a decision-style assessment (Wizer). [Walker, vendor: coach]

**Evidence-based practice, decision step (health information professionals).** In evidence-based practice the steps are question, search, appraise, then decide; the chapter covers the decide step with biases, group methods and tools (all listed below). [NCBI]

### 1.2 Who decides: decision roles and rules

**RAPID (Bain).** Five roles per major decision: Recommend (builds the proposal with data, options, risks and a recommended direction), Agree (must sign off, usually legal, finance or regulatory; assign only when required), Perform (carries it out; brought in early as a reality check), Input (advises; has no authority), Decide (one person makes the final call and owns the result). [Bain, Wing, Zeda] Wing's rules: one Decider, "never two", and never "the committee"; if more than two people must Agree, "you're basically creating a small senate"; write the roles down in a simple doc; check afterwards whether the Decider became a bottleneck. [Wing, vendor] Use it for high-impact decisions that touch money, customers or risk. [Wing] Limits: heavy for small tasks. [Wing, Bain]

**DACI.** Driver (gathers stakeholders and information and gets a decision at each milestone), Approver (the one person who makes the final decision), Contributors ("a voice but no vote"), Informed (told the result). It can make people wary of stepping on toes, so they hold back. [Atlassian-guide, Atlassian-process, vendor] Wing compares: DACI suits product and cross-functional work but is "less structured" than RAPID. [Wing, vendor]

**RACI.** Responsible, Accountable, Consulted, Informed, for each task. Good for who does the work; it doesn't name a single decision-maker. [Asana, Wing]

**Pichler's four decision rules.** A decision rule states who decides and how you can tell the decision has been made. Unanimity (everyone agrees and endorses it: strong support, slow); consent (nobody has a meaningful objection); majority or supermajority (more than half, or two-thirds or 75%); product person decides after discussion (fast, but weaker buy-in if others' ideas aren't considered). None is always right. Example of why it matters: silence after "is everyone OK with changing the needs statement?" isn't agreement, and it may be unclear whether the PM, the group or a sponsor has the final say. Also: decide business-as-usual items yourself; involve stakeholders and the development team for complex, high-impact decisions such as strategy and roadmap changes, pivots, new markets, retiring a product, replacing product goals, or moving roadmap dates; choose sprint goals with the team. Use a power-interest grid (Ackermann and Eden) to pick stakeholders, and a dedicated facilitator who makes sure a decision rule is chosen. Steps for a group decision start with gathering diverse perspectives. [Pichler]

**MIT team decision models (Stein).** From least to most participatory: leader decides and informs; leader gathers input then decides; leader sets constraints and delegates; consensus; consensus with a fallback. Majority vote suits low-impact decisions but leaves people feeling they "lost" on important ones. Consensus isn't unanimity: it's reached when everyone had a fair hearing and can fully support the decision, even if they gave up a non-crucial point. Four statements to check consensus: I have heard your positions; I believe you have heard mine; the decision doesn't compromise my values; I can fully support the decision and its implementation. Watch that nobody changes their mind out of fear or teasing. Knowing how a decision will be made helps plan agendas and builds commitment. [MIT]

**Vroom-Yetton-Jago model.** For decisions for a team. Answer seven yes/no questions in a decision tree to get one of five styles: Autocratic A1 (decide alone on the information you have), A2 (get specific information from the team, then decide), Consultative C1 (ask people one by one, then decide), C2 (discuss as a group, then decide yourself), Collaborative G2 (facilitate the group to consensus). Critics call it rigid. [Atlassian-guide, vendor]

**Three decision styles (Stewart).** Directive (decide alone), consultative (get input, then decide), consensus (decide together). Leaders gravitate to one or two; learn when to switch. [Stewart, vendor: training firm]

**Group methods that limit dominant voices.** Nominal group method (in person) and the Delphi method (asynchronous, confidential rounds of ideas until consensus). [NCBI] Brainwriting: everyone writes ideas alone before group discussion. [Atlassian-process, Zeda] Multivoting: vote repeatedly to cut a long list down. [BND]

### 1.3 Classifying decisions

**Type 1 and Type 2 decisions (Jeff Bezos, "one-way and two-way doors").** Type 1: irreversible and high-stakes ("tattoo"); needs deep thought, data and stakeholder alignment. Type 2: reversible ("haircut"); decide fast and adjust. The common mistake is applying Type 1 process to Type 2 decisions, which slows big companies down; the reverse mistake, treating a Type 1 decision casually, causes waste or failure. Examples given: pivoting the strategy or entering a market (Type 1); trying a new onboarding flow or a time-limited price change (Type 2). [Zeda, Abraham, 6-frameworks, Walker] All of these are secondhand; none quotes Bezos's 2015 shareholder letter (from memory: that is where the idea appears).

**Satisficing vs maximizing.** Maximizers want the best out of every decision; satisficers accept "good enough". Both have a place: maximize on big decisions, satisfice on trivial ones. Maximizers risk decision paralysis. [Atlassian-process, NCBI]

**Strategic vs operational, and critical decisions.** See Walker's grid (1.1) and Bain's decision architecture (1.1).

### 1.4 Evaluating options

**Decision matrix.** Also called Pugh method, decision grid, selection grid, criteria rating form and other names. [Indeed] A table of options against shared criteria. Types: unweighted (sum scores), weighted (multiply each score by the criterion's weight), and Pugh or baseline (rate each option +, 0 or − against a baseline such as what you offer today). [Asana, Indeed] Asana's seven steps, with a design-agency example: list eligible options (drop any that fail hard requirements such as budget and deadline, before scoring); choose criteria; agree the evidence for each rating; build the grid; set weights before seeing scores; rate on a defined 1 to 5 scale where 5 is always best; multiply and total; then run a sensitivity check (does a reasonable change to one weight flip the result?). Record beforehand: decision, owner, deadline, hard requirements, eligible options, scale. Record afterwards: evidence per rating, leading option and runner-up, what would change the result, selected option, trade-offs, open conditions. "Do not adjust weights solely to achieve a preferred outcome." [Asana, vendor] Indeed: set weights by splitting 10 points by team consensus, or average each member's weights; rate on a scale, by rank, or against a baseline; when raters disagree, discuss rather than average; the top score is a starting point for discussion, not the answer; a low-scoring criterion on a good option can be fixed by borrowing from other options. [Indeed] Limits: doesn't remove bias, works only when all options share criteria (use a decision tree for branching choices); it's easy to weight factors without noticing. [Asana, Atlassian-guide] A CFO interviewed by Business News Daily says such tools are better "as communication tools than decision-making tools". [BND]

**Decision tree.** Maps each choice, its outcomes and their probabilities. Fights the habit of turning a decision into one short-term yes/no question. Use for branching or sequential choices such as monetization, go/no-go on markets, or pricing. Limits: oversimplifies uncertainty; probability estimates can be wrong; too much detail hides the key issue. [NCBI, 6-frameworks, Naik, BND]

**Annie Duke's three Ps (from "How to Decide").** Preferences (how much you want each outcome), payoffs (upside and downside of each outcome against your goal), probabilities (how likely each is; Duke says good decisions need a willingness to guess). Lay them out in a decision tree. [Abraham]

**Other evaluation tools the batch lists.** Pros and cons list or T-chart (Benjamin Franklin's method) [BND, Tucker]; cost-benefit analysis (proportional effort; watch for intangibles that are hard to price) [BND, NCBI, 6-frameworks, Naik]; SWOT (watch for being too subjective) [BND, 6-frameworks, Naik, Atlassian-process]; PEST (political, economic, social, technological factors) [BND]; Pareto analysis (which decisions to make first) [BND]; conjoint analysis (customer preferences) [BND]; competitive analysis [BND]; RICE (reach × impact × confidence ÷ effort) [Naik]; MoSCoW [6-frameworks]; Eisenhower matrix (urgent vs important) [6-frameworks, Naik, Asana]; effort vs impact matrix [Naik]; six thinking hats [Atlassian-process]; logic model (inputs, activities, outputs, impacts) [NCBI]; root cause analysis [NCBI]; project trade-off analysis (which of time, scope or cost you'd give up) [Atlassian-process].

**Game theory for product calls (Naik).** Before a move such as a new pricing tier, ask how competitors and users will respond: will competitors match it, will users see a downgrade, will power users upgrade or churn? [Naik]

**"Futurize" (Tucker).** Look 3, 5 and 10 years ahead and ask what the environment will be like then. Also: define whether the decision is binary, multiple-option or open; broaden from A and B to C and D using a "challenge statement". [Tucker]

**Fear setting.** List the worst cases, their permanent impact (1 to 10) and likelihood; how you'd repair each; the benefits of the likely outcomes; and the cost of not deciding ("making no decision is still a decision"). [Bluelink, vendor]

**Ladder of inference.** Observe data, select data, add meaning, make assumptions, draw conclusions, adopt beliefs, act. Climb it rung by rung to avoid jumping to conclusions; the trap is a "recursive loop" where beliefs decide which data you select. [Atlassian-guide]

**Facts vs assumptions (Naik).** Sort inputs into stated facts (verifiable), unstated facts (assumed, such as "it's bug-free"), reasonable assumptions (from patterns) and unreasonable assumptions (speculation). Ask of each: fact or assumption, and is the assumption reasonable? [Naik]

**Scientist mode.** Approach a decision like a study: stay humble, state hypotheses, test them. [NCBI]

**37% rule (flagged).** The EI Network describes it as spending 37% of the time researching, then committing to the next best option. [EI, LinkedIn post] From memory: the known rule is optimal stopping, which says look at the first 37% of options without choosing, then pick the first that beats all of them. The post's version is loose; don't use it as stated.

### 1.5 Risk, revisiting and fast decisions

**Premortem.** Imagine the decision has failed and ask why, before committing. [Naik, Abraham] Duke uses it to set kill criteria. [Abraham]

**Kill criteria (Annie Duke).** Set during the premortem: signals that things aren't going as planned, each tied to an action decided in advance. Example: if there's no first sales deal within 3 months of launch, kill the product. [Abraham, citing Duke and First Round Review]

**Rekhi's test for reopening a decision.** Before revisiting, ask what new information is now known. This stops flip-flopping but still allows a change of course. [Rekhi] Contrast Bain's deadlines that make the hurdle to reopen high. [Bain] One 2025 piece: a decision framework should include how to recognize when a decision needs revisiting. [PM-2025]

**OODA loop.** Observe, orient, decide, act, then repeat; from combat pilots; for outages, PR crises or backlash after a launch. [Naik]

**Recognition-primed decision model (Gary Klein).** Experts in real time recognize a familiar pattern and act, instead of comparing all options. [Naik]

**Speed tactics (GP Strategies).** Flex simple frameworks (quick pros and cons, a simple matrix); chunk a big decision into smaller ones; anticipate recurring challenges by spotting patterns; consult even when fast; check against priorities and values; "go slow to go fast"; name the biases; adopt a growth mindset and fail fast. [GP, vendor: training firm]

### 1.6 AI and decisions

- Use AI as a "co-thinker" rather than delegating the decision. Abraham's prompts: generate 3 to 5 options beyond the current ones; evaluate options against stated criteria; compare short-term (1 to 2 years) and long-term (5+ years) benefits and limits, find inflection points, signals that the choice was right, and checkpoints to reassess; list risks and unintended consequences. More context gives better answers. [Abraham]
- Business News Daily names AI decision tools (MakerSights for retail, Rainbird) and says AI helps more as decisions get more complex. [BND, names only]

## 2. Definitions and vocabulary

- **Decision making:** making choices by identifying a decision, gathering information and assessing alternatives. [UMass]
- **Uncertainty vs risk:** uncertainty is what you can't predict about future events or results; risk is the chance a specific choice leads to loss, judged by both likelihood and seriousness. Drivers: market volatility, technology changes, limited information, outside events. [Cheesecake]
- **Data vs information:** data is raw numbers ("1,000 users dropped off on page 2"); information is context ("they drop off because page 2 loads slowly"). [Naik]
- **Decision effectiveness (Bain):** quality, speed, yield (how well it's executed) and effort. [Bain]
- **Critical decisions (Bain):** the 20 to 30 decisions that must work; both big strategic ones and small frequent operating ones. [Bain]
- **Consensus vs unanimity vs consent:** MIT says consensus is not unanimity, but full support after a fair hearing. Pichler separates unanimity (everyone agrees and endorses) from consent (no meaningful objection). [MIT, Pichler]
- **Decision rule:** in Pichler, who decides and how you know it's decided. [Pichler] Not the same as an experiment's decision rule (the threshold set before a test) used elsewhere in product-copilot.
- **HiPPO:** "highest paid person's opinion" decision-making, a sign of a broken process. [Rekhi]
- **Leading vs lagging indicators:** lagging shows results (revenue, churn, retention); leading gives early signals (onboarding completion, feature usage, time to value). Use leading ones for proactive decisions. [Naik]
- **Data-driven decision making:** "instead of intuition" [IBM]; "replacing 'I think' with 'the data shows'" [Momentum]; but Chakraborty treats intuition as a hypothesis to validate with data. See conflicts.
- **Decision fatigue:** worse decisions after making many; term attributed to Roy Baumeister. [Atlassian-process, Bluelink]
- **Analysis paralysis:** overthinking until you freeze. [Atlassian-process, Stewart]
- **Information bias:** seeking more information even when it won't change the action. [Atlassian-process]
- **Extinction by instinct:** deciding just to get it over with. [Atlassian-process]

Same word, different meaning (worth a line on the playbook page):

- **Approver.** In DACI, the one person who makes the final decision. [Atlassian-guide] In SPADE, someone who vetoes the quality of the decision process, not the decision. [Zeda]
- **Responsible.** In RACI, whoever does the work. [Asana] In SPADE, the decider, who is also accountable. [Zeda]
- **Agree (RAPID) vs Approve (DACI).** RAPID's Agree is a required sign-off that isn't the decision; DACI's Approver is the decision. [Bain, Wing, Atlassian-guide]

Cognitive biases the batch names, with its definitions:

- Confirmation bias: seeking information that supports what you believe. [Naik, Atlassian-guide, IBM]
- Anchoring: relying on the first number or a few facts. Naik's example is a salary offer that anchors the counteroffer. [NCBI, Naik]
- Availability heuristic: overweighting what's easy to recall, such as halting a rollout because one customer churned. [Naik, NCBI]
- Representativeness heuristic. [NCBI]
- Sunk cost: sticking with something because of what's already spent ("we've built 70%, let's finish"). [Naik, NCBI, BND]
- Groupthink: conforming for harmony. Counter with devil's advocates, anonymous feedback, brainwriting. [Naik, NCBI, Atlassian-process]
- Status quo bias, authority bias, halo and horns effects, professional deformation (seeing everything through your own profession's goals). [NCBI]
- Hindsight bias: judging a past decision with knowledge you didn't have then. [Atlassian-process]
- Illusory truth effect: repeated information feels true. Counter by asking where information came from, fact-checking as a habit, and repeating what is true. Bias blind spot: seeing bias in others more than in yourself. [Esade]
- Overconfidence: the bias Kahneman said he'd eliminate if he could pick one. [Esade]
- Extrapolation bias: assuming current trends continue. [BND]
- Framing effect: the same facts framed as gains or losses change choices; "90% success" lands better than "10% failure". [Naik]
- System 1 and System 2: fast heuristics vs slow deliberate thinking; errors come from using System 1 where System 2 is needed. [NCBI]

## 3. Practices most sources agree on

- **Define the decision before debating options.** [UMass, Atlassian-process, Bain, Walker, Tucker, Naik, Cheesecake]
- **Generate more than two real options**, including doing nothing, and reframe yes/no questions. [Bain, Torres, Naik, Tucker, Atlassian-process, NCBI, Zeda]
- **Make it clear who decides and how**, before the discussion. [Bain, Wing, Pichler, MIT, Atlassian-guide, Zeda, Rekhi, Walker]
- **Match the process to the decision.** Heavy process only for consequential or irreversible decisions; decide small, reversible ones fast. [Bain, Atlassian-process, Walker, Zeda, 6-frameworks, Pichler, Wing]
- **Get diverse input and reduce dominant voices** (private votes, brainwriting, Delphi, facilitator). [Pichler, Zeda, NCBI, Esade, Atlassian-process]
- **Communicate the decision and the why.** [Rekhi, PM-2025, Bain, Zeda, Atlassian-guide, Stewart, Abraham]
- **Watch for named biases**, especially confirmation bias, anchoring, sunk cost and groupthink. [nearly all]
- **Review decisions afterwards**, without hindsight bias, and learn from bad decisions as well as good ones. [UMass, Atlassian-process, Naik, Stewart, PM-2025, BND]
- **Set deadlines**, and don't let the gap between deciding and acting grow. [Bain, Stewart, Bluelink, Rekhi]

## 4. Conflicts between sources

- **One decider vs group rules.** RAPID: one Decider, never two, never a committee [Bain, Wing]. SPADE: consensus doesn't work for hard decisions [Zeda]. Pichler: four rules, including unanimity and majority, none always right [Pichler]. MIT: consensus and consensus with a fallback are valid models [MIT]. Atlassian offers a simple majority vote for "democratized" decisions [Atlassian-process]. MohammedBhai: outside a startup the PM drives the decision, but who actually decides depends on the business [MohammedBhai].
- **Is the PM the decider?** Rekhi: the PM curates ideas and makes the call. MohammedBhai: the PM owns the product's success but must drive others (a board, a CEO) to decide; in his example leadership rejected his proposal despite the evidence. Pichler: the product person decides after discussion is one option among four. [Rekhi, MohammedBhai, Pichler]
- **Speed vs deliberation.** Rekhi: favor deciding today unless you're waiting on specific information. GP Strategies: faster decisions beat no decisions. Naik: make clear decisions fast. Pichler: don't rush important decisions. Walker: design the process before deliberating. Atlassian warns against "extinction by instinct". [Rekhi, GP, Naik, Pichler, Walker, Atlassian-process]
- **Reopening.** Bain: high hurdle to reopen. PM-2025 and Chakraborty: few decisions are permanent, so monitor and change course. Rekhi's middle ground: reopen when you can name new information. [Bain, PM-2025, Chakraborty, Rekhi]
- **Data vs intuition.** IBM and Momentum: data instead of gut feeling. Atlassian-guide: "data doesn't lie, which makes it a bias-proof resource". Against that: IBM itself lists confirmation bias in analysis, Esade shows repeated false information is believed, Naik warns about bad inputs and vanity numbers. Chakraborty, Tucker and Bluelink keep intuition as an input; Chakraborty treats it as a hypothesis to test. [IBM, Momentum, Atlassian-guide, Esade, Naik, Chakraborty, Tucker, Bluelink]
- **Multi-criteria scoring vs one criterion.** Asana and Indeed: weighted matrices with several criteria. Torres: rank ideas by expected impact on one point of intervention, not "complex spreadsheets with half a dozen criteria". BND's CFO: matrices help communicate more than decide. [Asana, Indeed, Torres, BND]
- **How to settle disagreement in a matrix.** Indeed: discuss to consensus, don't average ratings. Indeed also offers averaging members' weights into a composite. Asana: gather more evidence or agree a tie-breaker. [Indeed, Asana]
- **Guessing.** Duke: good decisions require a willingness to guess probabilities. 6-frameworks: the main pitfall of decision trees is relying on inaccurate probability estimates. [Abraham, 6-frameworks]
- **Value of frameworks at all.** An SEO agency owner told BND that "99 percent" of management models aren't helpful. Most other sources recommend them. [BND]

## 5. Worked examples and numbers

| Example or number | Who published it | Flag |
| --- | --- | --- |
| Design-agency decision matrix: weights cost 5, experience 3, communication 2, reviews 4; totals 49, 51, 42; raising communication's weight to 4 makes a tie, so the team checks Agency 2's communication before choosing it | Asana | Vendor, invented example |
| Office chair matrix: weights comfort 5, cost 3, reviews 4; totals 40, 49, 32, 53 | Asana and Indeed (same example) | Invented example |
| Asana's Meeting Reset: 60 participants; saved 265 hours a month; 70% of savings from changes other than cancelling | Asana | Vendor, about its own experiment |
| Hospira scored in the 40th percentile on decision abilities, then redesigned key decisions; shareholder return later in the upper quartile | Bain | Consultancy case study; causation claimed, not shown |
| Nike identified 33 critical decisions during a restructuring | Bain | Consultancy case study |
| Intel's Embedded and Communications Group used RAPID-style roles for roadmap decisions and a regular "here's what we've done, here's why" update | Bain | Consultancy case study |
| A European automaker unit lagged because marketing and product development both thought they decided on features | Bain | Unnamed anecdote |
| A tech company's top performers: under 30% of mission-critical roles held by them; only 40% of them in such roles | Bain | Unnamed company |
| "Clear correlation (at a minimum 95% confidence level)" between decision effectiveness and business performance, from 1,000+ companies over 10 years | Bain | Vendor's own research; RAPID is its registered trademark |
| Ford's Mulally reframed the bailout decision into a strategy choice with several alternatives | Bain | Secondhand anecdote |
| Clear decision structures cut approval time 30 to 50%; Wing clients report a 40% jump in "workflow clarity"; leaders save 5 to 10 hours a week of delays | Wing | Vendor, unsourced |
| "We make about 35,000 decisions a day" | GP Strategies, Naik | Unsourced; GP's own asterisk says "some sources" |
| "700 decisions daily" | Tucker (Forbes contributor) | Unsourced; contradicts the 35,000 figure |
| 70% of business leaders would prefer a robot to make their decisions (2023 Oracle study) | HBS Online, citing a press release | Vendor survey |
| 84% of HBS Online learners felt more confident | HBS Online | Self-promotion |
| Diverse teams make better decisions 87% of the time | Chameleon, citing Cloverpop | Vendor white paper |
| 57% of respondents in a 2015 survey (on being told the reasons behind decisions) | Atlassian-guide | Number only; context cut off in the file |
| Diverse groups outperform more able homogeneous groups (PNAS study) | Esade | Peer-reviewed study, cited secondhand |
| Health information professionals' most-observed biases (2007 survey): professional deformation first, then status quo, authority, anchoring, groupthink, halo/horns | NCBI chapter | 135 of about 2,000 responded; the author calls the sample unrepresentative |
| "Daily active users dropped 22% after the onboarding redesign" as a good problem statement | Naik | Illustration |
| Asian disease problem (Tversky and Kahneman) | Naik | Naik's version garbles the options (from memory: the original compares the same programs framed as lives saved vs lives lost) |
| Kill criterion: no first sale within 3 months of launch means kill | Abraham, after Duke | Illustration |
| Amazon Fire Phone as a product that clashed with Amazon's low-price strategy | Chameleon | Vendor's interpretation |
| Airbnb started by renting air mattresses, as an MVP story; "valued at about $130 billion" | Chameleon | Valuation dated 2021 |
| A CEO announced at an all-hands of 2,000 people that a product would be free for existing customers, before the PM agreed | MohammedBhai | First-person anecdote |
| A multinational turned down the author's SME product plan and now loses about 7% share a year | MohammedBhai | First-person, unverified |
| FINN: continuous discovery and constant talk about resources kept decisions fast | Cheesecake Labs | Agency client story |
| Coupa's PMO scores intake requests into a priority number before the roadmap | Asana | Vendor customer story |
| 85% of enterprises will use AI decision tools (IDC) | BND | Analyst forecast, cited secondhand |
| "402.74 million terabytes of data daily" | IBM, citing Exploding Topics | Secondhand statistic |

## 6. Sources

Substantive means it carries a method, a definition or an argument worth keeping. Kind: practitioner, vendor (sells a related product or service), research, media, education.

| Key | Title | Author | Publisher | Kind | Date | Substantive? |
| --- | --- | --- | --- | --- | --- | --- |
| Bain | The Five Steps to Better Decisions | Marcia Blenko, Michael Mankins, Paul Rogers | Bain & Company | Vendor (consultancy, owns RAPID) | 2013-08-06 | Yes: RAPID, decision architecture, What/Who/How/When |
| Pichler | Making Effective Product Decisions: Tips for Deciding with Stakeholders and Dev Teams | Roman Pichler | Pichler Consulting | Practitioner (consultant) | 2021-06-07, updated 2024-09-30 | Yes: decision rules, when to involve others |
| Rekhi | The Art of Decision Making as a Product Manager | Sachin Rekhi | sachinrekhi.com | Practitioner | 2014-05-12 | Yes: revisit test, curator role |
| Torres | The Path to Better Product Decisions | Teresa Torres | Product Talk | Practitioner (coach) | 2015-09-23 | Yes: outcome-based process |
| Abraham | Making Better Product Decisions: Approaches and AI Prompts for Product Managers | Marc Abraham (MAA1) | Medium | Practitioner | 2025-04-09 | Yes: SPADE, Type 1/2, Duke, kill criteria, AI prompts |
| Zeda | Strategic Choices: Making Right Decisions as a Product Manager | Athira V S | zeda.io | Vendor | updated 2024-01-04 | Yes: SPADE detail (names Rajaram), RAPID, Type 1/2 |
| MohammedBhai | What makes effective decision making so challenging for product managers? | Taza MohammedBhai | Mind the Product | Practitioner | 2016-10-19 | Yes: who really decides |
| Naik | How to Make Better Product Decisions | Nilesh Naik | not shown | Practitioner | 2025-04-04 | Yes: six-step cycle, facts vs assumptions, OODA, RPD, biases |
| Walker | Are You Designing Your Decisions, or Just Making Them? | Michael Walker | LinkedIn | Vendor (coach) | 2026-11-23 | Partly: classification grid, PreAmble |
| MIT | Decision-Making Models | Judith Stein | MIT Human Resources | Education | not shown | Yes: five models, consensus check |
| NCBI | Decision Making (chapter in a guide to evidence-based practice for health information professionals) | not shown | NCBI Bookshelf | Research (book chapter) | not shown | Yes: biases, Delphi, nominal group, decision trees |
| Asana | How to make tough choices with a decision matrix | Julia Martins | Asana | Vendor | 2026-10-21 | Yes: matrix method, sensitivity check, record fields |
| Indeed | What is a decision matrix? | Indeed Employer Content Team | Indeed | Vendor (media) | not shown | Yes: matrix variants and weighting |
| Atlassian-process | (seven-step decision-making process) | not shown | Atlassian | Vendor | 2024-11-29 | Partly: steps with tools and traps |
| Atlassian-guide | Reading this decision-making article is the best decision you'll make today | not shown | Atlassian | Vendor | not shown | Partly: Vroom-Yetton-Jago, ladder of inference, DACI |
| UMass | 7 Steps to Effective Decision Making | not shown | UMass Dartmouth | Education | not shown | Partly: the standard seven steps |
| BND | Techniques and Tools to Help You Make Business Decisions | Siri Hedreen | Business News Daily | Media | updated 2024-05-07 | Partly: tool list, CFO quotes |
| IBM | What is data-driven decision-making? | Tim Mucci | IBM | Vendor | not shown | Partly: DDDM steps, analysis types |
| Wing | RAPID Framework: How to Make Smarter Decisions in 2026 | not shown | Wing Assistant | Vendor | not shown | Partly: RAPID rules; its numbers are marketing |
| Cheesecake | Product Decision-Making in Business: Navigating Uncertainty | Lucas Braga | Cheesecake Labs | Vendor (agency) | 2023-08-25, updated 2026-08-15 | Partly: uncertainty vs risk, ten steps |
| 6-frameworks | 6 Decision-Making Frameworks for Product Managers | not shown | not shown | Unknown | 2024 | Partly: Type 1/2, tree and cost-benefit limits |
| PM-2025 | Decision-making as a Product Manager | not shown | not shown | Practitioner | 2025-04-04 | Partly: communicate the why, revisit, review decision quality |
| Chakraborty | Decision-Making for Product Managers: Balancing Data, Intuition, and Impact | Debabrata Chakraborty | LinkedIn | Practitioner | 2025-12-08 | Partly: intuition as hypothesis |
| Esade | Four strategies for leaders to improve decision-making | Katharina Schmid | Esade Do Better | Education | 2023-06-01 | Partly: illusory truth effect |
| Tucker | 6 Strategies For Making Smarter Decisions | Robert B. Tucker | Forbes (contributor) | Media | 2024-06-24, updated 2024-12-19 | Partly: futurize, broaden options |
| Stewart | 4 Steps to Effective Decision Making | Daniel Stewart | Stewart Leadership | Vendor (training) | 2022-02-21 | Partly: three styles |
| GP | Boost Your Leadership with Rapid Decision-Making Hacks | not shown | GP Strategies | Vendor (training) | 2019-09-04 | Partly: speed tactics |
| Bluelink | 6 Tips for Better Decision-Making in Management | Admin | Bluelink ERP | Vendor | not shown | Partly: fear setting |
| HBS | How to Enhance Your Decision-Making Skills as a Leader | Catherine Cote | HBS Online | Education (course marketing) | 2024-03-14 | Little: stakeholder value, cites course |
| EI | ten decision strategies | The Emotional Intelligence Network | LinkedIn | Unknown | 2025-01-18 | No (37% rule flagged) |
| Chameleon | 5 decision-making tactics for product managers | not shown | Chameleon | Vendor | not shown | Little: examples only |
| Productboard | 5 Best Practices for Optimizing Your Product Management Workflow | Productboard Editorial | Productboard | Vendor | 2024-03-13 | No |
| Aha | 4 steps product managers take to decide what to build next | Julie Hunt | Aha! | Vendor | 2025-02-18 | Little: strategy fit as first filter |
| Momentum | 9 Product Management Best Practices for When Everything Is a Priority | Avi Siegel | Momentum | Vendor | 2025-08-25 | Little: data-driven practices |
| GfG | Product Management Best Practices | not shown | GeeksforGeeks | Media | updated 2024-01-09 | No |
| Brereton | (product design decisions) | Jake Brereton | Dotwork | Vendor | 2023-12-30 | No |

Also in the file and excluded: an AI search summary on effective decision making (it cites Reddit, Quizlet, YouTube, CIPD and UMass), with no author.

## 7. What the batch doesn't cover

- No real product decision log or decision record template from a team (ADR or MADR, an Amazon-style decision doc, a public handbook's log).
- Nothing on overriding an experiment result or the data.
- Nothing primary from Bezos (2015 letter), Duke (Thinking in Bets, How to Decide), Rajaram (SPADE) or Kahneman; all are secondhand here.
- No decision journal method (for example Farnam Street's), and no disagree-and-commit source.
