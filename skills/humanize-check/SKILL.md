---
name: humanize-check
description: Check and fix text written for people so it reads like a person wrote it, not a chatbot. Use on every document before you hand it over, and whenever the user asks to humanize, de-AI or edit a draft.
---

# humanize-check

You edit text so it sounds like one specific person with something to
say. Readers drop text the moment it smells machine-made, so the reader is
the only test that counts. Detector scores don't matter.

## Inputs

- The file to check, usually in `documents/`, or text the user pastes
  (save it to a scratch file first so the script can read it).
- The mode: `full` for prose people read (PRDs, reports, updates, strategy
  docs, emails). `light` for text another AI or a builder reads (demo
  specs, tickets), where precision matters more than rhythm.

Don't use it on wiki pages: their templates set their shape. Never edit a
quote from a source.

## Steps

1. **Ground it.** Name the reader, the one point the text makes, and whose
   voice it is. Read the "How to write for me" section of
   `wiki/ways-of-working.md`. Where it differs from this skill, it wins.
   **Output:** reader, point, voice, in one line each.
2. **Run the script.** `python3 skills/humanize-check/check.py <file>
   --mode <full|light>`. **Output:** the findings, or `RESULT: 0
   findings`.
3. **Fix each finding** with the smallest change that removes it and keeps
   the meaning. `references/examples.md` shows a fix for every check.
   Findings are candidates: if one is wrong (a product name that happens
   to be on the list, a term the reader uses), leave it and say why.
   **Output:** each fix, or why a finding stays, one line each.
4. **Edit for what the script can't see.** Read the text top to bottom
   against "Tells to fix by reading" below. **Output:** each fix, one line
   each, or "None".
5. **Read it aloud in your head.** Fix anything you wouldn't say to a
   smart colleague, and any stretch where the rhythm goes flat.
   **Output:** each fix, or "None".
6. **Check the facts didn't move.** Compare names, numbers, dates, links
   and citations with the text before your edits. Revert any edit that
   changed a fact. **Output:** "Facts unchanged", or each revert.
7. **Run the script again** until it prints `RESULT: 0 findings` or every
   remaining finding has a reason from step 3. **Output:** the final
   `RESULT` line.
8. **Learn the voice.** When the user rewrites your text or corrects your
   tone, propose one dated line for "How to write for me" in
   `wiki/ways-of-working.md`, such as "2026-11-24: no rhetorical questions
   in updates". Add it once they say yes. **Output:** the proposed line,
   or "None".
9. **Report** in one line: `Humanize check: clean`, or
   `Humanize check: fixed <n>; open: <what's left and why>`.

## Write like this

- **Specific over general.** Name the product, the number, the customer,
  the date. Each section has at least one detail only this team could
  know.
- **Plain words.** Use the short common word: use, help, show, important.
  Say what made something good instead of calling it good.
- **Uneven rhythm.** Mix short sentences with long ones. If three in a row
  are about the same length, change one. Paragraphs differ in size, and a
  one-line paragraph is fine.
- **A visible author.** Use "I" or "we" where someone noticed, decided or
  believes something. Take a position and say why. Hedge once, only where
  real doubt exists.
- **People and things act as they do.** A person found it, a test showed
  it. Tables, medians and charts don't show, hide or tell. Say what the
  number is.
- **Active voice, real verbs,** with cause and effect pointing the right
  way.
- **One name per thing.** Repeat the key noun instead of cycling synonyms.
- **Start with the point, stop when done.** No scene-setting opener. End on
  the last real point or the next step, not a summary.
- **Prose by default.** Bullets, headings and bold only when the format
  calls for them (documents with sections, lists of steps). Headings are
  plain labels in sentence case, never a teaser or a thesis.
- **Ordinary punctuation.** Periods and commas. Parentheses for asides. No
  em dashes, and no semicolons or setup colons in business prose.

## Tells to fix by reading

The script catches word- and phrase-level tells. These need judgment:

- **Announce-then-list.** "This combines X, Y and Z." Make the claim with
  one concrete example instead.
- **Rule of three.** Three balanced items where one matters. Keep that
  one, or give the real count.
- **Negation-first reveal in other words.** Any setup that says what
  something isn't before saying what it is.
- **Deferred noun and label-first framing.** A sentence that holds back
  its subject, or a noun phrase posing as a sentence.
- **Straw man.** Inventing a wrong reading so you can knock it down.
- **Aphoristic closer.** A paragraph that ends on a quotable line instead
  of a fact.
- **Dressed metaphor.** A figure of speech doing the work a plain claim
  should do.
- **False balance.** Granting every option equal merit to avoid a view.
  Pick a view or state the specific tradeoff.
- **Monotone structure.** Every paragraph the same length, opening with a
  topic sentence and closing with a recap, or the same point restated in
  each section.
- **Formatting tics.** Bold sprinkled on phrases, bullets where sentences
  belong, mixed quote styles. The script flags lists of bold-led items,
  short colon lead-ins before a list, and "a X, not a Y" lines. It can't
  see a list that would read better as two sentences, so read for that.
- **Teaser headings.** A heading that sells instead of labels, like "The
  work it takes off your plate". Name the section's subject.
- **Passing the script.** Text can pass every check and still read
  machine-made because of its shape. That's why steps 4 and 5 exist.

## Never

- Add typos or slang to seem human.
- Change what the text claims while fixing its style.
- Invent a detail to make text more specific. Where a detail belongs and
  you don't have one, write a visible placeholder like `[NEEDS: Q3
  churn number]` and list it in the report.
