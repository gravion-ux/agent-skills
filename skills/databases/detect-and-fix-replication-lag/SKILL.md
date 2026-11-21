---
name: detect-and-fix-replication-lag
description: Diagnose replication lag from workload, network, and replica state before applying a fix. Use when the user needs to find why a database replica is falling behind.
domain: databases
tags: [replication-lag, monitoring, performance]
triggers: ["detect replication lag", "fix database replica lag", "troubleshoot replication delay"]
---

# Diagnose replication lag from workload, network, and replica state before applying a fix

## Purpose

Diagnose replication lag from workload, network, and replica state before applying a fix.

## When to use

Use when the user needs to find why a database replica is falling behind.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Record lag over time and identify the affected replica and workload window.
2. Check apply progress, long transactions, locks, and blocked queries.
3. Compare network throughput, disk latency, and primary write volume.
4. Fix the confirmed bottleneck on a non-production replica first.
5. Verify lag returns to the agreed threshold and alert thresholds cover regressions.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `set-up-replication`
- `analyse-a-slow-dashboard-query`
- `archive-cold-data`
