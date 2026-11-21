---
name: partition-a-dataset-by-date
description: Split a dataset into date partitions so reads and maintenance stay bounded. Use when the user wants to partition a large table or dataset by date.
domain: data-engineering
tags: [partitioning, dates, storage]
triggers: ["partition a dataset by date", "date partition a table", "add date partitions for pruning"]
---

# Split a dataset into date partitions so reads and maintenance stay bounded

## Purpose

Split a dataset into date partitions so reads and maintenance stay bounded.

## When to use

Use when the user wants to partition a large table or dataset by date.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Choose the date column that reflects when the record became true.
2. Pick a partition interval that keeps each partition a manageable size.
3. Apply the partitioning rule to both new writes and historical data.
4. Add pruning rules so queries scan only the partitions they need.
5. Record the retention policy for how long old partitions are kept.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `publish-a-dataset-to-a-catalog`
- `version-a-dataset`
- `backfill-a-historical-period`
