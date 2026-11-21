---
name: model-a-many-to-many-relationship
description: Model a many-to-many relationship with a well-constrained junction table. Use when the user needs two entities to have a repeatable two-way relationship.
domain: databases
tags: [many-to-many, junction-table, schema-design]
triggers: ["model a many-to-many relationship", "design many-to-many junction table", "database many-to-many mapping"]
---

# Model a many-to-many relationship with a well-constrained junction table

## Purpose

Model a many-to-many relationship with a well-constrained junction table.

## When to use

Use when the user needs two entities to have a repeatable two-way relationship.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Define the junction table and the two foreign keys it requires.
2. Make the pair of foreign keys the composite primary key.
3. Add columns for relationship-specific attributes and timestamps.
4. Define cascade or restrict behavior for both entity references.
5. Verify duplicate pairs, orphan rows, and join queries are prevented.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `model-a-one-to-many-relationship`
- `analyse-a-slow-dashboard-query`
- `audit-a-schema-for-constraints`
