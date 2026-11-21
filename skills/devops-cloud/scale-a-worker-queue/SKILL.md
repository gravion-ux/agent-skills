---
name: scale-a-worker-queue
description: Scale queue workers against backlog depth and lag while keeping cost within the budget ceiling. Use when the user needs to tune worker concurrency because a cloud queue is falling behind.
domain: devops-cloud
tags: [queue-scaling, worker-concurrency, backlog, throughput]
triggers: ["scale a worker queue", "increase queue worker concurrency", "reduce a queue backlog"]
---

# Scale queue workers against backlog depth and lag while keeping cost within the budget ceiling

## Purpose

Scale queue workers against backlog depth and lag while keeping cost within the budget ceiling.

## When to use

Use when the user needs to tune worker concurrency because a cloud queue is falling behind.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Measure the queue depth, oldest message age, and processing latency per partition.
2. Calculate the required worker count from throughput per worker and the budget ceiling.
3. Set the target concurrency and a maximum scale-out limit in the worker configuration.
4. Watch the backlog drain rate and error rate for fifteen minutes after the change.
5. Reduce concurrency when the backlog clears and record the final worker configuration.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-cost-with-a-scheduled-scale-down`
- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
