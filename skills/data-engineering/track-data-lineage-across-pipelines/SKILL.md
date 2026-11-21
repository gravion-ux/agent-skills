---
name: track-data-lineage-across-pipelines
description: Track where every column came from across the pipelines that transform it. Use when the user wants to know where a field in the warehouse originally came from.
domain: data-engineering
tags: [lineage, metadata, provenance]
triggers: ["track data lineage across pipelines", "column level data lineage", "trace a field back to its source"]
---

# Track where every column came from across the pipelines that transform it

## Purpose

Track where every column came from across the pipelines that transform it.

## When to use

Use when the user wants to know where a field in the warehouse originally came from.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Record the source column for each field in every transformation step.
2. Attach the upstream dataset identifier to each output table definition.
3. Propagate the lineage metadata whenever a pipeline writes a new column.
4. Publish the lineage map in a queryable form, not only in the documentation.
5. Verify the map by tracing one important field back to its origin.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `automate-data-quality-checks`
- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
