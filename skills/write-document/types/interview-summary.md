# Type: interview summary

`doc_type: interview-summary`. Humanize mode: full.

**Reader:** the team. **They decide:** whether this call changes what we
believe about a problem or an assumption.

## Read first

- The interview's source page in `wiki/sources/` and its raw file.
- The problem, customer, account and experiment pages the source page
  touched.
- The interview guide in `documents/`, if one was used.

If the notes aren't ingested yet, stop. Ask the user to save them in
`raw/` and run `ingest`, or, if they pasted the notes in chat, save them
with the record workflow's note step first. A summary of notes that were
never ingested doesn't count as evidence anywhere.

## Sections

1. **Who and when.** Role, segment or account, company size, date and
   interviewer. No names of private people unless the user says so, and
   never contact details.
2. **Top takeaways.** Three at most, each backed by what they said or did.
3. **Current workflow.** Their workflow, tools, workarounds, and what
   the problem costs them.
4. **Against our assumptions.** For each problem or assumption the call
   touched: supports, contradicts, or no signal, with the reason.
5. **Commitment.** The next step they agreed to, or "none".
6. **Discount this.** Compliments, hypotheticals and generic claims from
   the call, so nobody counts them as evidence.
7. **Follow-ups.** Who does what next.

## Type rules

- Keep what they did apart from what they said they would do.
- One interview is one data point. Never write "users want" from it.
- Quotes come word for word from the raw file, as block quotes.
