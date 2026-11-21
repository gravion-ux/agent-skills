---
name: eliminate-a-race-condition
description: Make concurrent execution deterministic by identifying shared state and enforcing one ownership rule. Use when the user sees intermittent failures only under concurrent execution.
domain: software-engineering
tags: [concurrency, race-conditions, synchronization]
triggers: ["fix a race condition", "debug concurrent shared state"]
---

# Make concurrent execution deterministic by identifying shared state and enforcing one ownership rule

## Purpose

Make concurrent execution deterministic by identifying shared state and enforcing one ownership rule.

## When to use

Use when the user sees intermittent failures only under concurrent execution.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Build a deterministic reproducer that exercises overlapping operations.
2. Identify the shared state crossed by both execution paths.
3. Define one ownership or synchronization rule for that state.
4. Implement the narrowest race-free change.
5. Stress the reproducer across repeated concurrent runs.
6. Run existing tests and document rationale and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
- `automate-a-repetitive-code-change`
