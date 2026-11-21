---
name: write-an-architecture-decision-record
description: Record an architecture decision with context, options, consequences, and explicit assumptions. Use when the user needs to document a consequential technical choice for future reviewers.
domain: architecture-design
tags: [decision-record, architecture-trade-offs, governance]
triggers: ["architecture decision record", "write an adr", "record a technical decision"]
---

# Record an architecture decision with context, options, consequences, and explicit assumptions

## Purpose

Record an architecture decision with context, options, consequences, and explicit assumptions.

## When to use

Use when the user needs to document a consequential technical choice for future reviewers.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. State the decision, its status, its owners, and the date the decision was made.
2. Describe the requirements and constraints that made the decision necessary.
3. List the credible options with the evidence and trade-offs used to compare them.
4. Record the chosen option, rejected alternatives, and expected consequences.
5. Name the assumptions, review triggers, and conditions that would invalidate the decision.
6. Link the decision to the design sections, evidence, and follow-up work it governs.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `review-an-architecture-diagram`
- `design-an-event-driven-workflow`
- `design-an-idempotent-api`
