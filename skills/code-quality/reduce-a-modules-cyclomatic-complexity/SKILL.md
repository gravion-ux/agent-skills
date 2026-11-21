---
name: reduce-a-modules-cyclomatic-complexity
description: Reduce module complexity by extracting cohesive decisions and preserving every existing branch. Use when the user wants a module with high cyclomatic complexity made easier to reason about.
domain: code-quality
tags: [complexity, metrics, refactoring, code-quality]
triggers: ["reduce cyclomatic complexity", "lower module complexity", "complexity metric refactor"]
---

# Reduce module complexity by extracting cohesive decisions and preserving every existing branch

## Purpose

Reduce module complexity by extracting cohesive decisions and preserving every existing branch.

## When to use

Use when the user wants a module with high cyclomatic complexity made easier to reason about.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Measure cyclomatic complexity per function with the configured tool.
2. Identify branches that combine independent decisions or domain rules.
3. Extract cohesive helpers without changing return values or side effects.
4. Add focused tests for the newly separated decision paths.
5. Compare complexity and diff size, then run the linter and formatter.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `apply-a-formatter-consistently`
- `audit-a-file-for-hidden-side-effects`
- `enable-strict-mode-on-a-module`
