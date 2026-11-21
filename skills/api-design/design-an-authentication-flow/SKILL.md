---
name: design-an-authentication-flow
description: Designs token authentication with issuance, renewal, revocation, and failure behavior. Use when the user needs an API to authenticate clients safely.
domain: api-design
tags: [authentication, oauth, token-security]
triggers: ["api authentication flow", "design token authentication", "specify an oauth login flow"]
---

# Designs token authentication with issuance, renewal, revocation, and failure behavior

## Purpose

Designs token authentication with issuance, renewal, revocation, and failure behavior.

## When to use

Use when the user needs an API to authenticate clients safely.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the supported principals, credential types, and trust boundaries.
2. Describe token issuance, expiry, refresh, rotation, and revocation.
3. Specify the transport header and the claims each client must present.
4. Define authentication failures with stable error codes and no credential leakage.
5. Require TLS and document safe client-side token storage.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-an-authorization-model`
- `design-an-error-response-format`
- `design-an-event-streaming-api`
