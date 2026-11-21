---
name: design-a-failover-strategy
description: Design a failover strategy with detection, promotion, recovery, and ownership boundaries. Use when the user needs a service or data store to continue operating during a component failure.
domain: architecture-design
tags: [failover, resilience, recovery]
triggers: ["failover strategy design", "plan automatic failover", "service recovery architecture"]
---

# Design a failover strategy with detection, promotion, recovery, and ownership boundaries

## Purpose

Design a failover strategy with detection, promotion, recovery, and ownership boundaries.

## When to use

Use when the user needs a service or data store to continue operating during a component failure.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Identify the failure modes, recovery objectives, and critical dependencies for each component.
2. Define health signals, detection thresholds, and the operator or controller that acts.
3. Specify the promotion order, fencing mechanism, and authority for stateful components.
4. Document degraded behavior, traffic routing, data reconciliation, and recovery validation.
5. Assign incident ownership and define failover drills with pass and rollback criteria.
6. Record assumptions about split brain, partition tolerance, and recovery-time limits.

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
