---
name: plan-a-read-write-split
description: Plan a read-write split with replica selection, consistency rules, and failover behavior. Use when the user needs to offload reads from a primary database or service tier.
domain: architecture-design
tags: [read-write-split, replication, consistency]
triggers: ["read write split", "route reads to replicas", "plan database read scaling"]
---

# Plan a read-write split with replica selection, consistency rules, and failover behavior

## Purpose

Plan a read-write split with replica selection, consistency rules, and failover behavior.

## When to use

Use when the user needs to offload reads from a primary database or service tier.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Identify read-heavy operations and their tolerance for replication lag and staleness.
2. Define which replicas or read stores serve each operation and how callers select them.
3. Specify routing, health checks, lag thresholds, and fallback behavior for unavailable replicas.
4. Add consistency tokens or read-after-write checks where the workflow requires them.
5. Plan schema, backfill, deployment, and rollback steps for the new read path.
6. Monitor lag, error rates, and correctness and state the assumptions that bound the split.

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
- `plan-a-schema-evolution-strategy`
