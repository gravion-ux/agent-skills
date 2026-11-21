---
name: test-a-pipeline-with-synthetic-events
description: Test a pipeline with synthetic events that reproduce the cases real data misses. Use when the user wants to prove a pipeline behaves correctly before real data arrives.
domain: data-engineering
tags: [testing, synthetic, fixtures]
triggers: ["test a pipeline with synthetic events", "generate synthetic test events for a pipeline", "use a fixed seed to test a data job"]
---

# Test a pipeline with synthetic events that reproduce the cases real data misses

## Purpose

Test a pipeline with synthetic events that reproduce the cases real data misses.

## When to use

Use when the user wants to prove a pipeline behaves correctly before real data arrives.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. List the cases to cover, such as duplicates, out-of-order events and malformed records.
2. Generate a synthetic event for each case with a fixed seed so runs repeat.
3. Run the pipeline against the synthetic input and capture the output.
4. Assert the expected row counts, partitions and error handling for each case.
5. Keep the synthetic set in the repository as a regression fixture.

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
- `migrate-a-pipeline-to-a-new-engine`
