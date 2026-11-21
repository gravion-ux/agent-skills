---
name: keep-functions-short-and-focused
description: Split a long function into focused units while preserving its public behavior and callers. Use when the user wants an oversized function divided into smaller single-purpose units.
domain: code-quality
tags: [function-size, refactoring, cohesion, code-quality]
triggers: ["split a long function", "short focused functions", "function length refactor"]
---

# Split a long function into focused units while preserving its public behavior and callers

## Purpose

Split a long function into focused units while preserving its public behavior and callers.

## When to use

Use when the user wants an oversized function divided into smaller single-purpose units.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Map the function inputs outputs side effects and internal branches.
2. Group statements into cohesive units with one responsibility each.
3. Extract units without changing parameter order or error behavior.
4. Add or retain tests that cover each extracted unit.
5. Run the focused suite and compare the diff against the added complexity.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `detect-and-remove-duplicate-utility-functions`
- `keep-configuration-in-one-place`
- `remove-dead-dependencies-and-code`
