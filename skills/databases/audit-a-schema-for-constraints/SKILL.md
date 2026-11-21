---
name: audit-a-schema-for-constraints
description: Audit a database schema for missing keys, references, checks, and inconsistent defaults. Use when the user wants to find integrity gaps in an existing database schema.
domain: databases
tags: [schema-audit, constraints, data-integrity]
triggers: ["audit schema for constraints", "review database constraints", "find missing integrity constraints"]
---

# Audit a database schema for missing keys, references, checks, and inconsistent defaults

## Purpose

Audit a database schema for missing keys, references, checks, and inconsistent defaults.

## When to use

Use when the user wants to find integrity gaps in an existing database schema.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Inventory tables, columns, keys, defaults, and declared relationships.
2. Compare actual constraints with the application's write assumptions.
3. Identify missing uniqueness, foreign-key, nullability, and check constraints.
4. Rank gaps by corruption risk and propose non-destructive additions.
5. Validate the proposed constraints on a production-like copy first.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `review-a-schema-change-for-lock-risk`
- `build-a-search-index-for-entities`
- `design-a-normalised-schema`
