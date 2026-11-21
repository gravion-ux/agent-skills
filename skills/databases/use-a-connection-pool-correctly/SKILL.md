---
name: use-a-connection-pool-correctly
description: Size and operate a database connection pool without exhausting or leaking connections. Use when the user needs to tune or fix a connection pool under changing workload.
domain: databases
tags: [connection-pool, reliability, performance]
triggers: ["use a connection pool correctly", "tune database connection pool", "fix connection pool exhaustion"]
---

# Size and operate a database connection pool without exhausting or leaking connections

## Purpose

Size and operate a database connection pool without exhausting or leaking connections.

## When to use

Use when the user needs to tune or fix a connection pool under changing workload.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Measure active, idle, wait time, and acquisition timeout for the pool.
2. Size the pool against database limits and concurrent request demand.
3. Set bounded lifetimes, timeouts, and health checks for every connection.
4. Return connections reliably and close them after permanent failures.
5. Load-test the service and alert on pool saturation or leaks.

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
- `audit-a-schema-for-constraints`
- `build-a-search-index-for-entities`
