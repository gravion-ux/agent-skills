---
name: build-a-batch-ingestion-job
description: Build a scheduled batch job that loads a source table into a warehouse target. Use when the user wants a batch job that pulls data from a source into a warehouse.
domain: data-engineering
tags: [batch, etl, ingestion]
triggers: ["batch ingestion job", "build a scheduled batch load", "nightly warehouse load job"]
---

# Build a scheduled batch job that loads a source table into a warehouse target

## Purpose

Build a scheduled batch job that loads a source table into a warehouse target.

## When to use

Use when the user wants a batch job that pulls data from a source into a warehouse.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Pin the extraction query and the target table with its exact schema.
2. Read the source in bounded chunks instead of one unbounded query.
3. Write to a staging table first and only publish after the load succeeds.
4. Record the row count and a checksum for the extracted batch.
5. Make the job restartable from the last committed chunk.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-a-streaming-ingestion-consumer`
- `build-a-metric-definition`
- `build-a-raw-to-curated-data-layer`
