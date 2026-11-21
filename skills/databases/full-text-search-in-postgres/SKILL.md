---
name: full-text-search-in-postgres
description: Configure PostgreSQL full-text search with ranked queries and a tuned search vector. Use when the user needs document or row search using PostgreSQL full-text features.
domain: databases
tags: [postgres, full-text-search, search-index]
triggers: ["full text search in postgres", "postgres tsvector search", "rank postgres full text results"]
---

# Configure PostgreSQL full-text search with ranked queries and a tuned search vector

## Purpose

Configure PostgreSQL full-text search with ranked queries and a tuned search vector.

## When to use

Use when the user needs document or row search using PostgreSQL full-text features.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Choose the searchable columns and the language-specific text configuration.
2. Build or maintain a search vector with explicit weights for each column.
3. Write ranked queries with filters, indexes, and highlighted results.
4. Measure latency, ranking quality, and index usage with representative queries.
5. Plan how the vector changes when indexed content is edited.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `build-a-search-index-for-entities`
- `set-up-a-database-in-a-local-environment`
- `verify-a-backup-restore-in-a-staging-environment`
