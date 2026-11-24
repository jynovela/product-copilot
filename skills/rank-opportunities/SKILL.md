---
name: rank-opportunities
description: Rank the current problems against the active strategy and goals, file the ranking as an analysis, propose one pick, and record the opportunity decision once a person picks. Use when the user asks what to work on next, which problem matters most, or to rank or prioritize opportunities.
---

# rank-opportunities

You compare the current problems against what the company said it is
trying to do, and propose which one to work on next. A person picks.
Once they do, you record the decision.

The ranking depends on the strategy and the goals, so it lives on an
analysis page, never on the problem pages. Every judgment you make is
marked `Inference:`, and you never invent a number to break a tie.

## Inputs

- Optional: the goal or focus area to rank against. The default is the
  active strategy and current goals.
- Optional: the problems to compare. The default is every current problem
  page.
- The mode. **Guided** (the default): you stop at the pick and wait.
  **Without stopping**: only when the user says so; you record your own
  pick as unconfirmed.

Run `skills/synthesize-problems` first if a problem page has no Size
section, or an own source newer than the problem pages' `As of` reports a
customer pain.

## Steps

1. **Ground the ranking.** Read the active strategy page (Challenge, Focus
   areas, Won't do), the current goals and `wiki/overview.md`. If the user
   named a goal or focus, use that. Goals whose period has ended are
   context only; say "No current goals". If there's no strategy and no
   current goal,
   say so and ask the user what to rank against (without stopping: rank
   by evidence strength and urgency only, and say that's the basis).
   Never write a strategy or goal yourself. **Output:** the challenge,
   focus areas, goals and won't-do lines, each linked, or what's missing.
2. **List the candidates.** Take the current problem pages in scope. For
   each, open its related features and decisions. When a feature for it
   has launched, the candidate is what's left of the problem after the
   launch, shown by sources dated after it; say what that is, or "nothing
   left on record". **Output:** one line per candidate: problem, related
   features and their status, and what's left.
3. **Screen against the strategy.** A candidate that only matters to
   customers or markets in Won't do goes under "Outside the strategy" with
   the Won't do line it hits, and isn't ranked. Say so in the report; a
   person may still choose to reopen the strategy. **Output:** the
   screened-out candidates with their reasons, or "None".
4. **Assess each candidate.** Copy from the problem page, don't recount:
   own evidence strength, urgency, cost to us, biggest unknown. Then judge
   fit with the challenge, the focus areas and the goals. Public evidence
   is context only. A competitor's own claim is never evidence that a
   solution would work. Use a score such as RICE only when every input
   has a sourced Basis; otherwise compare in words. **Output:** a table
   with one row per candidate: problem, fits (which challenge, focus or
   goal), own evidence, urgency, cost to us, biggest unknown, and one
   `Inference:` line on why it ranks where it does.
5. **Rank and propose.** Order the candidates. Where two can't be told
   apart on the evidence, still order them, mark the pair `tie`, give an
   `Inference:` reason for the order, and name the cheapest check that
   would separate them. Propose one pick, and say what would change your
   mind. **Output:** the ranking, the proposed pick, and
   `Would change if: <signal>`.
6. **File the ranking.** Create
   `wiki/analyses/rank-opportunities-<YYYY-MM-DD>.md` from
   `templates/analysis.md`. The Answer holds steps 1 to 5, each claim
   cited to a page. Not in the wiki lists what would sharpen the ranking.
   Add it to `wiki/index.md`, and link it from the overview's Open
   questions as `Pick an opportunity: see [[rank-opportunities-<date>]]`
   so it isn't an orphan while the pick waits. **Output:** the path.
7. **Pick.** Guided: show the ranking and the proposed pick, and wait for
   the user to choose. Without stopping: use your proposed pick.
   **Output:** the pick and who made it.
8. **Record the decision.** Create `wiki/decisions/<short-pick>.md` from
   `templates/decision.md` with `kind: opportunity`. Decided by is the
   person who picked, as they named themselves, or `copilot (unconfirmed)`
   when running without stopping. Never write a person's name for your own
   pick. Save a person's pick first as a chat note and source page with
   `workflows/record.md`, its Save the note and Source page steps only (no Record report; log it
   under this skill's entry), and cite it. Under Known at decision, use the opportunity block: copy the
   problem's Size section with its As of date, and the goal it serves (or
   "none current"). For a copilot pick, Expected result is `direction
   only`, and Watch names the metric the strategy's challenge uses with
   "check date: set by a person"; never set a target.
   List the other ranked candidates under Options not chosen, plus "Do
   nothing". Link the analysis as evidence. Fill Revisit when with the
   "would change if" signal. Link the decision from the problem page, add
   it to the index, and add it to the strategy's Signals only if a person
   picked. Remove the overview's "Pick an opportunity" line from step 6.
   **Output:** the path.
9. **Log it.** Append to `wiki/log.md`:
   `## [YYYY-MM-DD] query | Rank opportunities against <basis>`, then one
   line per page created or updated. **Output:** the entry.
10. **Check.** Run `python3 tools/lint_wiki.py`. Fix every `ERROR` and run
    it again until it prints `RESULT: 0 errors`. **Output:** the final
    `RESULT` line.
11. **Report:**

    ```text
    ## Opportunity ranking report: <basis>
    ### Unconfirmed decisions
    ### Ranked against
    ### Ranking
    ### Outside the strategy
    ### Proposed pick
    ### Decision recorded
    ### What would sharpen the ranking
    ### Lint result
    ```

    "Unconfirmed decisions" comes first and names each decision the
    copilot recorded, so a person can confirm it.

## Never

- Write a rank, score or market size on a problem page.
- Invent a reach, revenue or cost figure, or use one with no Basis, to
  break a tie.
- Record a person as the decider of your own pick.
- Use a competitor's marketing claim, or a public survey share, as
  evidence about the user's customers or about what would work.
- Change the strategy or a goal to fit the ranking.
