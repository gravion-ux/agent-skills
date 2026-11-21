---
name: plan-an-api-deprecation
description: Plans an API deprecation timeline, migration path, and safe endpoint sunset. Use when the user needs to retire an API version without leaving consumers stranded.
domain: api-design
tags: [deprecation, sunset, migration]
triggers: ["api deprecation plan", "sunset an api version", "schedule an endpoint migration"]
---

# Plans an API deprecation timeline, migration path, and safe endpoint sunset

## Purpose

Plans an API deprecation timeline, migration path, and safe endpoint sunset.

## When to use

Use when the user needs to retire an API version without leaving consumers stranded.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Inventory deprecated endpoints, versions, and known consumer traffic.
2. Define the deprecation criteria and the notice communicated to consumers.
3. Set replacement guidance, migration deadlines, and a sunset date.
4. Publish a migration note before any response shape changes.
5. Monitor remaining usage and retain the old version until migration thresholds are met.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `plan-an-api-gateway-policy`
- `design-an-event-streaming-api`
- `rate-limit-an-api-endpoint`
