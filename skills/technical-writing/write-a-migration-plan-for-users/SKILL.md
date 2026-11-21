---
name: write-a-migration-plan-for-users
description: Write a migration plan that tells existing users what changes and what they must do. Use when the user is changing something that existing users will have to deal with.
domain: technical-writing
tags: [migration, users, communication]
triggers: ["write a migration plan for users", "tell customers about a breaking change", "user facing migration guide"]
---

# Write a migration plan that tells existing users what changes and what they must do

## Purpose

Write a migration plan that tells existing users what changes and what they must do.

## When to use

Use when the user is changing something that existing users will have to deal with.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State what is changing and what stays the same, in plain terms.
2. Give the date the change happens and the date the old behaviour is removed.
3. Write the steps each user must take, in the order they take them.
4. Explain how to tell whether they have completed the migration.
5. Give the support route for the users who get stuck, and keep the old path working until then.

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
- `write-a-technical-tutorial-for-developers`
- `write-an-architecture-decision-record-for-a-reviewer`
