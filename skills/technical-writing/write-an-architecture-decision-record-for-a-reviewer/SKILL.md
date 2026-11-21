---
name: write-an-architecture-decision-record-for-a-reviewer
description: Write an ADR that captures the decision, its context and its consequences for good. Use when the user wants to record a significant technical decision.
domain: technical-writing
tags: [adr, decision, architecture]
triggers: ["write an architecture decision record", "record why we chose this approach", "adr for a technical decision"]
---

# Write an ADR that captures the decision, its context and its consequences for good

## Purpose

Write an ADR that captures the decision, its context and its consequences for good.

## When to use

Use when the user wants to record a significant technical decision.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Give the record a short title and a number, and state the status and the date.
2. Write the context, including the forces that made a decision necessary.
3. State the decision in the active voice, as one chosen option.
4. List the consequences, including the ones that are not wanted.
5. Record the alternatives considered and why each was not chosen.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-runbook-for-an-operational-task`
- `write-a-migration-plan-for-users`
- `write-a-technical-tutorial-for-developers`
