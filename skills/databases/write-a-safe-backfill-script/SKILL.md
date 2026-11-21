---
name: write-a-safe-backfill-script
description: Write a resumable backfill script with batching, checks, and rollback controls. Use when the user needs to populate a new database column or table from existing rows.
domain: databases
tags: [backfill, data-migration, reliability]
triggers: ["write a safe backfill script", "resumable database backfill", "backfill rows in batches"]
---

# Write a resumable backfill script with batching, checks, and rollback controls

## Purpose

Write a resumable backfill script with batching, checks, and rollback controls.

## When to use

Use when the user needs to populate a new database column or table from existing rows.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Define the source rows, destination values, and completion predicate.
2. Process records in small primary-key batches within transaction limits.
3. Make each batch idempotent and checkpoint its progress.
4. Measure lock time, write volume, and error rate during a sample run.
5. Document the stop, resume, repair, and rollback procedure.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `write-a-data-retention-policy`
- `write-a-sql-query-with-a-clear-plan`
- `analyse-a-slow-dashboard-query`
