---
name: bisect-a-regression-to-one-commit
description: Bisect a regression to the first bad commit with a repeatable failing check. Use when the user needs a known-good and known-bad revision narrowed to one commit.
domain: software-engineering
tags: [git-bisect, regression, automation]
triggers: ["bisect regression to one commit", "find first bad git commit", "narrow regression by history"]
---

# Bisect a regression to the first bad commit with a repeatable failing check

## Purpose

Bisect a regression to the first bad commit with a repeatable failing check.

## When to use

Use when the user needs a known-good and known-bad revision narrowed to one commit.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Confirm the failure on the bad revision and success on the known-good revision.
2. Choose an automated check that fails for the regression and passes on the good revision.
3. Select a binary-search strategy with a documented midpoint.
4. Run the check at each midpoint and record the tested revision range.
5. Verify the first bad commit and report the bisect log and rollback candidate.

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
- `make-a-script-safe-to-run-twice`
