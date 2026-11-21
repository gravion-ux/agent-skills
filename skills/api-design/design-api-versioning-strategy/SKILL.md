---
name: design-api-versioning-strategy
description: Selects an API versioning scheme with explicit compatibility and migration rules. Use when the user needs to evolve an API without silently breaking existing consumers.
domain: api-design
tags: [versioning, compatibility, migration]
triggers: ["api versioning strategy", "choose api versioning", "version an api contract"]
---

# Selects an API versioning scheme with explicit compatibility and migration rules

## Purpose

Selects an API versioning scheme with explicit compatibility and migration rules.

## When to use

Use when the user needs to evolve an API without silently breaking existing consumers.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Inventory consumer versions and the response shapes they depend on.
2. Choose URL, header, or media-type versioning for the contract.
3. Define which request and response changes count as backward compatible.
4. Set the version lifecycle, deprecation window, and sunset criteria.
5. Publish a migration note before changing an existing response shape.

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
