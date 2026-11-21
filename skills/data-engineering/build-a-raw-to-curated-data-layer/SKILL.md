---
name: build-a-raw-to-curated-data-layer
description: Build a curated layer that turns raw ingested files into typed, deduplicated tables. Use when the user wants to shape raw ingested data into a curated layer.
domain: data-engineering
tags: [curated, raw, transform]
triggers: ["raw to curated data layer", "build a curated data layer", "shape raw files into curated tables"]
---

# Build a curated layer that turns raw ingested files into typed, deduplicated tables

## Purpose

Build a curated layer that turns raw ingested files into typed, deduplicated tables.

## When to use

Use when the user wants to shape raw ingested data into a curated layer.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Keep the raw landing zone immutable and untouched by transformation logic.
2. Parse and cast each field to its declared type in the curated layer.
3. Apply the business key and deduplicate before writing curated tables.
4. Record the transformation version that produced each curated table.
5. Publish the curated schema and the freshness of each table.

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
- `build-a-streaming-ingestion-consumer`
