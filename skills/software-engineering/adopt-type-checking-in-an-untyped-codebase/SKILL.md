---
name: adopt-type-checking-in-an-untyped-codebase
description: Introduce incremental static type checking that catches boundary mistakes without blocking unrelated work. Use when the user wants to add type safety to an untyped codebase.
domain: software-engineering
tags: [type-checking, static-analysis, typing]
triggers: ["adopt static type checking", "type an untyped codebase incrementally"]
---

# Introduce incremental static type checking that catches boundary mistakes without blocking unrelated work

## Purpose

Introduce incremental static type checking that catches boundary mistakes without blocking unrelated work.

## When to use

Use when the user wants to add type safety to an untyped codebase.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Choose a checker and a baseline configuration for the repository.
2. Type public interfaces and error-prone boundaries first.
3. Fix existing annotation errors without changing runtime behavior.
4. Exclude legacy areas with narrow, documented boundaries.
5. Add a type-check command to continuous integration.
6. Run tests and record migration guidance and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `work-in-a-legacy-codebase-without-tests`
- `fix-an-off-by-one-error`
- `handle-merge-conflicts-in-a-feature-branch`
