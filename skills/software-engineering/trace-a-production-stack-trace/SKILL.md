---
name: trace-a-production-stack-trace
description: Trace a production stack trace to the originating code path using versioned evidence. Use when the user has a production stack trace that needs a code-level cause.
domain: software-engineering
tags: [stack-trace, production-debugging, root-cause]
triggers: ["trace production stack trace", "map crash frames to code", "diagnose deployed exception path"]
---

# Trace a production stack trace to the originating code path using versioned evidence

## Purpose

Trace a production stack trace to the originating code path using versioned evidence.

## When to use

Use when the user has a production stack trace that needs a code-level cause.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Verify the deployed version, runtime, and request correlation details.
2. Map each stack frame to the matching source revision.
3. Trace inputs and state transitions to the first unexpected value.
4. Confirm the suspected cause with a local test or safe production evidence.
5. Report the cause, confidence, fix scope, and rollback considerations.

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
- `apply-solid-principles-to-a-class`
- `automate-a-repetitive-code-change`
