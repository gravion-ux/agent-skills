---
name: design-a-multi-tenant-data-model
description: Design a multi-tenant data model that isolates access while supporting tenant-specific needs. Use when the user needs to store data for multiple customers in one system.
domain: architecture-design
tags: [multi-tenancy, data-isolation, tenant-ownership]
triggers: ["multi tenant data model", "design tenant isolation", "tenant aware database schema"]
---

# Design a multi-tenant data model that isolates access while supporting tenant-specific needs

## Purpose

Design a multi-tenant data model that isolates access while supporting tenant-specific needs.

## When to use

Use when the user needs to store data for multiple customers in one system.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Define tenant identity, isolation guarantees, and the authoritative tenant registry.
2. Choose shared, isolated, or hybrid storage and record the selection criteria.
3. Include the tenant key in every access path, index, constraint, and uniqueness rule.
4. Model configuration, entitlements, and data-residency differences without bypassing isolation.
5. Specify provisioning, migration, deletion, backup, and restore behavior per tenant.
6. Test cross-tenant access paths and state the assumptions behind the isolation model.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-data-model-for-a-feature`
- `design-a-permission-model`
- `design-a-batch-processing-pipeline`
