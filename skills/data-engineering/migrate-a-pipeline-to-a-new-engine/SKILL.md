---
name: migrate-a-pipeline-to-a-new-engine
description: Move a pipeline to a new execution engine while keeping output, schedule and failure semantics intact. Use when the user wants an existing batch job ported to a different processing engine.
domain: data-engineering
tags: [pipeline-migration, job-porting, orchestration]
triggers: ["migrate pipeline to new engine", "port batch job to new engine", "replace pipeline runtime"]
---

# Move a pipeline to a new execution engine while keeping output, schedule and failure semantics intact

## Purpose

Move a pipeline to a new execution engine while keeping output, schedule and failure semantics intact.

## When to use

Use when the user wants an existing batch job ported to a different processing engine.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Record the current job's schedule, inputs, outputs and retry behaviour.
2. Rebuild the transformation on the new engine against the same source and target.
3. Run both pipelines over the same fixed date window and diff the outputs.
4. Compare row counts, schema and checksums between the old and new results.
5. Switch the schedule only after a dry run writes successfully to a shadow table.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `migrate-a-warehouse-to-a-new-platform`
- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
