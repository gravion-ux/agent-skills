---
name: manage-configuration-across-environments
description: Promote environment configuration through typed values, change review, and encrypted secret storage. Use when the user wants one controlled configuration source shared across deployment environments.
domain: devops-cloud
tags: [configuration, secrets, environments, promotion]
triggers: ["manage configuration across environments", "promote environment configuration", "validated config overlay"]
---

# Promote environment configuration through typed values, change review, and encrypted secret storage

## Purpose

Promote environment configuration through typed values, change review, and encrypted secret storage.

## When to use

Use when the user wants one controlled configuration source shared across deployment environments.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Define typed configuration keys with defaults, validation rules, and ownership.
2. Store secret values in the platform secret manager and grant least-privilege read access.
3. Render environment overlays from a reviewed template without copying plaintext secrets.
4. Validate the rendered configuration in a dry run before promotion.
5. Record the configuration diff, approver, and validation output for each environment.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-feature-flags-across-environments`
- `manage-environments-with-infrastructure-pipelines`
- `manage-a-service-on-a-managed-cloud-platform`
