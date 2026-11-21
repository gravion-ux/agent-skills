---
name: prevent-lost-updates
description: Prevent lost updates with atomic writes, row versions, or explicit transaction locks. Use when the user needs concurrent changes to one record without overwriting each other.
domain: databases
tags: [concurrency, lost-updates, transactions]
triggers: ["prevent lost updates", "database concurrent write conflict", "avoid overwrite race condition"]
---

# Prevent lost updates with atomic writes, row versions, or explicit transaction locks

## Purpose

Prevent lost updates with atomic writes, row versions, or explicit transaction locks.

## When to use

Use when the user needs concurrent changes to one record without overwriting each other.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Reproduce the race with two transactions updating the same row.
2. Choose an atomic update, optimistic version check, or row lock.
3. Return a conflict indicator when the version no longer matches.
4. Add a retry limit and telemetry for rejected updates.
5. Test the chosen mechanism under concurrent load and failure retries.

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
- `archive-cold-data`
- `audit-a-schema-for-constraints`
