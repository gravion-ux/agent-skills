---
name: fix-an-off-by-one-error
description: Fix an off-by-one boundary defect with a regression test for both adjacent valid values. Use when the user wants an inclusive or exclusive range boundary corrected.
domain: software-engineering
tags: [off-by-one, boundary, regression]
triggers: ["fix off by one error", "correct range boundary bug", "repair inclusive exclusive limit"]
---

# Fix an off-by-one boundary defect with a regression test for both adjacent valid values

## Purpose

Fix an off-by-one boundary defect with a regression test for both adjacent valid values.

## When to use

Use when the user wants an inclusive or exclusive range boundary corrected.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the boundary failure with the smallest valid example.
2. Trace the index, limit, slice, or range calculation that sets the boundary.
3. Add a regression test covering the last included and first excluded values.
4. Correct the calculation without broadening unrelated behavior.
5. Run focused and existing tests and document the fix and rollback path.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `adopt-type-checking-in-an-untyped-codebase`
- `bisect-a-regression-to-one-commit`
- `cut-a-release-branch-and-backport-a-fix`
