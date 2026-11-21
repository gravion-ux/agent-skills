---
name: plan-a-sharding-strategy
description: Plan database sharding around access patterns, rebalancing, and operational limits. Use when the user needs to split data across multiple database nodes for scale.
domain: databases
tags: [sharding, scalability, data-modeling]
triggers: ["plan a database sharding strategy", "design database shards", "shard a growing database"]
---

# Plan database sharding around access patterns, rebalancing, and operational limits

## Purpose

Plan database sharding around access patterns, rebalancing, and operational limits.

## When to use

Use when the user needs to split data across multiple database nodes for scale.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Measure data size, growth, and the hottest tenant or key ranges.
2. Choose a shard key that keeps common queries on one shard.
3. Define routing, resharding, and rebalancing procedures.
4. Estimate cross-shard query, transaction, and failure overhead.
5. Prototype the plan with skewed data and a node-loss scenario.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `read-a-query-execution-plan`
- `write-a-sql-query-with-a-clear-plan`
- `analyse-a-slow-dashboard-query`
