---
name: design-a-normalised-schema
description: Design a normalised schema that removes duplication while preserving required queries. Use when the user needs a relational schema with consistent entities and fewer anomalies.
domain: databases
tags: [normalization, schema-design, relational-modeling]
triggers: ["design a normalised schema", "normalize database schema", "review table normalization"]
---

# Design a normalised schema that removes duplication while preserving required queries

## Purpose

Design a normalised schema that removes duplication while preserving required queries.

## When to use

Use when the user needs a relational schema with consistent entities and fewer anomalies.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Separate repeated facts into entities with atomic attributes.
2. Give every relation a primary key and required foreign keys.
3. Remove transitive and partial dependencies from non-key attributes.
4. Verify that all high-value queries remain joinable without duplicating facts.
5. Document the functional dependencies that justify the structure.

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
- `design-a-multi-tenant-table`
- `migrate-a-schema-with-zero-downtime`
