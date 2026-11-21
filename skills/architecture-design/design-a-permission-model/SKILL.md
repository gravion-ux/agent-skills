---
name: design-a-permission-model
description: Design a permission model with roles, resource scopes, deny rules, and auditable checks. Use when the user needs to control which identities can perform actions on protected resources.
domain: architecture-design
tags: [permissions, authorization, access-control]
triggers: ["permission model design", "role based access architecture", "resource authorization policy"]
---

# Design a permission model with roles, resource scopes, deny rules, and auditable checks

## Purpose

Design a permission model with roles, resource scopes, deny rules, and auditable checks.

## When to use

Use when the user needs to control which identities can perform actions on protected resources.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. List the identities, protected resources, actions, and scope levels in the system.
2. Define roles, permissions, resource attributes, and the inheritance or delegation rules.
3. Specify allow and deny precedence, default posture, and behavior for missing policy data.
4. Enforce checks at every service boundary and keep ownership decisions close to resources.
5. Log authorization decisions with actor, action, resource, result, and policy version.
6. Test privilege escalation, stale grants, and cross-tenant access paths against explicit assumptions.

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
- `design-a-multi-tenant-data-model`
- `design-a-batch-processing-pipeline`
