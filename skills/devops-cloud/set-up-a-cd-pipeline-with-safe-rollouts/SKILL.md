---
name: set-up-a-cd-pipeline-with-safe-rollouts
description: Automate promotion from build to production with gates that stop unsafe releases. Use when the user wants a continuous delivery pipeline that deploys safely.
domain: devops-cloud
tags: [cd, deployment, release-gates]
triggers: ["set up a cd pipeline", "continuous delivery with safe rollouts", "automated deployment pipeline"]
---

# Automate promotion from build to production with gates that stop unsafe releases

## Purpose

Automate promotion from build to production with gates that stop unsafe releases.

## When to use

Use when the user wants a continuous delivery pipeline that deploys safely.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Promote the same immutable artefact through every environment unchanged.
2. Gate each promotion on the previous environment's smoke tests and error budget.
3. Roll out progressively and keep the previous version warm for instant rollback.
4. Stop the pipeline automatically when the error budget or latency gate breaks.
5. Record the deployed version and the rollback command in the release log.

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
- `set-up-a-canary-environment-for-testing`
- `set-up-a-virtual-network-and-subnets`
