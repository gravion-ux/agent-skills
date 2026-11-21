---
name: provision-a-cloud-environment
description: Provision a new cloud environment with the accounts, networks and guardrails it needs. Use when the user needs a new isolated environment created in a cloud account.
domain: devops-cloud
tags: [cloud-provisioning, environments, guardrails]
triggers: ["provision a cloud environment", "set up a new cloud account", "create a cloud environment"]
---

# Provision a new cloud environment with the accounts, networks and guardrails it needs

## Purpose

Provision a new cloud environment with the accounts, networks and guardrails it needs.

## When to use

Use when the user needs a new isolated environment created in a cloud account.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Confirm the account layout, region and naming convention for the environment.
2. Create the account or subscription with the organisation policies attached.
3. Build the network, subnet and routing baseline from the infrastructure code.
4. Apply budget alerts, quota limits and least-privilege roles before any workload runs.
5. Record the resulting resource ids and the state diff in the environment README.

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
- `configure-a-load-test-environment`
