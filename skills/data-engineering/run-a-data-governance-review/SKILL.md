---
name: run-a-data-governance-review
description: Review a dataset's ownership, retention, access and compliance evidence before production sign-off. Use when the user wants a governance review of a dataset before or after it goes live.
domain: data-engineering
tags: [data-governance, compliance, risk-review]
triggers: ["data governance review", "review dataset governance", "compliance sign-off for data"]
---

# Review a dataset's ownership, retention, access and compliance evidence before production sign-off

## Purpose

Review a dataset's ownership, retention, access and compliance evidence before production sign-off.

## When to use

Use when the user wants a governance review of a dataset before or after it goes live.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Collect the catalogue entry, owner, purpose and downstream consumers.
2. Check retention, residency and classification against the policy set.
3. Review access grants, encryption and audit coverage for restricted fields.
4. Log each finding with severity, owner and due date in the review record.
5. Obtain written approval from the data steward before sign-off.

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
