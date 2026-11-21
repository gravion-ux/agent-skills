---
name: plan-a-cloud-migration-wave
description: Group workloads into migration waves that each deliver value and carry known risk. Use when the user needs to plan an incremental migration of many workloads to the cloud.
domain: devops-cloud
tags: [migration, wave-plan, cloud]
triggers: ["plan a cloud migration wave", "group workloads into migration waves", "cloud migration wave planning"]
---

# Group workloads into migration waves that each deliver value and carry known risk

## Purpose

Group workloads into migration waves that each deliver value and carry known risk.

## When to use

Use when the user needs to plan an incremental migration of many workloads to the cloud.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Inventory the workloads with their owner, dependencies and current running cost.
2. Group them into waves by dependency and by how similar their configuration is.
3. Order the waves so a pilot proves the pattern before the bulk moves.
4. Name the rollback for each wave and the point where it can be declared done.
5. Report the projected spend and savings after every wave completes.

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
- `back-up-and-restore-a-cloud-data-store`
- `manage-a-service-on-a-managed-cloud-platform`
