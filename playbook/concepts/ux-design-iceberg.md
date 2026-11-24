---
type: concept
summary: Design a UX bottom up through four layers (conceptual design, information architecture, interaction design, visual design), aiming for usability and delight, with Olsen's Law and core layout principles.
updated: 2026-11-24
knowledge_source: ingested
---

# UX design iceberg

## What it is

UX is the top layer of the [[product-market-fit-pyramid]]. Even with the
other four layers right, you won't reach product-market fit with a poor UX
(Lean Product Playbook ch8). A great UX lets users get the benefits the
features offer; a poor one gets in the way (ch8). It has two attributes:

- **Usability:** can customers use it? This covers task success,
  efficiency (clicks, keystrokes, time), cognitive load, and ease of
  learning, all judged for a specific user profile (ch8).
- **Delight:** do they enjoy it? Aesthetics, simplicity, smart defaults
  that seem to read the user's mind, personality and humor, responsive
  animation and sound, and surprise (ch8).

**Olsen's Law of Usability:** the more effort an action takes, the fewer
users take it; the less effort, the more do (ch8). It matters most for
actions the business depends on, such as registering or paying (ch8).

Olsen's UX design iceberg has four layers. Only the top one shows (ch8):

| Layer | Question | Main deliverable |
| ----- | -------- | ---------------- |
| 4. Visual design | How does it look? | Mockups, style guide, layout grid |
| 3. Interaction design | How do user and product respond to each other? | Flowcharts, wireframes |
| 2. Information architecture | How are information and functions structured and labeled? | Sitemap |
| 1. Conceptual design | What core concept makes it intuitive? | The concept, informed by personas |

## When to use

- Designing an MVP prototype or a new feature (ch8).
- Sorting user feedback: map each comment to the iceberg layer it belongs
  to (ch8).
- Checking whether a team has the skills a good UX needs.

## Steps

1. **Ground it in user research.** Interviews, usability tests and surveys
   feed every layer. Have the whole team watch research live, debrief
   promptly, and write up the key findings (ch8).
2. **Choose the conceptual design.** Pick a model that matches how target
   customers think, such as a checkbook metaphor for personal finance or a
   live map of nearby cars for ride hailing. It sits right above the feature
   set and is where much UX innovation happens (ch8). Use the persona's tech
   skill and usage context (rushed, "lean back", noisy) to choose (ch8).
3. **Define the information architecture.** Decide which pages exist, how
   they're grouped and what they're called, in a sitemap. Use card sorting
   to learn how users group things. Test findability: can users find a
   given page, and do analytics show short paths (ch8)?
4. **Design the interactions.** Define user flows, form inputs and
   validation, modes such as edit or preview, and states such as "in stock"
   or "in cart" (ch8). Give feedback on every action: clear error messages
   that say how to fix the problem, a spinner or message for any delay, and
   progress bars for long tasks (ch8). Use flowcharts for flows with many
   branches; for simple flows, go straight to clickable wireframes (ch8).
5. **Wireframe.** Lay out each page with real copy. Explore many directions
   before narrowing, or you risk a local maximum. Reuse page templates and
   components for consistency. Test clickable wireframes with users before
   any visual design (ch8).
6. **Apply visual design.** Use a deliberate color palette with strong
   contrast for text and key controls; two fonts at most, with few sizes;
   standard icons where a symbol already exists; a style guide; and a
   layout grid (ch8). Then test clickable mockups (ch8).

## Design principles

- **Proximity:** items close together look related. Group related controls
  and keep unrelated ones apart (ch8).
- **Similarity:** items that look alike seem related. Give all links or all
  action buttons the same look (ch8).
- **Visual hierarchy:** size, contrast, faces and position (top left
  first, in left-to-right languages) tell users what matters. Rank the
  page's elements first, then design to that order. Squint or blur a
  screenshot to check it (ch8).
- **Composition:** unity, contrast, balance and enough white space (ch8).
- **Mobile first:** design the small screen first, in parallel with the
  large one, because it forces you to prioritize. A mobile version may
  play a complementary role, not just be a smaller copy (ch8).
- **Copy is UX:** labels, instructions and error messages need plain
  words, not jargon. When a test user stumbles on a word, ask what they'd
  call it (ch8).

## Good and bad signs

- Good: feedback is sorted by layer, and the deeper layers get fixed first.
- Good: effort for key tasks is counted and goes down release by release.
- Bad: debates about colors before the flows work.
- Bad: a valuable feature that users can't find. Users rate what they
  experience, not your intended value proposition (ch8).

## Pitfalls

- Starting at the visual layer. Looking good on the surface isn't enough
  (ch8).
- Narrowing to one design direction too early (ch8).
- Designing for a large screen and then squeezing it onto mobile, which
  often ends in a separate, inconsistent product (ch8).
- A "design gap". A great UX needs product management, interaction
  design, visual design and front-end development working together, which
  Olsen calls the "A-Team". Most designers are stronger in either visual
  or interaction design (ch8).
- Assuming early adopters' tolerance will last. Innovators forgive a rough
  UX; later segments won't (ch8).

## Pairs well with

- [[affordances-and-signifiers]]: how users know what they can do
- [[target-customer-and-personas]]: who you're designing for
- [[moderated-user-testing]]: how to test each artifact
- [[fogg-behavior-model]]: ability, the effort side of Olsen's Law

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[design-and-usability]]
