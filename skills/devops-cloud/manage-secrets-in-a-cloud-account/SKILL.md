---
name: manage-secrets-in-a-cloud-account
description: Store, rotate and scope cloud secrets so no long-lived credential sits in code. Use when the user needs to manage secrets, keys or credentials inside a cloud account.
domain: devops-cloud
tags: [secrets, rotation, cloud-security]
triggers: ["manage cloud secrets", "rotate a cloud credential", "store secrets in the cloud"]
---

# Store, rotate and scope cloud secrets so no long-lived credential sits in code

## Purpose

Store, rotate and scope cloud secrets so no long-lived credential sits in code.

## When to use

Use when the user needs to manage secrets, keys or credentials inside a cloud account.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Inventory every secret the account currently holds and where each one is used.
2. Move each secret into the cloud secret manager and remove it from code and logs.
3. Replace stored keys with short-lived identities wherever the platform allows it.
4. Set an automatic rotation schedule and prove one rotation end to end.
5. Restrict read access per workload and record the access policy in the runbook.

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
- `apply-a-cost-budget-to-cloud-resources`
- `back-up-and-restore-a-cloud-data-store`
