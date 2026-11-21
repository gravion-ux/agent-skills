---
name: design-a-rest-resource-model
description: Models API resources as URLs, methods, and relationships. Use when the user needs to shape a REST API around domain resources and consumer workflows.
domain: api-design
tags: [rest, resource-model, http-api]
triggers: ["rest resource model", "model rest resources", "design rest endpoints"]
---

# Models API resources as URLs, methods, and relationships

## Purpose

Models API resources as URLs, methods, and relationships.

## When to use

Use when the user needs to shape a REST API around domain resources and consumer workflows.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Map each consumer task to a resource and an operation.
2. Choose nouns for URLs and standard HTTP methods for actions.
3. Define resource fields, relationships, and required identifiers.
4. Specify filters, pagination, and idempotency for collection and write operations.
5. Record compatibility rules and migration notes for the contract.

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
- `design-a-search-endpoint`
