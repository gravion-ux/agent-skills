---
name: monitor-pipeline-freshness
description: Monitor pipeline freshness so stale output is detected before anyone depends on it. Use when the user wants to know whether a pipeline is producing fresh data on time.
domain: data-engineering
tags: [freshness, monitoring, sla]
triggers: ["monitor pipeline freshness", "detect stale warehouse data", "track how old the latest data is"]
---

# Monitor pipeline freshness so stale output is detected before anyone depends on it

## Purpose

Monitor pipeline freshness so stale output is detected before anyone depends on it.

## When to use

Use when the user wants to know whether a pipeline is producing fresh data on time.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Record the agreed freshness target for every published dataset.
2. Measure the time of the newest successful partition for each dataset.
3. Compare the measured freshness against the target on a fixed interval.
4. Alert with the dataset name, the measured lag and the last successful run.
5. Track the freshness trend so a slow degradation is visible early.

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
- `cost-optimise-a-data-pipeline`
- `design-an-ingestion-pipeline`
