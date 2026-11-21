---
name: profile-a-slow-function
description: Identify the dominant runtime cost in a slow function and validate a focused optimization with benchmarks. Use when the user wants to find why a repository function is slow.
domain: software-engineering
tags: [profiling, performance, benchmarks]
triggers: ["profile a slow function", "cpu profile a hot function"]
---

# Identify the dominant runtime cost in a slow function and validate a focused optimization with benchmarks

## Purpose

Identify the dominant runtime cost in a slow function and validate a focused optimization with benchmarks.

## When to use

Use when the user wants to find why a repository function is slow.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the slow path with a representative workload.
2. Capture CPU profiler samples around the hot call.
3. Rank functions by self time and allocation cost.
4. Form one hypothesis about the dominant cost.
5. Apply the smallest optimization within the requested scope.
6. Compare benchmarks, run tests, and record rationale and rollback.

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
- `refactor-a-long-function`
- `speed-up-a-slow-build`
