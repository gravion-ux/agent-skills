---
name: write-a-system-design-document
description: Produce a system design that maps requirements to components, interfaces, data flows, and failure handling. Use when the user needs a reviewed design for a new or substantially changed system.
domain: architecture-design
tags: [system-design, requirements, trade-offs]
triggers: ["system design document", "write a system design document", "architecture design proposal"]
---

# Produce a system design that maps requirements to components, interfaces, data flows, and failure handling

## Purpose

Produce a system design that maps requirements to components, interfaces, data flows, and failure handling.

## When to use

Use when the user needs a reviewed design for a new or substantially changed system.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Collect the functional requirements, non-functional targets, constraints, and existing-system dependencies.
2. Map every requirement to an owning component and mark each uncovered requirement as an open decision.
3. Define each component boundary, interface, data flow, ownership model, and dependency direction.
4. Describe expected failures, detection signals, containment actions, and degraded-mode behavior.
5. Write the migration path, rollback point, and sequencing from the current state.
6. List the assumptions, trade-offs, and unresolved risks, and label the design as a proposal.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-batch-processing-pipeline`
- `design-a-caching-layer`
- `design-a-data-model-for-a-feature`
