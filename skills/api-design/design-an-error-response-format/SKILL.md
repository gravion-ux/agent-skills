---
name: design-an-error-response-format
description: Defines a consistent machine-readable error envelope for API failures. Use when the user needs clients to handle API failures predictably.
domain: api-design
tags: [errors, error-codes, api-contracts]
triggers: ["api error response format", "standardize api errors", "design a stable error envelope"]
---

# Defines a consistent machine-readable error envelope for API failures

## Purpose

Defines a consistent machine-readable error envelope for API failures.

## When to use

Use when the user needs clients to handle API failures predictably.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Enumerate validation, authorization, rate-limit, and dependency failures.
2. Assign each failure a stable code, HTTP status, and structured detail fields.
3. Keep the top-level error envelope consistent across every endpoint.
4. Mark retryable failures and include safe remediation metadata.
5. Document how clients should branch on the error code.

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
- `design-an-event-streaming-api`
