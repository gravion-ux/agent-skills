---
name: apply-solid-principles-to-a-class
description: Apply a focused SOLID refactor to a class while preserving its public behavior and callers. Use when the user wants a class redesigned around solid design principles.
domain: software-engineering
tags: [solid, object-design, refactoring]
triggers: ["apply solid to a class", "refactor a class for solid"]
---

# Apply a focused SOLID refactor to a class while preserving its public behavior and callers

## Purpose

Apply a focused SOLID refactor to a class while preserving its public behavior and callers.

## When to use

Use when the user wants a class redesigned around solid design principles.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Identify the class's primary responsibility and extension points.
2. Select the single SOLID violation that causes the most friction.
3. Extract or invert only the behavior needed to fix it.
4. Keep the existing public contract intact.
5. Add focused tests for the refactored responsibility.
6. Run existing tests and document rationale and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `bisect-a-regression-to-one-commit`
- `make-a-script-safe-to-run-twice`
