---
name: configure-formatting-and-linting-for-a-repo
description: Configure repository formatting and linting with reproducible rules and a staged adoption path. Use when the user wants consistent formatting and static lint checks enforced in a codebase.
domain: software-engineering
tags: [linting, formatting, static-analysis]
triggers: ["configure repo formatting linting", "enforce consistent code style", "add formatter and linter checks"]
---

# Configure repository formatting and linting with reproducible rules and a staged adoption path

## Purpose

Configure repository formatting and linting with reproducible rules and a staged adoption path.

## When to use

Use when the user wants consistent formatting and static lint checks enforced in a codebase.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inspect existing style conventions, tooling, and CI commands.
2. Choose one formatter and linter configuration matching repository conventions.
3. Apply rules to a small representative subset before the full tree.
4. Add a single check command and document any temporary exceptions.
5. Run the linter, formatter check, and existing tests before enabling enforcement.

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
- `design-a-retry-and-backoff-policy`
- `prepare-a-pull-request-for-review`
