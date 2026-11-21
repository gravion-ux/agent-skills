---
name: write-a-code-smell-triage-list
description: Create a code smell triage list that ranks evidence impact effort and safe first fixes. Use when the user wants code smells collected prioritized into an actionable backlog.
domain: code-quality
tags: [technical-debt, triage, refactoring, code-quality]
triggers: ["code smell triage", "prioritize code smells", "technical debt smell list"]
---

# Create a code smell triage list that ranks evidence impact effort and safe first fixes

## Purpose

Create a code smell triage list that ranks evidence impact effort and safe first fixes.

## When to use

Use when the user wants code smells collected prioritized into an actionable backlog.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Collect candidate smells with file locations and short evidence excerpts.
2. Classify each item as correctness risk maintenance cost or consistency issue.
3. Estimate impact and effort using the repository's current signals.
4. Order the list by risk and dependency, marking safe refactor candidates.
5. Propose the first focused change and its behavior-preserving checks.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `write-self-documenting-code`
- `apply-a-formatter-consistently`
- `audit-a-file-for-hidden-side-effects`
