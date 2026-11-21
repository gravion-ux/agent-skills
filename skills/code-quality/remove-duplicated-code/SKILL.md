---
name: remove-duplicated-code
description: Remove duplicated code by extracting one focused implementation and preserving every caller contract. Use when the user wants repeated code consolidated into a smaller maintainable implementation.
domain: code-quality
tags: [duplication, refactoring, abstraction, code-quality]
triggers: ["duplicate code removal", "extract duplicated code", "consolidate repeated code"]
---

# Remove duplicated code by extracting one focused implementation and preserving every caller contract

## Purpose

Remove duplicated code by extracting one focused implementation and preserving every caller contract.

## When to use

Use when the user wants repeated code consolidated into a smaller maintainable implementation.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Compare the duplicate blocks and confirm their behavior is genuinely equivalent.
2. Choose the smallest shared abstraction that covers all variants.
3. Replace the duplicated blocks with calls to that abstraction.
4. Run tests for every original call path.
5. Run the formatter and explain the resulting diff size reduction.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `remove-dead-dependencies-and-code`
- `detect-and-remove-duplicate-utility-functions`
- `remove-a-feature-flag-left-behind`
