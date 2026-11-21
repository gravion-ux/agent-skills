---
name: simplify-a-complex-condition
description: Simplify a complex condition with equivalent logic, named predicates, and unchanged branch behavior. Use when the user wants a deeply nested or compound condition made easier to verify.
domain: code-quality
tags: [complexity, conditions, readability, code-quality]
triggers: ["complex condition simplification", "simplify nested condition", "condition readability refactor"]
---

# Simplify a complex condition with equivalent logic, named predicates, and unchanged branch behavior

## Purpose

Simplify a complex condition with equivalent logic, named predicates, and unchanged branch behavior.

## When to use

Use when the user wants a deeply nested or compound condition made easier to verify.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Record the current truth table for the condition and its edge cases.
2. Extract named predicates for each independent business rule.
3. Replace the nested condition with the simplest equivalent expression.
4. Prove equivalence with focused boundary-case tests.
5. Run the linter and review the diff for unrelated changes.

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
