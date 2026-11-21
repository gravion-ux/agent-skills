---
name: design-an-event-driven-workflow
description: Design an event-driven workflow with event contracts, delivery semantics, and recovery paths. Use when the user needs to coordinate asynchronous work through published events.
domain: architecture-design
tags: [event-driven, message-semantics, recovery]
triggers: ["event driven workflow", "design an event workflow", "asynchronous event architecture"]
---

# Design an event-driven workflow with event contracts, delivery semantics, and recovery paths

## Purpose

Design an event-driven workflow with event contracts, delivery semantics, and recovery paths.

## When to use

Use when the user needs to coordinate asynchronous work through published events.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define each business event with its schema, producer, consumers, and ownership.
2. Specify ordering, delivery, retry, deduplication, and retention requirements per event.
3. Choose an outbox or equivalent mechanism for reliable event publication.
4. Make consumers idempotent and define how they record processed messages.
5. Describe dead-letter handling, replay, poison-message isolation, and operational ownership.
6. State the consistency and latency assumptions that the workflow depends on.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-an-idempotent-api`
- `design-a-batch-processing-pipeline`
- `design-a-caching-layer`
