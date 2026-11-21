---
name: design-a-graphql-schema
description: Designs a GraphQL type system with queries, mutations, connections, and safe errors. Use when the user needs a GraphQL schema that exposes a coherent domain model.
domain: api-design
tags: [graphql, schema-design, type-system]
triggers: ["graphql schema design", "design graphql connections", "model graphql mutations"]
---

# Designs a GraphQL type system with queries, mutations, connections, and safe errors

## Purpose

Designs a GraphQL type system with queries, mutations, connections, and safe errors.

## When to use

Use when the user needs a GraphQL schema that exposes a coherent domain model.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define object, input, enum, and scalar types with explicit nullability.
2. Model queries, mutations, and connection-based pagination.
3. Define mutation inputs, outputs, and authorization behavior.
4. Specify stable error codes through GraphQL extensions.
5. Hide internal fields and document the schema version and compatibility policy.

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
- `design-a-rest-resource-model`
- `design-a-search-endpoint`
