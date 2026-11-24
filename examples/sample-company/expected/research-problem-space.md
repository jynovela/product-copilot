# Expected research-problem-space result

Skill: `skills/research-problem-space/SKILL.md`. Seeded wiki. Prompt:
"Research how small field service firms deal with technicians losing
signal. Run without stopping." Needs web access. The fixture's company
and competitors are invented, so this tests the save rules, not specific
findings.

## Must do

- [ ] Shows results and waits for picks (guided), or saves all it judged
      relevant (without stopping).
- [ ] Each saved file is a new `raw/public/` file named by the rules, from
      `templates/raw-extract.md`, with URL, fetch date and question;
      numbers copied exactly; at most three short quotes.
- [ ] Ingests each saved file in the same run, with `Evidence: public`.
- [ ] On the offline problem page, new findings are counted as public
      evidence, apart from own (T11).
- [ ] Says so when every saved page is a vendor's (run 1 saved seven
      vendor pages, all selling offline features).
- [ ] Logs `## [date] search | <question>` with one line per file saved
      and per result rejected.

## Must not do

- [ ] Edit or overwrite an existing raw file, including
      `raw/public/2026-09-10-fieldops-weekly-smb-technology-survey.md`.
- [ ] Save an AI search answer, a forum username or contact details.
- [ ] Present a public finding as how many Crewline customers have the
      problem.
