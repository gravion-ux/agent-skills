---
name: design-idempotency-keys
description: Defines idempotency keys so retried mutation requests return one safe outcome. Use when the user needs clients to retry unsafe API mutations without duplicates.
domain: api-design
tags: [idempotency, retries, mutation-safety]
triggers: ["idempotency key design", "support safe api retries", "define idempotent api mutations"]
---

# Defines idempotency keys so retried mutation requests return one safe outcome

## Purpose

Defines idempotency keys so retried mutation requests return one safe outcome.

## When to use

Use when the user needs clients to retry unsafe API mutations without duplicates.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. List the mutation endpoints that support idempotent execution.
2. Specify the key header, key format, storage scope, and retention period.
3. Bind each key to the authenticated client and request fingerprint.
4. Replay the original result for a repeated key and reject a mismatched fingerprint.
5. Document expiry, conflict errors, and the client retry procedure.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-a-bulk-endpoint`
- `design-a-graphql-schema`
- `design-a-rest-resource-model`
