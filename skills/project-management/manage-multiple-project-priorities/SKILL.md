---
name: manage-multiple-project-priorities
description: Prioritize multiple projects using shared capacity, deadlines, dependencies, and explicit trade-offs. Use when the user must sequence several active projects without exceeding the available team's capacity.
domain: project-management
tags: [portfolio, prioritization, capacity]
triggers: ["manage multiple project priorities", "prioritize several projects", "balance work across projects"]
---

# Prioritize multiple projects using shared capacity, deadlines, dependencies, and explicit trade-offs

## Purpose

Prioritize multiple projects using shared capacity, deadlines, dependencies, and explicit trade-offs.

## When to use

Use when the user must sequence several active projects without exceeding the available team's capacity.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. List each project's deadline, outcome, committed capacity, and external dependency.
2. Map resource conflicts and identify commitments that cannot run in parallel.
3. Rank projects by urgency, impact, reversibility, and dependency urgency.
4. Reallocate capacity and sequence work with explicit trade-offs for each project.
5. Record the decision, rejected lower priorities, and the date to revisit it.

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
- `build-a-project-schedule-with-dependencies`
- `close-a-project-and-capture-lessons`
