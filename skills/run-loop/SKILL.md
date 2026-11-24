---
name: run-loop
description: Run several product-loop skills in a row for one ask, such as "find the best opportunity for Q1 and write a PRD for it", guided or without stopping, and end with one report that lists every unconfirmed pick first. Use when the user asks for more than one loop step at once, or for an idea taken from goals or problems through to a document.
---

# run-loop

You chain the loop skills for one ask. You don't add method of your own:
each skill does its own work, keeps its own checkpoint and writes its own
report. Your job is to pick the chain, pass each skill what the last one
produced, stop when an input is missing, and sum up at the end.

## The loop

| Step | Skill | Run it when |
| ---- | ----- | ----------- |
| 0 | `set-outcome` | No current goal exists for the team, or the user asks to set goals |
| 1 | `research-problem-space` | The user asks for market or problem research, or allows the web and a problem has only one kind of evidence |
| 2 | `research-competitors` | The user names competitors, or asks how others solve the problem |
| 3 | `synthesize-problems` | A problem page has no Size section, or an own source is newer than the problem pages' As of |
| 4 | `rank-opportunities` | No current `opportunity` decision, or the user asks what to work on |
| 5 | `explore-solutions` | A problem is picked and its feature has no approved scope |
| 6 | `write-document` (prd, demo-spec) | The user asks for a PRD, a demo spec or "a plan" |
| 7 | `write-tickets` | Only when the user asks for tickets |
| 8 | `review-outcome` | Never in a chain. Run it alone, after a launch |

Launch happens outside the copilot. A chain never goes past step 7, and
never starts at step 8.

## Inputs

- The ask, in the user's words.
- The team, if the ask names one. When it doesn't, set-outcome works on
  `business` goals; say so in the plan so the person can correct it at
  set-outcome's checkpoint. Don't stop to ask before the chain starts.
- The mode. **Guided** (the default): every skill keeps its own
  checkpoint, so you stop once for each skill that has one. **Without
  stopping**: only when the user says so. Pass the mode to each skill in
  those words. The user's request is the chat note a skill saves and
  cites when it records an unconfirmed pick.

## Steps

1. **Plan the chain.** Find the first and last step the ask needs. Check
   the overview's Open questions for a `Loop stopped at` line for this
   ask, and start from that skill if there is one. Read `wiki/now.md`, the current goals, the active strategy and the newest
   `opportunity` and `scope` decisions to see which steps are already
   done. Drop a step whose output already exists and is current, and say
   why. write-document and write-tickets need an approved `scope`
   decision: if explore-solutions runs, say on their lines that they run
   only if the person approves a scope there. **Output:** the chain, one
   line per step: the skill and "run" or "skip: {reason}".
2. **Say the plan.** Show the chain to the user in one short message and
   start. Don't wait for a yes. The skills' own checkpoints are where the
   person decides. **Output:** "Plan shown".
3. **Run each skill in order.** Open its `SKILL.md` only when its turn
   comes, and follow it in full, including its report. Before you open the
   next one, keep only what the next skill needs (the table below) and the
   report's unconfirmed lines. Drop page contents you read: the next skill
   reads the wiki again. **Output:** for each skill, one line: what it
   produced and any unconfirmed pick.

    | From | To | Pass |
    | ---- | ---- | ---- |
    | the ask | set-outcome | the period, and the team or `business` |
    | set-outcome | rank-opportunities | the goal pages, or "No goal set: needs a person" and `direction only` |
    | research skills | synthesize-problems | the new source pages |
    | synthesize-problems | rank-opportunities | the problem pages changed |
    | rank-opportunities | explore-solutions | the picked problem page and the `opportunity` decision |
    | explore-solutions | write-document, write-tickets | the feature page and the `scope` decision |

4. **Stop when an input is missing.** Stop the whole chain when a
   skill's entry check fails, when it ends without the output the next
   skill needs, or when the user rejects a pick at a checkpoint.
   Never fill the gap yourself. Say what's missing and which skill or
   person would supply it. So a later session can pick the chain up, add
   one line to the overview's Open questions: `Loop stopped at <skill>:
   <what's missing>, for "<the ask>"`. Remove that line when the chain
   runs on or the person drops it. **Output:** "Ran to the end" or "Stopped at
   {skill}: {what's missing}".
5. **Check.** Run `python3 tools/lint_wiki.py` once more and fix every
   `ERROR` on a file this run wrote. **Output:** the final `RESULT` line.
6. **Report:**

    ```text
    ## Loop report: <the ask>
    ### Unconfirmed decisions
    ### Chain
    ### Stopped at
    ### Documents
    ### Needs a person
    ### Lint result
    ```

    Unconfirmed decisions comes first. List each `copilot (unconfirmed)`
    decision with its page and its line in `wiki/review-queue.md`, so a
    person can confirm or replace it. Chain has one line per skill from
    step 3. Documents lists each file under `documents/` with its status.
    Needs a person lists every choice a skill left open, such as a goal
    with no target.

## Never

- Record a goal, price, strategy, launch or outcome review as `copilot
  (unconfirmed)`. Only `opportunity` and `scope` decisions may be, and
  only in a run without stopping.
- Skip a skill's checkpoint in a guided run, or merge two checkpoints
  into one.
- Pick an opportunity that conflicts with the strategy's Won't do list
  without saying so in the report's first section.
- Write a target or number a skill left as `direction only`.
- Set a document to `status: final`.
- Run `review-outcome` in a chain, or treat a written PRD or ticket set
  as launched.
