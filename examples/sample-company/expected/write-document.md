# Expected write-document result

Draft: revise when the skill is written. Prompt: chat script line 4
("Write the offline mode results up as a weekly update for Dan"). Starts
from the seeded wiki.

## Must do

- [ ] Saves to `documents/<YYYY-MM-DD>-weekly-update-<slug>.md` from
      `templates/document.md`, listing the wiki pages it used and their
      dates.
- [ ] Leads with the point for Dan: both success thresholds met, and the
      crash guardrail breached once (T18).
- [ ] Every number traces to a wiki page; computed numbers are marked
      `Inference:`.
- [ ] Says what's unknown: no crash baseline, cause is before/after only,
      JobHarbor's launch overlaps.
- [ ] Mentions Brightline's move to JobHarbor only if chat line 1 was
      recorded, and calls it one account.
- [ ] Runs humanize-check at the end and fixes what it reports.

## Must not do

- [ ] Write into `wiki/`.
- [ ] State Priya's "about half" as a measured reach (T21).
- [ ] Invent a next-quarter target.
