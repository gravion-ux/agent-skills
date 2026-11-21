---
name: design-long-running-operations
description: Designs an asynchronous operation resource with status, polling, and completion rules. Use when the user needs an API action that may outlive a normal request timeout.
domain: api-design
tags: [async-operations, polling, job-status]
triggers: ["long running api operation", "design an async job endpoint", "specify api operation polling"]
---

# Designs an asynchronous operation resource with status, polling, and completion rules

## Purpose

Designs an asynchronous operation resource with status, polling, and completion rules.

## When to use

Use when the user needs an API action that may outlive a normal request timeout.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the operation resource and its unique identifier.
2. State the allowed lifecycle states and legal transitions between them.
3. Return an accepted response that includes a status URL and retry guidance.
4. Define polling cadence, cancellation, timeout, and terminal failure behavior.
5. Document the versioned representation returned when the operation completes.

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
