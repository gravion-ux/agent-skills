---
name: design-api-observability-headers
description: Defines request, rate-limit, and diagnostic headers for traceable API calls. Use when the user needs clients and operators to correlate requests across services.
domain: api-design
tags: [observability, request-tracing, headers]
triggers: ["api observability headers", "propagate a request id header", "design tracing response headers"]
---

# Defines request, rate-limit, and diagnostic headers for traceable API calls

## Purpose

Defines request, rate-limit, and diagnostic headers for traceable API calls.

## When to use

Use when the user needs clients and operators to correlate requests across services.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Choose a request identifier and define where it is generated.
2. Propagate or return the identifier on every response and error.
3. Add rate-limit and retry headers when clients need operational guidance.
4. Exclude credentials, personal data, and internal topology from header values.
5. Document header names, precedence, and retention in support workflows.

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
- `design-api-versioning-strategy`
