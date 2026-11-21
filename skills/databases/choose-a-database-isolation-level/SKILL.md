---
name: choose-a-database-isolation-level
description: Choose a database isolation level that balances consistency with concurrent write throughput. Use when the user needs to select transaction isolation for a correctness-critical workload.
domain: databases
tags: [transactions, isolation-level, concurrency]
triggers: ["choose database isolation level", "select sql transaction isolation", "balance consistency and concurrency"]
---

# Choose a database isolation level that balances consistency with concurrent write throughput

## Purpose

Choose a database isolation level that balances consistency with concurrent write throughput.

## When to use

Use when the user needs to select transaction isolation for a correctness-critical workload.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. List the anomalies each transaction must prevent and tolerate.
2. Compare read committed, repeatable read, and serializable behavior.
3. Measure conflict rate and latency under the expected concurrency.
4. Choose the lowest level that satisfies the stated anomaly requirements.
5. Add retry handling for serialization failures and lock timeouts.

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
- `choose-a-primary-key`
- `restore-a-database-from-backup`
