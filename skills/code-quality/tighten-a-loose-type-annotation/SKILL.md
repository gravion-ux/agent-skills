---
name: tighten-a-loose-type-annotation
description: Tighten a loose annotation to reflect proven constraints without narrowing valid inputs. Use when the user wants an any-like or overly broad annotation replaced precisely.
domain: code-quality
tags: [type-accuracy, static-types, type-annotations, code-quality]
triggers: ["tighten loose type", "precise type annotation", "broad any type cleanup"]
---

# Tighten a loose annotation to reflect proven constraints without narrowing valid inputs

## Purpose

Tighten a loose annotation to reflect proven constraints without narrowing valid inputs.

## When to use

Use when the user wants an any-like or overly broad annotation replaced precisely.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Find every caller and the actual runtime values passed to the symbol.
2. Define the narrowest type that covers all valid observed inputs.
3. Replace the loose annotation and update affected declarations.
4. Run the type checker plus focused tests to expose unsound assumptions.
5. Keep broader compatibility types where callers still rely on them.

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
