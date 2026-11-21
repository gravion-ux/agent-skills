---
name: choose-a-primary-key
description: Choose a primary key that stays stable, unique, compact, and practical for joins. Use when the user is selecting a primary key for a new or redesigned table.
domain: databases
tags: [primary-key, schema-design, data-modeling]
triggers: ["choose a primary key", "database primary key selection", "design a table primary key"]
---

# Choose a primary key that stays stable, unique, compact, and practical for joins

## Purpose

Choose a primary key that stays stable, unique, compact, and practical for joins.

## When to use

Use when the user is selecting a primary key for a new or redesigned table.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. List candidate keys and test each for uniqueness and nullability.
2. Reject keys whose values can change after records are referenced.
3. Compare key width, index overhead, and join compatibility.
4. Check whether the key supports the table's common access patterns.
5. Document the key choice and its migration implications.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `choose-a-database-isolation-level`
- `analyse-a-slow-dashboard-query`
- `audit-a-schema-for-constraints`
