---
name: write-infrastructure-as-code-for-a-service
description: Describe a service's infrastructure as reviewable code instead of console clicks. Use when the user wants a service's cloud resources defined as code.
domain: devops-cloud
tags: [infrastructure-as-code, terraform, provisioning]
triggers: ["write infrastructure as code", "define cloud resources in code", "infrastructure code for a service"]
---

# Describe a service's infrastructure as reviewable code instead of console clicks

## Purpose

Describe a service's infrastructure as reviewable code instead of console clicks.

## When to use

Use when the user wants a service's cloud resources defined as code.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List every resource the service needs, including the ones it depends on.
2. Write the resource definitions with explicit names, tags and region.
3. Parameterise the environment-specific values instead of hard-coding them.
4. Run a plan and read the diff for destructive changes before applying it.
5. Export the resulting resource ids as outputs for the deployment pipeline.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `write-a-dockerfile-for-a-service`
- `set-up-a-ci-pipeline-for-a-service`
- `write-a-runbook-for-an-on-call-engineer`
