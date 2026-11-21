---
name: assess-a-technical-proposal
description: Assess a technical proposal for feasibility, risk, operability, and alignment with constraints. Use when the user needs a critical architecture review of a proposed technical change.
domain: architecture-design
tags: [proposal-review, feasibility, risk-analysis]
triggers: ["assess a technical proposal", "review an architecture proposal", "evaluate a system design proposal"]
---

# Assess a technical proposal for feasibility, risk, operability, and alignment with constraints

## Purpose

Assess a technical proposal for feasibility, risk, operability, and alignment with constraints.

## When to use

Use when the user needs a critical architecture review of a proposed technical change.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Extract the proposal's goals, requirements, assumptions, and claimed deliverables.
2. Trace each requirement to a proposed component and mark any unsupported claim.
3. Check scale, security, operability, migration, cost, and timeline against known constraints.
4. Identify failure modes, unresolved dependencies, and the highest-impact design gaps.
5. Compare alternatives and recommend a decision, a revision, or a prototype with evidence.
6. State the review assumptions, confidence limits, and follow-up validation required.

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
- `choose-between-a-modular-monolith-and-microservices`
- `design-a-batch-processing-pipeline`
