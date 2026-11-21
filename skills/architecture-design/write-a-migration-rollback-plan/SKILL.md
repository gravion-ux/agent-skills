---
name: write-a-migration-rollback-plan
description: Write a migration rollback plan with triggers, checkpoints, data handling, and decision ownership. Use when the user needs a safe retreat path for a production migration or launch.
domain: architecture-design
tags: [rollback-plan, migration-safety, recovery-procedure]
triggers: ["migration rollback plan", "write a rollback procedure", "production migration retreat plan"]
---

# Write a migration rollback plan with triggers, checkpoints, data handling, and decision ownership

## Purpose

Write a migration rollback plan with triggers, checkpoints, data handling, and decision ownership.

## When to use

Use when the user needs a safe retreat path for a production migration or launch.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define the migration scope, success metrics, rollback triggers, and decision deadline.
2. Inventory pre-migration backups, checkpoints, and configuration snapshots.
3. Map each irreversible data or schema change to a compensating action or explicit stop.
4. Specify the rollback commands, traffic restoration steps, validation checks, and expected duration.
5. Assign the rollback authority and define how rollback decisions are communicated and logged.
6. Test the rollback path and record assumptions about data loss, latency, and recovery limits.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `plan-a-read-write-split`
- `plan-a-strangler-fig-migration`
- `plan-a-decomposition-of-a-god-service`
