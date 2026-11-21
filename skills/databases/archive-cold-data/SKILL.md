---
name: archive-cold-data
description: Archive cold database rows to lower storage cost while preserving a traceable copy. Use when the user needs to move rarely accessed data out of an active database.
domain: databases
tags: [archiving, data-retention, storage]
triggers: ["archive cold database data", "move old rows to archive", "database data archival plan"]
---

# Archive cold database rows to lower storage cost while preserving a traceable copy

## Purpose

Archive cold database rows to lower storage cost while preserving a traceable copy.

## When to use

Use when the user needs to move rarely accessed data out of an active database.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Define cold-data criteria from age, access, and retention rules.
2. Select rows and export them with schema, checksums, and timestamps.
3. Verify the exported row count and key ranges against the source.
4. Delete archived rows only after the copy passes restore checks.
5. Record the archive location, retention period, and purge procedure.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `seed-a-database-with-test-data`
- `write-a-data-retention-policy`
- `analyse-a-slow-dashboard-query`
