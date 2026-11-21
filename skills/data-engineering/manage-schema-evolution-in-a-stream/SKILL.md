---
name: manage-schema-evolution-in-a-stream
description: Evolve a streaming schema safely by versioning it and tolerating older events. Use when the user wants to change the schema of an event stream without breaking consumers.
domain: data-engineering
tags: [schema, evolution, streaming]
triggers: ["manage schema evolution in a stream", "version an event schema safely", "change a stream schema without breaking consumers"]
---

# Evolve a streaming schema safely by versioning it and tolerating older events

## Purpose

Evolve a streaming schema safely by versioning it and tolerating older events.

## When to use

Use when the user wants to change the schema of an event stream without breaking consumers.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Write the new field as optional and keep the old field for at least one release.
2. Register the new schema version alongside the previous version.
3. Update consumers to read both versions before producers emit the new one.
4. Reject unknown fields rather than failing the whole message.
5. Remove the deprecated field only after every consumer has migrated.

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
- `expose-a-stream-to-warehouse-sync`
- `handle-a-schema-mismatch-between-systems`
