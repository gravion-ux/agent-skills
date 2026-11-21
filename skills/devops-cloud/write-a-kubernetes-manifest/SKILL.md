---
name: write-a-kubernetes-manifest
description: Write a Kubernetes manifest that declares the workload, its service and its configuration. Use when the user needs a Kubernetes manifest for a new workload.
domain: devops-cloud
tags: [kubernetes, yaml, manifest]
triggers: ["write a kubernetes manifest", "create a k8s yaml for a service", "kubernetes manifest for a workload"]
---

# Write a Kubernetes manifest that declares the workload, its service and its configuration

## Purpose

Write a Kubernetes manifest that declares the workload, its service and its configuration.

## When to use

Use when the user needs a Kubernetes manifest for a new workload.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Choose the manifest kind that matches the workload and its scaling needs.
2. Declare the container image by digest and the resources it is allowed to use.
3. Add the service, config map or secret reference the workload reads at start-up.
4. Set the probe endpoints, the rollout strategy and the termination grace period.
5. Apply the manifest with a dry run and read the server-side validation errors.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `autoscale-a-kubernetes-workload`
- `run-a-service-in-kubernetes`
- `write-a-dockerfile-for-a-service`
