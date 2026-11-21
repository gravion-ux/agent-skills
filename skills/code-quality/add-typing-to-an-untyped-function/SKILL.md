---
name: add-typing-to-an-untyped-function
description: Add precise type annotations to an untyped function without altering its runtime behavior. Use when the user wants type annotations added to a public or error-prone function.
domain: code-quality
tags: [type-annotations, static-types, code-quality, typing]
triggers: ["add types to function", "annotate untyped function", "function typing pass"]
---

# Add precise type annotations to an untyped function without altering its runtime behavior

## Purpose

Add precise type annotations to an untyped function without altering its runtime behavior.

## When to use

Use when the user wants type annotations added to a public or error-prone function.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Record the function parameters return values and side effects.
2. Add annotations that express the accepted inputs and promised outputs.
3. Annotate only the requested function and its immediate types.
4. Run the type checker and focused tests to detect mismatch.
5. Format the file and explain any types that remain uncertain.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `remove-an-unsafe-cast`
- `apply-a-formatter-consistently`
- `audit-a-file-for-hidden-side-effects`
