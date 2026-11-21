---
name: validate-input-at-the-system-boundary
description: Reject malformed or unsafe input at the boundary before it reaches domain logic. Use when the user wants external requests or files validated before processing.
domain: software-engineering
tags: [input-validation, schema, boundary-checks]
triggers: ["validate input at api boundary", "reject malformed request input"]
---

# Reject malformed or unsafe input at the boundary before it reaches domain logic

## Purpose

Reject malformed or unsafe input at the boundary before it reaches domain logic.

## When to use

Use when the user wants external requests or files validated before processing.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map each accepted input field to a schema and limit.
2. Identify the boundary that receives untrusted data.
3. Reject malformed values with field-specific errors.
4. Normalize only values allowed by the public contract.
5. Test malformed, oversized, and boundary-valid inputs.
6. Run existing tests and document the validation rules.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `hand-over-code-to-the-next-owner`
- `plan-the-code-change-before-editing`
- `reduce-the-blame-of-a-failing-test-suite`
