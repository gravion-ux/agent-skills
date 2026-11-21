---
name: enforce-coding-standards-with-tooling
description: Enforce coding standards automatically with configured linters formatters and focused CI checks. Use when the user wants coding standards enforced automatically instead of through review reminders.
domain: code-quality
tags: [linting, automation, ci-checks, code-quality]
triggers: ["enforce code standards", "automated lint checks", "coding standard enforcement"]
---

# Enforce coding standards automatically with configured linters formatters and focused CI checks

## Purpose

Enforce coding standards automatically with configured linters formatters and focused CI checks.

## When to use

Use when the user wants coding standards enforced automatically instead of through review reminders.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Read the repository's existing lint and formatter configuration.
2. Select rules that match the local standard without changing unrelated code.
3. Configure the chosen linter and formatter on the target paths.
4. Add a CI command that fails on the new violations with a local reproduction command.
5. Run the formatter and linter, then confirm the CI check passes.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `replace-a-flag-argument-with-two-functions`
- `replace-magic-numbers-with-named-constants`
- `add-typing-to-an-untyped-function`
