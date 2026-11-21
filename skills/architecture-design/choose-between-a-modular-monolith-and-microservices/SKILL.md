---
name: choose-between-a-modular-monolith-and-microservices
description: Compare a modular monolith with microservices against team topology, scaling, and operating cost. Use when the user must choose a service architecture for a new or evolving application.
domain: architecture-design
tags: [modular-monolith, microservices, trade-offs]
triggers: ["modular monolith or microservices", "choose monolith versus microservices", "service architecture comparison"]
---

# Compare a modular monolith with microservices against team topology, scaling, and operating cost

## Purpose

Compare a modular monolith with microservices against team topology, scaling, and operating cost.

## When to use

Use when the user must choose a service architecture for a new or evolving application.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. List the required business capabilities, team boundaries, and independent scaling targets.
2. Estimate the deployment, network, observability, and incident-response cost of each option.
3. Evaluate module isolation and release coupling in the monolith against distributed failure modes.
4. Choose the option that satisfies current constraints rather than anticipated scale.
5. Define measurable migration triggers that would justify changing the architecture later.
6. Record the assumptions, rejected trade-offs, and a dated review checkpoint.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `choose-a-message-queue`
- `design-a-file-upload-and-processing-flow`
- `design-a-rate-limit-and-quota-policy`
