# Type: weekly update

`doc_type: weekly-update`. Humanize mode: full.

**Reader:** the person's manager and stakeholders, reading in two minutes.
**They decide:** whether anything needs their help or attention.

## Read first

- `wiki/now.md`: this week's goals and this month's focus.
- `wiki/log.md` entries dated in the week. Search for them by date, like
  `grep -n "^## \[2026-11-2" wiki/log.md`, instead of reading the log.
- Pages those entries touched: features whose Status changed, decisions
  made, experiment results, metric results at check dates.
- The last weekly update in `documents/`, to avoid repeating it.
- Not `wiki/review-queue.md`. Unconfirmed items stay out, or appear only
  labeled "unconfirmed".

## Sections

1. **Headline.** One or two sentences: the most important thing that
   happened or needs attention.
2. **This week's goals.** Each goal from now.md: done, moving or stuck,
   with one line on why.
3. **Shipped and decided.** What launched, and decisions with who made
   them. Optional.
4. **Numbers.** Only sourced numbers, each with its as-of date. Optional.
5. **Risks and asks.** What's at risk, and what you need from whom by
   when. Write "None" when there is nothing.
6. **Next week.** Up to three lines.

## Type rules

- Only what changed this week. No background the reader already knows.
- Aim for 250 words or fewer.
