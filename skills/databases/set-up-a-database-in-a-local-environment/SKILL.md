---
name: set-up-a-database-in-a-local-environment
description: Set up a local database with pinned versions, repeatable initialization, and safe credentials. Use when the user needs a reproducible database instance for local development.
domain: databases
tags: [local-development, database-setup, reproducibility]
triggers: ["set up database in local environment", "run a local database", "create reproducible local db"]
---

# Set up a local database with pinned versions, repeatable initialization, and safe credentials

## Purpose

Set up a local database with pinned versions, repeatable initialization, and safe credentials.

## When to use

Use when the user needs a reproducible database instance for local development.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Pin the database engine, version, extensions, and matching client tools.
2. Create an isolated local instance with a dedicated data directory.
3. Apply schema migrations and seed only the minimum required fixtures.
4. Store local credentials outside source-controlled configuration.
5. Verify the service restarts cleanly and local connections succeed.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `verify-a-backup-restore-in-a-staging-environment`
- `cache-a-database-query-safely`
- `choose-a-database-isolation-level`
