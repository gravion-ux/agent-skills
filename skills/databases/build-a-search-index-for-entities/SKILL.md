---
name: build-a-search-index-for-entities
description: Build a searchable entity index with deliberate tokenization, ranking, and freshness rules. Use when the user needs fast text search over application entities.
domain: databases
tags: [search-index, text-search, relevance]
triggers: ["build a search index for entities", "index entities for search", "create an entity search index"]
---

# Build a searchable entity index with deliberate tokenization, ranking, and freshness rules

## Purpose

Build a searchable entity index with deliberate tokenization, ranking, and freshness rules.

## When to use

Use when the user needs fast text search over application entities.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Define the searchable fields, query language, and ranking expectations.
2. Normalize tokens, handle synonyms, and decide which records are excluded.
3. Choose index storage and update events for each entity change.
4. Measure recall, ranking quality, latency, and index size on sample queries.
5. Provide a rebuild path for schema or tokenizer changes.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `audit-a-schema-for-constraints`
- `index-a-slow-query`
- `review-a-schema-change-for-lock-risk`
