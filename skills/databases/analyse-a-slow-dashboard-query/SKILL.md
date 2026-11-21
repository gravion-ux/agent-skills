---
name: analyse-a-slow-dashboard-query
description: Analyze a slow dashboard query and improve its measured latency without changing results. Use when the user needs to speed up a dashboard query with filters or aggregations.
domain: databases
tags: [dashboards, query-performance, analytics]
triggers: ["analyse a slow dashboard query", "slow analytics dashboard sql", "speed up dashboard query"]
---

# Analyze a slow dashboard query and improve its measured latency without changing results

## Purpose

Analyze a slow dashboard query and improve its measured latency without changing results.

## When to use

Use when the user needs to speed up a dashboard query with filters or aggregations.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Capture the dashboard's exact parameters, latency, and result row counts.
2. Inspect the plan for full scans, repeated aggregates, and wide joins.
3. Verify the query's indexes and grouping match the dashboard filters.
4. Test the proposed rewrite and compare results with the original output.
5. Track p95 latency and database load after release.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `index-a-slow-query`
- `cache-a-database-query-safely`
- `read-a-query-execution-plan`
