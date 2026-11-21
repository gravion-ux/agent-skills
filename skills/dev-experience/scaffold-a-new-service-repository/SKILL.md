---
name: scaffold-a-new-service-repository
description: Scaffold a service repository with deployable code, tests, local configuration, and CI wiring. Use when the user is starting a new service repository that should follow team conventions.
domain: dev-experience
tags: [service-scaffold, repository, ci]
triggers: ["scaffold a new service repository", "generate a service repo template", "bootstrap a new backend service repo"]
---

# Scaffold a service repository with deployable code, tests, local configuration, and CI wiring

## Purpose

Scaffold a service repository with deployable code, tests, local configuration, and CI wiring.

## When to use

Use when the user is starting a new service repository that should follow team conventions.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Collect the service boundary, runtime, data stores, and ownership requirements.
2. Generate the smallest runnable service with health, configuration, and error handling.
3. Add unit tests, a local startup path, and a CI build for the service.
4. Document the repository layout, secrets needed, and deployment boundary.
5. Verify the scaffold through a clean setup and one local request.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `adopt-a-new-linter-rule-safely`
- `configure-a-repository-template`
- `onboard-a-new-developer-in-a-week`
