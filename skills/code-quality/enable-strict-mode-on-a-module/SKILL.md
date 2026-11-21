---
name: enable-strict-mode-on-a-module
description: Enable strict type checking for one module and resolve its errors in focused changes. Use when the user wants strict type checking enabled for a single module.
domain: code-quality
tags: [strict-types, type-checking, static-analysis, code-quality]
triggers: ["enable strict type checking", "strict mode for module", "module type check hardening"]
---

# Enable strict type checking for one module and resolve its errors in focused changes

## Purpose

Enable strict type checking for one module and resolve its errors in focused changes.

## When to use

Use when the user wants strict type checking enabled for a single module.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Enable the configured strict checker options for the target module only.
2. Run the type checker and capture the complete error list.
3. Resolve errors with narrow annotations or behavior-preserving code changes.
4. Keep unrelated modules unchanged and document every error suppression.
5. Run focused tests and the formatter, then report remaining checker findings.

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
- `improve-a-codebase-readme`
