---
name: write-an-engineering-design-doc
description: Write an engineering design document that covers the context, the shape and the trade-offs. Use when the user needs to document how a system or feature should be built.
domain: technical-writing
tags: [design-doc, architecture, engineering]
triggers: ["write an engineering design doc", "document how this feature should be built", "design document for a system change"]
---

# Write an engineering design document that covers the context, the shape and the trade-offs

## Purpose

Write an engineering design document that covers the context, the shape and the trade-offs.

## When to use

Use when the user needs to document how a system or feature should be built.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Write the context and the problem in a form a new joiner could follow.
2. State the goals and the non-goals so the scope cannot drift.
3. Describe the design at the level of the components and the data that flows between them.
4. List the alternatives that were rejected and why.
5. Name the risks, the open questions and the testing strategy.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-an-api-design-document`
- `write-a-runbook-for-an-operational-task`
- `write-an-architecture-decision-record-for-a-reviewer`
