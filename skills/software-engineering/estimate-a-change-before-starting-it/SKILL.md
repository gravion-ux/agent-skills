---
name: estimate-a-change-before-starting-it
description: Estimate a code change from repository evidence and state assumptions, uncertainty, and validation slices. Use when the user wants a delivery estimate before implementation begins.
domain: software-engineering
tags: [estimation, delivery-planning, risk]
triggers: ["estimate code change upfront", "size repository work before starting", "forecast implementation effort"]
---

# Estimate a code change from repository evidence and state assumptions, uncertainty, and validation slices

## Purpose

Estimate a code change from repository evidence and state assumptions, uncertainty, and validation slices.

## When to use

Use when the user wants a delivery estimate before implementation begins.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inspect the repository, related past work, and explicit compatibility constraints.
2. Break the change into implementation, test, review, and rollout slices.
3. Assign a range to each slice using observed repository evidence.
4. List assumptions, unknowns, dependencies, and the effect of each uncertainty.
5. Re-estimate after the first slice exposes actual complexity.

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
- `plan-the-code-change-before-editing`
- `add-structured-logging-to-a-code-path`
