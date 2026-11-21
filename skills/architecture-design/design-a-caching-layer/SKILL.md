---
name: design-a-caching-layer
description: Design a cache that reduces load while preserving correctness and predictable invalidation. Use when the user needs to introduce caching into a data-access or service path.
domain: architecture-design
tags: [caching, invalidation, consistency]
triggers: ["cache layer design", "add a caching layer", "cache invalidation architecture"]
---

# Design a cache that reduces load while preserving correctness and predictable invalidation

## Purpose

Design a cache that reduces load while preserving correctness and predictable invalidation.

## When to use

Use when the user needs to introduce caching into a data-access or service path.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Inventory repeated reads, freshness requirements, and the source-of-truth owner.
2. Assign cache keys, value formats, time-to-live values, and ownership for each entry.
3. Choose eviction, admission, and stampede-control policies for the expected load.
4. Define invalidation events and the stale-read policy for each consistency class.
5. Instrument hit rate, load reduction, evictions, and stale-data errors in production.
6. Record the consistency assumptions and disable or bypass the cache when they are violated.

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
- `design-a-data-model-for-a-feature`
- `design-a-failover-strategy`
