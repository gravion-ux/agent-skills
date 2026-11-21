---
name: plan-a-release-milestone
description: Plan a release milestone around scope, quality gates, dependencies, communication, and rollback readiness. Use when the user needs to define and prepare a coordinated project release milestone.
domain: project-management
tags: [release-milestone, go-no-go, rollback]
triggers: ["plan a release milestone", "release readiness plan", "prepare a project release"]
---

# Plan a release milestone around scope, quality gates, dependencies, communication, and rollback readiness

## Purpose

Plan a release milestone around scope, quality gates, dependencies, communication, and rollback readiness.

## When to use

Use when the user needs to define and prepare a coordinated project release milestone.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Set the release outcome, target date, audience, and explicit exclusions.
2. List required deliverables, quality gates, approvals, and external dependencies.
3. Assign owners and dates for release preparation, validation, and communication.
4. Define entry criteria, rollback triggers, and the decision deadline for go or no-go.
5. Verify readiness from test and approval evidence before announcing release.

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
- `plan-a-proof-of-concept`
- `track-a-project-budget-against-plan`
