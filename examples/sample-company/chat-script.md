# Chat script

Things the people at Tidewater say to the copilot. Paste each one into the
agent, in order, after the raw sources are ingested. Each tests the record
workflow (`workflows/record.md`). Say "without stopping" only where the
line says so.

The date in brackets is when the person said it in the story. The copilot
will save the note with today's real date; that's fine.

## 1. Account and owner update (story date 2026-11-10)

```text
Priya Nair (Senior PM, Mobile) here. Brightline HVAC cancelled last week. They moved to JobHarbor, mostly because of offline mode. They were in our beta, but they said JobHarbor had it for everyone first and their office manager was already trained on it. Also, Tom Becker left the company on Friday. Ana Lima owns billing now, including the reminders rollout.
```

## 2. Stopped feature, no decider (story date 2026-11-19)

```text
Dan Reyes (VP Product) here. We're stopping the Android tablet app. It's decided. Customers on it get moved to the phone app, which works on tablets anyway. Last release is in December.
```

When the copilot asks for missing fields, answer:

```text
I'll send who decided and why later. Record what you can.
```

## 3. A guess, not a fact (story date 2026-11-21)

```text
Priya here. My gut says about half our customers hit the offline problem at least once a week. I haven't checked that against anything.
```

## 4. A document request (story date 2026-11-21)

Use this one for write-document once it exists.

```text
Priya here. Write the offline mode results up as a weekly update for Dan.
```
