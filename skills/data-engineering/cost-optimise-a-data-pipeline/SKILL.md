---
name: cost-optimise-a-data-pipeline
description: Reduce the cost of a data pipeline by finding the stages that consume the most resources. Use when the user wants to lower the compute or storage cost of a data pipeline.
domain: data-engineering
tags: [cost, optimisation, performance]
triggers: ["cost optimise a data pipeline", "reduce the cost of an etl job", "cut warehouse spend on a pipeline"]
---

# Reduce the cost of a data pipeline by finding the stages that consume the most resources

## Purpose

Reduce the cost of a data pipeline by finding the stages that consume the most resources.

## When to use

Use when the user wants to lower the compute or storage cost of a data pipeline.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Measure the cost of each pipeline stage over a representative period.
2. Identify the largest scans, the highest storage tiers and the longest runtimes.
3. Apply the change with the biggest saving first, such as partition pruning or column selection.
4. Re-measure cost and runtime after the change to confirm the saving.
5. Record the trade-off in cost, latency and freshness that the change introduced.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `document-a-data-pipeline`
- `schedule-a-data-pipeline`
- `build-a-raw-to-curated-data-layer`
