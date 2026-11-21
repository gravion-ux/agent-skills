---
name: reduce-a-container-image-size
description: Shrink a container image without changing how the service behaves. Use when the user wants a smaller or faster-to-pull container image.
domain: devops-cloud
tags: [image-size, multi-stage, performance]
triggers: ["reduce container image size", "shrink a docker image", "speed up image pulls"]
---

# Shrink a container image without changing how the service behaves

## Purpose

Shrink a container image without changing how the service behaves.

## When to use

Use when the user wants a smaller or faster-to-pull container image.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List the layers in the current image and find the ones that dominate the size.
2. Move build-only toolchains into a multi-stage build that never ships.
3. Remove package caches, test fixtures and documentation from the runtime layer.
4. Run the container's own smoke test against the slimmed image.
5. Compare pull time and start-up time before and after the change.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `build-a-container-image`
- `pin-a-container-base-image`
- `apply-a-cost-budget-to-cloud-resources`
