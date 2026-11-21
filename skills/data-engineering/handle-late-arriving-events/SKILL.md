---
name: handle-late-arriving-events
description: Handle events that arrive after their window closed by defining a correction policy. Use when the user wants a pipeline to cope with events that arrive late.
domain: data-engineering
tags: [late-data, events, windows]
triggers: ["handle late arriving events", "process events that arrive out of window", "apply late data corrections"]
---

# Handle events that arrive after their window closed by defining a correction policy

## Purpose

Handle events that arrive after their window closed by defining a correction policy.

## When to use

Use when the user wants a pipeline to cope with events that arrive late.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Set the lateness threshold that the pipeline accepts for each stream.
2. Route events inside the threshold into the current partition.
3. Route events beyond the threshold into a corrections table.
4. Recompute affected aggregates when a corrections batch is applied.
5. Report the late-event rate so the threshold can be tuned deliberately.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `handle-a-schema-mismatch-between-systems`
- `test-a-pipeline-with-synthetic-events`
- `automate-data-quality-checks`
