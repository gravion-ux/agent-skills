---
name: rate-limit-an-api-endpoint
description: Sets endpoint quotas, client identification, and retry behavior for API traffic. Use when the user needs to protect an endpoint from excessive or abusive requests.
domain: api-design
tags: [rate-limiting, quotas, throttling]
triggers: ["rate limit an api endpoint", "set api request quotas", "design endpoint throttling"]
---

# Sets endpoint quotas, client identification, and retry behavior for API traffic

## Purpose

Sets endpoint quotas, client identification, and retry behavior for API traffic.

## When to use

Use when the user needs to protect an endpoint from excessive or abusive requests.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Identify the request cost, client identity key, and endpoint capacity.
2. Choose sustained, burst, and concurrency limits for each client class.
3. Define the rate-limit response headers and their reset semantics.
4. Return a stable rate-limit error code with a Retry-After value when exceeded.
5. Document exemptions, client backoff, and how quotas are reviewed.

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
- `plan-an-api-deprecation`
- `plan-an-api-gateway-policy`
