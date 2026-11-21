---
name: plan-a-zero-downtime-schema-change
description: Plan a zero-downtime schema change using expand, migrate, and contract phases. Use when the user needs to alter a live database schema while services remain available.
domain: architecture-design
tags: [zero-downtime, database-migration, backfill]
triggers: ["zero downtime schema change", "live database migration plan", "expand and contract schema rollout"]
---

# Plan a zero-downtime schema change using expand, migrate, and contract phases

## Purpose

Plan a zero-downtime schema change using expand, migrate, and contract phases.

## When to use

Use when the user needs to alter a live database schema while services remain available.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Confirm the current and target schema, read-write paths, and compatibility constraints.
2. Expand the schema with the new structure in a backward-compatible form.
3. Deploy code that can read both forms and write the form required by the migration sequence.
4. Backfill data in bounded batches with checkpoints, validation, and restart controls.
5. Verify traffic, replication lag, and data correctness before removing the old structure.
6. Contract the old schema only after rollback is no longer needed and document that boundary.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `plan-a-schema-evolution-strategy`
- `plan-a-decomposition-of-a-god-service`
- `plan-a-read-write-split`
