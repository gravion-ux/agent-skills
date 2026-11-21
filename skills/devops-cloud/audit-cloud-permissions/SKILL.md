---
name: audit-cloud-permissions
description: Audit cloud iam grants for excessive roles, unused credentials, and public exposure across accounts. Use when the user wants to review cloud access permissions for privilege and exposure risks.
domain: devops-cloud
tags: [iam, permissions, least-privilege, audit]
triggers: ["audit cloud permissions", "iam grant review for cloud accounts", "unused cloud role assignments"]
---

# Audit cloud iam grants for excessive roles, unused credentials, and public exposure across accounts

## Purpose

Audit cloud iam grants for excessive roles, unused credentials, and public exposure across accounts.

## When to use

Use when the user wants to review cloud access permissions for privilege and exposure risks.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Export role assignments, group memberships, and credential inventory for each account.
2. Flag wildcard actions, resource wildcards, and cross-account trust policies.
3. Cross-check grants against ninety days of access logs to find unused permissions.
4. Rank findings by privilege, exposure, and business owner for remediation.
5. Attach the grant diff and a dated removal plan to the audit record.

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
