# Expected humanize-check result

Checked against `skills/humanize-check/SKILL.md` and `check.py`. Save this
paragraph as `scratch/planted.md` in a test repo (not in `documents/`,
where the check script expects a document header) and ask: "Humanize
scratch/planted.md."

```text
# Note

In today's fast-paced world, offline mode isn't just a feature — it's a game-changer. It empowers technicians, streamlines workflows, and unlocks unprecedented value. Moreover, it's worth noting that results may potentially suggest meaningful improvements. In conclusion, Crewline is poised to revolutionize field service.
```

## Must do

- [ ] Step 2 runs `check.py --mode full` and shows its 10 findings: puffery
      ("In today's fast-paced world"), the em dash, three AI words
      ("empowers", "game-changer", "unlocks"), filler ("it's worth
      noting"), two glue transitions ("Moreover", "In conclusion"), the
      stacked hedge ("may potentially") and flat rhythm.
- [ ] Step 4 fixes what the script doesn't catch: the "isn't just X, it's
      Y" reveal, the rule of three (empowers, streamlines, unlocks), and
      the hype in "poised to revolutionize" and "unprecedented".
- [ ] Where a fix needs a fact it doesn't have (what improved, by how
      much), it writes a `[NEEDS: ...]` placeholder instead of a number.
- [ ] Runs the script again until `RESULT: 0 findings`, or gives a reason
      for each finding left.
- [ ] Ends with the one-line report.

## Also run it on

- The weekly update from write-document: the second run changes no
  number, date or name (step 6 says "Facts unchanged").
- Tickets from write-tickets in `--mode light`: only filler outside
  criteria lines changes; criteria keep their exact text.

## Must not do

- [ ] Invent a result, such as a percentage improvement, to make the text
      specific.
- [ ] Change a quote taken from a source.
- [ ] Add typos or slang.

## Scoring

Count the boxes. Any miss under "Must not do" fails the run.
