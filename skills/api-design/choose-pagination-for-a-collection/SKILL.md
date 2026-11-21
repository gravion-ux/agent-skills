---
name: choose-pagination-for-a-collection
description: Chooses cursor or offset pagination and defines its collection contract. Use when the user needs a collection endpoint to return stable, navigable results.
domain: api-design
tags: [pagination, collections, api-contracts]
triggers: ["api collection pagination", "choose cursor pagination", "paginate a rest collection"]
---

# Chooses cursor or offset pagination and defines its collection contract

## Purpose

Chooses cursor or offset pagination and defines its collection contract.

## When to use

Use when the user needs a collection endpoint to return stable, navigable results.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Estimate the largest response size and the expected result count.
2. Choose cursor or offset pagination from ordering and mutation requirements.
3. Define the default and maximum page size with a stable sort order.
4. Specify the cursor format and responses for invalid, expired, and final cursors.
5. Document empty results and how clients request the next page.

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
