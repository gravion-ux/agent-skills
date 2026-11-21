---
name: router-databases
description: Route work in the Databases domain to the right leaf skill. Use when a task clearly belongs to databases.
domain: databases
tags: [router, routing, databases]
triggers: ["route a databases task", "which databases skill should I use"]
---

# Databases router

## Purpose

List every leaf skill in the databases domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside databases and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `analyse-a-slow-dashboard-query` | Use when the user needs to speed up a dashboard query with filters or aggregations. |
| `archive-cold-data` | Use when the user needs to move rarely accessed data out of an active database. |
| `audit-a-schema-for-constraints` | Use when the user wants to find integrity gaps in an existing database schema. |
| `build-a-search-index-for-entities` | Use when the user needs fast text search over application entities. |
| `cache-a-database-query-safely` | Use when the user wants to reduce repeated database reads without serving stale data. |
| `choose-a-database-isolation-level` | Use when the user needs to select transaction isolation for a correctness-critical workload. |
| `choose-a-primary-key` | Use when the user is selecting a primary key for a new or redesigned table. |
| `denormalise-for-read-performance` | Use when the user needs a faster read model but can tolerate controlled data duplication. |
| `design-a-multi-tenant-table` | Use when the user needs one database to securely hold records for multiple customers. |
| `design-a-normalised-schema` | Use when the user needs a relational schema with consistent entities and fewer anomalies. |
| `detect-and-fix-replication-lag` | Use when the user needs to find why a database replica is falling behind. |
| `full-text-search-in-postgres` | Use when the user needs document or row search using PostgreSQL full-text features. |
| `handle-a-deadlock` | Use when the user needs to diagnose and prevent recurring database deadlocks. |
| `index-a-slow-query` | Use when the user has a slow SQL query and needs a safe indexing fix. |
| `migrate-a-schema-with-zero-downtime` | Use when the user needs to change a live table while applications remain available. |
| `migrate-between-two-database-engines` | Use when the user needs to move an application from one database engine to another. |
| `model-a-many-to-many-relationship` | Use when the user needs two entities to have a repeatable two-way relationship. |
| `model-a-one-to-many-relationship` | Use when the user needs to represent a parent entity that owns multiple child records. |
| `partition-a-large-table` | Use when the user needs to manage a table whose size makes indexes or maintenance costly. |
| `plan-a-sharding-strategy` | Use when the user needs to split data across multiple database nodes for scale. |
| `prevent-lost-updates` | Use when the user needs concurrent changes to one record without overwriting each other. |
| `read-a-query-execution-plan` | Use when the user wants to diagnose a query using its execution plan. |
| `restore-a-database-from-backup` | Use when the user needs to recover a database from a backup without risking production. |
| `review-a-schema-change-for-lock-risk` | Use when the user needs to assess a proposed schema change before production deployment. |
| `seed-a-database-with-test-data` | Use when the user needs repeatable test data for development or automated checks. |
| `set-up-a-database-in-a-local-environment` | Use when the user needs a reproducible database instance for local development. |
| `set-up-replication` | Use when the user needs to replicate a database to a standby or read replica. |
| `tune-a-database-configuration` | Use when the user wants to change database configuration to improve performance or reliability. |
| `use-a-connection-pool-correctly` | Use when the user needs to tune or fix a connection pool under changing workload. |
| `verify-a-backup-restore-in-a-staging-environment` | Use when the user needs to prove that backups can be restored into a staging environment. |
| `write-a-data-retention-policy` | Use when the user needs to define how long database data must be kept and removed. |
| `write-a-safe-backfill-script` | Use when the user needs to populate a new database column or table from existing rows. |
| `write-a-sql-query-with-a-clear-plan` | Use when the user needs a database query written for a stated result and access pattern. |
