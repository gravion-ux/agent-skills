---
name: restore-a-database-from-backup
description: Restore a database backup into an isolated target and prove it matches the source. Use when the user needs to recover a database from a backup without risking production.
domain: databases
tags: [backup-restore, disaster-recovery, data-integrity]
triggers: ["restore database from backup", "database backup recovery", "restore a backup to staging"]
---

# Restore a database backup into an isolated target and prove it matches the source

## Purpose

Restore a database backup into an isolated target and prove it matches the source.

## When to use

Use when the user needs to recover a database from a backup without risking production.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Identify the backup, engine version, and recovery point to restore.
2. Restore into an isolated instance with credentials and network access restricted.
3. Check the recovered schema, row counts, and critical table constraints.
4. Run integrity checks and a representative application smoke test.
5. Document the recovery time, recovery point, and production cutover steps.

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
