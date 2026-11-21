---
name: plan-a-multi-day-migration
description: Plan a multi-day code migration with staged commits, compatibility checkpoints, and rollback gates. Use when the user wants a risky repository migration divided across several days.
domain: software-engineering
tags: [migration, staged-rollout, rollback]
triggers: ["plan multi day code migration", "stage repository migration over days", "schedule incremental code migration"]
---

# Plan a multi-day code migration with staged commits, compatibility checkpoints, and rollback gates

## Purpose

Plan a multi-day code migration with staged commits, compatibility checkpoints, and rollback gates.

## When to use

Use when the user wants a risky repository migration divided across several days.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the end state, compatibility window, migration boundaries, and data safeguards.
2. Order changes into independently testable stages with explicit entry criteria.
3. Define a verification checkpoint and rollback gate for every stage.
4. Prepare mixed-version operation steps and document compatibility assumptions.
5. Track progress against verified outputs rather than elapsed estimates.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
- `automate-a-repetitive-code-change`
