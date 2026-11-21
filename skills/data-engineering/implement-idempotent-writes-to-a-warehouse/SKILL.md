---
name: implement-idempotent-writes-to-a-warehouse
description: Make warehouse writes safe to repeat by keying every record and merging on conflict. Use when the user wants warehouse writes that can be rerun without duplicating rows.
domain: data-engineering
tags: [idempotency, warehouse, upsert]
triggers: ["idempotent warehouse writes", "make warehouse loads rerunnable", "upsert instead of duplicate inserts"]
---

# Make warehouse writes safe to repeat by keying every record and merging on conflict

## Purpose

Make warehouse writes safe to repeat by keying every record and merging on conflict.

## When to use

Use when the user wants warehouse writes that can be rerun without duplicating rows.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Choose a stable business key for every record the job writes.
2. Enforce a primary key or a unique constraint on that key in the target table.
3. Write with an upsert or merge so a rerun replaces rather than appends.
4. Stamp each record with the source batch identifier and the write time.
5. Replay one batch twice and confirm the row count stays unchanged.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `expose-a-stream-to-warehouse-sync`
- `migrate-a-warehouse-to-a-new-platform`
- `build-a-raw-to-curated-data-layer`
