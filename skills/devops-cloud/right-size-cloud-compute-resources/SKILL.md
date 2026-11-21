---
name: right-size-cloud-compute-resources
description: Resize cloud compute from measured usage so capacity matches real demand. Use when the user wants to reduce cloud waste or improve instance sizing.
domain: devops-cloud
tags: [rightsizing, cost, capacity]
triggers: ["right size cloud compute", "resize cloud instances to save cost", "cloud instance rightsizing"]
---

# Resize cloud compute from measured usage so capacity matches real demand

## Purpose

Resize cloud compute from measured usage so capacity matches real demand.

## When to use

Use when the user wants to reduce cloud waste or improve instance sizing.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Collect ninety days of CPU, memory and network usage per instance type.
2. Compare the peak usage with the current size to find over- and under-provisioned tiers.
3. Change one instance type at a time and watch latency and error rate afterwards.
4. Confirm the new size still handles the measured peak with headroom.
5. Record the before-and-after cost and utilisation for the next review.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `apply-a-cost-budget-to-cloud-resources`
- `audit-cloud-permissions`
- `back-up-and-restore-a-cloud-data-store`
