---
name: implement-row-level-access-rules
description: Apply row-level security so each user sees only the records their role permits in shared tables. Use when the user needs shared warehouse rows restricted by region, tenant or team.
domain: data-engineering
tags: [row-level-security, authorization, access-control]
triggers: ["row level access rules", "restrict rows by role", "apply row level security"]
---

# Apply row-level security so each user sees only the records their role permits in shared tables

## Purpose

Apply row-level security so each user sees only the records their role permits in shared tables.

## When to use

Use when the user needs shared warehouse rows restricted by region, tenant or team.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Map each role to the predicate that defines its visible row set.
2. Create the row-level policy on each protected table with a deny default.
3. Grant the role to the policy and remove broad table grants that bypass it.
4. Test one allowed and one denied query per role using session impersonation.
5. Log denied attempts and review the policy list after each schema change.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `implement-idempotent-writes-to-a-warehouse`
- `write-a-data-access-api`
- `automate-data-quality-checks`
