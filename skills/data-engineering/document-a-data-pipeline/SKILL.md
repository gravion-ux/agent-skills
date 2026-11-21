---
name: document-a-data-pipeline
description: Document a pipeline so another engineer can run, debug and extend it without help. Use when the user wants a data pipeline explained for other engineers.
domain: data-engineering
tags: [documentation, runbook, onboarding]
triggers: ["document a data pipeline", "write a pipeline runbook", "explain an etl job for other engineers"]
---

# Document a pipeline so another engineer can run, debug and extend it without help

## Purpose

Document a pipeline so another engineer can run, debug and extend it without help.

## When to use

Use when the user wants a data pipeline explained for other engineers.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Describe the purpose of the pipeline and the consumer of its output.
2. List every source, target, schedule and dependency in one diagram or table.
3. Document the schema contract, the freshness target and the alert thresholds.
4. Record the common failure modes and the exact recovery command for each.
5. Name the owning team and the review date for the document.

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
- `schedule-a-data-pipeline`
- `build-a-raw-to-curated-data-layer`
