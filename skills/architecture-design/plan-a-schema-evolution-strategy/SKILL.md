---
name: plan-a-schema-evolution-strategy
description: Plan a schema evolution strategy that supports compatible reads, writes, and deployments. Use when the user needs to change a shared schema without breaking existing clients or services.
domain: architecture-design
tags: [schema-evolution, compatibility, backfill]
triggers: ["schema evolution strategy", "change a shared database schema", "expand migrate contract plan"]
---

# Plan a schema evolution strategy that supports compatible reads, writes, and deployments

## Purpose

Plan a schema evolution strategy that supports compatible reads, writes, and deployments.

## When to use

Use when the user needs to change a shared schema without breaking existing clients or services.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Classify each schema change as additive, incompatible, or a semantic alteration.
2. Define the producer, consumer, and deployment compatibility windows for the change.
3. Sequence expand, migrate, and contract phases with an explicit verification point between them.
4. Specify backfill tooling, progress checks, restart behavior, and data validation.
5. Define the rollback action for each phase and the point after which rollback is unsafe.
6. Record assumptions about traffic, client versions, and temporary compatibility costs.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `plan-a-zero-downtime-schema-change`
- `design-a-failover-strategy`
- `plan-a-decomposition-of-a-god-service`
