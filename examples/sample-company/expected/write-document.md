# Expected write-document result

Checked against `skills/write-document/SKILL.md` and its type files. Build
the test repo with `setup.sh --seeded`. Run each prompt in a new session.

## Prompt A: weekly update

Chat script line 4:

```text
Priya here. Write the offline mode results up as a weekly update for Dan.
```

### Must do

- [ ] Picks `types/weekly-update.md`, mode full. Names Dan Reyes as
      reader and what he decides: whether anything needs his attention.
- [ ] Reads `wiki/now.md`, finds no goals set, and shows that as a gap
      (`[NEEDS: ...]` placeholder or an Open questions line), not
      invented goals.
- [ ] Gathers [[offline-mode]] and the metric pages it cites, listing
      each page read with its `updated` date.
- [ ] Headline leads with the result: both success thresholds met, and
      the crash rate guardrail breached once (0.6% in the week of
      2026-10-12).
- [ ] Numbers are sourced and dated: errors 1,886.6 average in August to
      860 in the week of 2026-11-09; share 41.13% to 46.34%. Computed
      numbers are marked as the writer's arithmetic.
- [ ] Says what's unknown: no crash baseline before 2026-10-05, cause is
      before/after only, JobHarbor's offline launch on 2026-10-07 overlaps.
- [ ] Risks and asks names the missing tier 1 launch decision, or the
      missing final review date, as something Dan can act on.
- [ ] Saves `documents/<date>-weekly-update-<short-title>.md` from
      `templates/document.md`, `status: draft`, no `[[links]]` in the body,
      `## Built from` listing pages with dates.
- [ ] Runs humanize-check in full mode; the report line is clean or names
      what's left.
- [ ] About 250 words or fewer.
- [ ] Report has all seven headings and ends with `RESULT: 0 errors`.

### Must not do

- [ ] Edit any wiki page.
- [ ] State a reach for the offline problem. If chat line 3 was recorded,
      Priya's "about half" may appear only as her guess.
- [ ] Use the late-September ticket drop as evidence offline mode worked.
- [ ] Invent a next-quarter target.

## Prompt B: PRD with thin evidence

```text
Write a PRD for multi-day jobs.
```

### Must do

- [ ] Picks `types/prd.md`. Reads the feature, the problem page, Arc
      Electric's account page and the pricing decision.
- [ ] Opens with a one-line evidence note: one account asked for it.
- [ ] Scope, first slice and success metrics are `[NEEDS: ...]`
      placeholders because the feature page has none, and each is an Open
      questions line.
- [ ] Says the 2026-10-28 pricing decision promises multi-day jobs to Pro,
      decided by Maya Okafor.

### Must not do

- [ ] Write a scope, first slice or target of its own.
- [ ] Count FieldPilot offering it as customer demand.

## Scoring

Count the boxes. Any miss under a "Must not do" fails the run.
