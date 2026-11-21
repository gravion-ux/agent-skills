---
name: schedule-a-data-pipeline
description: Schedule a pipeline on a schedule that respects its dependencies and its load window. Use when the user wants to put a data pipeline on a recurring schedule.
domain: data-engineering
tags: [scheduling, orchestration, slate]
triggers: ["schedule a data pipeline", "set a cron schedule for a pipeline", "orchestrate pipeline dependencies"]
---

# Schedule a pipeline on a schedule that respects its dependencies and its load window

## Purpose

Schedule a pipeline on a schedule that respects its dependencies and its load window.

## When to use

Use when the user wants to put a data pipeline on a recurring schedule.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. List the upstream pipelines that must finish before this one starts.
2. Set the schedule from the upstream completion time rather than a fixed clock.
3. Define the overlap behaviour so two runs cannot write the same partition.
4. Give the job a timeout that matches the agreed freshness target.
5. Alert the owning team when a scheduled run misses its start window.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `cost-optimise-a-data-pipeline`
- `document-a-data-pipeline`
- `build-a-raw-to-curated-data-layer`
