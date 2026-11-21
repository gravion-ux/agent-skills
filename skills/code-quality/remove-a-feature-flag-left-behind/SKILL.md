---
name: remove-a-feature-flag-left-behind
description: Remove a retired feature flag after confirming every branch and configuration key is dead. Use when the user wants a feature flag deleted after its rollout has finished.
domain: code-quality
tags: [feature-flags, cleanup, rollout, code-quality]
triggers: ["remove retired feature flag", "delete stale flag branch", "feature flag cleanup"]
---

# Remove a retired feature flag after confirming every branch and configuration key is dead

## Purpose

Remove a retired feature flag after confirming every branch and configuration key is dead.

## When to use

Use when the user wants a feature flag deleted after its rollout has finished.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Find every flag read, branch, default, and dashboard configuration reference.
2. Confirm the enabled and disabled behavior is now the intended behavior.
3. Delete the flag branches while preserving the active production path.
4. Remove the configuration key and update tests for the settled behavior.
5. Run the full affected suite and explain the rollout evidence.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `remove-a-temporary-workaround`
- `replace-a-flag-argument-with-two-functions`
- `apply-a-formatter-consistently`
