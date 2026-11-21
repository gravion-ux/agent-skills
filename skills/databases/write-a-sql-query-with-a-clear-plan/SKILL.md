---
name: write-a-sql-query-with-a-clear-plan
description: Write a SQL query from a clear execution plan, data model, and expected result shape. Use when the user needs a database query written for a stated result and access pattern.
domain: databases
tags: [sql, query-planning, relational]
triggers: ["write a SQL query", "SQL query plan", "build a database query"]
---

# Write a SQL query from a clear execution plan, data model, and expected result shape

## Purpose

Write a SQL query from a clear execution plan, data model, and expected result shape.

## When to use

Use when the user needs a database query written for a stated result and access pattern.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Write the expected result columns and row grain in one sentence.
2. Map each output column to its source table and join key.
3. Add filters that match the access pattern and preserve required rows.
4. Predict the join order and row-count growth before writing SQL.
5. Run the query against representative data and compare it with the expected shape.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `read-a-query-execution-plan`
- `analyse-a-slow-dashboard-query`
- `cache-a-database-query-safely`
