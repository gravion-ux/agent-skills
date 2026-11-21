---
name: deprecate-a-public-function
description: Retire a public function through a warning, migration path, and measurable removal plan. Use when the user wants to deprecate a widely used public function.
domain: software-engineering
tags: [deprecation, migration, public-api]
triggers: ["deprecate a public function", "add a function migration warning"]
---

# Retire a public function through a warning, migration path, and measurable removal plan

## Purpose

Retire a public function through a warning, migration path, and measurable removal plan.

## When to use

Use when the user wants to deprecate a widely used public function.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Find internal and external call sites of the function.
2. Add a deprecation warning with the replacement named.
3. Document the migration path and proposed removal version.
4. Add tests for the warning and unchanged current behavior.
5. Update examples and release notes for consumers.
6. Run existing tests and record rollback considerations.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `profile-a-slow-function`
- `refactor-a-long-function`
- `add-structured-logging-to-a-code-path`
