---
name: refactor-for-testability
description: Refactor code for testability by injecting dependencies without changing observable behavior. Use when the user wants difficult code refactored so its behavior can be tested reliably.
domain: code-quality
tags: [testability, dependency-injection, testing, code-quality]
triggers: ["refactor for testability", "make code easier to test", "inject dependencies for tests"]
---

# Refactor code for testability by injecting dependencies without changing observable behavior

## Purpose

Refactor code for testability by injecting dependencies without changing observable behavior.

## When to use

Use when the user wants difficult code refactored so its behavior can be tested reliably.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Identify external clocks networks files and randomness that block deterministic tests.
2. Define explicit dependency seams around those effects.
3. Inject the dependencies while preserving the public contract and side effects.
4. Add focused tests for the previously untestable branches.
5. Run the suite and compare behavior with the pre-refactor implementation.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `audit-a-file-for-hidden-side-effects`
- `review-a-diff-for-correctness`
- `review-a-pr-for-scope-discipline`
