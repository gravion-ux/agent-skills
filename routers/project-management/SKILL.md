---
name: router-project-management
description: Route work in the Project management domain to the right leaf skill. Use when a task clearly belongs to project-management.
domain: project-management
tags: [router, routing, project-management]
triggers: ["route a project-management task", "which project-management skill should I use"]
---

# Project management router

## Purpose

List every leaf skill in the project-management domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside project-management and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for the technical design of the work; use architecture-design instead.

## Inputs required

- The goal, deadline and constraints
- The people and their capacity
- The dependencies outside the team's control

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A plan with milestones, owners, dependencies, risks and a status view that stays true.

## Validation checklist

- [ ] Every task has one owner
- [ ] Dependencies and blockers are visible
- [ ] The plan reflects actual status, not the original estimate

## Safety notes

Never report progress that is not backed by delivered work.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `assign-task-owners-and-dates` | Use when the user needs to allocate project tasks across people with clear accountability. |
| `break-a-project-into-workstreams` | Use when the user needs to divide a cross-functional project into manageable workstreams. |
| `build-a-project-schedule-with-dependencies` | Use when the user needs to sequence project tasks and expose external dependencies. |
| `close-a-project-and-capture-lessons` | Use when the user needs to close a completed project and preserve its final records. |
| `collect-and-rank-backlog-items` | Use when the user needs a repeatable process for turning incoming requests into a prioritized backlog. |
| `coordinate-two-teams-on-one-delivery` | Use when the user needs two teams to deliver one coordinated outcome without ownership gaps. |
| `estimate-a-project-timeline` | Use when the user needs a defensible project completion estimate from known work and team capacity. |
| `estimate-a-task-with-story-points` | Use when the user needs a relative estimate for a backlog task before committing to it. |
| `maintain-a-project-risk-register` | Use when the user needs a repeatable process for keeping project risks current. |
| `manage-a-scope-change-request` | Use when the user needs to assess a proposed change to committed project scope. |
| `manage-multiple-project-priorities` | Use when the user must sequence several active projects without exceeding the available team's capacity. |
| `plan-a-project-handover` | Use when the user needs to transfer an active project to a new owner or team. |
| `plan-a-proof-of-concept` | Use when the user needs to test a technical or product idea before committing to a full project. |
| `plan-a-release-milestone` | Use when the user needs to define and prepare a coordinated project release milestone. |
| `report-a-schedule-slippage` | Use when the user needs to communicate a delayed project schedule to stakeholders. |
| `resolve-a-project-risk` | Use when the user needs to reduce a specific risk that threatens a project outcome. |
| `run-a-project-kickoff-meeting` | Use when the user needs to start a project with a cross-functional team. |
| `run-a-project-status-review` | Use when the user needs to assess project health and coordinate decisions across contributors. |
| `run-a-sprint-planning-session` | Use when the user needs to plan an upcoming sprint using an ordered and estimated backlog. |
| `run-a-sprint-review` | Use when the user needs to demonstrate sprint outcomes and gather stakeholder feedback. |
| `set-up-a-project-dashboard` | Use when the user needs a live, shared view of project delivery status. |
| `track-a-project-budget-against-plan` | Use when the user needs to monitor project spending and forecast the final budget position. |
| `track-a-project-milestone` | Use when the user needs to assess whether a specific project milestone is on track. |
| `write-a-project-charter` | Use when the user needs agreement on a project's purpose, scope, authority, and success measures. |
| `write-a-project-plan` | Use when the user needs a shared plan for delivering a defined project outcome. |
| `write-a-project-status-email` | Use when the user needs to update stakeholders on project delivery without overstating progress. |
