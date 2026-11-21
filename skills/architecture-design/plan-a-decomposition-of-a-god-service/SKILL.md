---
name: plan-a-decomposition-of-a-god-service
description: Plan a decomposition of a god service into owned capabilities with incremental extraction. Use when the user needs to split a large service that has unclear or excessive responsibilities.
domain: architecture-design
tags: [god-service, decomposition, incremental-extraction]
triggers: ["god service decomposition", "split a monolith by domain", "extract a capability from a large service"]
---

# Plan a decomposition of a god service into owned capabilities with incremental extraction

## Purpose

Plan a decomposition of a god service into owned capabilities with incremental extraction.

## When to use

Use when the user needs to split a large service that has unclear or excessive responsibilities.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Map the service's routes, jobs, tables, dependencies, and business capabilities.
2. Group responsibilities by domain ownership and identify the least coupled extraction seam.
3. Define the target interface, data ownership, and migration path for the first capability.
4. Route callers through an adapter so traffic can shift without a coordinated cutover.
5. Extract one capability at a time and verify behavior, latency, and failure isolation.
6. Define decommission criteria, remaining monolith obligations, and assumptions for each step.

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
- `plan-a-read-write-split`
- `plan-a-schema-evolution-strategy`
