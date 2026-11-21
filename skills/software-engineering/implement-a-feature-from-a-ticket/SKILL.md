---
name: implement-a-feature-from-a-ticket
description: Implement a ticket end to end with a focused change, regression test, rationale, and rollback note. Use when the user wants a repository change delivered from an agreed ticket.
domain: software-engineering
tags: [feature-implementation, ticket-work, testing]
triggers: ["implement feature from ticket", "build ticket in codebase", "deliver repository ticket"]
---

# Implement a ticket end to end with a focused change, regression test, rationale, and rollback note

## Purpose

Implement a ticket end to end with a focused change, regression test, rationale, and rollback note.

## When to use

Use when the user wants a repository change delivered from an agreed ticket.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Read the ticket and record its acceptance criteria, constraints, and out-of-scope items.
2. Trace the relevant code and existing tests before choosing the smallest change.
3. Add an automated test that fails for the missing behavior.
4. Implement only the behavior required by the ticket and keep the diff focused.
5. Run the new test and the existing suite, then record the rationale and rollback path.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `handle-merge-conflicts-in-a-feature-branch`
- `introduce-a-feature-flag`
- `raise-useful-errors-from-a-library`
