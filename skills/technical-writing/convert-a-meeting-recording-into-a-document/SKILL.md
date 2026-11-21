---
name: convert-a-meeting-recording-into-a-document
description: Convert a meeting recording into a document that records the decisions and the actions. Use when the user has a recording or transcript and wants a usable written record.
domain: technical-writing
tags: [transcript, minutes, conversion]
triggers: ["convert a meeting recording into a document", "write the minutes from a recording", "turn this transcript into notes"]
---

# Convert a meeting recording into a document that records the decisions and the actions

## Purpose

Convert a meeting recording into a document that records the decisions and the actions.

## When to use

Use when the user has a recording or transcript and wants a usable written record.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Remove the filler, the interruptions and the small talk from the transcript.
2. Group what was said into the topics discussed, in the order they came up.
3. Extract the decisions, the actions, the owners and the dates.
4. Mark the points that were discussed but not decided, so they are not lost.
5. Check the result against the recording before sending it to the attendees.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `edit-a-document-for-clarity`
- `review-a-technical-document-for-accuracy`
- `structure-a-long-document`
