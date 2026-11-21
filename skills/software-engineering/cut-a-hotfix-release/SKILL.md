---
name: cut-a-hotfix-release
description: Cut a hotfix that resolves a critical defect with a focused diff, regression test, and rollback path. Use when the user needs a critical production defect fixed for immediate release.
domain: software-engineering
tags: [hotfixes, production-defects, regression-testing]
triggers: ["cut a production hotfix", "release a critical defect patch"]
---

# Cut a hotfix that resolves a critical defect with a focused diff, regression test, and rollback path

## Purpose

Cut a hotfix that resolves a critical defect with a focused diff, regression test, and rollback path.

## When to use

Use when the user needs a critical production defect fixed for immediate release.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the defect and identify the smallest safe fix.
2. Branch from the intended production release baseline.
3. Add a regression test that fails before the fix.
4. Apply the focused change without weakening existing tests.
5. Run targeted and full checks before packaging.
6. Publish the patch and document release and rollback steps.

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
- `tag-and-release-a-version`
- `add-structured-logging-to-a-code-path`
