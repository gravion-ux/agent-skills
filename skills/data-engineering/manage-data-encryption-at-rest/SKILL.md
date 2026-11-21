---
name: manage-data-encryption-at-rest
description: Protect stored data with managed encryption keys, key rotation and access logging for every dataset. Use when the user needs data at rest encrypted and key handling under explicit control.
domain: data-engineering
tags: [encryption, key-management, security]
triggers: ["encryption at rest", "manage encryption keys for data", "encrypt warehouse storage"]
---

# Protect stored data with managed encryption keys, key rotation and access logging for every dataset

## Purpose

Protect stored data with managed encryption keys, key rotation and access logging for every dataset.

## When to use

Use when the user needs data at rest encrypted and key handling under explicit control.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Enable platform encryption on storage for the database, buckets and volumes.
2. Create a customer-managed key with a named rotation policy.
3. Grant the pipeline service account decrypt access and remove human grants.
4. Send key and data-access audit logs to a central retention account.
5. Run an access review confirming only the pipeline role can read plaintext.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `automate-data-quality-checks`
- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
