<!-- Research digest. Written on 2026-11-24 by Claude from research the user pasted into the project, at the user's request, so the knowledge is kept without the original pages. Not a copy of any article. -->

# Pricing: what the research taught

Summary of Juan's pricing research batch 1 (pasted 2026-11-23, about 40 articles), plus three sources from my own web research the same day, marked "(my research)". Written 2026-11-24 for turning into playbook pages. Everything below is paraphrase unless quoted. Each claim names the article it comes from (full details in section 6). "Vendor" means the publisher sells a tool, research service, consulting or course on the topic, so its claims are marketing until checked. Where I add something from model memory it is marked "General knowledge:"; my own reasoning is marked "Inference:".

Left out: the AI search summary at the top of the paste (not a source), product and course pitches, salary content (none appeared), and one off-topic Forbes Council piece on AI search (Tyler Jordan, 2026-11-23).

Decision already taken for product-copilot (Juan, 2026-11-23): no new page type for pricing. Plans and prices live as a table in the overview; a price change is a decision page that names who decided.

## 1. Frameworks, models, methods and lists

### 1.1 The three foundations: cost, competition, value

Nearly every source starts from the same three anchors, sometimes drawn as a floor and a ceiling.

- **Floor and ceiling.** Cost sets the floor (below it you lose money long term); what the customer values sets the ceiling; competitors' prices sit between and shape what customers see as fair. Sources: BDC quoting Eric Dolansky (Brock University); Product Management Journal "Pricing – how to price" (Fig. 1: costs, willingness to pay, competition); Qualtrics; HBS Online Value Stick (1.5).
- **Three main strategies** named as cost-based, competition-based and value-based: Qualtrics ("three major types that dominate the market"), LogRocket (Dhiman), "Pricing Strategy for Product Managers" (unnamed PM guide), Dovetail, ProdPad, BDC.
- **A different "three"**: the Product Management Journal names three *basic* strategies as market skimming (high vs competitors, to maximize profit), market penetration (low, to maximize share) and competitor matching (similar, to maximize retention). It puts value-based on top as "the ultimate pricing strategy". So "three main strategies" means two different lists depending on the source.

### 1.2 Cost-plus (markup, cost-based) pricing

- What it is: add a markup to the unit cost. Named by nearly every source.
- Formula: price = unit cost × (1 + markup %).
- Worked examples (all illustrative, none sourced to real firms):
  - Melio: $55 cost × 1.5 = $82.50.
  - Salesforce (vendor blog): $35 boomerang cost + 300% = $140.
  - Shopify (vendor): $45 t-shirt × 1.35 = $60.75.
  - PMA (Bryony Pearce): trainers $60 + 30% = $78.
  - "Pricing Strategy for Product Managers": $10 make + $3 pack + $12 ship = $25, + 50% markup = $37.50.
  - Esade: sale price = cost + % profit.
- Margin-based variant: price = variable cost ÷ (1 − target margin), e.g. a 20% margin (CO—, US Chamber of Commerce).
- **Markup vs margin (two sources get it wrong):** markup is profit ÷ cost; margin is profit ÷ price. Shopify calls a 35% markup a "35% profit margin"; the real margin is 25.9%. Aha! calls $10 → $15 a "50 percent margin"; it's a 50% markup and a 33% margin. Qualtrics defines the terms correctly (COGS, gross margin, operating, EBITDA and net margin, markup).
- Variant: standard markup at each step of a distribution chain (Nationwide).
- "Open-book" cost-plus: the supplier shows costs and a fixed margin is agreed with the customer; rare, seen in professional services and government contracts (Product Management Journal).
- When to use: physical goods, commodities, grocery and department stores, small firms without research budget (Unleashed, Gupta's table, Melio). Unleashed warns about hidden costs (labour, overheads) eating margin.
- Pros: simple, easy to justify to customers (Unleashed, Melio, PMA).
- Cons: ignores demand and competitors; if your cost falls, your price and revenue fall too (Melio); company-centric, removes the incentive to control cost, and pushes sales to discount (PMA); cost changes squeeze margins later (LogRocket).
- Standing: Melio and the HubSpot data cited by Nationwide call it the most common strategy. Gupta: "generally not recommended for software PMs" and "fundamentally broken for software", because marginal cost is near zero.

### 1.3 Competition-based (competitive, market-based) pricing

- What it is: set price relative to rivals' prices for similar products. Also called competitor-based (Qualtrics), competitive positioning, price indexing.
- Three positions: below, match, above (Melio, Salesforce; ProdPad calls them lowest cost, price match, premium). Revology (vendor) lists premium, price matching and loss leader.
- Dolansky (BDC) and Deland (Forbes Council) name three stances:
  - **Co-operative**: match competitors.
  - **Aggressive**: stay below them and cut further when they cut.
  - **Dismissive**: a market leader that ignores competitors' prices.
- When to use: saturated markets with mass goods (gum, big-box beer, household products) (Unleashed); mature, slow-growth markets where any move is matched (Product Management Journal says matching gives "a more stable market for everyone"); second-tier players aligning with a leader (same).
- Examples: gas stations (several); Samsung pricing slightly under Apple (Qualtrics); meditation app $9.99 vs a newcomer at $7.99 ("Pricing Strategy for Product Managers"); Peep Laja matching a competitor's $195.
- How: track competitors constantly, including price history (Unleashed, Qualtrics, Gupta). Gupta reads history as a signal: steady increases (his example: Salesforce) suggest inelastic demand and room for a premium entrant; frequent discounts signal a commoditized market. Tools named: Prisync, Dataweave (Gupta).
- Risks: price wars and margin erosion (several); customers see you as the same as rivals (LogRocket).
- Product Management Journal advice when your audit finds no real differentiator: a market leader may justify a small premium over the average; a non-leader a small discount; a seriously weaker product may need penetration pricing, or better, delay and rework the proposition.

### 1.4 Value-based (customer-based, price-to-value) pricing

- What it is: price on the value the customer gets or perceives, not on your cost. Named by every source.
- Dolansky's steps (BDC):
  1. Pick a product the customer would compare yours with, and its price.
  2. List how yours differs.
  3. Put a money value on each difference: add the positives, subtract the negatives.
  4. Check the resulting value is above your cost.
  5. Explain the price to customers.
- PMA example in the same shape (economic value to the customer): next best alternative shoe $50 + insole $10 + $15 for the built-in feature = $75. Price can differ by segment.
- ROI examples:
  - Gupta: a CRM feature saves 10 hours per rep per month at a fully loaded $75 an hour = $750 value; price $50/rep/month is an easy yes. Build an ROI calculator and put it in sales and marketing material.
  - Product Management Journal: saves 10 hours a month at £10 an hour = £1,200 a year, the "Objective Price". Perceived value then moves it: opportunity value and brand push it up; migration and setup costs, uncertainty and inertia push it down (hence promotions and free trials).
  - Stripe (vendor): software that saves $100k can charge $10k.
- Investopedia splits **good-value pricing** (right mix of quality and price) from **value-added pricing** (charge more for added features). It also lists misconceptions: value-based doesn't guarantee success; customers don't value every feature; brand value is hard to price.
- Melio's three checks: what the market will pay, the benefit to the buyer, and competitor prices. Example: Starbucks.
- When to use: B2B SaaS with clear ROI (Gupta: "the gold standard for most modern B2B SaaS"); subscriptions (LogRocket); bespoke goods, expert services, craft and premium products (Unleashed); pharma using patient savings or time gained (Unleashed).
- Standing: called the default or best for SaaS and B2B by Gupta, Salunke, Paddle ("winner hands down", vendor), Product School ("most B2B software companies"), ProdPad ("where most product-led SaaS land"), Qualtrics ("often the go-to choice" because it "tends to maximize profits").
- Cons: guesswork, needs research, harder to keep stable, time-consuming (Melio, Unleashed, PMA).

### 1.5 HBS Value Stick (Felix Oberholzer-Gee)

- Source: Tim Stobierski, HBS Online, 2022-11-10 (first published 2020-11-03). HBS Online sells the Business Strategy course.
- Four points on a vertical stick, top to bottom: **willingness to pay (WTP)**, **price**, **cost**, **willingness to sell (WTS)** (the lowest price suppliers will accept, also called willingness to accept).
- Three wedges: WTP − price = **customer delight**; price − cost = **firm margin**; cost − WTS = **supplier surplus**.
- Oberholzer-Gee's definition: "Value for customers is the difference between their appreciation of a product or a service and what they have to pay for it."
- Four ways to raise margin:
  1. Raise price (takes value from customers).
  2. Raise customers' WTP (makes the stick longer).
  3. Lower cost by paying suppliers less (takes value from suppliers).
  4. Lower suppliers' WTS (makes the stick longer).
- Point: 2 and 4 create value for everyone; 1 and 3 only move it around.

### 1.6 Penetration pricing

- What it is: enter low to win share fast, raise prices later. Named by most sources.
- When to use: crowded markets, network-effect and PLG products (Gupta), high expected demand that rivals can copy easily (LogRocket), subscriptions with a free month or 50% off, ride-hailing (Unleashed).
- Examples: Comcast (Melio), game consoles (Dolansky), Slack freemium (Gupta), Virgin America's US entry in the early 2000s (Qualtrics), Spotify/Netflix and Android vs Apple (PMA; these look shaky as penetration examples).
- Requirements and risks: an "iron grip" on cost because profit usually comes only with scale; price buyers are "the most fickle" and leave for the next cheaper offer; the Japanese electronics firms of the 1980s were undercut by Korean and Chinese firms and had to move to quality and brand (Product Management Journal). Also: customers come to expect low prices, price wars, hard to raise later, early losses some startups can't survive (Melio, Unleashed, Qualtrics).
- Qualtrics: know how long you will run it and whether the early loss is sustainable.

### 1.7 Price skimming

- What it is: launch high for early adopters, then lower in steps to reach more price-sensitive buyers. The name comes from skimming cream (Qualtrics).
- When to use: innovative, anticipated products with no real rival, or a strong moat (Unleashed, Gupta); only product in market or highly differentiated with limited supply, using price to limit demand (Product Management Journal); patented, luxury and new products (LogRocket's "premium" row).
- Examples: iPhone (lowered when the next model nears, Qualtrics), PlayStation and other consoles, pharma, Salesforce's early CRM (Paddle).
- Timing: Gupta suggests lowering over 6–18 months; Qualtrics asks whether you can predict the schedule.
- Risks: copycats; early buyers feel cheated if price drops soon after launch; buyers learn to wait; works mainly for brands seen as innovative or exclusive (Unleashed, Qualtrics). Defense when rivals arrive: add lower-end versions (versioning) (Product Management Journal).
- Close cousin: Melio's "high-low pricing" (start high, discount), but discount-driven retail.
- **Misdefinition:** Indeed's employer content describes skimming as market-driven produce prices. Don't use.

### 1.8 Premium (prestige) and economy pricing

- **Premium**: deliberately charge more than rivals and trade on quality and brand. Brand and quality must be built and kept up; margins are higher (Qualtrics). Examples: McKinsey (Qualtrics), Starbucks vs Dunkin' (Shopify), Tesla (Qualtrics, under value-based). Sources: Stripe, Shopify, Product School, LogRocket.
- **Economy**: low cost so low price; works at scale; store own-brands; good in downturns, but bargain hunters switch easily and revenue needs volume (Unleashed). Examples: Walmart, Dollar Shave Club (Paddle, Shopify, Product School). Shopify notes competitive pricing isn't the same as economy pricing.
- Product Management Journal: pricing in a category tends toward the average as markets mature and decline.

### 1.9 Dynamic, surge and time-based pricing

- What it is: change price in real time with demand, time, stock, competitors or buyer (yield management in airlines and hotels). Examples: Uber surge, airlines, hotels, sports events, Amazon (Revology, Dovetail, Unleashed).
- Risks: buyer backlash when they learn others paid less (Unleashed); Wendy's backlash (Product School); fairness and legality, since price discrimination on protected traits is illegal (PMA); needs data and technology, so costly for small firms (Unleashed).
- Esade, citing Marco Bertini: transparency about how prices move builds trust.
- Paddle (vendor): not for SaaS subscriptions.
- Related but distinct: personalized pricing, by individual buyer (Revology); market pricing like gas, which follows supply and demand (Qualtrics, as a "model"); demand-based pricing (Esade).
- Scale claim: 25–30% of UK and EU retailers use dynamic pricing, FT Strategies via ProCFO (vendor, not checked).

### 1.10 Freemium and free trials

- What it is: a free basic tier, paid upgrades. Examples: Spotify, Canva, Dropbox storage (Qualtrics), Slack (Gupta).
- Pros: wide adoption and no-commitment trial (Qualtrics, LogRocket).
- Cons: cost of serving free users, low conversion without a must-have paid feature, churn (Qualtrics, others).
- Paddle (vendor): freemium is "an acquisition model, not a part of pricing"; the best companies wait 2–3 years before adding it; paid users converted from free show higher NPS and lower CAC.
- ProdPad: often paired with a reverse trial (start on the paid tier, drop to free).
- Conversion benchmarks (my research, Ada Chen Rekhi, compiled vendor figures 2006–2016): freemium 1–10%; trial without card up to about 25%; trial with card 30–50%. Old and compiled; treat as rough.

### 1.11 Tiered, good-better-best and price lining

- What it is: several packages at different price points and feature sets. Sources: Nationwide (citing Rafi Mohammed, HBR 2018), Product School (Netflix tiers), Shopify (basic/pro/enterprise), Gupta (free/pro/enterprise), Qualtrics, LogRocket, "Pricing Strategy for Product Managers" (Mailchimp).
- When to use: a wide range of customers with different needs (LogRocket).
- Anchoring use: lowest and highest tiers make the middle look like best value (Qualtrics).
- Cons: choice paralysis, harder forecasting (Qualtrics).
- Peep Laja's beer test (no study cited): with two beers ($2.50 premium, $1.80 bargain) about 80% picked $2.50. Adding a $1.60 beer moved about 80% to $1.80. Replacing it with a $3.40 beer moved most to $2.50 and about 10% to $3.40. Lesson: options steer choice, and three options make people choose between your plans instead of whether to buy.
- Paddle (vendor) says good-better-best is "dying out" in software. See conflicts.

### 1.12 Bundling, loss leaders and promotional pricing

- **Bundling**: one price for several items. Pros: perceived value, convenience, moves slow stock with a best-seller (Qualtrics). Examples: McDonald's Happy Meal, Microsoft Office, Disney+ bundle, Glossier Night Out Set at 15% off.
- **Loss leader**: sell one item at little or no margin to draw buyers to profitable ones. Examples: Gillette razors, printers, supermarket free samples near the deli (Qualtrics).
- **Predatory pricing**: the extreme form, pricing low to destroy rivals; illegal in many places; in the US often judged with the Areeda-Turner test (Qualtrics).
- **Promotional pricing**: temporary discounts for short-term cash, acquisition or loyalty (LogRocket); supermarkets run constant offers (Product Management Journal).
- **Multiple pricing**: buy-one-get-one (Nationwide). **Volume or bulk pricing**: e.g. 5% off at 500 units, 10% at 1,000 (Shopify); common in B2B and wholesale, risk of overstock (Qualtrics). **Loyalty pricing** (Shopify).
- Other structures (Product Management Journal): up-selling, cross-selling, segment pricing (students, over-60s), and price complexity, which mature telecoms use to make comparison hard.

### 1.13 Psychological pricing

- **Charm pricing (ending in 9)**: Peep Laja cites the book *Priceless* (William Poundstone): the same item at $34, $39 and $44 sold most at $39. Peep Laja: never charge $100, charge $99.95; above $100, go to $109.95. Paddle (vendor): 9s vs round numbers is inconclusive for tech.
- **Prestige rounding**: round prices signal quality (several retail sources).
- **Former price vs current price ("better than nine")**: showing a crossed-out former price beats a 9-ending (Peep Laja; Amazon as example). Shopify and others call it strikethrough savings.
- **Contrast principle and anchoring**: a $3,000 shoe makes the $800 shoe look reasonable; a $49 steak looks fine next to $100 dishes; watch shops stock $50,000 watches to sell $3,000 ones (Peep Laja).
- **Decoy pricing** (Dan Ariely, *Predictably Irrational*):
  - Paris with breakfast / Paris without breakfast / Rome with breakfast: most pick Paris with breakfast because it's easy to compare with the worse Paris option.
  - The Economist subscription: three options, 16 / 0 / 84 chose them; with the middle option removed, 68 / 32. See conflicts for which option cost what.
  - Peep Laja's three-package recipe: a cheaper decoy ($49, minimal features), the target ($59, lots of features), a contrast option ($159, a few extras only).
  - CO— example: digital $50 / print $90 / both $100.
- **Daily reframing (hyperbolic discounting)**: a per-day price was "five times more likely to be rated a great deal" (Phill Agnew via PMA; study not named).
- **Price as quality signal**: perfume priced $40 → $80, top ratings 33% → 78% (Agnew via PMA; unsourced). Qualtrics and Unleashed also say a too-low price can signal low quality; Unleashed adds that supermarkets may give shelf space to higher-priced rivals because they earn more margin.
- **Removing currency signs** (menus) (several retail sources).
- **Value before price**: never show a price before explaining the value (Peep Laja's $50 loaf of bread). "Pricing Strategy for Product Managers": use testimonials and case studies to justify price.

### 1.14 Other strategies that appear once or twice

- **Target costing**: start from the market price and work back to the allowed cost (PMA, citing CIMA).
- **Targeted-return pricing** (Aha!): price = unit cost + (target return × capital invested) ÷ units. Example: $10 + (0.30 × $500,000) ÷ 20,000 = $17.50.
- **Geographic or localized pricing**: Microsoft Office 365 (Olafioye); Netflix's cheaper India plans (Shopify). Paddle (vendor) claims showing the correct currency symbol lifts revenue per customer about 30%.
- **Marginal cost pricing** (Shopify). **Market-share pricing** (CO—). **Sustainability pricing** (Esade). **Discount pricing** (Shopify).
- **Pay what you want**: Radiohead's *In Rainbows* (2007); goodwill but unpredictable revenue (Qualtrics).
- **Sliding scale**: price varies with the customer's means, around a published standard price; used in healthcare (Qualtrics).
- **Services**: hourly, project and retainer pricing (unnamed services piece).
- **Kotler's price/quality matrix** (ProdPad; Aha! template): high price + high quality = premium; low + low = economy; high price + low quality = rip-off; low price + high quality = superb value.
- **Peep Laja's four strategies**: expensive, cheap, niche, optimum.
  - Niche rule of thumb: for a new kind of product, charge consumers 20–50% and businesses 30–100% more than the highest alternative; for an existing benefit done differently, charge the median.
  - Optimum: find the break-even floor. Example: $1,000 fixed + 500 units × $25 = $13,500 ÷ 500 = $27 minimum.
  - Peep Laja's general advice: better to charge more than less.
- **Life-cycle pricing** (Unleashed, Roughan):
  - Launch: penetration, skimming or competitive.
  - Growth/mid: dynamic, value-based or competitive; consider raising prices as demand grows.
  - Later (rivals catch up): competitive or cost-plus, or add extras instead of cutting price.
  - End of life: economy, discounts, bundles or extras to clear remaining demand.
  - Pharma: skimming or value-based for unique drugs, competitive or penetration for saturated ones (colds, heartburn).
- **Deal pricing**: in corporate sales it's "much more about deal pricing than product pricing"; PMs must make sure approval committees know product costs and margins (James Harvey-Samuel, Cable & Wireless, via Product Management Journal).

### 1.15 Pricing models (the mechanics customers see)

- **Strategy vs model** (see section 2): the strategy sets the level; the model is the format the customer pays in.
- Aha!'s six SaaS models: flat rate, per user (seat), usage-based (pay as you go), tiered, feature-based, freemium.
- Other models named:
  - **Subscription**: recurring fee; predictable revenue (Adobe Creative Cloud in "Pricing Strategy for Product Managers"; Stripe).
  - **Flat-rate subscription**: easy and predictable, but one size fits all and cost to serve varies by customer (Qualtrics; Spotify).
  - **Pay as you go / usage / consumption**: AWS (several).
  - **Per user**: fits when all users need the same features (LogRocket).
  - **Transaction-based** (Stripe). **Hybrid** (ProdPad, Poyar). **Outcome-based** (ProdPad).
  - **Per seat with AI as a premium tier** (ProdPad's AI options).
  - LogRocket's table of model, how, when: premium, penetration, dynamic, promotional, tiered, per-user, freemium (it mixes strategies and models).
  - Qualtrics's seven: freemium, flat-rate subscription, tiered subscription, pay what you want, bulk, market, sliding scale.
- **ProdPad's three questions for AI pricing**: what does it cost to serve? How predictable does the bill need to be for the buyer? Can the outcome be measured?
- **Market data (my research)**: Growth Unhinged / Kyle Poyar poll of 230 companies, 2026-05-13 (sponsored by Metronome, a billing vendor): hybrid pricing 37%, up from 25%; AI credits 29%; median AI gross margin target about 50%; 3 in 4 changed pricing in the last year.

### 1.16 Value metric

- What it is: the unit you charge by (seats, contacts, data, usage). Sources: Paddle (vendor, the most detailed), Xactly, Revology, Gupta, Agnew via PMA.
- Paddle: "get the value metric right and you'll do ok". List 5–10 candidate metrics and test them with customers. A good metric grows with the value the customer gets.
- Examples: HubSpot charges on contacts, not seats (Paddle); MailChimp on contacts, AWS on data (Agnew); Wistia, Zapier; Rolls-Royce charging per engine use (Paddle says per engine mile; General knowledge: the scheme is "Power by the Hour"), Husqvarna, a Barcelona theater charging per laugh, MainStreet taking a share of savings (Paddle).
- Paddle calls seats a "relic". Paddle claim (vendor, ProfitWell data, not checked): value-metric companies grow about 2x with half the churn and 2x expansion.
- Gupta lists a misaligned value metric among the top pricing mistakes.

### 1.17 Paddle's pricing order of work (vendor)

1. Segments and value metric.
2. Rough price level (order of magnitude), positioning, packaging.
3. Add-ons, exact price, localization, discounting, contract terms.
4. Freemium, new markets, vertical expansion, multi-product.

- Start with the range ($10 vs $100), not $500 vs $505.
- Build quantified buyer personas in a spreadsheet with WTP, LTV and CAC.

### 1.18 Willingness-to-pay research and testing methods

- **Van Westendorp price sensitivity meter**: four questions — at what price is it too cheap (doubt quality), a bargain, getting expensive, too expensive (Gupta). Gives an acceptable range.
- **Gabor-Granger**: ask whether people would buy at a series of prices to estimate a demand curve (Gupta; General knowledge for the mechanics).
- **Conjoint analysis (discrete choice)**: people pick between bundles of features and prices; shows how features shift price tolerance and lets you simulate changes. Qualtrics (it sells this) calls it "the gold standard" and calls Van Westendorp and Gabor-Granger "dated". Also Revology, CO—.
- **Sawtooth view (my research)**: Bryan Orme and Keith Chrzan, Quirk's 2022 (Sawtooth sells conjoint software): conjoint is best; they "cannot think of a good reason to recommend" Gabor-Granger; Van Westendorp only as a first step.
- **A/B tests on the pricing page**: Gupta calls them the "gold standard" (example: $29 vs $35). LogRocket: A/B test before launch.
- **Monadic tests** (each person sees one price), **cohort analysis by signup price** (Gupta: a cohort with 30% higher LTV, illustrative), **price-sensitivity surveys**, **localized rollout tests** (CO—), **focus groups** (Unleashed), **customer interviews** (LogRocket, "Pricing Strategy for Product Managers").
- Gupta gives a table of method, best for, complexity and key question.
- **Price elasticity**: % change in quantity ÷ % change in price (PMA). Milk is inelastic, Coca-Cola elastic (PMA).
  - Revology worked example (vendor, illustrative): 10,000 units at $20, cost $12, gross profit $80,000. At elasticity −1.5, a 5% rise sells 9,250 units for $83,250 profit (+4%). At −3.0, it sells 8,500 for $76,500 (−$3,500).
- **Revology's five steps to optimize price** (vendor): set the goal and limits; gather data (net prices, costs, competitor prices, promotions, ideally two years weekly); segment; measure elasticity; set prices and watch them. Its misconceptions: treating pricing as pure engineering, overcomplex models, assuming linear demand, black-box AI.

### 1.19 Gupta's five-step process for pricing a new product

Source: Aakash Gupta, 2025-11-30 (PM newsletter author; sells courses).

1. **Objective**: market share or profit? "Every single pricing decision flows from this."
2. **Data**: competitor price history, adjacent products competing for the same budget (his example: pricing an AI code tool against CI/CD, hosting and IDE tools), tracking tools.
3. **Model and justification**: pick a model and say why the others lost.
4. **Stakeholder buy-in**: a pricing document (executive summary, market and competitors, segments and value, chosen model and rejected options, financial projections), told in each function's terms: Sales (ACV, sales velocity), Marketing (leads, PQLs), Finance (margin, LTV/CAC), Leadership (company goals).
5. **Test and iterate**.

- Strategy → metric table:
  - Penetration: DAU, market share, CAC payback.
  - Skimming: ARPU, gross margin, conversion at each price.
  - Value-based: LTV, NRR, churn.
  - Cost-plus: gross and contribution margin.
  - Competitive: price vs key rivals, win/loss rate.
- Top mistakes: cost-plus for software; anchoring yourself as "the cheap option"; a misaligned value metric.
- Review at least yearly, plus on triggers.

### 1.20 Other process frameworks

- **Product Management Journal pricing cycle**: audit (gather data and insight) → objectives (from company strategy) → choose strategy → structure and price levels → approval → implementation → repeat. Most pricing work is on in-life products, often just a tweak. Implementation means training and tools for every channel where price is discussed, and buy-in from executives who join negotiations. Review triggers: falling share, discounts that no longer drive growth or have become normal, competitors' new offers or aggressive prices.
- **LogRocket (Dhiman) four steps**: choose a strategy (cost-plus, competitive, value-based); understand customer lifetime value, CLTV = (A − B) × C where A is revenue per period, B the cost to serve per period and C the number of periods retained, and aim for CLV above acquisition cost; choose a model; monitor and adjust. Factors: target market, competition, WTP, cost, company goals.
- **"Pricing Strategy for Product Managers" five practices**: know the target market, analyze competitors, assess costs (fixed and variable), test and iterate, communicate value.
- **Qualtrics "how to choose"**: be clear on cost (add a margin for loss and waste), benchmark competitors including their history, plan the timeline for time-bound strategies, do pricing research.
- **Simon-Kucher price build-up** (consultancy): reference price → value and regional differentials → list price → customer markdowns tied to performance → service differentials. Also: good vs bad market share; a disciplined process; pricing officers support decisions but don't make them.
- **Revology discount governance** (vendor): floor, target and ceiling prices by segment are the fastest win; measure price realization and discount dispersion.
- **Unleashed new-product homework**: explore the market (similar products, why they sell, what makes yours different), know the audience (why they want it, what value it adds), find WTP (focus groups).

### 1.21 Changing prices

- Grandfather loyal customers (Stripe, ProdPad).
- Prefer small additive moves, such as a new tier plus migration (ProdPad).
- Communicate clearly and don't apologize; align sales first (ProdPad).
- Watch activation, conversion and revenue per account after a change (ProdPad).
- Signs you're too cheap: no pushback at all; a "sold-out tour" (ProdPad).
- Add value before discounting (Stripe). Paddle (vendor): don't discount more than 20% (it correlates with churn); for annual upgrades offer whole dollars or free months, not percentages.
- Services: announce yearly increases (e.g. 5%), tie to inflation, or tie to client results (client sales +25% → fees +2.5%) (unnamed services piece).
- Lawrence Poynter (Infonic, via Product Management Journal): do due diligence first; once a price is in market you have to stick with it, and customers who know each other will find out if you vary it.
- James Harvey-Samuel (via Product Management Journal): good pricing schemes fail when they aren't marketed; you should be able to state your pricing in one or two sentences.
- Silvia Kiely Frucci (Castor, via PMA), five lessons: follow the process but don't be bound by it; pricing is a team effort; the perfect structure is a myth; failed price tests are the best chance to re-examine the value proposition; pricing is not just a number.
- Revisit cadence: see conflicts.

### 1.22 Metrics for judging pricing

- Stripe (vendor): profit margin, revenue and volume, conversion or win/loss, deal size, churn and retention, LTV, market share.
- Revology: price realization, discount dispersion.
- ProdPad: activation, conversion, revenue per account.
- Gupta's strategy → metric table (1.19).

### 1.23 Who owns pricing

- Most sources: PMs rarely own pricing alone. Aha! (PM plays a supporting role); ProductPlan (myth 1 "PMs own pricing", myth 2 "it's a solo effort", myth 3 "it's not part of strategy"); Olafioye; Scrum.org (the Product Owner is a key player); LogRocket (many teams).
- Product School: owners are PMM, PM, revenue or finance, and sales ops; PMM owns it more often in self-serve and PLG; product leadership owns monetization strategy. It quotes Alvaro Morales (Orb) and Jaime DeLanghe (Slack).
- Salesforce: build a pricing team. ProCFO (vendor): the CFO's role.
- Dissent: Gupta says the PM brings the number and the story behind it.
- Simon-Kucher: pricing specialists support, they don't decide. Product Management Journal: keep a close working relationship with any pricing specialist.

## 2. Definitions and vocabulary

- **Pricing strategy**: how you set the price level. Qualtrics: "the way you set the price", "your game plan", also called a pricing method.
- **Pricing model**: the format the customer pays in (subscription vs one-off, per seat, usage). Qualtrics: "a kind of price format"; in SaaS often called **packaging**. Dovetail and Qualtrics: strategy is internal, model is external and shown to customers. ProdPad: strategy is the "why", model the "how". Product School adds a third layer, the **monetization model** (how the business makes money at all). Several sources (LogRocket, Aha!) mix the two lists.
- **Price point vs strategy**: the number itself vs the method (Forbes/Deland, Aha!).
- **Markup vs margin**: markup = profit ÷ cost; margin = profit ÷ price (see 1.2 for the errors).
- **COGS**: cost to get the product to market (materials, production labor, suppliers, wastage), excluding overheads and sales and marketing, which are operating costs (Qualtrics).
- **Gross, operating, EBITDA and net margin** (Qualtrics).
- **Willingness to pay (WTP)**: the most a customer will pay (HBS). **Willingness to sell (WTS)**: the least a supplier will accept (HBS).
- **Customer delight, firm margin, supplier surplus** (HBS Value Stick).
- **Objective price**: the money value of the benefit before perception adjusts it (Product Management Journal).
- **Value metric**: the unit of charge (Paddle).
- **Price elasticity**: % change in quantity ÷ % change in price (PMA).
- **Price realization, discount dispersion** (Revology).
- **CLV/CLTV/LTV**: revenue from a customer over their life (LogRocket formula in 1.20).
- **Penetration vs economy**: penetration is low *for now*; economy is low *by design* (Inference from how sources describe them).
- **Loss leader vs predatory pricing**: the second aims to kill rivals and is often illegal (Qualtrics).
- **Freemium vs free trial vs reverse trial** (ProdPad, Rekhi).
- **Disagreements**: whether freemium is a pricing model at all (Paddle says no); whether tiered and dynamic are strategies or models (sources file them both ways); what "the three main strategies" are (1.1); skimming (Indeed's wrong definition, 1.7).

## 3. Practices most sources agree on

1. Start from business goals: share or profit (Gupta, Product Management Journal, LogRocket, Simon-Kucher).
2. Know your full cost; it's the floor (nearly all).
3. Research what customers value and will pay, by segment (nearly all).
4. Benchmark competitors, including their price history, but don't just copy (most).
5. Combine strategies; few firms use one alone (Melio, Nationwide, others).
6. Communicate value before or with the price (Peep Laja, "Pricing Strategy for Product Managers", Harvey-Samuel).
7. Test and keep reviewing; pricing is never set and forget (nearly all).
8. Pricing is a team effort across product, marketing, sales and finance (ProductPlan, Product School, Frucci, LogRocket).
9. Be careful with discounts; add value first (Stripe, Paddle, Revology).
10. Change prices carefully: grandfather, explain, align sales (Stripe, ProdPad).
11. Strategy shifts across the product life cycle (Unleashed, Product Management Journal, Qualtrics).

## 4. Conflicts between sources

1. **Best WTP method.** Gupta: A/B tests are the "gold standard". Qualtrics and Sawtooth (both sell conjoint): conjoint is; Van Westendorp and Gabor-Granger are dated or weak. Inference: both camps sell or teach their method; A/B tests need traffic, conjoint works pre-launch.
2. **Per-seat pricing.** Paddle: seats are a "relic". ProdPad and Slack's model treat per-seat as standard, with AI as an add-on tier.
3. **Good-better-best.** Paddle: "dying out" in software. Gupta, Shopify, Product School, Qualtrics: a staple.
4. **Which tier buyers pick.** ProductPlan says most pick the cheapest; Product School says the middle; Qualtrics says tiers anchor buyers to the middle.
5. **How dominant hybrid pricing is.** ProdPad treats hybrid as where most land; Poyar's poll (my research) has it at 37%.
6. **Review cadence.** Every 6 months (Patrick Campbell via ProdPad); quarterly experiments (Paddle); quarterly reviews (Stripe, CO—); at least yearly (Gupta); on triggers (Product Management Journal); once set, stick with it (Poynter).
7. **Does the PM own the number?** Gupta yes; Aha!, ProductPlan, Product School, Olafioye no.
8. **Is freemium pricing?** Paddle: an acquisition model. Most others: a pricing model.
9. **Most common strategy.** Melio and HubSpot via Nationwide: cost-plus. SaaS sources: value-based. Probably both true in their own markets (Inference).
10. **Penetration for SaaS.** Salesforce says it benefits SaaS and Gupta ties it to PLG; Paddle steers SaaS away from economy and dynamic pricing.
11. **Charge more or less.** Peep Laja: better to charge more than less. Penetration advocates: start low.
12. **Single currency vs localization.** Peep Laja: think in USD. Paddle, PMA, Shopify: localize.
13. **The Economist decoy.** Ariely's original (General knowledge): web only $59, print only $125, print + web $125; without the decoy, 68 chose web only and 32 the combo. PMA (Agnew) has it that way. Peep Laja swaps print and web ("print only $59; web only $125"). Use Ariely's version.
14. **Markup vs margin.** Shopify and Aha! mislabel (1.2).
15. **Skimming.** Indeed's definition is wrong (1.7).
16. **Oracle as a cost-based example** (Olafioye): doubtful; no support given.
17. **How many strategies.** "3" (Qualtrics, LogRocket, Product Management Journal, with different lists), "4" (Melio, Peep Laja), "5" (Salesforce, BDC), "7" (Melio, Paddle, Stripe, Unleashed, Qualtrics models), "10" (Shopify, Product School, Salunke). No canonical list.
18. **Competitor matching.** Product Management Journal: gives a stable market and suits mature markets. LogRocket: makes you look the same as rivals. Both can hold.
19. **Unleashed's strategy list** says seven but numbers 1, 3–7 (competitive pricing is described in the body as number 2). Minor, but don't count from the list.

## 5. Examples and numbers, with flags

Illustrative examples (invented by the author, not data): all cost-plus calculations in 1.2, Gupta's ROI and cohort examples, Revology's elasticity example, Peep Laja's break-even, Aha!'s targeted-return example, Product Management Journal's £1,200 objective price, Stripe's $100k/$10k, PMA's $75 shoe.

Claimed data:

| Claim | Who says it | Flag |
| --- | --- | --- |
| Small pricing changes move revenue 20–50% | Paddle | Vendor, unsourced |
| Under 5% of Fortune 500 have a pricing function; under 10 hours a year spent on pricing | Paddle | Vendor, unsourced |
| Pricing up to 7.5x more powerful than acquisition | Paddle | Vendor (ProfitWell) |
| Value propositions shift WTP ±20% B2B, ±15% DTC; case studies +10–15%; design +20% | Paddle | Vendor |
| Correct currency symbol +30% revenue per customer | Paddle | Vendor |
| Value-metric firms: 2x growth, half churn, 2x expansion | Paddle | Vendor |
| Discounts over 20% correlate with churn | Paddle | Vendor |
| 1% price rise → up to 11% operating profit | Revology | Vendor (General knowledge: echoes Marn and Rosiello, HBR 1992, McKinsey authors) |
| Medical device client recovered 5% price realization | Revology | Vendor case study |
| Firms leave 20–30% of revenue on the table | CO— | Unsourced |
| SaaS price inflation 8.7% (TechTarget); 81% (Capgemini); 25–30% of UK/EU retailers use dynamic pricing (FT Strategies) | ProCFO | Vendor, citing others, not checked |
| Netflix 2022: $15.49 / $19.99 / $6.99 ad tier, $9.99 basic dropped; stock +3%; 33% would cancel; 25% resubscribe | Product School | Course seller; survey sources not named |
| Daily price framing 5x more likely rated a great deal | Agnew via PMA | Study not named |
| Perfume $40 → $80 raised top ratings 33% → 78% | Agnew via PMA | Unsourced |
| $34 / $39 / $44 test, $39 sold most | Peep Laja citing *Priceless* | Secondhand |
| Beer $1.60 / $1.80 / $2.50 / $3.40 test | Peep Laja | No study named |
| Economist decoy 16/0/84 and 68/32 | Ariely, via PMA and Peep Laja | Real study; option labels disputed (conflict 13) |
| Software margins "as high as 50%", supermarkets 1–2% | Unnamed services piece | Unsourced |
| Target Canada failed partly over high prices | Indeed | Weak source |
| Hybrid 37% (from 25%), AI credits 29%, AI gross margin target ~50%, 3 in 4 changed pricing in a year | Poyar, Growth Unhinged (my research) | Poll of 230, sponsored by Metronome (billing vendor) |
| Freemium 1–10%, trial without card ~25%, with card 30–50% | Ada Chen Rekhi (my research) | Compiled vendor figures 2006–2016 |
| "Pricing is your most powerful and most immediate lever to accelerate growth" | Kyle Poyar, quoted by Peep Laja | Opinion |

Real-company examples used (as described by sources, not checked): Walmart (cost and economy), Samsung vs Apple (competitive), Tesla and McKinsey (premium/value), Virgin America (penetration), iPhone and PlayStation (skimming), Uber, airlines, Amazon, Wendy's (dynamic), Spotify, Canva, Dropbox, Slack (freemium), Netflix (tiers, localization), HubSpot, MailChimp, AWS (value metric), McDonald's, Microsoft Office, Disney+, Glossier (bundles), Gillette, printers (loss leader), Radiohead (pay what you want), Japanese 1980s electronics (penetration undercut), Salesforce (price history, early skimming).

## 6. Sources

Kind: V = vendor (sells a tool, service or course on the topic), P = practitioner or editorial, A = academic or institutional. "Substantive" marks the ones worth reading again.

### Product management and product marketing

| Source | Author | Publisher | Kind | Date | Substantive? |
| --- | --- | --- | --- | --- | --- |
| A Product Manager's Guide to Pricing Strategy for New Products | Aakash Gupta | Personal newsletter | P (sells courses) | 2025-11-30 | Yes: process, metric table, methods |
| Pricing – how to price | Not named; quotes James Harvey-Samuel (Cable & Wireless), Lawrence Poynter (Infonic) | Product Management Journal | P (training firm) | Not given | Yes: floor/ceiling, pricing cycle, 3 strategies, objective price |
| Pricing strategy | Janna Bastow | ProdPad | V | 2026-05-28 | Yes: AI questions, price changes |
| Pricing (with Phill Agnew, Silvia Kiely Frucci, Yannick Kpodar) | Bryony Pearce | Product Marketing Alliance | V (courses) | 2023-03-29 | Yes: psychology, elasticity, EVC |
| Pricing strategies and models | Will Webster, Ethan Wing | Qualtrics | V (conjoint) | 2024-01-06 | Yes: definitions, models, examples |
| A Beginner's Guide to Value-Based Strategy | Tim Stobierski | HBS Online | A (sells course) | 2022-11-10 | Yes: Value Stick |
| 4 Common & Advanced Pricing Strategies | Peep Laja | CXL | V (courses) | 2023-03-08, upd. 2024-11-08 | Yes: psychology; decoy error |
| How to price your product in 4 steps | Monica Dhiman | LogRocket | V | Not given | Partly: CLTV, model table |
| 7 Essential Product Pricing Strategies for New Products | Greg Roughan | Unleashed Software | V | 2021-07-15 | Yes: life-cycle pricing |
| Pricing Strategy for Product Managers | Not named | Not named | Unknown | Not given | Generic |
| Product pricing strategy | Carlos Gonzalez de Villaumbrosia | Product School | V (courses) | 2024-12-25 | Partly: ownership, Netflix |
| How to price your product | Not named | Aha! | V | Updated 2024-03 | Partly: SaaS models; margin error |
| Demystifying PM's Role in Pricing Strategy | Not named | ProductPlan | V | Not given | Ownership myths |
| Product Pricing Strategies | Not named | Scrum.org | V (training) | Not given | Thin |
| Comprehensive Guide to Product Pricing Strategy | Not named | Xactly | V | 2022-11-15 | Thin |
| Pricing strategy | Editorial team | Dovetail | V | 2024-10-17 | Definitions |
| Pricing article | Seyifunmi Olafioye | Medium | P | Not given | Thin |
| Pricing article | Dishant Salunke | GDG contributor | P | 2025-10-02 | Thin |
| Pricing article | Jake Brereton | Dotwork | P | 2021-03-06 | Generic |
| Product Pricing: What Do I Charge? | Not named | Penn State Extension | A | Upd. 2026-01-13 | Small business basics |
| Pricing strategy guide | Not named | Paddle | V (billing; ProfitWell) | Not given | Yes: value metric, order of work |

### Retail, small business and general

| Source | Author | Publisher | Kind | Date | Substantive? |
| --- | --- | --- | --- | --- | --- |
| Pricing strategies | Hallie Goldstein | Melio | V (payments) | 2023-05-10, upd. 2026-07-17 | Partly |
| Pricing strategies | Janeen Marquardt | Salesforce | V | 2026-11-18 | Partly |
| Strategy of pricing | Not named | Stripe | V | Upd. 2025-08-07 | Partly: metrics, changes |
| Pricing article quoting Eric Dolansky | Not named | BDC | A-ish (state bank) | Upd. 2025-03-27 | Yes: value steps, competitive stances |
| Pricing for profit | Not named | Simon-Kucher | V (consulting) | 2024-06-05 | Yes: price build-up |
| 5 Best Practices | Not named | ProCFO Partners | V | 2025-03-14 | Numbers only |
| How to choose a pricing strategy | Not named | Nationwide | P (insurer) | Not given | Cites HBR (Mohammed 2018, Dholakia 2018), HubSpot 2020 |
| Retail pricing article | Matthew Pavich | Revionics | V | Not given | Thin |
| Pricing article | "Beyond" team | Esade | A (sells courses) | 2025-08-18 | Partly: Bertini on transparency |
| Pricing article | Ashley Deland | Forbes Council | P (paid post) | 2022-08-22 | Competitive stances |
| Pricing strategy | Andrew Bloomenthal | Investopedia | P | Upd. 2026-05-20 | Value-based types |
| Pricing Best Practices: Protecting Margin | Not named | Revology Analytics | V (consulting) | Not given | Yes: elasticity, governance |
| High, market and low price | Not named | UK education-style site | Unknown | Not given | Thin |
| Pricing article | Leanne Haas | CO— (US Chamber of Commerce) | P | Not given | Partly |
| 3 Major Pricing Strategies | Not named | Price-monitoring vendor | V | Not given | Thin |
| Services pricing article | Not named | Not named | Unknown | Not given | Price-rise tactics |
| Pricing strategies | Employer Content Team | Indeed | P | Over 2 years old | Weak; skimming error |
| Pricing Strategy Guide: 10 Types (2026) | Not named | Shopify | V | 2026 | Partly; margin error |

### From my own web research (2026-11-23)

| Source | Author | Publisher | Kind | Date | Substantive? |
| --- | --- | --- | --- | --- | --- |
| Pricing poll of 230 companies | Kyle Poyar | Growth Unhinged | P (sponsored by Metronome) | 2026-05-13 | Yes: market data |
| Freemium and trial conversion benchmarks | Ada Chen Rekhi | Personal blog | P | Compiles 2006–2016 | Rough benchmarks |
| Pricing research methods | Bryan Orme, Keith Chrzan | Quirk's (Sawtooth executives) | V | 2022 | Yes: method ranking |
