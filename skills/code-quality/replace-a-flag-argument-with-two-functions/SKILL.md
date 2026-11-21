---
name: replace-a-flag-argument-with-two-functions
description: Replace a boolean flag with two named functions so each call path states its intent. Use when the user wants a boolean argument removed because it controls unrelated behavior.
domain: code-quality
tags: [api-design, boolean-flags, refactoring, code-quality]
triggers: ["remove boolean flag argument", "split flag argument functions", "boolean parameter refactor"]
---

# Replace a boolean flag with two named functions so each call path states its intent

## Purpose

Replace a boolean flag with two named functions so each call path states its intent.

## When to use

Use when the user wants a boolean argument removed because it controls unrelated behavior.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Identify the branches selected by the flag and their observable differences.
2. Create two public functions with names that describe those branches.
3. Move each branch into the function that owns it.
4. Update callers to choose the function that matches their intent.
5. Run tests for both paths and the formatter before review.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `remove-a-feature-flag-left-behind`
- `replace-magic-numbers-with-named-constants`
- `apply-a-formatter-consistently`
