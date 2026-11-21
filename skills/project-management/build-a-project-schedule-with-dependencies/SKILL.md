---
name: build-a-project-schedule-with-dependencies
description: Build a dependency-aware schedule that exposes sequencing constraints, blockers, and milestone dates. Use when the user needs to sequence project tasks and expose external dependencies.
domain: project-management
tags: [schedule, dependencies, critical-path]
triggers: ["dependency project schedule", "build a project schedule with dependencies", "sequence tasks with blockers"]
---

# Build a dependency-aware schedule that exposes sequencing constraints, blockers, and milestone dates

## Purpose

Build a dependency-aware schedule that exposes sequencing constraints, blockers, and milestone dates.

## When to use

Use when the user needs to sequence project tasks and expose external dependencies.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. List every task, its owner, duration, and completion evidence.
2. Connect finish-to-start and other required task relationships.
3. Identify dependencies owned outside the team and name a contact for each.
4. Calculate milestone dates from the critical path and show current blockers.
5. Verify that each task has one owner and an updated status date.

## Output contract

A plan with milestones, owners, dependencies, risks and a status view that stays true.

## Validation checklist

- [ ] Every task has one owner
- [ ] Dependencies and blockers are visible
- [ ] The plan reflects actual status, not the original estimate

## Safety notes

Never report progress that is not backed by delivered work.

## Related skills

- `break-a-project-into-workstreams`
- `close-a-project-and-capture-lessons`
- `estimate-a-project-timeline`
