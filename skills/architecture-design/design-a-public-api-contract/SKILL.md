---
name: design-a-public-api-contract
description: Specify a versioned public API with resources, errors, compatibility, and usage policies. Use when the user needs a stable contract for an API consumed by clients outside the team.
domain: architecture-design
tags: [api-contract, versioning, compatibility]
triggers: ["public api contract", "design a versioned api", "api compatibility specification"]
---

# Specify a versioned public API with resources, errors, compatibility, and usage policies

## Purpose

Specify a versioned public API with resources, errors, compatibility, and usage policies.

## When to use

Use when the user needs a stable contract for an API consumed by clients outside the team.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define the public resources, operations, identifiers, and representation formats.
2. Specify validation rules, error bodies, status codes, pagination, and idempotency behavior.
3. Set authentication scopes, authorization checks, rate limits, and versioning expectations.
4. Document compatibility guarantees and the deprecation process for removable changes.
5. Create contract examples for successful and failed requests.
6. State the assumptions, review owners, and change-control process for the contract.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-batch-processing-pipeline`
- `design-a-caching-layer`
- `design-a-data-model-for-a-feature`
