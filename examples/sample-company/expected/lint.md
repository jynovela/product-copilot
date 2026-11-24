# Expected lint result

Testable now, after the ingest run (and the record run, if done). Prompt:

```text
Lint the wiki.
```

## Must do

- [ ] Prints the check script's output and ends at `RESULT: 0 errors`.
- [ ] Contradictions and stale claims include: the two "active team"
      definitions (T1), offline pain daily vs never (T2), 300 vs 212
      tickets (T3), and, after the record run, Brightline active vs
      cancelled (T8) and JobHarbor first vs dated release notes (T23).
- [ ] Flags the missed committed goals with no decision page: Billing KR1
      (T17) and Mobile KR1, missed by one day (T12).
- [ ] Flags the overdue strategy review (T24) and the strategy drift in
      the Northgate request (T22).
- [ ] Suggested sources include ones that would close real gaps: an NRR
      and 90-day churn report, the cancellation survey behind Sam's 14
      teams, Raj's upgrade numbers, a crash rate baseline, the plan price
      list.
- [ ] Freshness warnings, if any, are listed but not fixed by changing
      `as_of` without a new source.

## Must not do

- [ ] Delete or merge a page without asking.
- [ ] Set `as_of` to today on a page no new source confirmed.

## Scoring

Count the boxes. Any miss under "Must not do" is a failed run.
