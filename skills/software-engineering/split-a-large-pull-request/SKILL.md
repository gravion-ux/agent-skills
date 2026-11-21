---
name: split-a-large-pull-request
description: Split an oversized pull request into reviewable changes without losing behavior or history. Use when the user wants a pull request too large for review split into coherent units.
domain: software-engineering
tags: [pull-request, scope-control, reviewability]
triggers: ["split large pull request", "break oversized code review", "stack pull request into parts"]
---

# Split an oversized pull request into reviewable changes without losing behavior or history

## Purpose

Split an oversized pull request into reviewable changes without losing behavior or history.

## When to use

Use when the user wants a pull request too large for review split into coherent units.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map the pull request's commits and dependencies against the requested behavior.
2. Define ordered change groups with independent checks and clear boundaries.
3. Rebase or cherry-pick each group without dropping required shared code.
4. Run focused tests per group and the full suite on the final stack.
5. Publish a review sequence and document dependencies, rationale, and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `prepare-a-pull-request-for-review`
- `review-a-pull-request-as-a-pair`
- `revive-a-stale-pull-request`
