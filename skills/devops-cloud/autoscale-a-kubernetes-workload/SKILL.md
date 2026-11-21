---
name: autoscale-a-kubernetes-workload
description: Set horizontal and vertical autoscaling so a workload follows real demand. Use when the user wants a Kubernetes workload to scale with traffic.
domain: devops-cloud
tags: [autoscaling, kubernetes, capacity]
triggers: ["autoscale a kubernetes workload", "scale a deployment automatically", "kubernetes autoscaling setup"]
---

# Set horizontal and vertical autoscaling so a workload follows real demand

## Purpose

Set horizontal and vertical autoscaling so a workload follows real demand.

## When to use

Use when the user wants a Kubernetes workload to scale with traffic.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Measure the current request rate and the CPU and memory per request.
2. Set a minimum replica count that covers the traffic floor without wasting capacity.
3. Define a target utilisation that scales out before the service starts to degrade.
4. Add a pod disruption budget and a topology spread rule across nodes.
5. Load-test the scaling policy and confirm it scales back down again.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `migrate-a-workload-to-a-managed-service`
- `run-a-service-in-kubernetes`
- `write-a-kubernetes-manifest`
