---
name: assign-task-owners-and-dates
description: Assign every project task to one accountable owner with a due date and delivery evidence. Use when the user needs to allocate project tasks across people with clear accountability.
domain: project-management
tags: [ownership, task-assignment, accountability]
triggers: ["assign project task owners", "set task owners and dates", "allocate project tasks"]
---

# Assign every project task to one accountable owner with a due date and delivery evidence

## Purpose

Assign every project task to one accountable owner with a due date and delivery evidence.

## When to use

Use when the user needs to allocate project tasks across people with clear accountability.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. List the open tasks and the acceptance condition for each task.
2. Match tasks to people using role, capacity, and required expertise.
3. Assign exactly one accountable owner to every task.
4. Set a due date that reflects dependencies and confirmed capacity.
5. Confirm each owner accepted the task and its due date.

## Output contract

A plan with milestones, owners, dependencies, risks and a status view that stays true.

## Validation checklist

- [ ] Every task has one owner
- [ ] Dependencies and blockers are visible
- [ ] The plan reflects actual status, not the original estimate

## Safety notes

Never report progress that is not backed by delivered work.

## Related skills

- `close-a-project-and-capture-lessons`
- `collect-and-rank-backlog-items`
- `estimate-a-task-with-story-points`
