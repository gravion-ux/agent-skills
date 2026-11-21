---
name: make-error-messages-actionable
description: Rewrite error messages to state the failed operation, relevant context, and next action. Use when the user wants unclear exception or validation messages made easier to act on.
domain: code-quality
tags: [error-messages, validation, diagnostics, code-quality]
triggers: ["actionable error messages", "improve exception message", "clearer validation errors"]
---

# Rewrite error messages to state the failed operation, relevant context, and next action

## Purpose

Rewrite error messages to state the failed operation, relevant context, and next action.

## When to use

Use when the user wants unclear exception or validation messages made easier to act on.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Collect the current messages and the conditions that trigger them.
2. Include the failed operation, key input, and expected constraint.
3. State a safe next action without exposing secrets or internals.
4. Update message assertions and error-path tests.
5. Run the focused tests and review every changed message for clarity.

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
- `apply-a-formatter-consistently`
- `audit-a-file-for-hidden-side-effects`
