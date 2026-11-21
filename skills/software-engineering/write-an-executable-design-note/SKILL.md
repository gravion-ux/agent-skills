---
name: write-an-executable-design-note
description: Write an executable design note that links assumptions to code, checks, and a verifiable rollout plan. Use when the user wants a technical design captured in an implementation-ready repository artefact.
domain: software-engineering
tags: [design-note, implementation-planning, verification]
triggers: ["write executable design note", "capture implementation ready design", "link design to code checks"]
---

# Write an executable design note that links assumptions to code, checks, and a verifiable rollout plan

## Purpose

Write an executable design note that links assumptions to code, checks, and a verifiable rollout plan.

## When to use

Use when the user wants a technical design captured in an implementation-ready repository artefact.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. State the required behavior, constraints, assumptions, and explicit non-goals.
2. Map each requirement to the affected module, interface, and automated check.
3. Include failure handling, compatibility notes, rollback steps, and the stop condition.
4. Link the note to a small proof in code or a failing test before full implementation.
5. Have a maintainer review the note and record approved changes in version control.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `write-an-idempotent-background-job`
- `adopt-type-checking-in-an-untyped-codebase`
- `design-a-retry-and-backoff-policy`
