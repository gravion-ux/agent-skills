---
name: make-a-script-safe-to-run-twice
description: Make a script converge to the same safe state when it is run twice without deleting user data. Use when the user wants a maintenance script to be safe across accidental reruns.
domain: software-engineering
tags: [idempotent-scripts, automation, state-management]
triggers: ["make a script safe to rerun", "make a maintenance script idempotent"]
---

# Make a script converge to the same safe state when it is run twice without deleting user data

## Purpose

Make a script converge to the same safe state when it is run twice without deleting user data.

## When to use

Use when the user wants a maintenance script to be safe across accidental reruns.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the desired final state and the operations that reach it.
2. Detect existing state before changing anything.
3. Use atomic writes, stable markers, or narrow locks.
4. Make repeated execution stop when the goal is already met.
5. Test two consecutive runs against a temporary fixture.
6. Document idempotency, safety limits, and rollback.

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
- `bisect-a-regression-to-one-commit`
