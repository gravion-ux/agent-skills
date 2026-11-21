---
name: remove-a-hot-path-allocation
description: Remove repeated allocations from a hot path without changing observable behavior or ownership semantics. Use when the user wants to lower allocation pressure in a frequently executed path.
domain: software-engineering
tags: [allocations, hot-path, latency]
triggers: ["remove hot path allocations", "optimize repeated object allocation"]
---

# Remove repeated allocations from a hot path without changing observable behavior or ownership semantics

## Purpose

Remove repeated allocations from a hot path without changing observable behavior or ownership semantics.

## When to use

Use when the user wants to lower allocation pressure in a frequently executed path.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Measure allocation counts under a stable benchmark workload.
2. Locate allocations that dominate the hot path.
3. Choose a reuse or pooling strategy that preserves object lifetimes.
4. Implement the allocation reduction in the narrowest scope.
5. Check correctness for shared and aliased values.
6. Compare allocation and latency results, run tests, and document rollback.

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
- `remove-a-dependency-safely`
- `apply-solid-principles-to-a-class`
