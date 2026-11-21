---
name: write-api-documentation-examples
description: Writes copyable API examples that cover normal flows and important failures. Use when the user needs examples that help developers use an API correctly.
domain: api-design
tags: [api-docs, examples, reference]
triggers: ["api documentation examples", "write copyable api examples", "document api errors and pagination"]
---

# Writes copyable API examples that cover normal flows and important failures

## Purpose

Writes copyable API examples that cover normal flows and important failures.

## When to use

Use when the user needs examples that help developers use an API correctly.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Choose representative consumer workflows and the endpoints they call.
2. Write complete request and response examples for each workflow.
3. Include authentication, pagination, and idempotency details where relevant.
4. Add examples for validation errors, authorization failures, and rate limits.
5. Validate every example against the OpenAPI contract and redact secrets.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-an-event-streaming-api`
- `design-api-key-scopes`
- `design-api-observability-headers`
