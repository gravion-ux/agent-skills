---
name: design-a-blue-green-deployment
description: Plan a blue-green release that keeps a known-good environment running until cutover. Use when the user wants to release infrastructure or application changes with a blue-green strategy.
domain: devops-cloud
tags: [blue-green, release, cutover]
triggers: ["design a blue green deployment", "blue green release plan", "plan a blue green cutover"]
---

# Plan a blue-green release that keeps a known-good environment running until cutover

## Purpose

Plan a blue-green release that keeps a known-good environment running until cutover.

## When to use

Use when the user wants to release infrastructure or application changes with a blue-green strategy.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Stand up the green environment at full parity with the blue environment.
2. Run the full smoke suite against green using production-shaped traffic.
3. Prove the rollback path by shifting traffic back to blue on demand.
4. Cut traffic over during a low-traffic window and watch the error rate.
5. Keep blue running for the agreed soak period, then decommission it.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `gate-a-deployment-on-quality-checks`
- `implement-blue-green-traffic-shifting`
- `roll-back-a-bad-deployment`
