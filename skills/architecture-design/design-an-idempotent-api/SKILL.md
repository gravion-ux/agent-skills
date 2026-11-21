---
name: design-an-idempotent-api
description: Design an idempotent API that safely tolerates retries, duplicates, and partial failures. Use when the user needs an operation that clients can retry without duplicate side effects.
domain: architecture-design
tags: [idempotency, retry-safety, api-design]
triggers: ["idempotent api design", "make an api retry safe", "idempotency key contract"]
---

# Design an idempotent API that safely tolerates retries, duplicates, and partial failures

## Purpose

Design an idempotent API that safely tolerates retries, duplicates, and partial failures.

## When to use

Use when the user needs an operation that clients can retry without duplicate side effects.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define the operation's completion criteria and the exact side effects that must occur once.
2. Choose an idempotency key scope, validation rule, storage period, and conflict response.
3. Specify how the server records and retrieves the result of an in-flight or completed request.
4. Separate retry-safe failures from failures that require operator intervention.
5. Define behavior for concurrent requests, key reuse, and expired request records.
6. Document assumptions about key uniqueness and the safe replay window.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-public-api-contract`
- `design-an-event-driven-workflow`
- `design-a-batch-processing-pipeline`
