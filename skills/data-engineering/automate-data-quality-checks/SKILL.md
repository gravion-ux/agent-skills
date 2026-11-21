---
name: automate-data-quality-checks
description: Automate data quality checks so every load is tested against agreed expectations. Use when the user wants repeatable quality checks running on a data pipeline.
domain: data-engineering
tags: [quality, checks, monitoring]
triggers: ["automate data quality checks", "run quality tests on every load", "add data quality assertions to a pipeline"]
---

# Automate data quality checks so every load is tested against agreed expectations

## Purpose

Automate data quality checks so every load is tested against agreed expectations.

## When to use

Use when the user wants repeatable quality checks running on a data pipeline.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Define the quality dimensions to test, such as completeness, validity and uniqueness.
2. Write one check per dimension with an explicit pass threshold.
3. Run the checks after each load and fail the load when a threshold breaks.
4. Store the check results per run so trends are visible over time.
5. Alert the owning team when the same check fails repeatedly.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `run-a-data-quality-report`
- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
