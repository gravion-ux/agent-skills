---
name: build-a-container-image
description: Build a reproducible container image that runs the same in every environment. Use when the user wants to package a service as a container image for deployment.
domain: devops-cloud
tags: [container, image-build, reproducibility]
triggers: ["build a container image", "package the service as a container", "container image build"]
---

# Build a reproducible container image that runs the same in every environment

## Purpose

Build a reproducible container image that runs the same in every environment.

## When to use

Use when the user wants to package a service as a container image for deployment.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Pin the base image to a digest and install only the runtime dependencies.
2. Copy the source and install the package with a lockfile-pinned command.
3. Run the entrypoint as a non-root user with a read-only root filesystem.
4. Tag the image with the commit sha and push it to the registry.
5. Record the image digest in the deployment manifest so the release is traceable.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `pin-a-container-base-image`
- `reduce-a-container-image-size`
- `promote-a-build-through-environments`
