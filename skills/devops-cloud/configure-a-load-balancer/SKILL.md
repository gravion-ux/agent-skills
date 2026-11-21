---
name: configure-a-load-balancer
description: Configure a load balancer with health checks, sensible timeouts and a known drain procedure. Use when the user needs to put a load balancer in front of a service or fleet.
domain: devops-cloud
tags: [load-balancer, health-check, networking]
triggers: ["configure a load balancer", "set up a load balancer for a service", "load balancer health check"]
---

# Configure a load balancer with health checks, sensible timeouts and a known drain procedure

## Purpose

Configure a load balancer with health checks, sensible timeouts and a known drain procedure.

## When to use

Use when the user needs to put a load balancer in front of a service or fleet.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List the target instances and the port the service actually listens on.
2. Set the health check path, interval and timeout to match the service's real readiness.
3. Choose the algorithm and the session-affinity behaviour the app needs.
4. Write the drain procedure so a target leaves rotation before it is stopped.
5. Verify the balancer in a test environment and record the configuration.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `configure-a-load-test-environment`
- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
