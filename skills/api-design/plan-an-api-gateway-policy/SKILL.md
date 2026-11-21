---
name: plan-an-api-gateway-policy
description: Plans gateway routing, authentication, quotas, and resilience policies for API routes. Use when the user needs to enforce cross-cutting traffic rules at an API gateway.
domain: api-design
tags: [api-gateway, routing, traffic-policy]
triggers: ["api gateway policy", "plan gateway routing rules", "define api traffic policy"]
---

# Plans gateway routing, authentication, quotas, and resilience policies for API routes

## Purpose

Plans gateway routing, authentication, quotas, and resilience policies for API routes.

## When to use

Use when the user needs to enforce cross-cutting traffic rules at an API gateway.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Inventory routes, consumers, upstream services, and trust boundaries.
2. Define authentication, quota, transformation, and routing rules per route.
3. Set timeouts, retry limits, payload limits, and circuit-breaker behavior.
4. Normalize gateway failures into the API error format.
5. Test each policy and assign ownership for rule updates and incident response.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `plan-an-api-deprecation`
- `design-an-event-streaming-api`
- `rate-limit-an-api-endpoint`
