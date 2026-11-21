---
name: set-up-a-project-dashboard
description: Set up a project dashboard that shows owners, dependencies, milestone health, and evidence-backed status. Use when the user needs a live, shared view of project delivery status.
domain: project-management
tags: [project-dashboard, visibility, status-tracking]
triggers: ["set up a project dashboard", "project delivery dashboard", "build a milestone status dashboard"]
---

# Set up a project dashboard that shows owners, dependencies, milestone health, and evidence-backed status

## Purpose

Set up a project dashboard that shows owners, dependencies, milestone health, and evidence-backed status.

## When to use

Use when the user needs a live, shared view of project delivery status.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Choose dashboard fields for tasks, owners, dates, dependencies, risks, and milestones.
2. Link each task to its source artefact and define a status-update rule.
3. Configure views for current status, blockers, upcoming milestones, and overdue work.
4. Assign dashboard owners for data quality and review cadence.
5. Reject status changes that lack delivered-work evidence and record corrections.

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
