---
name: review-an-api-for-consistency
description: Reviews an API contract for inconsistent naming, payloads, and response behavior. Use when the user wants an existing API checked for contract consistency.
domain: api-design
tags: [api-review, consistency, contracts]
triggers: ["review api consistency", "check api contract conventions", "audit api endpoint consistency"]
---

# Reviews an API contract for inconsistent naming, payloads, and response behavior

## Purpose

Reviews an API contract for inconsistent naming, payloads, and response behavior.

## When to use

Use when the user wants an existing API checked for contract consistency.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Inventory every endpoint, method, payload, and response status.
2. Compare resource naming, parameter names, and media types across endpoints.
3. Check that errors, pagination, filtering, and idempotency follow one pattern.
4. Verify authentication requirements, version markers, and backward compatibility.
5. List each inconsistency by severity with a concrete correction.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `review-an-api-change-for-clients`
- `design-an-event-streaming-api`
- `plan-an-api-deprecation`
