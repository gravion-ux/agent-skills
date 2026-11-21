---
name: review-a-pr-for-scope-discipline
description: Review a pull request for scope discipline by separating behavior fixes from unrelated changes. Use when the user wants a pull request checked for focus size and mixed concerns.
domain: code-quality
tags: [pull-request, scope-control, review, code-quality]
triggers: ["pull request scope review", "review pr for scope", "scope discipline check"]
---

# Review a pull request for scope discipline by separating behavior fixes from unrelated changes

## Purpose

Review a pull request for scope discipline by separating behavior fixes from unrelated changes.

## When to use

Use when the user wants a pull request checked for focus size and mixed concerns.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. List every changed file and group the edits by intent.
2. Flag behavior changes mixed with broad refactors in the same patch.
3. Check that each change has focused tests and no unrelated formatting churn.
4. Compare the diff size with the debt removed and recommend a split when needed.
5. Return prioritized scope findings without changing the pull request.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `review-a-diff-for-correctness`
- `audit-a-file-for-hidden-side-effects`
- `apply-a-formatter-consistently`
