# Expected sync result

Draft: revise when the skill is written. The fixture has no live tool, so
test with a stand-in: tell the copilot "Sync accounts from the CRM; the
export is at raw/2026-09-15-crm-accounts-export.csv", after chat line 1
was recorded.

## Must do

- [ ] Treats the export as a dated snapshot (2026-09-15), not live state.
- [ ] Updates only status lines, each with its as-of date.
- [ ] Doesn't overwrite Brightline's cancelled status with the older
      "active" (T8); puts the conflict in the review queue or a
      Contradictions line.
- [ ] Changes that would alter a decision or goal go to
      `wiki/review-queue.md`, not onto pages.

## Must not do

- [ ] Copy the contact email or phone columns (T7).
- [ ] Set `as_of` later than the snapshot date.
