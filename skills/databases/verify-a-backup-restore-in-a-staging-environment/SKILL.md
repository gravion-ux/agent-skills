---
name: verify-a-backup-restore-in-a-staging-environment
description: Verify a backup restore in staging with timed recovery, integrity checks, and evidence. Use when the user needs to prove that backups can be restored into a staging environment.
domain: databases
tags: [backup-restore, staging, disaster-recovery]
triggers: ["verify backup restore in staging", "test database restore in staging", "staging restore drill"]
---

# Verify a backup restore in staging with timed recovery, integrity checks, and evidence

## Purpose

Verify a backup restore in staging with timed recovery, integrity checks, and evidence.

## When to use

Use when the user needs to prove that backups can be restored into a staging environment.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Select a recent backup and record its expected recovery point.
2. Restore it into an isolated staging instance with access controls in place.
3. Measure restore duration and verify schema, row counts, and key ranges.
4. Run integrity checks, constraint validation, and a smoke-test workload.
5. Record evidence, gaps, and the next scheduled restore exercise.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `restore-a-database-from-backup`
- `set-up-a-database-in-a-local-environment`
- `analyse-a-slow-dashboard-query`
