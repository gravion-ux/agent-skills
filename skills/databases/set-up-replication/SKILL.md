---
name: set-up-replication
description: Set up database replication with explicit consistency, lag, and failover expectations. Use when the user needs to replicate a database to a standby or read replica.
domain: databases
tags: [replication, high-availability, database-operations]
triggers: ["set up database replication", "configure postgres replication", "create a read replica"]
---

# Set up database replication with explicit consistency, lag, and failover expectations

## Purpose

Set up database replication with explicit consistency, lag, and failover expectations.

## When to use

Use when the user needs to replicate a database to a standby or read replica.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Confirm engine versions, storage settings, and network access for replication.
2. Configure credentials, WAL or binlog settings, and the replication user.
3. Create the replica from a consistent snapshot or base backup.
4. Measure initial synchronization and steady-state replication lag.
5. Document promotion, rejoin, and rollback steps for the replica.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `set-up-a-database-in-a-local-environment`
- `detect-and-fix-replication-lag`
- `analyse-a-slow-dashboard-query`
