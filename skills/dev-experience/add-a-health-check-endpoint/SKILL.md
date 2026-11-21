---
name: add-a-health-check-endpoint
description: Add a health-check endpoint that reports service readiness without exposing sensitive internals. Use when the user needs a lightweight readiness signal for a locally run or deployed service.
domain: dev-experience
tags: [health-check, service-readiness, observability]
triggers: ["add a health check endpoint", "create a service readiness probe", "implement liveness and readiness endpoints"]
---

# Add a health-check endpoint that reports service readiness without exposing sensitive internals

## Purpose

Add a health-check endpoint that reports service readiness without exposing sensitive internals.

## When to use

Use when the user needs a lightweight readiness signal for a locally run or deployed service.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define the minimum dependency checks required for the service to accept traffic.
2. Implement a health endpoint that checks those dependencies with short timeouts.
3. Return distinct liveness and readiness states without secrets or stack traces.
4. Document the endpoint, response schema, and expected polling behavior.
5. Exercise failure modes and confirm the endpoint never blocks beyond its timeout.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `add-editor-support-files-to-a-repo`
- `adopt-a-new-linter-rule-safely`
- `configure-a-repository-template`
