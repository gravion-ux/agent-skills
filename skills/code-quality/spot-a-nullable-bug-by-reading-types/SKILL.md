---
name: spot-a-nullable-bug-by-reading-types
description: Locate a nullable dereference bug by following declared types and ownership boundaries. Use when the user suspects a null dereference or missing-value bug in typed code.
domain: code-quality
tags: [null-safety, static-types, bug-detection, code-quality]
triggers: ["nullable type bug", "read types to spot null bug", "nullable dereference review"]
---

# Locate a nullable dereference bug by following declared types and ownership boundaries

## Purpose

Locate a nullable dereference bug by following declared types and ownership boundaries.

## When to use

Use when the user suspects a null dereference or missing-value bug in typed code.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Trace each nullable value from its source to the dereference site.
2. Check every guard, assertion, and ownership transfer along that path.
3. Write a minimal failing test that captures the missing-value case.
4. Apply the narrowest null-safety fix without refactoring nearby code.
5. Run the focused test suite and the configured type checker.

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
