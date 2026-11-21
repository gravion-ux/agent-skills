---
name: design-a-search-endpoint
description: Defines a searchable collection with query filters, ordering, and bounded results. Use when the user needs an endpoint that finds resources by user-supplied criteria.
domain: api-design
tags: [search, filtering, query-parameters]
triggers: ["api search endpoint", "design a filtered search api", "specify api search pagination"]
---

# Defines a searchable collection with query filters, ordering, and bounded results

## Purpose

Defines a searchable collection with query filters, ordering, and bounded results.

## When to use

Use when the user needs an endpoint that finds resources by user-supplied criteria.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the query grammar, accepted filters, sort fields, and search scope.
2. Specify returned fields, result ordering, and a stable pagination contract.
3. Set maximum limits for query length, filters, page size, and result depth.
4. Define empty, invalid, and partially unavailable search results.
5. Document the response fields, error codes, and expected latency characteristics.

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
