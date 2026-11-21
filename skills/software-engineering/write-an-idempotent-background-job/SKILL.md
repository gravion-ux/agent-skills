---
name: write-an-idempotent-background-job
description: Make a background job safe to retry by recording a durable idempotency key for each requested effect. Use when the user wants a background job to tolerate duplicate delivery safely.
domain: software-engineering
tags: [idempotency, background-jobs, event-processing]
triggers: ["make a background job idempotent", "handle duplicate background delivery"]
---

# Make a background job safe to retry by recording a durable idempotency key for each requested effect

## Purpose

Make a background job safe to retry by recording a durable idempotency key for each requested effect.

## When to use

Use when the user wants a background job to tolerate duplicate delivery safely.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the idempotency key from the job identity and payload.
2. Persist the processed marker before emitting external effects.
3. Make each side effect conditional on that marker.
4. Handle retries and concurrent delivery of the same job.
5. Add a duplicate-delivery regression test.
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

- `write-an-executable-design-note`
- `adopt-type-checking-in-an-untyped-codebase`
- `fix-an-off-by-one-error`
