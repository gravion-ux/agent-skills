---
name: design-a-data-model-for-a-feature
description: Model a feature's entities, relationships, invariants, indexes, and lifecycle states. Use when the user needs a concrete data model for a new feature or a change to existing data.
domain: architecture-design
tags: [data-model, entities, constraints]
triggers: ["feature data model", "design a database model", "entity relationship design for a feature"]
---

# Model a feature's entities, relationships, invariants, indexes, and lifecycle states

## Purpose

Model a feature's entities, relationships, invariants, indexes, and lifecycle states.

## When to use

Use when the user needs a concrete data model for a new feature or a change to existing data.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Translate the feature requirements into entities, attributes, relationships, and ownership.
2. Define keys, nullability, constraints, referential rules, and lifecycle state transitions.
3. Specify the queries the feature must perform and the indexes that support them.
4. Capture invariants and the transaction boundaries that preserve them.
5. Document expected volumes, growth, archival, retention, and deletion behavior.
6. List assumptions about data quality and migration impact before approving the model.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-multi-tenant-data-model`
- `design-a-permission-model`
- `design-a-batch-processing-pipeline`
