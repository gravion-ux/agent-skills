---
name: model-a-one-to-many-relationship
description: Model a one-to-many relationship with explicit keys, cardinality, and deletion rules. Use when the user needs to represent a parent entity that owns multiple child records.
domain: databases
tags: [one-to-many, relationships, schema-design]
triggers: ["model a one-to-many relationship", "design one-to-many tables", "parent child database schema"]
---

# Model a one-to-many relationship with explicit keys, cardinality, and deletion rules

## Purpose

Model a one-to-many relationship with explicit keys, cardinality, and deletion rules.

## When to use

Use when the user needs to represent a parent entity that owns multiple child records.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Identify the parent entity and the repeating child attributes.
2. Place the foreign key on the child table and define its cardinality.
3. Choose cascade, restrict, or nullify behavior for parent deletion.
4. Add constraints for required child fields and referential integrity.
5. Test joins, deletion behavior, and growth of the child table.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `model-a-many-to-many-relationship`
- `analyse-a-slow-dashboard-query`
- `audit-a-schema-for-constraints`
