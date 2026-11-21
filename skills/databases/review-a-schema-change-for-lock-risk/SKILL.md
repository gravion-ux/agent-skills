---
name: review-a-schema-change-for-lock-risk
description: Review a database schema change for blocking locks, rewrite risk, and safe execution order. Use when the user needs to assess a proposed schema change before production deployment.
domain: databases
tags: [schema-review, locking, deployment-safety]
triggers: ["review schema change for lock risk", "database ddl lock review", "assess migration lock risk"]
---

# Review a database schema change for blocking locks, rewrite risk, and safe execution order

## Purpose

Review a database schema change for blocking locks, rewrite risk, and safe execution order.

## When to use

Use when the user needs to assess a proposed schema change before production deployment.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Read the engine's behavior for the exact DDL and target data volume.
2. Identify metadata locks, table rewrites, and blocking write paths.
3. Estimate lock duration and choose an equivalent lower-risk operation.
4. Require a production-like copy run and a confirmed backup for destructive steps.
5. Document the execution order, monitoring signals, and rollback path.

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
- `build-a-search-index-for-entities`
- `design-a-normalised-schema`
