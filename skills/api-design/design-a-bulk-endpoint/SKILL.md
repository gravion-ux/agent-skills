---
name: design-a-bulk-endpoint
description: Designs a bulk API operation with item limits, partial results, and safe retries. Use when the user needs clients to submit or update many items in one request.
domain: api-design
tags: [bulk-operations, batch-processing, error-handling]
triggers: ["bulk api endpoint", "design a batch api operation", "accept many api items"]
---

# Designs a bulk API operation with item limits, partial results, and safe retries

## Purpose

Designs a bulk API operation with item limits, partial results, and safe retries.

## When to use

Use when the user needs clients to submit or update many items in one request.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the request item schema and maximum items per request.
2. Choose synchronous processing or an asynchronous operation for the batch.
3. Return a per-item status and stable error code for every item.
4. Define atomicity, idempotency, and duplicate-item behavior for the batch.
5. Document partial failure handling, quotas, and the versioned response contract.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-a-search-endpoint`
- `design-a-graphql-schema`
- `design-a-rest-resource-model`
