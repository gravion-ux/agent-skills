---
name: refactor-a-long-function
description: Refactor a long function into named units without changing behavior or widening the change. Use when the user wants an existing function simplified while its behavior stays compatible.
domain: software-engineering
tags: [refactoring, function-design, regression-safety]
triggers: ["refactor long function", "break up oversized function", "simplify procedural function"]
---

# Refactor a long function into named units without changing behavior or widening the change

## Purpose

Refactor a long function into named units without changing behavior or widening the change.

## When to use

Use when the user wants an existing function simplified while its behavior stays compatible.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Record current inputs, outputs, side effects, and test coverage.
2. Identify cohesive steps and sketch smaller function boundaries.
3. Move one cohesive unit at a time while preserving public behavior.
4. Run focused and existing regression tests after each move.
5. Review the diff for scope, document the rationale, and note how to revert it.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `deprecate-a-public-function`
- `profile-a-slow-function`
- `add-structured-logging-to-a-code-path`
