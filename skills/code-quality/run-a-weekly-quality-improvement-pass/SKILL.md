---
name: run-a-weekly-quality-improvement-pass
description: Run a weekly quality pass that selects one small debt item verifies it and records the result. Use when the user wants an agent to run a repeatable weekly code quality improvement.
domain: code-quality
tags: [weekly-quality, automation, technical-debt, code-quality]
triggers: ["weekly quality improvement", "automated weekly code cleanup", "recurring quality pass"]
---

# Run a weekly quality pass that selects one small debt item verifies it and records the result

## Purpose

Run a weekly quality pass that selects one small debt item verifies it and records the result.

## When to use

Use when the user wants an agent to run a repeatable weekly code quality improvement.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Collect the latest lint findings complexity metrics and stale dependency reports.
2. Select one small item whose fix stays smaller than the debt it removes.
3. Create a focused branch and change only the selected issue.
4. Run the relevant tests linter formatter and type checker.
5. Record the diff, measured result, and any remaining finding for the next run.

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
