---
name: migrate-between-two-database-engines
description: Migrate data between database engines while preserving semantics and proving equivalence. Use when the user needs to move an application from one database engine to another.
domain: databases
tags: [engine-migration, data-portability, database-operations]
triggers: ["migrate between database engines", "move sql database to another engine", "database vendor migration"]
---

# Migrate data between database engines while preserving semantics and proving equivalence

## Purpose

Migrate data between database engines while preserving semantics and proving equivalence.

## When to use

Use when the user needs to move an application from one database engine to another.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Inventory engine-specific types, constraints, functions, and behaviours.
2. Translate the schema and write engine-specific compatibility tests.
3. Migrate production-like data and compare row counts and business results.
4. Run a staged cutover with write reconciliation and a rollback path.
5. Certify the new engine against performance, recovery, and monitoring targets.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `cache-a-database-query-safely`
- `choose-a-database-isolation-level`
- `migrate-a-schema-with-zero-downtime`
