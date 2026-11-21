---
name: partition-a-large-table
description: Partition a large database table to make maintenance and pruning predictable. Use when the user needs to manage a table whose size makes indexes or maintenance costly.
domain: databases
tags: [partitioning, large-tables, performance]
triggers: ["partition a large table", "database table partitioning", "split table into partitions"]
---

# Partition a large database table to make maintenance and pruning predictable

## Purpose

Partition a large database table to make maintenance and pruning predictable.

## When to use

Use when the user needs to manage a table whose size makes indexes or maintenance costly.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Measure table size, growth rate, and the dominant maintenance pain.
2. Choose a partition key aligned with retention or query filters.
3. Define partition boundaries that cover future data without resizing hot partitions.
4. Move existing rows and measure pruning, indexes, and write latency.
5. Document attach, detach, and archive procedures for each partition.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `design-a-multi-tenant-table`
- `analyse-a-slow-dashboard-query`
- `audit-a-schema-for-constraints`
