---
name: model-an-analytical-star-schema
description: Design a star schema that separates facts and dimensions so analysts can query it without joins. Use when the user wants to model an analytics warehouse as facts and conformed dimensions.
domain: data-engineering
tags: [dimensional-modeling, star-schema, warehouse-design]
triggers: ["analytical star schema", "model a star schema warehouse", "design facts and dimensions"]
---

# Design a star schema that separates facts and dimensions so analysts can query it without joins

## Purpose

Design a star schema that separates facts and dimensions so analysts can query it without joins.

## When to use

Use when the user wants to model an analytics warehouse as facts and conformed dimensions.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. List each business event as a fact table with one row per transaction grain.
2. Group descriptive attributes into dimension tables keyed by a surrogate key.
3. Add conformed dimension keys so cross-subject reporting shares one definition.
4. Declare the grain, nullable keys and row estimates in a schema document.
5. Load a small sample and confirm every fact joins to exactly one dimension row.

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
- `design-an-ingestion-pipeline`
