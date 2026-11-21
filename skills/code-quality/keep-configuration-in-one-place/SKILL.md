---
name: keep-configuration-in-one-place
description: Consolidate scattered configuration into one typed source with documented defaults. Use when the user wants configuration values scattered across a codebase brought together.
domain: code-quality
tags: [configuration, centralization, typed-config, code-quality]
triggers: ["centralize configuration", "one configuration source", "collect scattered config"]
---

# Consolidate scattered configuration into one typed source with documented defaults

## Purpose

Consolidate scattered configuration into one typed source with documented defaults.

## When to use

Use when the user wants configuration values scattered across a codebase brought together.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Inventory each configuration key, source, default, and consuming code path.
2. Choose one configuration owner and define the supported key set.
3. Move scattered values without changing their effective values.
4. Replace direct reads with the shared typed configuration accessor.
5. Run configuration tests plus the linter and formatter.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `keep-functions-short-and-focused`
- `add-typing-to-an-untyped-function`
- `apply-a-formatter-consistently`
