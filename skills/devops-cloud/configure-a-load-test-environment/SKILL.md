---
name: configure-a-load-test-environment
description: Stand up an isolated environment that can absorb production-scale load safely. Use when the user wants to test a service under production-like load.
domain: devops-cloud
tags: [load-testing, environment, isolation]
triggers: ["configure a load test environment", "set up load testing infrastructure", "isolated load test setup"]
---

# Stand up an isolated environment that can absorb production-scale load safely

## Purpose

Stand up an isolated environment that can absorb production-scale load safely.

## When to use

Use when the user wants to test a service under production-like load.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Mirror the production topology in a separate account or namespace.
2. Scale the environment to a documented fraction of production capacity.
3. Write the load profile with ramp-up, steady state and cooldown phases.
4. Block outbound traffic from the test environment to real customer systems.
5. Collect latency percentiles and error rates, then tear the environment down.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `configure-a-load-balancer`
- `provision-a-cloud-environment`
- `set-up-a-canary-environment-for-testing`
