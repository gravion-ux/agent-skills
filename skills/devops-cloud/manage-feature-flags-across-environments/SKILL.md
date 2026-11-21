---
name: manage-feature-flags-across-environments
description: Control feature flag targeting per environment and audit every exposure change before rollout. Use when the user wants to enable or disable a feature independently in each environment.
domain: devops-cloud
tags: [feature-flags, targeting, configuration, audit]
triggers: ["feature flag environment targeting", "manage feature flags across environments", "toggle flags per environment"]
---

# Control feature flag targeting per environment and audit every exposure change before rollout

## Purpose

Control feature flag targeting per environment and audit every exposure change before rollout.

## When to use

Use when the user wants to enable or disable a feature independently in each environment.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Inventory each flag with its owner, environment defaults, and expiry date.
2. Apply targeting rules so production flags never inherit test overrides.
3. Attach a scheduled removal date to every temporary flag.
4. Review the flag diff with the owning team before enabling it.
5. Export the current flag configuration as an audit record.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-configuration-across-environments`
- `manage-environments-with-infrastructure-pipelines`
- `manage-a-service-on-a-managed-cloud-platform`
