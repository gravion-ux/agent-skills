---
name: design-an-event-streaming-api
description: Defines an event stream contract with schemas, delivery semantics, replay, and backpressure. Use when the user needs a streaming API for ordered domain events.
domain: api-design
tags: [event-streaming, messaging, event-contracts]
triggers: ["event streaming api", "design a streaming event contract", "specify event topic retention"]
---

# Defines an event stream contract with schemas, delivery semantics, replay, and backpressure

## Purpose

Defines an event stream contract with schemas, delivery semantics, replay, and backpressure.

## When to use

Use when the user needs a streaming API for ordered domain events.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define event topics, keys, producers, and the fields in each envelope.
2. Specify schema versions and rules for evolving event payloads.
3. Choose delivery, ordering, acknowledgement, and consumer-offset semantics.
4. Define retention, replay, backpressure, and failure handling.
5. Document authentication, rate limits, and observability for the stream.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-an-authentication-flow`
- `design-an-authorization-model`
- `design-an-error-response-format`
