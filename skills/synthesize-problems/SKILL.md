---
name: synthesize-problems
description: Read across every ingested source and bring the problem pages up to date - find missed problems, propose merges and splits, recount evidence and size each problem with own and public evidence kept apart. Use when the user asks what customers' problems are, to synthesize or size problems, or before ranking opportunities.
---

# synthesize-problems

Ingest writes problem pages one source at a time. This skill reads across
all of them: it finds pains that no page holds yet, spots pages that are
the same problem or two problems in one, and recounts each problem's
evidence and size from scratch.

You count and you record. You never rank problems here
(`skills/rank-opportunities` does that), never score them, and never
guess a number.

## Inputs

- The scope: all current problems (the default), or a segment, feature
  area or list of problem pages the user names.
- The mode. **Guided** (the default): you stop once, to confirm merges,
  splits and new pages. **Without stopping**: only when the user says so.

## Steps

1. **Take stock.** List the current problem pages in scope and the source
   pages, each marked own or public (its `Evidence:` line). For each
   problem, count the sources it cites. List own sources that feed no
   problem page. **Output:** a table of problem, own sources, public
   sources; then the list of sources that feed none.
2. **Read across the sources.** For every own source in scope, read its
   Key points and Quotes, and the raw file when a detail matters. Write
   down each pain, need or complaint it shows, with who has it and when.
   Read public sources too, and keep their pains marked public.
   **Output:** one line per pain: what hurts, who, source, own or public.
3. **Group the pains.** Put each pain under an existing problem page, or
   under a new problem when no page holds it. A problem is one pain for
   one kind of customer in one situation. Two pages describing the same
   pain for the same people should merge. A page holding two pains with
   different people or situations should split. A pain that shows up in
   public sources only becomes a problem page only if the user asks; list
   it instead. A signal that isn't a customer's pain (a deal lost on
   price, feedback on a fix already shipped) goes on the related page as
   evidence, or under "Not filed" with a reason. **Output:** the
   grouping, then "Create", "Merge", "Split" and "Not filed" lists, each
   with a one-line reason.
4. **Confirm.** Guided: show the Create, Merge and Split lists and wait.
   Without stopping: create the new pages, but don't merge, split, rename
   or delete anything (AGENTS.md says to ask first); keep those as
   proposals for the report. **Output:** the user's answer, or "Running
   without stopping: merges and splits proposed only".
5. **Update each problem page** by `rules/pages.md` and
   `templates/problem.md`:
   - Evidence: one line per finding, each cited. Public findings start
     `Public:`.
   - Size, Evidence strength: count it yourself from Evidence. Own and
     public apart: sources, distinct customers or accounts, segments,
     first and last seen, kinds. A public source never adds to the own
     count.
   - Size, Magnitude: every line has a value, a range or `unknown`, and a
     Basis from the shared list (`measured`, `stated by source`,
     `team guess (<who>)`, `inference`). Use `team guess` only when a
     source or a recorded note names who guessed. Arithmetic on sourced
     numbers is `inference` and shows its working.
   - Urgency: the highest step a source shows people taking. Sources
     disagree when they show different steps for the same segment; then
     use the lower step and add a Contradictions line naming both
     sources. Cancelling isn't a step on the ladder: put it under Cost to
     us.
   - Biggest unknown: the line that matters most and is least known, and
     the cheapest way to find out (a count in the ticket tool, five calls,
     a query).
   - Set `As of`, `as_of` and `updated` to today.
   **Output:** each page, with one line on what changed.
6. **Flag thin evidence.** A problem is thin when it rests on one own
   source, or when everything about who has it comes from one account
   with no measured count across customers (such as a ticket count). A
   thin problem gets a line under Size: `Inference: thin evidence (<what it
   rests on>).` If a decision or a goal leans on a thin problem, say so on
   the same line, linking it. **Output:** each thin problem, or "None".
7. **Queue what has no source.** Pages built from ingested sources need
   no confirmation. A fact that comes from no ingested source (something
   said in chat but not recorded, an email not yet saved in `raw/`) goes
   to `wiki/review-queue.md`, not onto a page. **Output:** the lines
   added, or "None".
8. **Update the overview and index.** Make sure every current problem is
   under Top problems in `wiki/overview.md`, with one line each, in no
   ranked order. Add new pages to `wiki/index.md`. **Output:** the lines
   changed.
9. **Log it.** Append to `wiki/log.md`:
   `## [YYYY-MM-DD] query | Synthesize problems: <scope>`, then one line
   per page created or updated. **Output:** the entry.
10. **Check.** Run `python3 tools/lint_wiki.py`. Fix every `ERROR` and run
    it again until it prints `RESULT: 0 errors`. **Output:** the final
    `RESULT` line.
11. **Report:**

    ```text
    ## Problem synthesis report: <scope>
    ### Problems
    ### Pages created
    ### Pages updated
    ### Merges and splits proposed
    ### Public-only pains
    ### Not filed
    ### Thin evidence
    ### Contradictions
    ### Biggest unknowns
    ### Review queue additions
    ### Lint result
    ```

    Under Problems, one line each: name, own sources and accounts, public
    sources, urgency. List them alphabetically, not by size.

## Never

- Put a RICE, ICE or other score, a rank or a market size on a problem
  page.
- Multiply reach by frequency, or add own and public counts together.
- Use a public figure (a survey share, a vendor stat) as the share of the
  user's customers who have a problem.
- Turn a guess into `measured`, or write a number no source gives.
- Merge, split, rename or delete a page without the user's yes.
