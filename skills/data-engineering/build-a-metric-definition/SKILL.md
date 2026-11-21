---
name: build-a-metric-definition
description: Write a metric definition that fixes the numerator, denominator, grain and owner for one business number. Use when the user needs one agreed business metric before dashboards or models consume it.
domain: data-engineering
tags: [metric-definition, business-metrics, governance]
triggers: ["metric definition", "define a business metric", "write a metric spec"]
---

# Write a metric definition that fixes the numerator, denominator, grain and owner for one business number

## Purpose

Write a metric definition that fixes the numerator, denominator, grain and owner for one business number.

## When to use

Use when the user needs one agreed business metric before dashboards or models consume it.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Write the metric name, business purpose and accountable owner.
2. Define the numerator, denominator and the exact filter predicates.
3. State the grain, time window and the source columns used.
4. Attach a worked example with expected values for a known date.
5. Save the definition with a query template and a review date.

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
- `build-a-raw-to-curated-data-layer`
- `build-a-streaming-ingestion-consumer`
