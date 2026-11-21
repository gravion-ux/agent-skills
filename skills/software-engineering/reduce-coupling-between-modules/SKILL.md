---
name: reduce-coupling-between-modules
description: Replace direct module dependencies with a narrow interface that preserves existing behavior. Use when the user wants one code module to depend less on another.
domain: software-engineering
tags: [coupling, interfaces, modularization]
triggers: ["reduce module coupling", "introduce a narrow module interface"]
---

# Replace direct module dependencies with a narrow interface that preserves existing behavior

## Purpose

Replace direct module dependencies with a narrow interface that preserves existing behavior.

## When to use

Use when the user wants one code module to depend less on another.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map the dependency edges that create unwanted coupling.
2. Define the smallest interface needed by the caller.
3. Move shared behavior behind that interface.
4. Replace direct imports with the interface abstraction.
5. Add contract tests for both sides of the boundary.
6. Run the suite and document rationale and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `reduce-the-blame-of-a-failing-test-suite`
- `split-a-monolith-into-modules`
- `add-structured-logging-to-a-code-path`
