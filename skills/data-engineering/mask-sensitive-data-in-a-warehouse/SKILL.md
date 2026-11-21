---
name: mask-sensitive-data-in-a-warehouse
description: Mask sensitive fields in the warehouse so analysts see only the columns their role requires. Use when the user wants sensitive columns redacted before non-privileged users query them.
domain: data-engineering
tags: [data-masking, pii, privacy]
triggers: ["mask sensitive data in warehouse", "redact pii columns", "anonymize warehouse tables"]
---

# Mask sensitive fields in the warehouse so analysts see only the columns their role requires

## Purpose

Mask sensitive fields in the warehouse so analysts see only the columns their role requires.

## When to use

Use when the user wants sensitive columns redacted before non-privileged users query them.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Classify each column as public, internal, confidential or restricted.
2. Replace identifiable values with deterministic tokens in a staging view.
3. Keep raw sensitive columns in a restricted schema with audited grants.
4. Compare masked and raw aggregates to confirm totals stay within tolerance.
5. Dry-run the view change in a sandbox before repointing the dashboard.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `deduplicate-records-in-a-warehouse`
- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
