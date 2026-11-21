---
name: explain-a-tradeoff-with-numbers
description: Explain a trade-off with the numbers that show what each option costs and saves. Use when the user needs to justify a technical trade-off with measurements rather than opinion.
domain: technical-writing
tags: [trade-off, numbers, analysis]
triggers: ["explain a tradeoff with numbers", "justify this tradeoff with data", "cost and benefit of this design choice"]
---

# Explain a trade-off with the numbers that show what each option costs and saves

## Purpose

Explain a trade-off with the numbers that show what each option costs and saves.

## When to use

Use when the user needs to justify a technical trade-off with measurements rather than opinion.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State the decision and the two sides of it.
2. Give the measured cost of each side, with the source and the date of the measurement.
3. State the assumptions each number depends on.
4. Show what happens to the result if the assumption is wrong.
5. Name the threshold at which the trade-off would reverse.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `explain-a-technical-concept-to-a-senior-reader`
- `convert-a-meeting-recording-into-a-document`
- `edit-a-document-for-clarity`
