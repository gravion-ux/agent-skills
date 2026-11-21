---
name: write-a-postmortem
description: Write a postmortem that explains what happened and what changes, without assigning blame. Use when the user wants to document an incident so the same failure is less likely to repeat.
domain: technical-writing
tags: [postmortem, incident, review]
triggers: ["write a postmortem", "write a blameless incident review", "document what went wrong in our outage"]
---

# Write a postmortem that explains what happened and what changes, without assigning blame

## Purpose

Write a postmortem that explains what happened and what changes, without assigning blame.

## When to use

Use when the user wants to document an incident so the same failure is less likely to repeat.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State the impact in measurable terms, starting with what users experienced.
2. Give the timeline of the events with the times in one time zone.
3. Explain the contributing conditions, including the decisions that were reasonable at the time.
4. List the actions, each with an owner, a priority and a date.
5. Publish it in a way that people can read without fear of being blamed.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-technical-postmortem-timeline`
- `write-a-benchmark-report`
- `write-a-comparison-of-two-approaches`
