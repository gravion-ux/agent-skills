---
name: design-api-key-scopes
description: Defines scoped API keys with least-privilege permissions and safe lifecycle controls. Use when the user needs to issue API keys that expose only intended capabilities.
domain: api-design
tags: [api-keys, scopes, access-control]
triggers: ["api key scopes", "define api key permissions", "scope an api access key"]
---

# Defines scoped API keys with least-privilege permissions and safe lifecycle controls

## Purpose

Defines scoped API keys with least-privilege permissions and safe lifecycle controls.

## When to use

Use when the user needs to issue API keys that expose only intended capabilities.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define key ownership, metadata, expiration, and allowed environments.
2. Map scopes to specific operations and resource boundaries.
3. Apply least privilege and deny access when no scope matches.
4. Define rotation, revocation, and audit behavior for every key.
5. Document scope naming and the errors returned for missing permissions.

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
- `design-api-observability-headers`
- `design-api-versioning-strategy`
