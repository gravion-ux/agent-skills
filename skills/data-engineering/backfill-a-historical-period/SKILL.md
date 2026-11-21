---
name: backfill-a-historical-period
description: Backfill a historical period safely by isolating the run and proving the result. Use when the user wants to reload historical data into a warehouse table.
domain: data-engineering
tags: [backfill, history, warehouse]
triggers: ["backfill a historical period", "reload historic warehouse data", "rewrite old table partitions"]
---

# Backfill a historical period safely by isolating the run and proving the result

## Purpose

Backfill a historical period safely by isolating the run and proving the result.

## When to use

Use when the user wants to reload historical data into a warehouse table.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Define the exact date range and the partitions the backfill will rewrite.
2. Back up the affected partitions before the run starts.
3. Run the backfill into a staging copy first and diff it against production.
4. Swap the staged partitions in only after the diff is reviewed.
5. Record the backfill window, the source snapshot and the reviewer.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-a-batch-ingestion-job`
- `build-a-metric-definition`
- `build-a-raw-to-curated-data-layer`
