---
name: index-a-slow-query
description: Add a targeted index to a slow database query and prove the latency improvement. Use when the user has a slow SQL query and needs a safe indexing fix.
domain: databases
tags: [indexing, query-performance, sql]
triggers: ["index a slow query", "database query indexing", "speed up a slow SQL query"]
---

# Add a targeted index to a slow database query and prove the latency improvement

## Purpose

Add a targeted index to a slow database query and prove the latency improvement.

## When to use

Use when the user has a slow SQL query and needs a safe indexing fix.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Capture the query plan, latency, and row counts on representative data.
2. Identify the filter, join, or ordering operation causing the slowdown.
3. Choose an index whose leading columns match that operation.
4. Create the index on a production-like copy and rerun the benchmark.
5. Compare before-and-after latency and document the rollback path.

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
- `build-a-search-index-for-entities`
- `cache-a-database-query-safely`
