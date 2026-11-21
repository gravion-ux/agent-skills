---
name: fix-a-memory-leak
description: Trace retained memory to its owning reference and add a regression test for the leak. Use when the user reports steadily growing memory during repeated execution.
domain: software-engineering
tags: [memory-leaks, heap-analysis, regression]
triggers: ["trace a memory leak", "find retained heap memory"]
---

# Trace retained memory to its owning reference and add a regression test for the leak

## Purpose

Trace retained memory to its owning reference and add a regression test for the leak.

## When to use

Use when the user reports steadily growing memory during repeated execution.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the growth under a bounded repeated workload.
2. Compare heap snapshots before and after a fixed interval.
3. Trace retained objects to their owning references.
4. Fix ownership or release semantics without deleting user data.
5. Add a soak regression test that detects renewed growth.
6. Run the full suite and document rationale and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `cut-a-release-branch-and-backport-a-fix`
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
