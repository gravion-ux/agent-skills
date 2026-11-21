---
name: back-up-and-restore-a-cloud-data-store
description: Back up a managed cloud data store and restore it into an isolated instance with verified data. Use when the user wants a protected backup and a proven restore for a managed cloud datastore.
domain: devops-cloud
tags: [backup, restore, database, data-protection]
triggers: ["cloud datastore backup and restore", "restore a managed database snapshot", "validate a database backup"]
---

# Back up a managed cloud data store and restore it into an isolated instance with verified data

## Purpose

Back up a managed cloud data store and restore it into an isolated instance with verified data.

## When to use

Use when the user wants a protected backup and a proven restore for a managed cloud datastore.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Enable scheduled point-in-time recovery on the target database.
2. Record the backup retention window and the encryption key policy.
3. Restore the latest snapshot into a separate validation instance.
4. Compare row counts and checksums for critical tables between source and restore.
5. Keep the validation instance isolated until the restore report is approved.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `set-up-a-virtual-network-and-subnets`
- `apply-a-cost-budget-to-cloud-resources`
- `manage-a-service-on-a-managed-cloud-platform`
