---
name: design-an-ingestion-pipeline
description: Design an ingestion pipeline from source systems to a warehouse layer with clear contracts. Use when the user wants to plan how data should move from sources into a warehouse.
domain: data-engineering
tags: [ingestion, pipeline, warehouse]
triggers: ["ingestion pipeline design", "plan data ingestion into a warehouse", "source to warehouse pipeline plan"]
---

# Design an ingestion pipeline from source systems to a warehouse layer with clear contracts

## Purpose

Design an ingestion pipeline from source systems to a warehouse layer with clear contracts.

## When to use

Use when the user wants to plan how data should move from sources into a warehouse.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. List every source system with its owner, update pattern and expected volume.
2. Map each source to the target tables and the columns it supplies.
3. Decide per source whether the load is batch, streaming or both.
4. Define the freshness target and the failure behaviour for each load.
5. Write the pipeline contract covering schema, volume and freshness guarantees.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-an-offline-feature-pipeline`
- `design-an-enterprise-wide-naming-convention`
- `build-a-batch-ingestion-job`
