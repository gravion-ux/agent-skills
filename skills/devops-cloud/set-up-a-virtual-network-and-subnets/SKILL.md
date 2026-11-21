---
name: set-up-a-virtual-network-and-subnets
description: Build a virtual network with subnets sized for the workloads that will run in them. Use when the user needs to design or create a cloud network and its subnets.
domain: devops-cloud
tags: [vpc, subnet, network]
triggers: ["set up a virtual network", "create cloud subnets", "design a vpc layout"]
---

# Build a virtual network with subnets sized for the workloads that will run in them

## Purpose

Build a virtual network with subnets sized for the workloads that will run in them.

## When to use

Use when the user needs to design or create a cloud network and its subnets.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List the workloads and decide which need public addresses and which stay private.
2. Size each subnet from the address count the workloads need with room to grow.
3. Attach the subnets to the right availability zones for the region's failover model.
4. Route outbound traffic through the egress path the security policy requires.
5. Verify the routing and DNS resolution from inside each subnet before deploying.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `back-up-and-restore-a-cloud-data-store`
- `set-up-a-canary-environment-for-testing`
- `set-up-a-cd-pipeline-with-safe-rollouts`
