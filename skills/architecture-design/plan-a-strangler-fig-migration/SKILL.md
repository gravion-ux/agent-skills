---
name: plan-a-strangler-fig-migration
description: Plan a strangler-fig migration that routes traffic incrementally and preserves a tested rollback path. Use when the user needs to replace a legacy capability without a risky cutover.
domain: architecture-design
tags: [strangler-fig, migration, traffic-routing]
triggers: ["strangler fig migration", "plan an incremental migration", "route traffic from a legacy system"]
---

# Plan a strangler-fig migration that routes traffic incrementally and preserves a tested rollback path

## Purpose

Plan a strangler-fig migration that routes traffic incrementally and preserves a tested rollback path.

## When to use

Use when the user needs to replace a legacy capability without a risky cutover.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define the legacy behavior, target behavior, and the boundary where traffic can be intercepted.
2. Implement a routing facade that can direct requests by tenant, cohort, or route.
3. Move one capability behind the facade and compare both implementations against shared cases.
4. Expand traffic in measurable stages with explicit success and rollback thresholds.
5. Retain compatibility adapters until the legacy path reaches zero traffic.
6. Document the decommission criteria, data cleanup, assumptions, and rollback owner.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `write-a-migration-rollback-plan`
- `plan-a-decomposition-of-a-god-service`
- `plan-a-read-write-split`
