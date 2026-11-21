---
name: add-structured-logging-to-a-code-path
description: Add structured logging to a code path with consistent fields, safe values, and testable output. Use when the user wants a code path to emit searchable logs without exposing sensitive data.
domain: software-engineering
tags: [structured-logging, observability, redaction]
triggers: ["add structured logging to code path", "emit searchable application logs", "instrument path with log fields"]
---

# Add structured logging to a code path with consistent fields, safe values, and testable output

## Purpose

Add structured logging to a code path with consistent fields, safe values, and testable output.

## When to use

Use when the user wants a code path to emit searchable logs without exposing sensitive data.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map the events, correlation identifiers, and actors needed for diagnosis.
2. Define a stable event name and field schema for the target path.
3. Emit structured fields at each decision point and omit sensitive values.
4. Assert log output in a focused test and inspect a representative sample.
5. Run the existing suite and document the schema, retention, and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `migrate-code-to-a-new-language-version`
- `apply-solid-principles-to-a-class`
- `automate-a-repetitive-code-change`
