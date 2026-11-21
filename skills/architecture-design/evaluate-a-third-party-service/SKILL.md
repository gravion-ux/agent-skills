---
name: evaluate-a-third-party-service
description: Evaluate a third-party service against reliability, security, cost, and exit constraints. Use when the user is considering an external service as part of a system design.
domain: architecture-design
tags: [vendor-evaluation, due-diligence, exit-strategy]
triggers: ["evaluate a third party service", "assess an api vendor", "third party dependency review"]
---

# Evaluate a third-party service against reliability, security, cost, and exit constraints

## Purpose

Evaluate a third-party service against reliability, security, cost, and exit constraints.

## When to use

Use when the user is considering an external service as part of a system design.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. List the required capabilities, service levels, data classes, and integration boundaries.
2. Review the provider's reliability history, incident process, security posture, and compliance evidence.
3. Model request volume, pricing tiers, support needs, and the cost of redundant use.
4. Test the integration for failure modes, timeout handling, quotas, and degraded operation.
5. Define data export, contract termination, credential rotation, and migration procedures.
6. Record the assumptions, unresolved risks, and approval owner for the dependency.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `plan-a-decomposition-of-a-god-service`
- `assess-a-technical-proposal`
- `choose-a-message-queue`
