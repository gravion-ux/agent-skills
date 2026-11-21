---
name: seed-a-database-with-realistic-test-data
description: Seed a disposable database with realistic, deterministic fixtures that exercise common application paths. Use when the user needs repeatable test data for local development or automated checks.
domain: dev-experience
tags: [test-data, database-seeding, fixtures]
triggers: ["seed database with realistic test data", "create deterministic database fixtures", "load realistic local test data"]
---

# Seed a disposable database with realistic, deterministic fixtures that exercise common application paths

## Purpose

Seed a disposable database with realistic, deterministic fixtures that exercise common application paths.

## When to use

Use when the user needs repeatable test data for local development or automated checks.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define representative entities, relationships, boundary values, and invalid cases.
2. Build deterministic factories that create the fixture set without live records.
3. Load the fixtures into an isolated database and reset it between suites.
4. Document the seed command and the account or role each fixture represents.
5. Verify key user journeys against the seeded data before sharing the command.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `parallelise-a-slow-test-suite`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
