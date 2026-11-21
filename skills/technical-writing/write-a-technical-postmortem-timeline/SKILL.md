---
name: write-a-technical-postmortem-timeline
description: Write an incident timeline where every entry is timed and traceable to a source. Use when the user needs the chronological record for an incident review.
domain: technical-writing
tags: [timeline, incident, evidence]
triggers: ["write a technical postmortem timeline", "chronological record of our outage", "incident event timeline with times"]
---

# Write an incident timeline where every entry is timed and traceable to a source

## Purpose

Write an incident timeline where every entry is timed and traceable to a source.

## When to use

Use when the user needs the chronological record for an incident review.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Fix the reference time and state the time zone at the top of the timeline.
2. Record the first symptom as the start, not the moment it was noticed.
3. Add each detection, escalation and action with its exact time.
4. Note the source of each entry, such as a log, a message or a person.
5. Mark the intervals that are unexplained rather than leaving them blank.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-postmortem`
- `write-a-technical-abstract`
- `write-a-technical-proposal`
