---
name: make-a-blocking-call-non-blocking
description: Move a blocking dependency behind an asynchronous boundary while preserving results, errors, and cancellation. Use when the user needs a blocking operation removed from an event loop or latency path.
domain: software-engineering
tags: [async, blocking-io, event-loop]
triggers: ["make a blocking call async", "move blocking io off the event loop"]
---

# Move a blocking dependency behind an asynchronous boundary while preserving results, errors, and cancellation

## Purpose

Move a blocking dependency behind an asynchronous boundary while preserving results, errors, and cancellation.

## When to use

Use when the user needs a blocking operation removed from an event loop or latency path.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Locate the blocking call and its caller response contract.
2. Choose an async adapter or worker execution model.
3. Move the operation behind the non-blocking boundary.
4. Propagate completion, failure, and cancellation signals.
5. Measure event-loop latency under representative load.
6. Run tests and record rationale and rollback steps.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `make-a-script-safe-to-run-twice`
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
