---
type: concept
summary: Choose an MVP candidate: brainstorm features per benefit, write them as user stories, break them into small chunks, rank by value over effort, and pick the chunks that make the product viable and different.
updated: 2026-11-24
knowledge_source: ingested
---

# MVP feature set

## What it is

The step from value proposition to features, the fourth layer of the
[[product-market-fit-pyramid]]. You don't build the full value proposition
first; it would take too long and risk too much. You look for the least
functionality that shows you're heading the right way (Lean Product
Playbook ch6). Olsen calls the result an **MVP candidate**: a bundle of
hypotheses that customers haven't yet confirmed is viable (ch6).

## When to use

- After the [[value-proposition-grid]] is done, before designing screens.
- Planning a v2, a redesign or a large feature.
- Keeping a ranked backlog during development (ch12).

## Steps

1. **Brainstorm per benefit.** For each benefit in the value proposition,
   generate as many feature ideas as you can, with no judgment yet:
   divergent thinking first, convergent later (ch6).
2. **Group and shortlist.** Sort ideas by the benefit they deliver. Score
   each on expected customer value and keep the top three to five per
   benefit. Looking further is wasted effort, since things change a lot
   once customers see a prototype (ch6).
3. **Write user stories.** "As a [type of user], I want to [do something],
   so that I can [benefit]", which keeps the benefit attached (ch6). Check
   each against INVEST (ch6):
   - **Independent:** no overlap; can be built in any order.
   - **Negotiable:** the how stays open for discussion.
   - **Valuable** to the customer.
   - **Estimable:** scope can be estimated.
   - **Small:** big stories carry more uncertainty, so split them.
   - **Testable:** has acceptance criteria that show when it's done.
4. **Chunk.** Break each story into smaller pieces and trim the less
   valuable ones (ch6). Example: "share photos" splits into one chunk per
   channel, and a first version can share only the photo, leaving captions
   and tags for later chunks (ch6). Set a maximum story-point size; any
   story above it must be split (ch6).
5. **Rank by ROI.** ROI is customer value divided by effort, for example
   in developer-weeks (ch6):
   - Score value on a **ratio scale**: a 10 should be worth twice a 5 (ch6).
   - When two chunks have the same ROI, do the smaller one first. It
     reaches customers and brings feedback sooner (ch6).
   - The aim is to compare items, not to get precise numbers. Estimates can
     only be as accurate as the definition behind them (ch6).
   - If numbers are hard, rate value and effort high, medium or low. That
     makes a 3×3 grid whose nine cells you rank, from high value and low
     effort down (ch6).
   - Once a product is live, the return can be business value in money,
     such as revenue from a better conversion rate (ch6).
6. **Pick the MVP candidate.** Lay out a grid with one row per benefit and
   its chunks in priority order. Then choose the chunks for v1 (ch6):
   - All the must-haves.
   - Enough of your main performance benefit that customers can see the
     difference.
   - Your top delighter, unless your lead on the performance benefit is
     large.
   - Overall, something customers find better than the alternatives, and
     ideally unique.
   You may have to skip down the ROI ranking to make the product complete
   (ch6).
7. **Sketch a short roadmap.** Push the remaining chunks into columns for
   v1.1 and v1.2. Plan only one or two minor versions ahead, and be ready to
   throw them out after customers react (ch6).

## Keeping the backlog ranked

- Rank every item, not just high, medium and low. Fifteen "high" items
  don't tell a developer what to start next (ch12).
- Treat the order like ice: frozen most of the time, melted briefly to
  slot in a new item, then frozen again (ch12).
- Keep breaking stories down, a five-point story into a three and a two
  and smaller still. Small batches give faster feedback and smaller
  estimation errors (ch6, ch12). Overruns are lopsided: big tasks hide
  "unknown unknowns", and splitting them turns those into known unknowns
  (ch12).
- Product managers stay one or two sprints ahead of designers, and
  designers one or two ahead of developers, so developers always have a
  groomed sprint ready (ch12).
- Define more than the happy path, but don't stall on every detail (ch12).

## Good and bad signs

- Good: every chunk in v1 traces to a must-have, the main performance
  benefit or the top delighter.
- Good: the team can say what it cut and why.
- Bad: v1 tries to cover every benefit in the grid.
- Bad: stories describe screens with no "so that".

## Pitfalls

- Treating "minimum" as permission for too little function, or a buggy,
  hard-to-use product. See [[minimum-viable-product]] (ch7).
- Low-ROI work. Its large effort shows up during the build, but its low
  value usually shows only after launch (ch6).
- Precise roadmaps beyond the next release (ch6).
- Skipping design because the team is "Agile". You still design before you
  code, only in smaller pieces (ch12).

## Contradictions

- [[rice-scoring]] and [[ice-scoring]] add reach and confidence to the
  value-over-effort ratio. Olsen's ROI uses only value and effort, with
  uncertainty handled by testing and re-scoring (ch6).
- [[moscow-method]] sorts a release into must, should, could and won't.
  Olsen builds v1 from Kano categories instead: all must-haves plus the
  chosen differentiators (ch6).

## Pairs well with

- [[story-map]]: another way to slice the first release
- [[value-vs-effort-matrix]]: the 2×2 cousin of the 3×3 grid
- [[mvp-test-matrix]]: how to test the candidate
- [[agile-and-scrum]]: the delivery process for the chunks

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[product-frameworks]]
- [[startups-and-business-building]]
