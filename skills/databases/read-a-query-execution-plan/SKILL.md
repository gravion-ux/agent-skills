---
name: read-a-query-execution-plan
description: Read a database execution plan and identify the operation that dominates query cost. Use when the user wants to diagnose a query using its execution plan.
domain: databases
tags: [query-plan, performance-analysis, sql]
triggers: ["read a query execution plan", "explain database query plan", "analyze SQL execution plan"]
---

# Read a database execution plan and identify the operation that dominates query cost

## Purpose

Read a database execution plan and identify the operation that dominates query cost.

## When to use

Use when the user wants to diagnose a query using its execution plan.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Capture the execution plan for the statement with actual row counts.
2. Compare estimated and actual rows at each scan and join node.
3. Find the node with the largest time, rows, or repeated inner access.
4. Check indexes, join order, and filters against that expensive node.
5. Record one testable change and its expected cost reduction.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `write-a-sql-query-with-a-clear-plan`
- `analyse-a-slow-dashboard-query`
- `cache-a-database-query-safely`
