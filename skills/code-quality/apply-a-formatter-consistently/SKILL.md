---
name: apply-a-formatter-consistently
description: Apply the repository formatter consistently and keep the resulting diff behavior-neutral. Use when the user wants formatting normalized across files without changing behavior.
domain: code-quality
tags: [formatting, automation, style-consistency, code-quality]
triggers: ["apply code formatter", "format files consistently", "repository formatting pass"]
---

# Apply the repository formatter consistently and keep the resulting diff behavior-neutral

## Purpose

Apply the repository formatter consistently and keep the resulting diff behavior-neutral.

## When to use

Use when the user wants formatting normalized across files without changing behavior.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Identify the configured formatter, version, and supported file scope.
2. Run the formatter on only the files in the requested change.
3. Inspect the diff and revert any formatter version churn outside the scope.
4. Run the linter and focused tests after formatting.
5. Report the formatter command and the number of files changed.

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
- `enable-strict-mode-on-a-module`
- `improve-a-codebase-readme`
