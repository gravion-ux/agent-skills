---
name: write-a-runbook-for-an-operational-task
description: Write a runbook that lets someone carry out an operational task under pressure. Use when the user wants a runbook for a recurring or risky operational task.
domain: technical-writing
tags: [runbook, operations, procedure]
triggers: ["write a runbook for an operational task", "procedure for handling this production task", "step by step ops runbook"]
---

# Write a runbook that lets someone carry out an operational task under pressure

## Purpose

Write a runbook that lets someone carry out an operational task under pressure.

## When to use

Use when the user wants a runbook for a recurring or risky operational task.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State the trigger, so the reader knows when to open the runbook.
2. List the preconditions, including the access and the permissions needed.
3. Give the commands or steps in order, with the expected output at each one.
4. Mark the step where the operator must confirm before continuing.
5. Add what to do when the expected output does not appear, for each likely failure.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-an-architecture-decision-record-for-a-reviewer`
- `write-a-migration-plan-for-users`
- `write-a-technical-tutorial-for-developers`
