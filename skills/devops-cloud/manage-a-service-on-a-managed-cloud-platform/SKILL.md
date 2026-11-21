---
name: manage-a-service-on-a-managed-cloud-platform
description: Operate a service on a managed platform using its supported configuration surface. Use when the user wants to run a service on a managed cloud application platform.
domain: devops-cloud
tags: [managed-platform, paas, deployment]
triggers: ["manage a service on a managed platform", "run a service on a cloud app platform", "paas deployment"]
---

# Operate a service on a managed platform using its supported configuration surface

## Purpose

Operate a service on a managed platform using its supported configuration surface.

## When to use

Use when the user wants to run a service on a managed cloud application platform.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Map the service's runtime needs onto the platform's supported build and runtime options.
2. Configure scaling, health checks and the environment variables the platform exposes.
3. Attach the managed database and secret store rather than self-managing them.
4. Deploy to a preview environment and run the smoke suite before production.
5. Record the platform configuration and the supported operational levers.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-secrets-in-a-cloud-account`
- `migrate-a-workload-to-a-managed-service`
- `apply-a-cost-budget-to-cloud-resources`
