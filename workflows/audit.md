# Workflow: audit

Use when the user asks to audit the wiki, or to check that its claims
match their sources. The check script proves a page names a source and
that quotes are word for word. Only reading can tell whether a claim says
what its source says. This workflow samples claims and reads.

1. **Draw the sample.** Run `python3 tools/lint_wiki.py --sample 10`, or
   with the number the user gave. It picks cited lines at random, so you
   don't choose the easy ones. If the user named pages, take every cited
   line on those pages instead. **Output:** the lines, numbered.
2. **Check each claim.** Open the source page it cites, then the raw
   file. Compare who, what, how many, when, and how strongly it is
   worded. Give one verdict:
   - `supported`: the raw file says it.
   - `partly`: something differs. Say what: a number, a date, a name, a
     guess written as a fact, one customer written as many.
   - `not supported`: the raw file doesn't say it, or says the opposite.
   - `can't check`: the raw file isn't on this computer.
   **Output:** one line per claim: the verdict and, unless supported, the
   words from the raw file that matter.
3. **Propose fixes.** For each `partly` or `not supported` claim, write
   the corrected line. Follow `rules/pages.md`: a wording fix is an edit;
   a factual error gets a dated correction line, never a silent edit; a
   locked section gets a Deviations line or a new page. Say which other
   pages repeat the claim (`grep`). Show the fixes and wait for a yes,
   unless the user said to run without stopping. **Output:** the fixes
   and the user's answer.
4. **Fix.** Make the approved changes. Each changed page gets today's
   date in `updated`. **Output:** each path changed, one line each.
5. **Log and check.** Append `## [YYYY-MM-DD] audit | <n> claims,
   <k> wrong` to `wiki/log.md`, one line per page changed. Run `python3
   tools/lint_wiki.py` until `RESULT: 0 errors`. **Output:** the entry
   and the final `RESULT` line.
6. **Report:**

   ```text
   ## Audit report: <date>
   ### Sample
   ### Supported
   ### Partly supported
   ### Not supported
   ### Could not check
   ### Fixes made
   ### Fixes waiting on a person
   ### Lint result
   ```

   If two or more claims in ten were wrong, say so first and suggest a
   larger sample of the page types they came from.

## Never

- Change a claim to match your own view of what is likely. The raw file
  decides.
- Edit a raw file or a source page's quote to make a claim fit.
- Mark a claim `supported` from the source page alone when the raw file
  is there to read.
