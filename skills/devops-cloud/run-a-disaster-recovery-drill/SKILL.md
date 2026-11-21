---
name: run-a-disaster-recovery-drill
description: Exercise a disaster recovery plan with a timed failover and prove recovery of critical services. Use when the user wants to rehearse regional failure recovery for critical infrastructure.
domain: devops-cloud
tags: [disaster-recovery, failover, drill, rpo]
triggers: ["disaster recovery drill", "regional failover rehearsal", "test recovery time objectives"]
---

# Exercise a disaster recovery plan with a timed failover and prove recovery of critical services

## Purpose

Exercise a disaster recovery plan with a timed failover and prove recovery of critical services.

## When to use

Use when the user wants to rehearse regional failure recovery for critical infrastructure.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Define the failure scenario, recovery objectives, and a hard drill stop time.
2. Take a verified backup snapshot and record the recovery point timestamp.
3. Fail over the critical service into the secondary region using the runbook.
4. Measure restore time against the recovery time objective for each service.
5. Document gaps, owner assignments, and the next drill date.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `run-a-canary-release-with-metrics`
- `run-a-service-in-kubernetes`
- `apply-a-cost-budget-to-cloud-resources`
