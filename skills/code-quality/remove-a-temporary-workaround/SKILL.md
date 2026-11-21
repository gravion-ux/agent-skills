---
name: remove-a-temporary-workaround
description: Remove a temporary workaround after proving the underlying cause is fixed and covered. Use when the user wants an old workaround removed because its root cause has been fixed.
domain: code-quality
tags: [workarounds, technical-debt, cleanup, code-quality]
triggers: ["remove temporary workaround", "delete stale workaround", "workaround cleanup review"]
---

# Remove a temporary workaround after proving the underlying cause is fixed and covered

## Purpose

Remove a temporary workaround after proving the underlying cause is fixed and covered.

## When to use

Use when the user wants an old workaround removed because its root cause has been fixed.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Find the workaround and record the failure it currently masks.
2. Confirm the underlying fix exists and has a regression test.
3. Delete the workaround and any obsolete compatibility branches.
4. Run the affected tests plus the formatter and linter.
5. Explain the deletion and the test evidence in the diff summary.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `remove-a-feature-flag-left-behind`
- `apply-a-formatter-consistently`
- `audit-a-file-for-hidden-side-effects`
