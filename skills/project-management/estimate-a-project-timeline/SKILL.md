---
name: estimate-a-project-timeline
description: Estimate a project timeline from capacity, task dependencies, and explicit uncertainty buffers. Use when the user needs a defensible project completion estimate from known work and team capacity.
domain: project-management
tags: [timeline, capacity, critical-path]
triggers: ["project timeline estimate", "estimate a project timeline", "forecast project completion date"]
---

# Estimate a project timeline from capacity, task dependencies, and explicit uncertainty buffers

## Purpose

Estimate a project timeline from capacity, task dependencies, and explicit uncertainty buffers.

## When to use

Use when the user needs a defensible project completion estimate from known work and team capacity.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Break the outcome into tasks with a named owner and measurable completion condition.
2. Map task dependencies and identify work that must occur in parallel.
3. Convert effort into calendar time using each owner's actual capacity.
4. Add scenario buffers for uncertainty without hiding the critical path.
5. Compare the estimate with the deadline and state any feasible gap.

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
