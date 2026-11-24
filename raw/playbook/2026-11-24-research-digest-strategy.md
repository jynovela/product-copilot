<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Product strategy: what the research taught

Summary of Juan's product-strategy research batch 1 (pasted 2026-11-23, about 31 articles). Written 2026-11-24 for turning into playbook pages. Everything below is paraphrase unless quoted. Each claim names the article it comes from. "Vendor" means the publisher sells a tool, research service, agency work or course on the topic. Where I add something from model memory it is marked "General knowledge:"; my own reasoning is marked "Inference:".

Left out: the AI search summary at the top of the paste (it is not a source), course and tool pitches, and the off-topic parts listed in section 6.

## 1. Frameworks, models, methods and lists

### 1.1 Melissa Perri's product strategy canvas (vision, challenge, target condition, current state)

- What it is: a four-part structure for product strategy, built on Toyota Kata ("Unified Field Theory" by Bill Costantino and Mike Rother). Source: Melissa Perri, "What is Good Product Strategy?", Medium, 2016-07-18.
- Parts:
  - **Vision**: where the company or business line is going in the long term. Qualitative. In large companies, narrow it to a business line or customer journey.
  - **Challenge**: the first business goal on the way to the vision, as a strategic objective (which part of the funnel or journey to fix first). Can be qualitative or quantitative, still broad.
  - **Target condition**: breaks the challenge into smaller, measurable, achievable goals. The team shouldn't know exactly how to reach it, only where to start looking.
  - **Current state**: today's measured reality against the target condition, measured before work starts.
- How it works: set the four, then the team runs the "Product Kata": find the obstacles and experiment to remove them until it hits the target condition.
- Who sets what: vision by CEO, CPO, board and executives; challenge by the next level down (VP of product for a journey or business line); target conditions by direct managers with their teams, handed down at first and co-set as teams mature.
- Worked example (hypothetical, labelled so by Perri): Uber. Vision (a real CEO quote): Uber as the cheap, efficient alternative to owning a car and to public transport. Challenge: cut wait times in cities over 10 minutes to under 5 minutes by 2018-01-30 (assumes people in 5-minute cities are 80% more likely to use Uber). Target condition: at least one driver per 50 people in each city. Note: the article's dates are inconsistent (challenge by January 2018, target condition by January 2017).
- Position: "Product Strategy is a system of achievable goals and visions"; it "emerges from experimentation towards a goal"; KPIs and OKRs are part of it. Perri says it may look like business strategy, and that's the point: products exist to reach business objectives.
- A blank canvas was offered as a PDF (Dropbox link). airfocus later points to the same canvas and describes it as vision, goal, then initiatives in OKR form.

### 1.2 Roman Pichler's Product Vision Board and the elements of a product strategy

- Sources: Roman Pichler, "Elements of an Effective Product Strategy" (romanpichler.com, first published 2015-05-19, updated 2026-01-29); "The Product Strategy Framework: A Revised Guide for Product Leaders" (Medium, 2026-05-12). Pichler sells training and books (*Strategize*), so treat as practitioner with a commercial interest.
- Strategy elements (four choices):
  1. **Market or segment**: who the users and customers are.
  2. **Needs**: the main problem solved, benefit given, or job done.
  3. **Standout features / key features and differentiators**: the 3 to 5 things that make people choose it over alternatives. "Don't make the mistake of creating a mini product backlog or a wish list." Examples: the first iPhone (mobile internet, iPod-like player, touch screen); Chrome (speed, safety, simplicity).
  4. **Business goals**: how the product benefits the company (revenue, selling another product, cutting cost, brand equity). Example: Chrome earns no money directly but reduced Google's dependence on third-party browsers.
- The Product Vision Board puts the vision on top and the four strategy sections below it. Free download at romanpichler.com/tools.
- Making these choices means saying no. A new or significantly changed strategy must be validated by addressing its biggest assumptions and risks ("product strategy discovery").

### 1.3 Pichler's product strategy framework (vision, strategy, roadmap, backlog)

- Source: Pichler, Medium, 2026-05-12.
- A four-level hierarchy:
  - **Vision**: purpose and the positive change the product should bring, a stable "North Star"; a short inspiring statement or slogan; 5 to 10 years; not measurable (a BHAG, credited to Jim Collins).
  - **Strategy**: the approach to realise the vision; "guardrails" for discovery and delivery; usually 12 to 24 months for a digital product, but review it at least every three months.
  - **Roadmap**: how the strategy will be implemented; built on outcomes or product goals (e.g. acquire users, increase engagement), optionally time frames, coarse features and metrics. Usually 12 months; 6 months under high change; a single outcome if you can't see past 2 to 3 months. A speculative roadmap creates unrealistic expectations.
  - **Backlog**: copy the next outcome in, with its features, then add epics, stories, journeys, non-functional requirements, or prototypes.
- Links run both ways: big backlog changes can change the roadmap; roadmap changes can change the strategy; no validated strategy means changing or dropping the vision. He calls this "continuous strategizing".
- OKRs and KPIs: OKRs belong on the roadmap (or an objective as a product goal), not on the vision or strategy. Strategy contains user, customer and business goals but they are "usually neither measurable nor time-bound". Use the needs and business goals to choose KPIs.
- Ownership: Pichler recommends the product manager with an extended team (designer, tech lead, tester, key stakeholders) owns all four levels; the PM has the final say if the team can't agree. Needs the right knowledge and an overarching portfolio strategy.
- Getting started: (1) capture the strategy on the Vision Board and validate it until free of major assumptions (for an existing product, describe the current one and check it); (2) derive one specific measurable outcome and decide what to build; (3) after 2 to 3 months review the goal and the strategy, then consider a 6 to 12 month outcome roadmap with his GO Product Roadmap template.
- On AI tools (he names Claude Cowork and Perplexity Computer): apply the framework by hand first, then automate.

### 1.4 Pichler's Strategy Stack

- Source: Pichler, Medium, 2026-05-12.
- Five layers, seven elements: business (corporate) strategy; product portfolio strategy; technology strategy and product strategy; product roadmap and technology roadmap; product backlog. The product vision sits inside the product strategy element. Used with senior management; the four-level framework is used with product managers.

### 1.5 Pichler's product life cycle and strategic inflection points

- Source: Pichler, 2015/2026 article. Four key events: launch, product-market fit, life cycle extension, end of life. A new product's strategy should first get it to launch, then to PMF, then sustain growth. When growth stagnates, choose to extend the life cycle (rejuvenate, new market) or let it mature and decline. Example: iPhone changes since 2007 (apps, sizes, variants).

### 1.6 Ant Murphy's four steps

- Source: Ant Murphy (co-founder and CPO at Wafr), "4 Steps to Building a Product Strategy", LinkedIn, 2025-10-21. Practitioner who sells a template and coaching. The piece was pasted twice.
- Not a fill-in-the-blanks template. Steps, non-linear:
  1. **Gathering inputs**: data about market, customers, product and business. Don't spend weeks or months here.
  2. **Building strategic narratives**: filter signal from noise and form hypotheses. "Strategic Narrative = Insights based on data + hypothesis about the future." Cites Roger Martin: "Strategy needs to have a theory." Example: does AI-driven redundancy data mean more job losses, or (like past technology shifts) new jobs later?
  3. **Finding leverage**: ideate choices with the highest return; look at moat, unique advantages, pros and cons of paths, what you're best positioned for, flywheels. Martin's "how will we win" (step 2 narrows "where will we play"). Takes the most time: "take whatever time you think you need and double it".
  4. **Choices**: hard choices that focus the product. "If the choices don't feel hard to make, then they're probably not the right choices." If it doesn't eliminate work, it's too high-level. Often no single right answer.
- Choice scaffolding: what is the choice (to do, to be, or not to do; e.g. "building a Freemium version"); who it targets and why; why we believe it (link to narratives); how it supports higher business goals; how we'll do it; how we'll measure progress.
- Quotes Jony Ive on Steve Jobs: focus means saying no to something you think is a phenomenal idea.

### 1.7 Hustle Badger's strategy stack and seven steps

- Source: Ed Biden (ex Depop, JobandTalent, Rocket Internet), "How to write a great product strategy", Hustle Badger, updated 2026-05-15. Sells courses and templates; the most substantive of the commercial pieces.
- Definitions (their strategy stack): **Objective** (the challenge the strategy responds to, its purpose and measure); **Vision** (an inspiring picture of the future our work creates); **Strategy** (the pillars or focus areas and why); **Opportunities** (a team's theme of work under a pillar); **Features** (shippable work exploiting an opportunity); **Goals** (how we measure progress on vision, strategy, opportunities and features); **Roadmap** (visual plan over time). Each squad's stack is a zoomed-in copy of the product's, with two-way feedback.
- "Progress is inversely proportional to the number of priorities we have." "Strategy must result in action to be effective."
- Process: write a strawman in a day, validate the main assumptions in about two weeks, then keep updating from discovery. Three activities: analysis (funnels, behavioural metrics, user research, support contacts, sales and marketing, competitor audits); interviews and meetings (leadership, other disciplines, team, peers); consolidating into a narrative. Tips: be hypothesis-driven (your first view is often "80% correct"); co-create with difficult senior stakeholders; find the 2 to 3 "killer slides"; verify surprising results ("9 times out of 10" a tracking or definition problem).
- Seven steps:
  1. **Objective** = mission (inspiring, qualitative) + measure, in the form "Move [metric] from [baseline] to [target] by [date]". Examples: revenue $100m to $120m by 2024; day-30 retention 20% to 25% by end of Q3. Missions quoted: Shopify, Tesla, Stripe, Slack, Google, Etsy.
  2. **Users**: defined by needs (Jobs to Be Done; ask "why" one or two more times), and explicitly who you are *not* targeting. Journey maps; personas only if needs come first, not demographics.
  3. **Superpowers**: how the company is uniquely positioned; uses Helmer's 7 Powers (1.8). Decided at product level, not squad level.
  4. **Vision**: 3 to 5 years; a paragraph, mock-ups or a clickable prototype; usually owned by product and design leadership. Order of mission and vision doesn't matter.
  5. **Pillars**: 2 to 4 themes that meet user needs, deliver the vision and grow your powers. Work outside pillars should be avoided or done with minimum effort; stakeholders pushing such work haven't bought in.
  6. **Impact**: build an impact model to size each pillar (which metrics move, and by how much, from past work or segment differences). Quotes George Box: "All models are wrong, but some are useful."
  7. **Roadmap**: decide audience, content and format for updates.

### 1.8 Helmer's 7 Powers (as described by Hustle Badger)

- Source: Hustle Badger (above), which links its own 7 Powers article and template. General knowledge: from Hamilton Helmer's book *7 Powers* (2016).
- The seven hard-to-copy advantages:
  1. Network effects: each user gets more value as others join.
  2. Scale economies: unit costs fall as volume grows.
  3. Switching costs: moving to an alternative is costly or painful.
  4. Counter-positioning: a new business model incumbents can't copy without damaging their own business.
  5. Cornered resource: unique access to a valuable asset.
  6. Branding: an identical offering is valued more.
  7. Process power: embedded culture and process that give lower cost or better quality.
- Heuristic (Hustle Badger's): if your solution doesn't generate 2 or 3 powers, expect trouble keeping margins. Investors look for them. Check strength by finding other companies that built durable businesses on similar advantages, and by asking independent investors, board members or experts.
- Related lists of defensibility elsewhere: Phenomenon Studio's technical defensibility (data network effects, integration depth creating switching costs, API ecosystems); the "10 examples" piece's competitive advantages (proprietary technology, unique partnerships, superior service, network effects); Murphy's "moat".

### 1.9 Where to play and how to win (Roger Martin and A.G. Lafley)

- Sources: Userpilot (Abrar Abutouq, 2026; vendor) and Ant Murphy (2025). Both cite Roger Martin; Userpilot credits *Playing to Win* to Martin alone. General knowledge: *Playing to Win* (2013) is by A.G. Lafley and Roger L. Martin.
- **Where to play**: segments, use cases, channels and geographies in scope, and critically which to exclude. Anchored in the company mission, long-term business goals and the target customers the product is optimized for; validated by market analysis.
- **How to win**: the specific capabilities, data advantages or experience qualities competitors can't copy quickly.
- Userpilot: a strategy that tries to serve every segment with every feature "has deferred a bet". Cites Pragmatic Institute's 2025 State of Product Management: prioritization "often turns into negotiation, shaped by executive opinion".

### 1.10 Strategy as insight plus conviction (John Cutler, via Userpilot)

- Userpilot quotes John Cutler: strategy equals insights raised to the level of conviction. Userpilot says analytics now supply most insight; conviction (committing to an uncomfortable no and defending it) is where "strategy theater" collapses.

### 1.11 Three meanings of "strategic product manager" (Userpilot)

- Upstream (shaping bets before building); a senior IC with wider scope; a bridge between company strategy and product direction. Also: "strategy decides the 'why' and the 'what.' Execution decides the 'how.'" Cites Perri's build trap (measuring outputs rather than outcomes stops strategic work). Warns about leadership deciding an opportunity first and asking the PM to validate it, turning discovery into confirmation.

### 1.12 The anonymous three-year strategy process

- Source: a practitioner post (author and site not shown in the paste) describing a 3-year product vision and strategy written in under 2 months after joining a company.
- Steps: (1) research context: global trends, industry, founders' and old-timers' insight, customer conversations; (2) hypotheses about the biggest pain points for target personas, tested with stakeholders and experts; (3) agree the biggest problem worth solving that fits the company's strengths, and describe the solved future state, which becomes the vision statement; (4) agree a North Star metric measurable daily (example: CO2 saved per customer per month); (5) 3 to 5 levers (sub-problems) that move the North Star; (6) connect each lever's input metric to the North Star. Solving the sub-problems is the strategy; split them across teams or years.
- Daily use: compare options by strategic impact; aims for 70% of time on strategic work (possible because the company is young).

### 1.13 Hemnet's four principles

- Source: a Hemnet product leader (name not shown; writes about Hemnet's three-year product strategy), Product in Practice blog, "Jan 12" (year not shown).
- Purpose: describe "the good we want to bring into our customers' lives"; strategy describes outcomes and behaviours, never features.
- Principles:
  1. **Timeframe**: it must hold for at least a year. If you change direction every couple of months (for example, chasing an investment round), you're not ready for strategy; focus on purpose, problem size, uniqueness and your riskiest assumption. Optimal: three years, broken down yearly, checked quarterly through OKRs.
  2. **Make it explicit**: no vague words, superlatives or taglines; say exactly what behaviour you want to drive, not how to get there (that's discovery).
  3. **Not a one-person show**: defining it is the CPO's most important responsibility, but co-created with teams; hold the vision, be flexible on wording and measures; anchor it in every sprint planning.
  4. **Directions, not constraints**: make clear how it connects to OKRs; it holds "our best bets at that specific time", not a law; outcomes change when evidence arrives, which is learning, not failure.

### 1.14 Strategy by company stage (Stanford Online)

- Source: Stanford Online, summary of the webinar "Tailoring Your Product Strategy" by Donna Novitsky and Laura Marino (date not shown). Course provider.
- **Early-stage (product-market fit)**: focused vision and MVP; customer discovery (interviews, surveys, user testing); develop product and market together; avoid big-company processes and long roadmaps. Action plan: at least 30 prospect interviews over three months. Tip: build trust with early adopters.
- **Growth-stage (scaling)**: embed knowledge in processes; shift from founder selling to brand; revisit technical debt; balance key customers' demands with the market (customer councils). Tip: rein in powerful early customers.
- **Mature (optimization)**: align product strategy with corporate vision and competitive advantage; incremental innovation; use established resources (data, partners, capital, acquisitions); separate teams for new products. Action plan: quarterly reviews. Tip: avoid complacency.

### 1.15 Company strategy and product strategy (Product Management Journal)

- Source: "What is product strategy and why is it important?", an unnamed Product Management Journal (publisher not shown; sells product management training).
- A strategy typically includes: analysis of the current situation, a hypothesis about what will happen, goals, options, the decision, and a plan.
- Common confusions: an objective presented as a strategy ("move into the cloud" doesn't say how); the roadmap presented as the strategy (it covers development, not financial or marketing plans); strategy vs tactics ("head" vs "hands"); company vs product strategy.
- Single-product startups: company strategy is the product strategy. Multi-product: each product has its own; company strategy sets direction and allocates resources; product strategy brings it to life.
- Missing or vague company strategy: don't prioritize by loudest customer or biggest money; write a product strategy for senior management whose assumptions about company strategy force decisions.
- Inputs: customers, sales, competitive and market analysis. Constraints: company strategy, other strategies (regions, channels), capacity and capability. Output: a document or presentation that can be challenged, and plans (marketing mix, financial forecast, launch plans for a new product). Strategy drives the product plan.
- Review: not too often; a quarterly or six-monthly review. In practice strategy work is often kicked off by annual planning and is "an internal sales pitch" for resources.

### 1.16 Saying no: twelve arguments for adding a feature (Intercom)

- Source: Des Traynor, "Product strategy means saying no", Intercom blog, 2013-07-03.
- Arguments that sneak features in, and the answer: the data looks good (selective analysis; does it fit the product?); it'll only take a few minutes (scope is never a reason; "there are no small changes"); this customer is about to quit ("feature blackmail"; leads to consulting-ware); we can make it optional ("death by preferences"); my cousin's neighbour said (anecdote); we've nothing else planned (pay down debt instead); we're allowed to work on whatever we want; 713,000 people want it (raw numbers); competitors have it; if we don't someone else will (you're afraid to "draw the line"; cinema-plus-restaurant-plus-cab example); the boss wants it; this could be "the one" (appeal to the unknown).
- Real product decisions are saying no to good ideas.

### 1.17 Strategy "types" lists (they don't agree)

- **Ansoff-style growth directions**: market penetration, market development, product development, diversification (Hanover Research; Atlassian, which adds "cost competition" and "quality differentiation" to make six; IBM's three ways to grow through product development: new offering, tweak existing, take existing to new markets).
- **Five Porter-style types**: cost, quality, service, differentiation, focus (Shopify; nvecta, 2021-04-30; Notion, 2026-01-17). airfocus has its own five: target-customer focused, exceptional service, quality-led, low-cost, feature differentiation. These say most companies mix types; airfocus says start with one for a new product.
- **Ten types** ("10 Product Strategy Examples", Content Team, updated 2026-08-17; publisher appears to sell Atlassian Marketplace apps): differentiation (Snap), quality (Jira Service Management vs ServiceNow, unsourced), cost (SpaceX reusable rockets), focus (Tesla starting high-end), pioneer (Apple Vision Pro), niche (their own Marketplace apps), challenger (challenger banks), equivalence (converging smartphones), requests-based (MVP stage), upselling (Jira standard to premium).
- **Urban and Hauser's nine** (via Railsware, which credits Glen L. Urban and John R. Hauser, 1980): proactive = invest in market research, R&D, in-house entrepreneurship (Google's 20% time producing Gmail and AdSense), alliances (Uber and Spotify, 2014), acquisitions (Facebook and Instagram, 2012); reactive = respond to customer requests, defend against competition, copy competitors, second but better. Railsware spells Hauser as "Houser".
- **Productboard's product development types**: incremental, breakthrough, platform development, open innovation, diversification.
- **Dragonboat's framework table**: JTBD (low adoption, unclear differentiation, churn), Value Proposition Canvas (competitive market, messaging), design thinking (early stage, UX-heavy), agile (fast-moving industries), GEM (growth, efficiency, margin; established portfolios), "DHM (Differentiation, Hub, Modularity)" for platforms (wrong, see 5), Three Horizons (multiple lines at different maturity), GLEe (continuous learning). General knowledge: GEM and GLEe are also Gibson Biddle's models; GLEe stands for Get big on a niche, Lead the category, Expand the category.
- Inference: these are positioning and growth categories, not strategies. Several entries (requests-based, copy competitors, equivalence) contradict the saying-no sources.

### 1.18 Gibson Biddle's DHM (only secondhand)

- Mentioned by Dragonboat (with a wrong expansion) and in Hustle Badger's further reading (Biddle, "How to define a Product Strategy"). General knowledge: Biddle (ex-Netflix) asks how the product will delight customers in hard-to-copy, margin-enhancing ways: Delight, Hard to copy, Margin-enhancing.

### 1.19 Triggers to rethink a strategy

- Hanover Research (vendor): declining sales; falling satisfaction and renewals; a shift in customer needs; new technology (e.g. AI); competitors taking your customers; new entrants; a saturated market; an adjacent market showing interest.
- airfocus: market conditions change, competition heats up, customer demand changes, or the strategy isn't moving you toward the vision (example: a cost strategy when input costs rise until you lose money).
- Product Management Journal: the market moved, a competitor responded, or you learned something new about customers.
- Pichler: bigger roadmap changes (e.g. an unrealistic business goal) can force a strategy change.
- ProductPlan: users no longer match the personas, or new markets find value.
- Hanover's five questions to pick a direction: how products support company goals; whether current products can be improved or expanded; how best to address gaps; where demand is; whether enhancements will stay profitable.

### 1.20 Vendor component lists (what the templates put in a strategy)

- Atlassian (2 pieces): market vision, product goals (SMART), initiatives. Steps: define vision, understand market, craft value proposition, create initiatives, monitor and adapt.
- Asana: vision and business goals, personas and target audience, competitive positioning, value proposition, goals and success metrics, roadmap, plus marketing strategy and launch plan. Three illustrative examples: a differentiation strategy (real-time collaboration for remote teams), market expansion upmarket (permissions, audit logs, executive dashboards), customer-led growth (time to first value, activation).
- Aha! (support article): vision, business model (SWOT, Lean Canvas, Aha! business model canvas, with AI drafting), positioning, personas, competitor profiles, goals with a success metric and time frame (list for the next 6 to 12 months; example "Grow revenue for Fredwin Cycling, +35%, 2020 Q2"), initiatives (e.g. expand integrations, partner portal, refresh mobile app), strategy roadmap and presentations. Motto "goal first" (The Responsive Method).
- airfocus (Quadri Oshibotu guide): vision as "element 0", then goals and initiatives. Three goal types: business (revenue +30%), market (leading solution), customer (churn -20%). Goal frameworks: SMART, OKRs, 4 Disciplines of Execution (wildly important goals, lead measures, scoreboard, cadence of accountability). Signs of unreachable goals: budget, people or resources too small, time too short, scale similar to past failures. Initiatives: medium-to-high effort, cross-functional (localization, UI revamp, faster payments); goals come first. A 7-step framework that includes go-to-market (segments, pricing, channels) and regular reviews. A product strategy document comes before the PRD and holds customer needs, product and company assessment, competitive analysis, market analysis, goals, go-to-market and reviews; there's no standard template. Vision template in the "For... who needs... unlike..." form.
- ProdPad (Janna Bastow, 2025-07-17): principles: customer-focused, goal-oriented and measurable, flexible, well communicated, current. Components: vision and mission, ICP and buyer personas, competitive positioning, value proposition, North Star metric and OKRs, roadmap as prototype (Now-Next-Later, which Bastow says she invented), objectives to initiatives to experiments. Seven invented examples (see 5).
- Notion (Alyssa Zacharias, updated 2026-01-17): vision, goals, initiatives; six steps (know the market, define vision, set SMART goals, choose the team, determine initiatives, share the document). Suggests drafting the vision with AI.
- Shopify: vision, roadmap, target audience, market and competitive analysis. Eight steps: target audience, problem, vision, current state and target condition (Perri's terms), design principles, roadmap, success metrics, execute and iterate. A strategy should include goals, vision, research, personas, competitive analysis, roadmap, risks, resources, production plans and metrics. Review at least quarterly.
- Dragonboat (2025-03-31): customer and market insights, value proposition, competitive positioning, revenue and business model, prioritization framework, scalability. Tables: vision is why and long-term; strategy is how and adaptable; roadmap is features, schedules and milestones.
- nvecta (Afreen Sheikh, 2021-04-30): market vision (including a go-to-market plan), product goals (time-based), product initiatives. Strategy shows what you won't do, "explicitly, or by omission". Tips: sell a solution to human needs (Coca-Cola, Apple, IKEA); adapt to change; self-disrupt (cites Christensen's *The Innovator's Dilemma*; iPhone and iPod, iPad and Mac, Kindle).
- "10 examples" piece: components (vision and mission, goals, initiatives, KPIs and metrics); steps include risks (market, technical, business) and scalability.
- Salem E. (Walmart product leader, 2020-09-23): structure (target segment with an eye on addressable opportunity, the problem focusing on ONE big problem, market analysis, vision and USP) and methodology (problem scope including what's out of scope, success metrics, dependencies and risks, communicate targets prioritized by impact, value and revenue, tweak systematically). Positioning template: FOR [user] HAS [problem] wants [goal]; [product] with [benefits]; UNLIKE [competitor]. Puts features, journey and UX in the strategy document.

### 1.21 Tech-company practices (Phenomenon Studio)

- Source: Oleksandr Kostiuchenko, Phenomenon Studio (design agency), 2026-09-21.
- Five practices: 15 to 20 user interviews before writing any strategy; define technical defensibility (data network effects, integration depth, API ecosystem), not only commercial differentiation; check the strategy fits engineering capacity; define the activation event that predicts retention and validate it before scaling acquisition ("leaking bucket"); a process for turning strategy into a quarterly roadmap and judging feature requests against it.
- Mistakes: using TAM/SAM instead of user research; writing too abstractly to generate engineering requirements (test: would an architect get requirements from it? Example: "a weekly performance report from raw data in under five minutes without SQL" vs "the best analytics experience"); treating the strategy as done when written rather than when delivery and behaviour validate it.

### 1.22 ProductPlan's guide

- Source: ProductPlan, "The Ultimate Guide to Product Strategy" (vendor; date not shown).
- Competitive analysis should cover every alternative; not every feature-matrix checkbox matters (avoid the feature factory). PMs should take part in pricing because they know COGS and value.
- Two phases: initial strategy changes fast until product-market fit; after traction it shifts less.
- Inherited strategies: don't scrap them; unpack their history and revisit their assumptions.
- Avoid stale strategy: revisit monthly or quarterly starting from the assumptions; small corrections beat rare large changes; revisit personas.

### 1.23 Spotify's Buket Baran via Product School

- Source: Product School, 2023-08-11, based on a talk by Buket Baran (Spotify senior PM). Course seller.
- Why strategy: gives the vision a voice, focus, the ability to say no, alignment. Steps: research and data, plan (align with company goals, North Star metric, group challenges into strategic pillars), spread the word. Tips: zoom in on pain points cross-referenced with business goals; clarity (Amazon PR/FAQ style); flexibility, including deciding in advance which parts are "set in stone" and "who holds the reins for potential pivots"; communicate and iterate; Kano "delighters"; make pillars measurable.

### 1.24 Off-topic models worth a line

- IBM: seven stages of product development (idea, research, planning, prototype, sourcing and manufacturing, costing, commercialization); three kinds of value to measure (customer, business, product); a core-competencies matrix plotting strategic importance against current strength (credited to McKinsey).
- Product School, "11 Product Management Best Practices" (Carlos Gonzalez de Villaumbrosia, 2025-09-23): includes "delete a feature every quarter (or a year)" and connecting vision to business strategy (revenue, competitors, risks, channels).
- Railsware's BRIDGeS framework (their own discovery method, derived from Pivotal Labs' Inception).

## 2. Definitions and vocabulary

- **Product strategy**, as defined:
  - The approach chosen to realise the vision, as guardrails for discovery and delivery (Pichler).
  - A system of achievable goals and visions that align the team (Perri).
  - What your teams will focus on and why (Hustle Badger).
  - Deciding what we want to do and how best to do it (Product Management Journal).
  - A high-level plan defining vision, goals and initiatives (Atlassian, airfocus, Notion).
  - "Insights raised to the level of conviction" (Cutler via Userpilot).
  - Choices, including what not to do (Murphy; Traynor; Userpilot).
- **Vision**: long-term, stable, qualitative, inspiring (Pichler 5 to 10 years; Hustle Badger 3 to 5 years; Railsware "fixed and rarely deviate"). Not measurable (Pichler). Dragonboat: the "why"; strategy the "how".
- **Mission vs vision**: Hustle Badger: mission is why the work matters; vision is the future we build. airfocus: vision is the what (future state), mission is why it exists (LinkedIn example). The "10 examples" piece: mission says how the product achieves the vision. So "mission" means opposite things in different sources.
- **Challenge / objective**: Perri: the first business goal toward the vision. Hustle Badger: the challenge the strategy responds to, with a measure. General knowledge: close to Rumelt's "diagnosis".
- **Strategic pillars / focus areas / levers**: 2 to 4 themes (Hustle Badger); pillars from grouped challenges (Baran); 3 to 5 levers (anonymous practitioner).
- **Initiatives**: large cross-functional efforts toward goals (airfocus, Aha!, Atlassian). Notion and nvecta use "initiatives" for broad aspirations instead ("improve users' lives", "big-picture trends"), which is the opposite usage.
- **Roadmap**: downstream of strategy in every source. Atlassian says a strategy "serves as a roadmap"; airfocus has a "product strategy roadmap".
- **Strategy vs plan**: Perri: a list of features with dates is a plan, not a strategy. Product Management Journal: strategy drives the product plan.
- **Strategy vs tactics**: head vs hands (Product Management Journal); why and what vs how (Userpilot).
- **Product strategy vs go-to-market**: the "10 examples" piece: product strategy is the long-term plan (vision, market, positioning, value proposition); GTM is the shorter-term launch plan (sales, marketing, distribution). airfocus, Asana and nvecta fold GTM into the strategy document.
- **Product strategy vs product development strategy**: Productboard, IBM and Railsware use "product development strategy" for how products get built and launched; Railsware also uses it for vision-level strategy. Inference: different subjects that share a name.
- **KPI**: several sources use KPIs. The wiki says "metric" and "target" instead.

## 3. Practices most sources agree on

1. Strategy is choices and focus: say no, exclude segments and work (Murphy, Traynor, Hustle Badger, Userpilot, Pichler, Baran, nvecta, Salem E., Railsware, ProdPad).
2. Start from customer needs and evidence, not features or market size (Pichler, Hustle Badger, Phenomenon, Stanford, Userpilot, Hemnet, Atlassian, Shopify).
3. Name a differentiator or advantage that competitors can't easily copy (Pichler, Hustle Badger, Phenomenon, Userpilot, Murphy, Asana, ProdPad).
4. Tie the strategy to business goals or company strategy (Pichler, Perri, Product Management Journal, Stanford, airfocus, Murphy).
5. The roadmap comes after the strategy and implements it (nearly all).
6. Review regularly, at least quarterly in most sources (Pichler, Shopify, ProductPlan, Stanford, Product Management Journal, Hemnet via OKRs), and start reviews from the assumptions (ProductPlan, Pichler).
7. Treat a new strategy as a hypothesis to validate (Pichler, Phenomenon, Hustle Badger, Murphy, Hemnet).
8. Co-create and communicate it widely; it must guide everyday decisions (Hemnet, Hustle Badger, Pichler, ProdPad, Baran, airfocus, Notion).
9. Be explicit; avoid fluff and taglines (Hemnet, Baran, airfocus "remove any fluff", Phenomenon).
10. Adapt to the product's stage (Stanford, Pichler, ProductPlan, Dragonboat, "10 examples").

## 4. Conflicts between sources

1. **Measurable goals inside the strategy or not.** Inside and measured: Perri, Hustle Badger, ProdPad, Atlassian, Aha!, airfocus, Notion. Inside but unmeasured: Pichler. Separate: Murphy (choices link to higher goals).
2. **Fixed or living.** Railsware: vision and strategy are fixed and rarely deviate. airfocus, ProdPad, Notion, Dragonboat: never set in stone. Pichler: continuous strategizing. Baran: decide which parts are fixed and who can change them.
3. **Horizon.** Pichler 12 to 24 months; Hemnet at least 12 months, ideally 3 years; anonymous practitioner 3 years; ProductPlan implies it changes often before product-market fit.
4. **Review cadence.** Monthly or quarterly (ProductPlan); at least quarterly (Pichler, Shopify); quarterly or six-monthly (Product Management Journal); metrics twice weekly and performance monthly (Salem E., which is closer to goal tracking).
5. **Ownership.** PM and extended team (Pichler); CPO, co-created (Hemnet); split by level (Perri); product and design leadership own the vision (Hustle Badger); executives set goals first (airfocus).
6. **Features in the strategy.** 3 to 5 standout features (Pichler); features, journey and UX in the document (Salem E.); never features (Hemnet, Perri); a feature list is a plan (Perri, Product Management Journal).
7. **Go-to-market and roadmap inside the strategy document.** Yes: airfocus, Asana, nvecta, Shopify. No: the "10 examples" piece, Pichler, Dragonboat.
8. **Business strategy first?** airfocus: business strategy must be defined first. Product Management Journal: if it's missing, write the product strategy and force the discussion. Pichler: product strategy guided by business and portfolio strategy.
9. **TAM.** Phenomenon: user research first, market size only to check scale later. Salem E.: an early eye on addressable opportunity. Atlassian's planning guide: market sizing as part of research.
10. **Strategy types.** The lists (1.17) disagree on number and names, and some entries (requests-based, copy competitors) contradict the saying-no sources.
11. **Mission vs vision** (section 2).
12. **Customer requests.** The "10 examples" piece and Railsware's reactive strategies treat responding to requests as a strategy. Traynor, Stanford ("rein in powerful early customers") and Railsware itself ("neglect some feedback") warn against it.

## 5. Examples and numbers, with flags

- Perri's Uber example: hypothetical by her own label; date inconsistency (2017 vs 2018).
- Pichler: iPhone, Chrome and healthy-eating app examples, illustrative.
- ProdPad's seven examples (B2B analytics, personal finance, wellness coaching, fintech compliance, freelancer marketplace, eco e-commerce, sports wearable): invented, not real companies. Several "OKRs" are outputs: "Launch integrations with top banks", "Roll out new modules", "Launch regulatory alert integrations for 3 new regions", "Launch 50 new verified brands", "Deploy to 10 new NCAA programs".
- Asana's three examples: illustrative, no company named.
- Netflix (Railsware): vision "best global entertainment distribution service"; strategy: original content, personalization, watching experience, interactive storytelling. Unsourced.
- Railsware's own products (Mailtrap, Smart Checklist for Jira, Coupler.io): real but self-described by the vendor.
- "10 examples" claims: ServiceNow losing share to Jira Service Management (unsourced, from a vendor of Atlassian apps); SpaceX cost leadership; Tesla starting high-end.
- Hustle Badger metric examples ($100m to $120m; retention 20% to 25%; returns 22% to 18%): illustrative.
- Stanford: at least 30 interviews over three months (advice, not data).
- Phenomenon: 15 to 20 interviews; 40 to 60% activation before scaling acquisition (unsourced); "since 2019" claim about lasting differentiation (unsourced); cites Nielsen Norman Group research vaguely.
- Anonymous practitioner: 70% of time on strategic work (personal target).
- Unsupported statistics, not to be repeated as fact:
  - nvecta: "70% of companies refer to the product strategy whenever they need to make major decisions" (no source).
  - Hanover: 40% of launches fail (credited to McKinsey); almost $100,000 average spent creating a product; research gives "15x ROI" and saves 1.5 months; "21% of products are found not viable at the pricing analysis stage"; 2/3, 74%, 83% figures from its own report (vendor research).
  - Product School: "roughly 75% of companies aren't fully adopting modern product management practices" from "one survey of 5,000 product managers" (not named).
  - IBM: "as many as half of all companies, and 70% of top-performing companies" use internally developed software (IBM's own institute).
  - Notion: BetterCloud's "average of 106 SaaS tools" (vendor report, off topic); a Heliyon study saying lack of customer focus is a main reason products fail (academic, not checked).
  - Userpilot: Pragmatic Institute 2025 report quote (vendor report).
- Factual errors (from general knowledge):
  - Railsware lists Slack among Microsoft acquisitions; Salesforce acquired Slack.
  - Dragonboat expands DHM as "Differentiation, Hub, Modularity"; Biddle's DHM is Delight, Hard-to-copy, Margin-enhancing.
  - Userpilot credits *Playing to Win* to Martin alone; it's Lafley and Martin.
  - airfocus spells Perri "Perry"; Railsware spells Hauser "Houser".
  - Airfocus says LinkedIn's vision and mission are as quoted; not checked.

## 6. Sources

Substantive (worth citing for ideas):

| Author | Publisher | Kind | Date | Notes |
| --- | --- | --- | --- | --- |
| Melissa Perri | Medium | practitioner | 2016-07-18 | Strategy canvas; Product Kata |
| Roman Pichler | romanpichler.com | practitioner (sells training) | 2015-05-19, updated 2026-01-29 | Elements; Vision Board; life cycle |
| Roman Pichler | Medium | practitioner | 2026-05-12 | Framework; Strategy Stack; OKRs; ownership |
| Ant Murphy | LinkedIn | practitioner (sells template) | 2025-10-21 | Four steps; choices; pasted twice |
| Ed Biden | Hustle Badger | course seller | updated 2026-05-15 | Strategy stack; 7 steps; 7 Powers |
| Not shown (Hemnet product leader) | Product in Practice | practitioner | "Jan 12", year not shown | Four principles; horizon |
| Des Traynor | Intercom | practitioner (vendor blog) | 2013-07-03 | Saying no |
| Not shown | Product Management Journal | training provider | not shown | Company vs product strategy |
| Not shown | unknown practitioner post | practitioner | not shown | 3-year strategy process |
| Buket Baran via Product School | Product School | course seller | 2023-08-11 | Pillars; what's set in stone |
| Donna Novitsky, Laura Marino | Stanford Online | course provider | not shown | Strategy by stage |
| Oleksandr Kostiuchenko | Phenomenon Studio | agency | 2026-09-21 | Tech defensibility; TAM warning |
| Abrar Abutouq | Userpilot | vendor | 2026 | Where to play/how to win; Cutler |

Vendor templates and guides (sources, not fact): Atlassian, "Product strategy" (not shown); Asana, "Product strategy template"; Aha!, "Best practices for setting product strategy" (support article); ProductPlan, "The Ultimate Guide to Product Strategy"; Janna Bastow, ProdPad, "7 Product Strategy Examples" (2025-07-17); Quadri Oshibotu, airfocus, "The Ultimate Guide to Product Strategy"; Dragonboat Crew, "Product Strategy: Driving Outcomes Through Strategic Alignment" (2025-03-31); Shopify, "What Is a Product Strategy?"; Alyssa Zacharias, Notion, "How to create a product strategy in 6 steps" (updated 2026-01-17); Afreen Sheikh, nvecta (2021-04-30); Content Team, "10 Product Strategy Examples You Need To Know" (updated 2026-08-17); Salem E. (LinkedIn, 2020-09-23; Walmart product leader, practitioner); Hanover Research, "Everything You Need to Know About Product Development".

Off topic (product development, planning or general PM; left out except for a line in 1.24): IBM, "How to build a successful product development strategy"; Productboard Editorial, "Product Development Strategy: Tips and Best Practices" (2023-11-12); Sergiy Korolov, Railsware, "Product Development Strategy Explained" (2025-09-12); Atlassian, "The complete guide to product planning"; Carlos Gonzalez de Villaumbrosia, Product School, "11 Product Management Best Practices No One Talks About" (2025-09-23).

Not in the batch, only mentioned: Richard Rumelt (no mention at all; the "challenge" idea appears through Perri and Hustle Badger); Lafley and Martin (via Userpilot and Murphy); Hamilton Helmer (via Hustle Badger); Gibson Biddle (via Dragonboat and Hustle Badger's reading list); Marty Cagan (SVPG link in Hustle Badger's reading list); Deb Liu and Reforge (reading list only).
