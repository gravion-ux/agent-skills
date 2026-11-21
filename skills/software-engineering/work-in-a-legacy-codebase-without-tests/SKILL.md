---
name: work-in-a-legacy-codebase-without-tests
description: Work safely in untested legacy code by capturing current behavior before changing it. Use when the user needs a change in legacy code that lacks reliable automated tests.
domain: software-engineering
tags: [legacy-code, characterization, regression]
triggers: ["work in legacy code without tests", "change untested legacy module", "capture behavior before refactor"]
---

# Work safely in untested legacy code by capturing current behavior before changing it

## Purpose

Work safely in untested legacy code by capturing current behavior before changing it.

## When to use

Use when the user needs a change in legacy code that lacks reliable automated tests.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map the legacy entry points, callers, side effects, and current runtime behavior.
2. Create a characterization test or manual golden-output check around the target.
3. Make the smallest compatible change and compare old and new observable results.
4. Run available checks and expand coverage only for the modified behavior.
5. Document the evidence, remaining gaps, rationale, and rollback revision.

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
- `handle-merge-conflicts-in-a-feature-branch`
- `rename-a-symbol-across-the-codebase`
