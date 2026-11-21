---
name: design-a-multi-tenant-table
description: Design a multi-tenant table that isolates access while preserving useful indexes. Use when the user needs one database to securely hold records for multiple customers.
domain: databases
tags: [multi-tenancy, row-level-security, schema-design]
triggers: ["design a multi-tenant table", "multi tenant database schema", "tenant isolation table design"]
---

# Design a multi-tenant table that isolates access while preserving useful indexes

## Purpose

Design a multi-tenant table that isolates access while preserving useful indexes.

## When to use

Use when the user needs one database to securely hold records for multiple customers.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Choose the tenant key and include it in every tenant-owned table.
2. Add composite keys and indexes that lead with the tenant identifier.
3. Enforce tenant-scoped foreign keys and unique constraints.
4. Require the tenant identifier in every application query predicate.
5. Test cross-tenant reads, writes, and index usage against realistic volume.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `design-a-normalised-schema`
- `partition-a-large-table`
- `analyse-a-slow-dashboard-query`
