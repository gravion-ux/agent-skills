---
name: rotate-a-service-account-key
description: Replace a service account key without interrupting the workloads that use it. Use when the user needs to rotate a cloud service account key safely.
domain: devops-cloud
tags: [key-rotation, service-account, credentials]
triggers: ["rotate a service account key", "replace a cloud access key", "service account key rotation"]
---

# Replace a service account key without interrupting the workloads that use it

## Purpose

Replace a service account key without interrupting the workloads that use it.

## When to use

Use when the user needs to rotate a cloud service account key safely.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List every workload and pipeline that authenticates with the key.
2. Create the replacement key and grant it the same scoped permissions.
3. Update one non-critical consumer and prove it authenticates successfully.
4. Roll the remaining consumers across and confirm none still use the old key.
5. Revoke the old key and verify the revocation in the audit log.

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
- `manage-secrets-in-a-cloud-account`
- `migrate-a-workload-to-a-managed-service`
