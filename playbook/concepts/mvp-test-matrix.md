---
type: concept
summary: Choose how to test an MVP from a 2x2 of product versus marketing and qualitative versus quantitative tests, from five-second tests and landing pages to clickable mockups, concierge MVPs and fake doors.
updated: 2026-11-24
knowledge_source: ingested
---

# MVP test matrix

## What it is

Olsen ends the argument over whether a landing page "is an MVP" by calling
all such checks **MVP tests**. They test the hypotheses behind an MVP, and
"MVP" is kept for real products (Lean Product Playbook ch7). Tests differ in
two ways (ch7):

- **Product or marketing.** A marketing test shows a description of the
  product, so it tests the message and demand. A product test shows
  functionality, even as wireframes, so it tests product-market fit (ch7).
- **Qualitative or quantitative.** Qualitative tests talk to a few people
  and tell you **why**. Quantitative tests measure many people and tell you
  **what** and **how many**, but not why (ch7).

| | Marketing | Product |
| --- | --- | --- |
| **Qualitative** | Marketing materials, five-second test | Wireframes, mockups, interactive prototypes, Wizard of Oz, concierge, live product |
| **Quantitative** | Landing page or smoke test, explainer video, ad campaign, A/B and multivariate tests, crowdfunding | Fake door or 404 page, product analytics, A/B tests |

## When to use

- Deciding how to test an MVP candidate before building it.
- Testing a new feature on a live product.
- Teams lean only on numbers, or only on interviews.

## Steps

1. **Name what you need to learn**: demand, message, product value,
   usability, or willingness to pay.
2. **Start qualitative.** Quantitative tests run without qualitative work
   first usually do worse, and when they do well you don't know why. Most
   teams then alternate between the two (ch7).
3. **Pick a quadrant and a test** (below).
4. **Raise fidelity step by step.** Changing a design is much cheaper than
   changing code, so test designs before you build (ch7).
5. **Test the live product too.** It is the highest fidelity, and catches
   what designs miss, such as slow pages or broken browsers (ch7).

### Qualitative marketing

- **Marketing materials:** show a landing page, video, ad or email and ask
  how compelling it is and why. Show competitors' materials too, to test
  your differentiation (ch7).
- **Five-second test:** show the page for five seconds, then ask what they
  remember and liked. This checks whether the message says what the product
  does and why anyone would want it (ch7).

### Quantitative marketing

- **Landing page or smoke test:** describe the planned product and measure
  conversion, the share of visitors who click "sign up" or "pricing". A
  "coming soon" page collects emails (ch7). Add a page of plans and prices
  to test willingness to pay (ch7). Design and copy affect the result as
  much as the benefits (ch7).
- **Explainer video:** a landing page that uses video; good for products
  hard to explain in words (ch7).
- **Ad campaign:** compare click rates across taglines or targeting. Ads
  are too small to carry a whole value proposition, so use them to tune
  acquisition, not to validate fit (ch7).
- **A/B and multivariate tests:** run versions at the same time, not one
  after another, so seasonality or promotions don't skew results.
  Multivariate tests try every combination of page elements (ch7).
- **Crowdfunding:** customers pay before you build, which settles whether
  anyone will pay. It needs a rich description, since there's nothing to
  try (ch7).

### Qualitative product

Ordered by fidelity and interactivity (ch7):

- **Hand sketches:** for the team only, too rough for customers (ch7).
- **Wireframes:** layout without visual design. Use real copy early to find
  layout problems. Make them clickable along the "happy path" and test on
  the target device (ch7).
- **Mockups:** visual design added, linked into clickable flows (ch7).
- **Interactive prototypes:** working controls such as menus, forms and
  players (ch7).
- **Concierge MVP:** deliver the service by hand to a few customers, who
  know it's manual, to learn what the product should do. Best for services
  that need a lot of customer input (ch7).
- **Wizard of Oz MVP:** looks like the real product, with manual steps
  hidden behind the curtain (ch7).
- **Live product:** moderated, in person or remote, or unmoderated and
  recorded (ch7). See [[moderated-user-testing]].

### Quantitative product

- **Fake door or 404 page:** add a link to a feature that doesn't exist and
  measure clicks. Show a thank-you page, perhaps asking why they'd value it.
  Take it down once you reach the sample size you need (ch7).
- **Product analytics:** see which features people use; watch metrics after
  changes (ch7).
- **Product A/B tests:** split traffic between two experiences. The split
  needn't be even if the smaller arm has enough data (ch7).

## Good and bad signs

- Good: each test names the hypothesis and the pyramid layer it checks.
- Good: qualitative rounds come before quantitative ones.
- Bad: a high landing-page conversion treated as proof of product-market
  fit. Marketing tests don't create customer value; you still have to test
  a product (ch7).

## Pitfalls

- Relying on one kind of test, usually quantitative (ch7).
- Leaving fake doors up long enough to annoy customers (ch7).
- Waiting for the live product to show customers anything (ch7).
- Under-powered A/B tests: small differences need very large samples (ch7).

## Contradictions

- [[pretotyping]] and the research digest place cheap demand tests before
  minimal products, and Strategyzer calls a smaller product a poor test
  artifact (see [[2026-11-24-research-digest-experiments]]). Olsen agrees on
  testing before building but insists you must eventually test a product
  prototype, because marketing tests can't show product value (ch7).

## Pairs well with

- [[fake-door-test]], [[concierge-and-wizard-of-oz]], [[ab-testing]]: each
  test in depth
- [[experiment-design-doc]]: write the plan before the test
- [[ux-design-iceberg]]: design the artifact you'll test

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[product-experimentation]]
- [[discovery-and-customer-insight]]
