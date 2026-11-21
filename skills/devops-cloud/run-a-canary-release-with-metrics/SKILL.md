---
name: run-a-canary-release-with-metrics
description: Release a build to a small traffic slice and promote it only when latency and error budgets hold. Use when the user wants to validate a new build in production before a full rollout.
domain: devops-cloud
tags: [canary, release-metrics, slo, rollout]
triggers: ["canary release with metrics", "run a metrics gated canary", "canary traffic rollout"]
---

# Release a build to a small traffic slice and promote it only when latency and error budgets hold

## Purpose

Release a build to a small traffic slice and promote it only when latency and error budgets hold.

## When to use

Use when the user wants to validate a new build in production before a full rollout.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Deploy the candidate build to the canary target with production configuration.
2. Route five percent of live requests to the canary for fifteen minutes.
3. Compare canary error rate and p95 latency against the stable release.
4. Hold the rollout when the canary exceeds the agreed error budget.
5. Promote to fifty percent, then full traffic after each clean check.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `automate-a-release-with-a-pull-request`
- `manage-cost-with-a-scheduled-scale-down`
- `run-a-disaster-recovery-drill`
