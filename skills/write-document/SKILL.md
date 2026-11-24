---
name: write-document
description: Write a document for people from what the wiki knows, such as a PRD, weekly update, demo spec, interview guide or interview summary. Use when the user asks you to write, draft or prepare any document to read, share or hand to a builder.
---

# write-document

You write documents a person will read, share or hand to someone else. The
wiki is your source, and the document is the product. Each document type has
its own file in `types/` that says who reads it, what to read first and
what shape it takes. This file holds what every type shares.

## Types

| The user asks for | Type file | Humanize mode |
| ----------------- | --------- | ------------- |
| A PRD, spec, feature brief or one-pager for a feature | `types/prd.md` | full |
| A weekly update, status update or what happened this week | `types/weekly-update.md` | full |
| A demo spec, prototype brief, or a description an AI can build a demo from | `types/demo-spec.md` | light |
| An interview guide, script or questions for customer calls | `types/interview-guide.md` | light |
| A summary or write-up of a customer interview | `types/interview-summary.md` | full |

For anything else, use the closest type's shape and say so, or follow only
this file and set `doc_type` to a short name for it.

## Steps

1. **Pick the type.** Match the ask to a row above and read that type file.
   **Output:** the type and its file.
2. **Ground it.** Read `wiki/ways-of-working.md` and `wiki/now.md`. Name
   the reader, what they must decide or do after reading, and the length
   that fits. Where "Formats I prefer" covers this type, it wins over the
   type file. **Output:** reader, decision, length, one line each.
3. **Gather.** Read the pages the type file lists. Find them with
   `wiki/index.md` or `grep`, and open only those. Skip archived pages unless
   the user asks for history. Note each page's `updated` date and flag any
   that lint would call outdated. **Output:** the pages read, with dates.
4. **Check the evidence.** List what the document must say and which page
   supports each point. **Output:** two lists, "Supported" and "Gaps".
   - A gap becomes a visible placeholder in the text, like
     `[NEEDS: baseline for weekly active teams]`, and a line under Open
     questions. Never fill a gap yourself.
   - No baseline or target means "direction only". Never estimate a
     number. Arithmetic on sourced numbers is fine, marked as yours.
   - When the evidence is thin (one interview, public sources only, pages
     past their freshness window), say so in one line at the top of the
     document, before the reader relies on it.
5. **Draft.** Run `date +%F`. Create
   `documents/<YYYY-MM-DD>-<doc type>-<short-title>.md` from
   `templates/document.md` with `status: draft`, and follow the type
   file's sections. Write the body for the reader: plain prose, no
   `[[links]]`, the point first. List every wiki page you used under
   `## Built from` with its `updated` date. **Output:** the path.
6. **Humanize.** Run `skills/humanize-check` on the file in the type's
   mode and fix what it finds. **Output:** its one-line report.
7. **Read it as the reader.** Does the first paragraph tell them what they
   need? Is every section earning its place? Cut a section the type marks
   optional when it would be empty. **Output:** each change, or "None".
8. **Check.** Run `python3 tools/lint_wiki.py` and fix every `ERROR` on
   the document. **Output:** the final `RESULT` line.
9. **Report:**

    ```text
    ## Document report: <title>
    ### File
    ### Type, reader and decision
    ### Built from
    ### Gaps and placeholders
    ### Evidence note
    ### Humanize check
    ### Lint result
    ```

## Rules for every type

- A document records nothing. If writing it surfaces a decision, a new
  fact or a status change, offer to record it with `workflows/record.md`;
  don't edit wiki pages from here.
- Never set a goal, target, price, scope or decision in a document. Write
  what the wiki says a person decided, and who.
- Keep own and public evidence apart, as the wiki does: public sources
  show what a market says, never how many of our customers have a problem.
- Quote people exactly and only from a raw file or source page, at most 25
  words a quote, as a block quote (`>`). The humanize check skips quotes.
- No contact details for anyone, and no real customer data in sample or
  example data.
- A new version is a new file with a new date. Never overwrite a document
  the user has seen.
- Set `status: final` only when the user says it's done.
