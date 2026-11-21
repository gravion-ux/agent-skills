---
name: set-up-a-canary-environment-for-testing
description: Provision an isolated canary environment that mirrors production configuration for pre-release testing. Use when the user wants a temporary cloud environment for validating a release before production.
domain: devops-cloud
tags: [canary-environment, testing, isolation, teardown]
triggers: ["set up a canary environment", "create an isolated canary test environment", "mirror production config for canary"]
---

# Provision an isolated canary environment that mirrors production configuration for pre-release testing

## Purpose

Provision an isolated canary environment that mirrors production configuration for pre-release testing.

## When to use

Use when the user wants a temporary cloud environment for validating a release before production.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Create the canary account or namespace with isolated networking and separate credentials.
2. Mirror production configuration from the secret manager without copying live data.
3. Seed representative test data and point synthetic checks at the canary endpoints.
4. Run the release candidate and verify synthetic traffic and logs in the canary account.
5. Set a teardown date and confirm the cost estimate for the canary period.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `set-up-a-ci-pipeline-for-a-service`
- `set-up-a-cd-pipeline-with-safe-rollouts`
- `set-up-a-virtual-network-and-subnets`
