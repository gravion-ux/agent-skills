---
name: tune-a-database-configuration
description: Tune a database setting against measured workload evidence and preserve a rollback path. Use when the user wants to change database configuration to improve performance or reliability.
domain: databases
tags: [configuration, database-tuning, performance]
triggers: ["tune database configuration", "database setting tuning", "adjust database config"]
---

# Tune a database setting against measured workload evidence and preserve a rollback path

## Purpose

Tune a database setting against measured workload evidence and preserve a rollback path.

## When to use

Use when the user wants to change database configuration to improve performance or reliability.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Record the current value, workload profile, and measurable objective.
2. Change one setting at a time on a production-like environment.
3. Measure throughput, latency, resource use, and errors before and after.
4. Verify that logs and replication behavior remain healthy.
5. Apply the change with a timed rollback and owner confirmation.

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
- `restore-a-database-from-backup`
