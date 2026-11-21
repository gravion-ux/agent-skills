---
name: define-service-boundaries
description: Define service boundaries around business capabilities, data ownership, and change cadence. Use when the user needs to split a system into cohesive, independently owned services.
domain: architecture-design
tags: [service-boundaries, domain-ownership, interfaces]
triggers: ["define service boundaries", "split a system into services", "bounded context service design"]
---

# Define service boundaries around business capabilities, data ownership, and change cadence

## Purpose

Define service boundaries around business capabilities, data ownership, and change cadence.

## When to use

Use when the user needs to split a system into cohesive, independently owned services.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Model the business capabilities and the domain language used by each team.
2. Assign one owning service to each capability and each authoritative data set.
3. Define the interface, data contract, latency target, and failure policy at every boundary.
4. Remove calls that require shared tables or coordinated transactions across boundaries.
5. Check that each boundary can change, deploy, and scale without hidden shared state.
6. Record dependency assumptions and unresolved ownership disputes for review.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `evaluate-a-third-party-service`
- `plan-a-decomposition-of-a-god-service`
- `assess-a-technical-proposal`
