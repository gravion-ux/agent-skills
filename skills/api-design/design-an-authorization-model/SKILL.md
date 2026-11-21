---
name: design-an-authorization-model
description: Maps roles and resource permissions to enforceable API authorization decisions. Use when the user needs to control which clients and users may perform API actions.
domain: api-design
tags: [authorization, rbac, permissions]
triggers: ["api authorization model", "design endpoint permissions", "map roles to api actions"]
---

# Maps roles and resource permissions to enforceable API authorization decisions

## Purpose

Maps roles and resource permissions to enforceable API authorization decisions.

## When to use

Use when the user needs to control which clients and users may perform API actions.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Define the resources, actions, roles, and permission boundaries.
2. Map every endpoint action to an explicit permission or policy.
3. Apply deny-by-default behavior when no rule matches.
4. Define object-level ownership or tenancy checks for protected resources.
5. Document authorization failures and the audit fields to record.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `design-a-rest-resource-model`
- `design-an-authentication-flow`
- `design-an-error-response-format`
