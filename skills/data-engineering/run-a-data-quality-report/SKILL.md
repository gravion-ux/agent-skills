---
name: run-a-data-quality-report
description: Produce a data quality report covering freshness, row counts, schema drift and null rates. Use when the user wants evidence about whether a pipeline output is fit to consume.
domain: data-engineering
tags: [data-quality, data-observability, reporting]
triggers: ["data quality report", "check pipeline output quality", "freshness and row count checks"]
---

# Produce a data quality report covering freshness, row counts, schema drift and null rates

## Purpose

Produce a data quality report covering freshness, row counts, schema drift and null rates.

## When to use

Use when the user wants evidence about whether a pipeline output is fit to consume.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Select the quality dimensions required by the consumer contract.
2. Run freshness, row-count, schema and null-rate checks against the latest load.
3. Compare each result with the agreed threshold from the data contract.
4. Record failing checks, the owner and the first-seen date in the report.
5. Publish the report with the load identifier so results can be traced.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `run-a-data-governance-review`
- `automate-data-quality-checks`
- `build-a-raw-to-curated-data-layer`
