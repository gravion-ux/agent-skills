---
name: remove-an-unsafe-cast
description: Remove an unsafe cast by validating the value or replacing it with a sound type. Use when the user wants an unsafe type cast replaced with a provably safe alternative.
domain: code-quality
tags: [type-safety, casts, static-types, code-quality]
triggers: ["remove unsafe cast", "replace unsafe type cast", "cast safety cleanup"]
---

# Remove an unsafe cast by validating the value or replacing it with a sound type

## Purpose

Remove an unsafe cast by validating the value or replacing it with a sound type.

## When to use

Use when the user wants an unsafe type cast replaced with a provably safe alternative.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Locate the cast and identify every possible runtime type at that point.
2. Add an explicit check for the type the code actually requires.
3. Replace the cast with the validated value or a sound abstraction.
4. Delete any stale suppression attached to the cast.
5. Run the type checker and tests that exercise invalid input paths.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `add-typing-to-an-untyped-function`
- `detect-and-remove-duplicate-utility-functions`
- `remove-a-feature-flag-left-behind`
