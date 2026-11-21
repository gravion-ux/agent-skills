---
name: write-a-technical-debt-register
description: Record technical debt with evidence, impact, effort, ownership, and a clear prioritization order. Use when the user wants a practical register of outstanding code debt.
domain: software-engineering
tags: [technical-debt, prioritization, planning]
triggers: ["create a technical debt register", "rank technical debt by cost"]
---

# Record technical debt with evidence, impact, effort, ownership, and a clear prioritization order

## Purpose

Record technical debt with evidence, impact, effort, ownership, and a clear prioritization order.

## When to use

Use when the user wants a practical register of outstanding code debt.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Collect debt items from defects, reviews, and maintenance findings.
2. Link each item to concrete code locations and evidence.
3. Estimate impact, effort, risk, and dependency constraints.
4. Rank items by cost of delay and remediation effort.
5. Assign an owner and review date to each committed item.
6. Keep the register concise and actionable for weekly review.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `write-a-changelog-entry`
- `write-a-postmortem-for-a-defect`
- `add-structured-logging-to-a-code-path`
