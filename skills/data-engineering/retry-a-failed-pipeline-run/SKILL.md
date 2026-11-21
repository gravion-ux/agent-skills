---
name: retry-a-failed-pipeline-run
description: Retry a failed pipeline run from the last good point without reprocessing clean work. Use when the user wants to recover a pipeline run that failed partway through.
domain: data-engineering
tags: [recovery, retry, failure]
triggers: ["retry a failed pipeline run", "recover a failed data job", "restart a pipeline from the failed stage"]
---

# Retry a failed pipeline run from the last good point without reprocessing clean work

## Purpose

Retry a failed pipeline run from the last good point without reprocessing clean work.

## When to use

Use when the user wants to recover a pipeline run that failed partway through.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Read the failure log and identify the first stage that stopped being correct.
2. Confirm the upstream stages produced complete output before the failure.
3. Clear or quarantine the partial output the failed stage left behind.
4. Restart the run from the failed stage with the same input parameters.
5. Compare the recovered output against the expected row count and schema.

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
