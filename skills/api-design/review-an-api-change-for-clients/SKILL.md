---
name: review-an-api-change-for-clients
description: Reviews an API change for client breakage, compatibility, and migration impact. Use when the user needs to assess how a proposed contract change affects existing consumers.
domain: api-design
tags: [client-compatibility, change-review, migration]
triggers: ["review an api change for clients", "assess client breaking changes", "check api migration impact"]
---

# Reviews an API change for client breakage, compatibility, and migration impact

## Purpose

Reviews an API change for client breakage, compatibility, and migration impact.

## When to use

Use when the user needs to assess how a proposed contract change affects existing consumers.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Diff the current and proposed requests, responses, and status codes.
2. Identify changed fields, defaults, validation rules, and ordering guarantees.
3. Check authentication, pagination, error codes, and idempotency for client impact.
4. Require a version bump and migration note before changing a response shape.
5. Publish a client impact checklist with rollout and rollback steps.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `review-an-api-for-consistency`
- `design-an-event-streaming-api`
- `plan-an-api-deprecation`
