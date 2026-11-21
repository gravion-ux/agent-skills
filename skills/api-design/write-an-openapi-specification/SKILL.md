---
name: write-an-openapi-specification
description: Writes an OpenAPI contract that captures schemas, operations, and error responses. Use when the user needs an executable or implementation-ready description of an HTTP API.
domain: api-design
tags: [openapi, api-specification, documentation]
triggers: ["openapi specification", "write an openapi spec", "document an http api in openapi"]
---

# Writes an OpenAPI contract that captures schemas, operations, and error responses

## Purpose

Writes an OpenAPI contract that captures schemas, operations, and error responses.

## When to use

Use when the user needs an executable or implementation-ready description of an HTTP API.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the OpenAPI info block, servers, and security schemes.
2. Model reusable request and response schemas under components.
3. Document every path, method, parameter, status, and response body.
4. Represent errors, pagination, filtering, and idempotency in the schema.
5. Run an OpenAPI linter and resolve every warning before publishing.

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
- `design-an-error-response-format`
