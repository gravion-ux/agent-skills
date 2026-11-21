---
name: review-dependency-hygiene
description: Review dependencies for unused packages duplicates vulnerabilities and unnecessary runtime weight. Use when the user wants a project dependencies audited for hygiene and maintenance cost.
domain: code-quality
tags: [dependencies, supply-chain, maintenance, code-quality]
triggers: ["dependency hygiene review", "audit project dependencies", "unused package cleanup"]
---

# Review dependencies for unused packages duplicates vulnerabilities and unnecessary runtime weight

## Purpose

Review dependencies for unused packages duplicates vulnerabilities and unnecessary runtime weight.

## When to use

Use when the user wants a project dependencies audited for hygiene and maintenance cost.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Generate the current direct and transitive dependency inventory.
2. Compare each dependency with actual imports and declared tool usage.
3. Check for duplicate capabilities unused packages and known advisories.
4. Rank each finding by risk and removal effort.
5. Propose one safe dependency change at a time with validation commands.

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
- `review-a-pr-for-scope-discipline`
- `add-typing-to-an-untyped-function`
