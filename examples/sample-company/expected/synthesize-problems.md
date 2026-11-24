# Expected synthesize-problems result

Skill: `skills/synthesize-problems/SKILL.md`. Starts from a wiki with
every source ingested (`setup.sh --seeded`, or after the ingest run).
Prompt: "Synthesize the customer problems across all our sources. Run
without stopping."

## Must do

- [ ] Finds at least these problems: technicians can't work without
      signal; owners wait too long to get paid; the accounting sync
      creates duplicate customers; long jobs need multi-day scheduling.
- [ ] Each problem's Size counts own and public evidence apart (T11).
      Offline: own sources include Brightline, the support export and the
      PRD; public is the FieldOps survey only.
- [ ] Every Magnitude line has a Basis from the shared list. Offline
      frequency `stated by source` (Brightline, "every day"); reach
      `unknown`, or `team guess (Priya Nair)` if chat line 3 was recorded.
- [ ] Offline urgency is the lower step where Brightline and Mendez
      disagree, with a Contradictions line (T2).
- [ ] Slow payment urgency `built a workaround` (Mendez's spreadsheet).
- [ ] Multi-day jobs: evidence strength one account, flagged thin (T10).
- [ ] Names the biggest unknown per problem and the cheapest way to find
      out.
- [ ] Without stopping: creates new problem pages if needed, but only
      proposes merges and splits.
- [ ] Logs `## [date] query | Synthesize problems: ...` and ends with the
      report, every heading present.

## Must not do

- [ ] Put a RICE or ICE score, or a market size, on a problem page.
- [ ] Multiply reach by frequency.
- [ ] Count the survey's 31% as Crewline customers.
- [ ] Merge, split, rename or delete a page without asking.
- [ ] Rank the problems or list them by size.
