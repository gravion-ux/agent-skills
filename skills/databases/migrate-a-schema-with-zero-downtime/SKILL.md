---
name: migrate-a-schema-with-zero-downtime
description: Migrate a database schema without downtime using expand, backfill, and contract phases. Use when the user needs to change a live table while applications remain available.
domain: databases
tags: [schema-migration, zero-downtime, deployment]
triggers: ["migrate schema with zero downtime", "zero downtime database migration", "expand backfill contract migration"]
---

# Migrate a database schema without downtime using expand, backfill, and contract phases

## Purpose

Migrate a database schema without downtime using expand, backfill, and contract phases.

## When to use

Use when the user needs to change a live table while applications remain available.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Choose an expand, backfill, and contract sequence for the schema change.
2. Add the new structure without removing or renaming the old one.
3. Backfill historical rows with a resumable and observable script.
4. Switch readers and writers, then verify compatibility during the overlap.
5. Remove the old structure only after rollback and cleanup checks pass.

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
- `design-a-normalised-schema`
- `review-a-schema-change-for-lock-risk`
