---
name: review-an-architecture-diagram
description: Review an architecture diagram for missing components, unclear flows, and unverifiable guarantees. Use when the user needs to check whether a diagram accurately represents a proposed architecture.
domain: architecture-design
tags: [diagram-review, architecture-accuracy, dependency-flow]
triggers: ["architecture diagram review", "check a system diagram", "validate an architecture drawing"]
---

# Review an architecture diagram for missing components, unclear flows, and unverifiable guarantees

## Purpose

Review an architecture diagram for missing components, unclear flows, and unverifiable guarantees.

## When to use

Use when the user needs to check whether a diagram accurately represents a proposed architecture.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Verify that every diagram element has a named purpose, owner, and responsibility boundary.
2. Trace each request, event, and data path through queues, stores, and external dependencies.
3. Check that the diagram shows failure isolation, trust boundaries, and state ownership.
4. Reconcile the diagram with the written requirements and identify unsupported guarantees.
5. Flag ambiguous arrows, missing error paths, unversioned interfaces, and hidden coupling.
6. List corrections, unresolved questions, assumptions, and the reviewers who must approve them.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `write-an-architecture-decision-record`
- `design-an-event-driven-workflow`
- `design-an-idempotent-api`
