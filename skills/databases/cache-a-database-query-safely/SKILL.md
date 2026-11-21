---
name: cache-a-database-query-safely
description: Cache database query results safely with explicit invalidation and freshness bounds. Use when the user wants to reduce repeated database reads without serving stale data.
domain: databases
tags: [query-cache, caching, invalidation]
triggers: ["cache a database query safely", "database query caching", "invalidate cached query results"]
---

# Cache database query results safely with explicit invalidation and freshness bounds

## Purpose

Cache database query results safely with explicit invalidation and freshness bounds.

## When to use

Use when the user wants to reduce repeated database reads without serving stale data.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Choose cacheable queries and state the permitted staleness for each result.
2. Define cache keys, time-to-live, and tenant or user scope.
3. Invalidate or version entries from the write path that changes them.
4. Prevent cache stampedes with request coalescing or bounded locking.
5. Compare hit rate, query load, and stale-result rate against the baseline.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `analyse-a-slow-dashboard-query`
- `choose-a-database-isolation-level`
- `index-a-slow-query`
