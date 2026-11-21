---
name: plan-the-code-change-before-editing
description: Turn a requested code change into a bounded plan with touched files, tests, risks, and rollback. Use when the user wants a code-change plan before any repository files are edited.
domain: software-engineering
tags: [change-planning, repository-plan, scope-control]
triggers: ["plan code change before editing", "map repository change", "scope a code modification"]
---

# Turn a requested code change into a bounded plan with touched files, tests, risks, and rollback

## Purpose

Turn a requested code change into a bounded plan with touched files, tests, risks, and rollback.

## When to use

Use when the user wants a code-change plan before any repository files are edited.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inspect repository guidance and the code paths affected by the request.
2. Enumerate files likely to change and mark any uncertain areas explicitly.
3. Define the automated test that will prove the new behavior.
4. Record compatibility risks, out-of-scope work, and the rollback route.
5. Share the plan and wait for agreement before editing implementation files.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `automate-a-repetitive-code-change`
- `estimate-a-change-before-starting-it`
- `hand-over-code-to-the-next-owner`
