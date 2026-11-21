---
name: router-data-engineering
description: Route work in the Data engineering domain to the right leaf skill. Use when a task clearly belongs to data-engineering.
domain: data-engineering
tags: [router, routing, data-engineering]
triggers: ["route a data-engineering task", "which data-engineering skill should I use"]
---

# Data engineering router

## Purpose

List every leaf skill in the data-engineering domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside data-engineering and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `automate-data-quality-checks` | Use when the user wants repeatable quality checks running on a data pipeline. |
| `backfill-a-historical-period` | Use when the user wants to reload historical data into a warehouse table. |
| `build-a-batch-ingestion-job` | Use when the user wants a batch job that pulls data from a source into a warehouse. |
| `build-a-metric-definition` | Use when the user needs one agreed business metric before dashboards or models consume it. |
| `build-a-raw-to-curated-data-layer` | Use when the user wants to shape raw ingested data into a curated layer. |
| `build-a-streaming-ingestion-consumer` | Use when the user wants to consume a live event stream into a data store. |
| `build-an-offline-feature-pipeline` | Use when the user needs historical training data with features computed as of each label time. |
| `cost-optimise-a-data-pipeline` | Use when the user wants to lower the compute or storage cost of a data pipeline. |
| `deduplicate-records-in-a-warehouse` | Use when the user wants to clean duplicate rows out of a warehouse table. |
| `design-a-real-time-aggregation` | Use when the user wants rolling counters updated continuously over event streams. |
| `design-a-semantic-layer` | Use when the user wants analysts and applications to query governed metrics through a single layer. |
| `design-a-slowly-changing-dimension` | Use when the user wants to track attribute changes over time in a dimension table. |
| `design-an-enterprise-wide-naming-convention` | Use when the user wants consistent layer, table and column names across teams. |
| `design-an-ingestion-pipeline` | Use when the user wants to plan how data should move from sources into a warehouse. |
| `document-a-data-pipeline` | Use when the user wants a data pipeline explained for other engineers. |
| `expose-a-stream-to-warehouse-sync` | Use when the user wants events from a broker or api landed continuously in the warehouse. |
| `handle-a-schema-mismatch-between-systems` | Use when the user must join or migrate data whose field types or names differ. |
| `handle-late-arriving-events` | Use when the user wants a pipeline to cope with events that arrive late. |
| `implement-idempotent-writes-to-a-warehouse` | Use when the user wants warehouse writes that can be rerun without duplicating rows. |
| `implement-row-level-access-rules` | Use when the user needs shared warehouse rows restricted by region, tenant or team. |
| `manage-data-encryption-at-rest` | Use when the user needs data at rest encrypted and key handling under explicit control. |
| `manage-schema-evolution-in-a-stream` | Use when the user wants to change the schema of an event stream without breaking consumers. |
| `mask-sensitive-data-in-a-warehouse` | Use when the user wants sensitive columns redacted before non-privileged users query them. |
| `migrate-a-pipeline-to-a-new-engine` | Use when the user wants an existing batch job ported to a different processing engine. |
| `migrate-a-warehouse-to-a-new-platform` | Use when the user wants an existing warehouse and its workloads moved to another platform. |
| `model-an-analytical-star-schema` | Use when the user wants to model an analytics warehouse as facts and conformed dimensions. |
| `monitor-pipeline-freshness` | Use when the user wants to know whether a pipeline is producing fresh data on time. |
| `partition-a-dataset-by-date` | Use when the user wants to partition a large table or dataset by date. |
| `plan-a-consumption-based-cost-model` | Use when the user wants to attribute data platform spend to teams and workloads. |
| `publish-a-dataset-to-a-catalog` | Use when the user wants a production dataset discoverable in the enterprise data catalog. |
| `retry-a-failed-pipeline-run` | Use when the user wants to recover a pipeline run that failed partway through. |
| `run-a-data-governance-review` | Use when the user wants a governance review of a dataset before or after it goes live. |
| `run-a-data-quality-report` | Use when the user wants evidence about whether a pipeline output is fit to consume. |
| `schedule-a-data-pipeline` | Use when the user wants to put a data pipeline on a recurring schedule. |
| `serve-a-feature-set-to-a-model` | Use when the user wants training and serving to read the same feature definitions. |
| `test-a-pipeline-with-synthetic-events` | Use when the user wants to prove a pipeline behaves correctly before real data arrives. |
| `track-data-lineage-across-pipelines` | Use when the user wants to know where a field in the warehouse originally came from. |
| `validate-an-incoming-data-contract` | Use when the user wants to check that incoming data matches an agreed contract. |
| `version-a-dataset` | Use when the user wants each dataset release to be identifiable and reproducible. |
| `write-a-data-access-api` | Use when the user wants an application to read curated warehouse data through a stable endpoint. |
