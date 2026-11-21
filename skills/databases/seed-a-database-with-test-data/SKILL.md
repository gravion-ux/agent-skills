---
name: seed-a-database-with-test-data
description: Seed a test database with valid, deterministic fixtures that cover key constraints. Use when the user needs repeatable test data for development or automated checks.
domain: databases
tags: [test-data, database-seeding, fixtures]
triggers: ["seed database with test data", "create deterministic test fixtures", "load sample database records"]
---

# Seed a test database with valid, deterministic fixtures that cover key constraints

## Purpose

Seed a test database with valid, deterministic fixtures that cover key constraints.

## When to use

Use when the user needs repeatable test data for development or automated checks.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. List the fixtures needed to cover core entities and relationships.
2. Make each fixture deterministic, valid, and small enough for fast tests.
3. Include edge cases for required fields, uniqueness, and boundaries.
4. Load fixtures through the same constraints used by production writes.
5. Reset the database and rerun the seed to confirm repeatability.

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
