---
name: collect-and-rank-backlog-items
description: Collect, deduplicate, and rank backlog items using value, risk, effort, and dependency evidence. Use when the user needs a repeatable process for turning incoming requests into a prioritized backlog.
domain: project-management
tags: [backlog, prioritization, triage]
triggers: ["collect and rank backlog items", "prioritize the project backlog", "rank incoming backlog requests"]
---

# Collect, deduplicate, and rank backlog items using value, risk, effort, and dependency evidence

## Purpose

Collect, deduplicate, and rank backlog items using value, risk, effort, and dependency evidence.

## When to use

Use when the user needs a repeatable process for turning incoming requests into a prioritized backlog.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Collect requests with the problem, desired outcome, requester, and business impact.
2. Merge duplicates and flag missing owners, unclear outcomes, or unsupported claims.
3. Score each item for value, effort, risk reduction, and dependency enablement.
4. Rank items within themes and record ties, assumptions, and required reviews.
5. Publish the ranked backlog with the scoring evidence and next review date.

## Output contract

A plan with milestones, owners, dependencies, risks and a status view that stays true.

## Validation checklist

- [ ] Every task has one owner
- [ ] Dependencies and blockers are visible
- [ ] The plan reflects actual status, not the original estimate

## Safety notes

Never report progress that is not backed by delivered work.

## Related skills

- `assign-task-owners-and-dates`
- `close-a-project-and-capture-lessons`
- `break-a-project-into-workstreams`
