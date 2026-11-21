---
name: denormalise-for-read-performance
description: Denormalise selected database fields to remove costly joins on measured read paths. Use when the user needs a faster read model but can tolerate controlled data duplication.
domain: databases
tags: [denormalization, read-performance, data-modeling]
triggers: ["denormalise for read performance", "denormalize database tables", "reduce joins on reads"]
---

# Denormalise selected database fields to remove costly joins on measured read paths

## Purpose

Denormalise selected database fields to remove costly joins on measured read paths.

## When to use

Use when the user needs a faster read model but can tolerate controlled data duplication.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Measure the join-heavy read path and record its latency baseline.
2. Choose only the fields required by that read path.
3. Define the source of truth and the event that refreshes the copy.
4. Add a consistency check and a repair path for stale values.
5. Compare read latency, storage, and write cost after the change.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `audit-a-schema-for-constraints`
- `build-a-search-index-for-entities`
- `read-a-query-execution-plan`
