---
name: pin-a-container-base-image
description: Pin a container base image to an immutable digest and update it through a controlled rebuild. Use when the user wants to remove mutable image tags from a container build.
domain: devops-cloud
tags: [base-image, digest-pinning, container, dependency]
triggers: ["pin a container base image", "replace an image tag with a digest", "pin a docker base image digest"]
---

# Pin a container base image to an immutable digest and update it through a controlled rebuild

## Purpose

Pin a container base image to an immutable digest and update it through a controlled rebuild.

## When to use

Use when the user wants to remove mutable image tags from a container build.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Identify the base image tag used by the dockerfile and its current digest.
2. Replace the tag with the digest and record the source registry and build date.
3. Rebuild the image and compare the installed package versions with the previous build.
4. Run the vulnerability scan and the image smoke test on the rebuilt artifact.
5. Open a dependency update change when the pinned digest reaches its review date.

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
- `reduce-a-container-image-size`
- `apply-a-cost-budget-to-cloud-resources`
