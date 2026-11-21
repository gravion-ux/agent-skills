---
name: implement-blue-green-traffic-shifting
description: Shift production traffic between blue and green stacks with weighted routing and a tested rollback. Use when the user wants to release infrastructure changes through a blue-green deployment.
domain: devops-cloud
tags: [blue-green, traffic-shift, load-balancer, release]
triggers: ["blue green traffic shifting", "shift traffic to the green stack", "blue-green deployment routing"]
---

# Shift production traffic between blue and green stacks with weighted routing and a tested rollback

## Purpose

Shift production traffic between blue and green stacks with weighted routing and a tested rollback.

## When to use

Use when the user wants to release infrastructure changes through a blue-green deployment.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Deploy the green stack alongside the unchanged blue stack.
2. Prove the rollback command restores traffic to the blue stack.
3. Shift ten percent of traffic to green and watch error rate and latency.
4. Increase traffic in ten-point steps until green serves all requests.
5. Record the routing weights and final state diff in the release notes.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `design-a-blue-green-deployment`
- `apply-a-cost-budget-to-cloud-resources`
- `audit-cloud-permissions`
