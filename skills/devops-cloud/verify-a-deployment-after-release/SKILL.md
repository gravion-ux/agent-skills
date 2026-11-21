---
name: verify-a-deployment-after-release
description: Confirm a released service is healthy, reachable, and behaving as expected before closing the change. Use when the user wants post-release verification that a deployment completed correctly.
domain: devops-cloud
tags: [verification, post-release, health-check, observability]
triggers: ["verify a deployment after release", "post release deployment verification", "confirm deployment health"]
---

# Confirm a released service is healthy, reachable, and behaving as expected before closing the change

## Purpose

Confirm a released service is healthy, reachable, and behaving as expected before closing the change.

## When to use

Use when the user wants post-release verification that a deployment completed correctly.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Check the deployment status and confirm the expected version serves traffic.
2. Query the health endpoint from inside and outside the target network.
3. Compare error rate and latency for ten minutes against the pre-release baseline.
4. Inspect recent application and platform logs for startup or configuration failures.
5. Record the verification output and any follow-up action in the change ticket.

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
- `design-a-blue-green-deployment`
- `gate-a-deployment-on-quality-checks`
