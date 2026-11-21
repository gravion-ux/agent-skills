---
name: migrate-a-workload-to-a-managed-service
description: Move a self-managed workload onto a managed service with a tested rollback. Use when the user wants to replace a self-run service with a managed cloud equivalent.
domain: devops-cloud
tags: [migration, managed-service, cutover]
triggers: ["migrate a workload to a managed service", "replace self hosted with managed", "managed service migration"]
---

# Move a self-managed workload onto a managed service with a tested rollback

## Purpose

Move a self-managed workload onto a managed service with a tested rollback.

## When to use

Use when the user wants to replace a self-run service with a managed cloud equivalent.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Compare the managed service's limits against the workload's measured peak usage.
2. List every feature the workload uses and check each one is supported or has a workaround.
3. Migrate a copy of the data and run both versions side by side for a comparison window.
4. Move the traffic over and keep the original running until the data matches.
5. Decommission the old system only after the rollback window closes cleanly.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-a-service-on-a-managed-cloud-platform`
- `respond-to-a-service-outage`
- `apply-a-cost-budget-to-cloud-resources`
