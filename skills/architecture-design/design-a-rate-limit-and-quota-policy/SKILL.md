---
name: design-a-rate-limit-and-quota-policy
description: Design a rate-limit and quota policy that protects capacity while serving fair demand. Use when the user needs to protect an API or service from excessive or unfair usage.
domain: architecture-design
tags: [rate-limiting, quotas, capacity-protection]
triggers: ["api rate limit policy", "design request quotas", "rate limiting architecture"]
---

# Design a rate-limit and quota policy that protects capacity while serving fair demand

## Purpose

Design a rate-limit and quota policy that protects capacity while serving fair demand.

## When to use

Use when the user needs to protect an API or service from excessive or unfair usage.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Identify protected endpoints, capacity limits, client tiers, and legitimate peak demand.
2. Choose the rate-limit algorithm, measurement window, burst allowance, and enforcement scope.
3. Define quota allocation, rollover rules, renewal windows, and exemptions.
4. Specify limit headers, error responses, retry guidance, and client-identification rules.
5. Plan storage, distributed enforcement, administrative overrides, and audit records.
6. Test fairness, overload behavior, and fail-open or fail-closed assumptions before rollout.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-file-upload-and-processing-flow`
- `choose-between-a-modular-monolith-and-microservices`
- `design-a-batch-processing-pipeline`
