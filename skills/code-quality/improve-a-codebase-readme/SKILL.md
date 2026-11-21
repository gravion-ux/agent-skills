---
name: improve-a-codebase-readme
description: Improve a codebase README with verified setup usage architecture and maintenance guidance. Use when the user wants a repository README corrected or expanded for contributors.
domain: code-quality
tags: [readme, documentation, developer-experience, code-quality]
triggers: ["improve codebase readme", "fix repository readme", "contributor readme review"]
---

# Improve a codebase README with verified setup usage architecture and maintenance guidance

## Purpose

Improve a codebase README with verified setup usage architecture and maintenance guidance.

## When to use

Use when the user wants a repository README corrected or expanded for contributors.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Verify every setup and run command against the current repository configuration.
2. Document the architecture boundaries and the main contributor entry points.
3. Add examples for the expected inputs outputs and supported environment.
4. Remove stale claims and link each section to its source of truth.
5. Run the documented commands and ask a reviewer to follow the README.

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
