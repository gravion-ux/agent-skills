---
name: deduplicate-records-in-a-warehouse
description: Remove duplicate records from a warehouse table while keeping the correct survivor. Use when the user wants to clean duplicate rows out of a warehouse table.
domain: data-engineering
tags: [deduplication, cleanup, warehouse]
triggers: ["deduplicate warehouse records", "remove duplicate rows from a table", "clean duplicate records in a warehouse"]
---

# Remove duplicate records from a warehouse table while keeping the correct survivor

## Purpose

Remove duplicate records from a warehouse table while keeping the correct survivor.

## When to use

Use when the user wants to clean duplicate rows out of a warehouse table.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Identify the business key that should be unique and count the duplicates.
2. Choose the rule that keeps the survivor, such as the latest update timestamp.
3. Back up the table before deleting anything.
4. Delete the losing rows in bounded batches and record the deleted keys.
5. Re-run the uniqueness check and publish the before-and-after counts.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `mask-sensitive-data-in-a-warehouse`
- `expose-a-stream-to-warehouse-sync`
- `implement-idempotent-writes-to-a-warehouse`
