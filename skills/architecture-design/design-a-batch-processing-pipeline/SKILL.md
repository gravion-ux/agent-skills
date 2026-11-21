---
name: design-a-batch-processing-pipeline
description: Design a batch pipeline with checkpoints, retries, idempotency, and observable completion. Use when the user needs to process large input volumes reliably through scheduled or streaming jobs.
domain: architecture-design
tags: [batch-processing, checkpoints, pipeline-reliability]
triggers: ["batch processing pipeline", "design a resilient data job", "checkpointed batch architecture"]
---

# Design a batch pipeline with checkpoints, retries, idempotency, and observable completion

## Purpose

Design a batch pipeline with checkpoints, retries, idempotency, and observable completion.

## When to use

Use when the user needs to process large input volumes reliably through scheduled or streaming jobs.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Partition the input into stable batches and define the expected record and batch volumes.
2. Persist a checkpoint after each committed batch so processing can resume safely.
3. Make each write idempotent and send rejected records to a recoverable failure queue.
4. Configure bounded retries, timeouts, backoff, and dead-letter handling per stage.
5. Emit progress, lag, failure-rate, and completion metrics for every scheduled run.
6. Reconcile source and output counts, then record data assumptions and completion criteria.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-file-upload-and-processing-flow`
- `design-a-caching-layer`
- `design-a-data-model-for-a-feature`
