---
name: plan-a-consumption-based-cost-model
description: Estimate pipeline and storage cost per consumer using measured queries, scan volume and retention. Use when the user wants to attribute data platform spend to teams and workloads.
domain: data-engineering
tags: [cost-optimization, finops, cloud-costs]
triggers: ["consumption based cost model", "estimate pipeline cloud cost", "attribute warehouse spend"]
---

# Estimate pipeline and storage cost per consumer using measured queries, scan volume and retention

## Purpose

Estimate pipeline and storage cost per consumer using measured queries, scan volume and retention.

## When to use

Use when the user wants to attribute data platform spend to teams and workloads.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Collect compute, storage and egress charges for the billing period.
2. Measure scan bytes and query counts per workload over the same window.
3. Assign each workload to its owner and split shared costs by a stated rule.
4. Compute unit cost per job run, per terabyte stored and per query.
5. Flag the top three cost drivers with a concrete optimisation candidate each.

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
- `serve-a-feature-set-to-a-model`
- `backfill-a-historical-period`
