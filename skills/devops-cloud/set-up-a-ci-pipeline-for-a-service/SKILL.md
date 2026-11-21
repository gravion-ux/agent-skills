---
name: set-up-a-ci-pipeline-for-a-service
description: Build a CI pipeline that installs, tests and publishes a service on every change. Use when the user wants a continuous integration pipeline for a service.
domain: devops-cloud
tags: [ci, pipeline, automation]
triggers: ["set up a ci pipeline", "continuous integration for a service", "build a ci workflow"]
---

# Build a CI pipeline that installs, tests and publishes a service on every change

## Purpose

Build a CI pipeline that installs, tests and publishes a service on every change.

## When to use

Use when the user wants a continuous integration pipeline for a service.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Run formatting, linting, type checks and tests in that order on every push.
2. Cache the dependency and build directories between runs.
3. Fail the pipeline on the first failing stage and publish the logs as the job summary.
4. Build the release artefact once and reuse that exact artefact in later stages.
5. Protect the release branch so only reviewed changes produce a published image.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `set-up-a-canary-environment-for-testing`
- `set-up-a-cd-pipeline-with-safe-rollouts`
- `set-up-a-virtual-network-and-subnets`
