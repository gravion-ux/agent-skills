---
name: apply-a-cost-budget-to-cloud-resources
description: Set budgets, quotas and alerts so cloud spend stays inside an agreed ceiling. Use when the user wants to control or predict cloud spending.
domain: devops-cloud
tags: [cost, budget, quota]
triggers: ["apply a cloud cost budget", "control cloud spending", "set a cloud budget alert"]
---

# Set budgets, quotas and alerts so cloud spend stays inside an agreed ceiling

## Purpose

Set budgets, quotas and alerts so cloud spend stays inside an agreed ceiling.

## When to use

Use when the user wants to control or predict cloud spending.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Establish last month's spend as the baseline and split it by service and team.
2. Set a monthly budget with thresholds that notify before the ceiling is reached.
3. Apply quotas on the resources that can grow without a human decision.
4. Tag every resource with an owner so unattributed spend can be charged back.
5. Review the budget report weekly and adjust the alert thresholds.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `back-up-and-restore-a-cloud-data-store`
- `manage-a-service-on-a-managed-cloud-platform`
- `manage-cost-with-a-scheduled-scale-down`
