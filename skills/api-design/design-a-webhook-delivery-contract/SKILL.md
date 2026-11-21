---
name: design-a-webhook-delivery-contract
description: Defines webhook events, signed deliveries, retries, ordering, and consumer handling. Use when the user needs an API to notify external systems about domain events.
domain: api-design
tags: [webhooks, event-delivery, signatures]
triggers: ["webhook delivery contract", "design signed webhooks", "define webhook retry behavior"]
---

# Defines webhook events, signed deliveries, retries, ordering, and consumer handling

## Purpose

Defines webhook events, signed deliveries, retries, ordering, and consumer handling.

## When to use

Use when the user needs an API to notify external systems about domain events.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the event envelope with identifier, type, timestamp, version, and data.
2. Specify delivery attempts, backoff intervals, timeout, and retry limits.
3. Require a signature and publish the verification and secret-rotation procedure.
4. Define acknowledgement status codes, duplicate handling, and event ordering guarantees.
5. Document replay, endpoint disablement, and backward-compatible event changes.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-a-bulk-endpoint`
- `design-a-graphql-schema`
- `design-a-rest-resource-model`
