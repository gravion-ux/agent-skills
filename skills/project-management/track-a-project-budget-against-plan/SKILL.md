---
name: track-a-project-budget-against-plan
description: Track a project budget against plan by recording commitments, actual spend, variances, and forecast outcomes. Use when the user needs to monitor project spending and forecast the final budget position.
domain: project-management
tags: [budget, cost-tracking, variance]
triggers: ["track a project budget against plan", "project budget variance", "monitor project spend versus plan"]
---

# Track a project budget against plan by recording commitments, actual spend, variances, and forecast outcomes

## Purpose

Track a project budget against plan by recording commitments, actual spend, variances, and forecast outcomes.

## When to use

Use when the user needs to monitor project spending and forecast the final budget position.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Reconcile each approved budget line with invoices, commitments, and receipts.
2. Record actual spend separately from committed and forecast future costs.
3. Calculate variance by budget line and identify recurring or one-time drivers.
4. Flag any forecast overspend with its cause, impact, and proposed response.
5. Publish the spend position and the next review date without hiding variances.

## Output contract

A plan with milestones, owners, dependencies, risks and a status view that stays true.

## Validation checklist

- [ ] Every task has one owner
- [ ] Dependencies and blockers are visible
- [ ] The plan reflects actual status, not the original estimate

## Safety notes

Never report progress that is not backed by delivered work.

## Related skills

- `plan-a-project-handover`
- `track-a-project-milestone`
- `write-a-project-plan`
