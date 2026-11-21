---
name: review-a-diff-for-correctness
description: Review a code diff for correctness while keeping behavior unchanged and tests passing. Use when the user wants a code diff reviewed for correctness before it is merged.
domain: code-quality
tags: [diff-review, correctness, code-quality, tests]
triggers: ["diff correctness review", "review code diff for correctness", "correctness review of a diff"]
---

# Review a code diff for correctness while keeping behavior unchanged and tests passing

## Purpose

Review a code diff for correctness while keeping behavior unchanged and tests passing.

## When to use

Use when the user wants a code diff reviewed for correctness before it is merged.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Read the diff and list every changed behavior in the affected code paths.
2. Trace each changed branch through its callers and existing tests.
3. Reject any unrelated refactor that could obscure a behavioral correction.
4. Run the focused test suite and the configured linter.
5. Summarize confirmed defects separately from optional simplification ideas.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `review-a-pr-for-scope-discipline`
- `audit-a-file-for-hidden-side-effects`
- `apply-a-formatter-consistently`
