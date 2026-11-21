---
name: name-things-well
description: Rename misleading identifiers so their names state purpose, scope, and ownership clearly. Use when the user wants variables functions or types renamed for clearer intent.
domain: code-quality
tags: [naming, readability, maintainability, code-quality]
triggers: ["better code names", "rename unclear identifiers", "identifier naming review"]
---

# Rename misleading identifiers so their names state purpose, scope, and ownership clearly

## Purpose

Rename misleading identifiers so their names state purpose, scope, and ownership clearly.

## When to use

Use when the user wants variables functions or types renamed for clearer intent.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. List each misleading identifier with its current and intended meaning.
2. Search every declaration and reference to map the rename safely.
3. Choose names that reveal type and ownership without abbreviating meaning.
4. Apply the rename without changing surrounding behavior.
5. Run tests and the linter, then document each semantic change.

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
