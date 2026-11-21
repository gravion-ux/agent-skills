---
name: drift-detect-infrastructure-changes
description: Detect unmanaged changes between declared infrastructure code and the live cloud state. Use when the user wants scheduled or on-demand detection of cloud configuration drift.
domain: devops-cloud
tags: [drift-detection, infrastructure-as-code, reconciliation, audit]
triggers: ["detect infrastructure drift", "compare cloud state to terraform code", "infrastructure drift report"]
---

# Detect unmanaged changes between declared infrastructure code and the live cloud state

## Purpose

Detect unmanaged changes between declared infrastructure code and the live cloud state.

## When to use

Use when the user wants scheduled or on-demand detection of cloud configuration drift.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Refresh the remote state snapshot for the target account and region.
2. Plan the infrastructure code against the refreshed state and list each difference.
3. Classify each difference as harmless, security-relevant, or cost-relevant.
4. Notify the owning team with the drift diff and a suggested reconciliation path.
5. Archive each run's plan output as the detection record.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-environments-with-infrastructure-pipelines`
- `write-infrastructure-as-code-for-a-service`
- `apply-a-cost-budget-to-cloud-resources`
