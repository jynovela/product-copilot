# Expected humanize-check result

Draft: revise when the skill is written. Run it on the weekly update from
write-document, and on this planted paragraph saved as a file:

```text
In today's fast-paced world, offline mode isn't just a feature — it's a game-changer. It empowers technicians, streamlines workflows, and unlocks unprecedented value. Moreover, it's worth noting that results may potentially suggest meaningful improvements. In conclusion, Crewline is poised to revolutionize field service.
```

## Must do

- [ ] The script flags, with line numbers: the filler opener, the
      em-dash, "not just X, it's Y" framing, the group of three, the
      stacked hedge ("may potentially suggest"), "Moreover", "it's worth
      noting", "In conclusion", and the hype words.
- [ ] The rewrite keeps every fact and number from the weekly update.
- [ ] The light strength, used on a demo spec or tickets, drops only
      filler and keeps precise terms.

## Must not do

- [ ] Change a number, a date or a citation while rewriting.
- [ ] Add a claim that wasn't in the input.
