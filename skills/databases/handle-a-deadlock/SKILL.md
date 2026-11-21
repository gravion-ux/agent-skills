---
name: handle-a-deadlock
description: Resolve a database deadlock from evidence, a minimal transaction fix, and a regression test. Use when the user needs to diagnose and prevent recurring database deadlocks.
domain: databases
tags: [deadlocks, locking, transactions]
triggers: ["handle a database deadlock", "fix SQL deadlock", "diagnose transaction deadlock"]
---

# Resolve a database deadlock from evidence, a minimal transaction fix, and a regression test

## Purpose

Resolve a database deadlock from evidence, a minimal transaction fix, and a regression test.

## When to use

Use when the user needs to diagnose and prevent recurring database deadlocks.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Capture the deadlock graph, conflicting statements, and transaction scopes.
2. Identify the lock order and the smallest shared resource causing the cycle.
3. Reproduce the deadlock with a concurrent test and a short timeout.
4. Standardize lock order or shorten the transaction in the affected path.
5. Run the regression test and monitor deadlock counts after release.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `analyse-a-slow-dashboard-query`
- `audit-a-schema-for-constraints`
- `build-a-search-index-for-entities`
