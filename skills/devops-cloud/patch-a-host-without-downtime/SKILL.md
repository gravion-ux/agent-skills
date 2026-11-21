---
name: patch-a-host-without-downtime
description: Patch a running cloud host by draining its traffic, installing updates, and returning it to service. Use when the user needs to patch a live server while keeping its service available.
domain: devops-cloud
tags: [host-patching, zero-downtime, drain, maintenance]
triggers: ["patch a host without downtime", "drain and patch a live server", "zero downtime host update"]
---

# Patch a running cloud host by draining its traffic, installing updates, and returning it to service

## Purpose

Patch a running cloud host by draining its traffic, installing updates, and returning it to service.

## When to use

Use when the user needs to patch a live server while keeping its service available.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Drain the host from the load balancer and confirm zero active requests.
2. Apply the approved package updates or kernel patch with the service stopped.
3. Run the service health check and review the boot and application logs.
4. Return the host to the load balancer only after the check passes.
5. Record the patch version, host state, and any reboot outcome.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
- `autoscale-a-kubernetes-workload`
