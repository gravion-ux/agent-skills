---
name: write-a-dockerfile-for-a-service
description: Write a lean Dockerfile with a deterministic build, a small runtime and a clear entrypoint. Use when the user needs a Dockerfile for a new or existing service.
domain: devops-cloud
tags: [dockerfile, container, build]
triggers: ["write a dockerfile", "dockerfile for a service", "create a container build file"]
---

# Write a lean Dockerfile with a deterministic build, a small runtime and a clear entrypoint

## Purpose

Write a lean Dockerfile with a deterministic build, a small runtime and a clear entrypoint.

## When to use

Use when the user needs a Dockerfile for a new or existing service.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Choose a base image that matches the runtime version the service supports.
2. Copy the dependency manifest first and install dependencies in their own layer.
3. Copy the application source and set the working directory and entrypoint.
4. Drop the package manager caches and development files from the final image.
5. Build the image and confirm the container starts and answers a health check.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `write-infrastructure-as-code-for-a-service`
- `set-up-a-ci-pipeline-for-a-service`
- `write-a-runbook-for-an-on-call-engineer`
