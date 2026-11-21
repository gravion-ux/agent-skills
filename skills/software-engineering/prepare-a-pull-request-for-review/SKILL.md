---
name: prepare-a-pull-request-for-review
description: Prepare a pull request for review with a scoped diff, verified checks, rationale, and rollback note. Use when the user wants a completed repository change made ready for reviewer approval.
domain: software-engineering
tags: [pull-request, review, release-readiness]
triggers: ["prepare pull request for review", "make code change review ready", "package diff for reviewer approval"]
---

# Prepare a pull request for review with a scoped diff, verified checks, rationale, and rollback note

## Purpose

Prepare a pull request for review with a scoped diff, verified checks, rationale, and rollback note.

## When to use

Use when the user wants a completed repository change made ready for reviewer approval.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Re-read the ticket and remove unrelated edits from the working diff.
2. Run the focused regression test, existing suite, and configured lint or build checks.
3. Review the diff for debug code, credentials, migrations, and compatibility risks.
4. Write a concise title, rationale, test evidence, and rollback instructions.
5. Open the pull request only after confirming the target branch and reviewers.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `review-a-pull-request-as-a-pair`
- `prepare-code-for-a-code-freeze`
- `revive-a-stale-pull-request`
