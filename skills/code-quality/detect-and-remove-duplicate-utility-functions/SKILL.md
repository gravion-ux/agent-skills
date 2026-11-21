---
name: detect-and-remove-duplicate-utility-functions
description: Detect duplicate utility functions and consolidate them into one tested shared helper. Use when the user wants overlapping helper functions found and merged safely.
domain: code-quality
tags: [utilities, duplication, helpers, code-quality]
triggers: ["duplicate utility functions", "merge overlapping helpers", "find redundant helpers"]
---

# Detect duplicate utility functions and consolidate them into one tested shared helper

## Purpose

Detect duplicate utility functions and consolidate them into one tested shared helper.

## When to use

Use when the user wants overlapping helper functions found and merged safely.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Search by purpose and signature for helpers that overlap across modules.
2. Compare inputs outputs errors and side effects before selecting a canonical helper.
3. Move the canonical implementation to an appropriate shared owner.
4. Replace every duplicate call and delete the redundant helpers.
5. Run tests for all former call sites and check the formatter.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `keep-functions-short-and-focused`
- `remove-dead-dependencies-and-code`
- `remove-a-feature-flag-left-behind`
