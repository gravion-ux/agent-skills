---
name: replace-magic-numbers-with-named-constants
description: Replace unexplained numeric literals with named constants that reveal their domain meaning. Use when the user wants unexplained numeric literals replaced with readable named constants.
domain: code-quality
tags: [constants, readability, maintainability, code-quality]
triggers: ["replace magic numbers", "named numeric constants", "extract numeric literals"]
---

# Replace unexplained numeric literals with named constants that reveal their domain meaning

## Purpose

Replace unexplained numeric literals with named constants that reveal their domain meaning.

## When to use

Use when the user wants unexplained numeric literals replaced with readable named constants.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Locate each meaningful numeric literal and its surrounding business rule.
2. Group related values and define a descriptive constant near their owner.
3. Replace the literals with constants without changing their types or values.
4. Add boundary tests for thresholds and limits where behavior matters.
5. Run the focused suite and the formatter before reviewing the diff.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `replace-a-flag-argument-with-two-functions`
- `enforce-coding-standards-with-tooling`
- `add-typing-to-an-untyped-function`
