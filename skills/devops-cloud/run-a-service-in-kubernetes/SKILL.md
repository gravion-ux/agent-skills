---
name: run-a-service-in-kubernetes
description: Deploy a service to Kubernetes with the right workload kind, probes and resources. Use when the user wants to run a service on a Kubernetes cluster.
domain: devops-cloud
tags: [kubernetes, deployment, workload]
triggers: ["run a service in kubernetes", "deploy to a kubernetes cluster", "kubernetes workload setup"]
---

# Deploy a service to Kubernetes with the right workload kind, probes and resources

## Purpose

Deploy a service to Kubernetes with the right workload kind, probes and resources.

## When to use

Use when the user wants to run a service on a Kubernetes cluster.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Decide between a Deployment, a StatefulSet and a Job from the workload's state needs.
2. Set CPU and memory requests and limits from measured usage rather than guesses.
3. Configure readiness and liveness probes against a real dependency.
4. Apply the manifest to a test namespace and watch the rollout status.
5. Record the namespace, service name and how to scale the workload.

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
- `manage-a-service-on-a-managed-cloud-platform`
- `manage-secrets-in-a-cloud-account`
