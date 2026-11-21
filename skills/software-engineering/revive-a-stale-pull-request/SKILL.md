---
name: revive-a-stale-pull-request
description: Revive a stale pull request by reconciling it with current code and re-proving its requested behavior. Use when the user wants an old pull request updated and reconsidered for review.
domain: software-engineering
tags: [stale-pr, integration, review]
triggers: ["revive stale pull request", "update old code contribution", "reopen outdated pull request"]
---

# Revive a stale pull request by reconciling it with current code and re-proving its requested behavior

## Purpose

Revive a stale pull request by reconciling it with current code and re-proving its requested behavior.

## When to use

Use when the user wants an old pull request updated and reconsidered for review.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inspect the original request, review feedback, current target branch, and recent changes.
2. Rebase or recreate the branch without discarding the contributor's intent.
3. Resolve conflicts, refresh tests, and remove behavior superseded elsewhere.
4. Run focused and existing checks and summarize the risk of reintroducing old code.
5. Request review again with the updated rationale and rollback path.

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
- `split-a-large-pull-request`
