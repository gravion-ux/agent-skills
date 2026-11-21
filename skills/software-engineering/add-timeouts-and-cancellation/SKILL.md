---
name: add-timeouts-and-cancellation
description: Bound dependency waits with explicit deadlines and propagate cancellation through nested work. Use when the user needs operations to stop reliably at a deadline.
domain: software-engineering
tags: [timeouts, cancellation, resource-safety]
triggers: ["add timeouts and cancellation", "cancel an operation at a deadline"]
---

# Bound dependency waits with explicit deadlines and propagate cancellation through nested work

## Purpose

Bound dependency waits with explicit deadlines and propagate cancellation through nested work.

## When to use

Use when the user needs operations to stop reliably at a deadline.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Set a deadline for each external dependency call.
2. Propagate the cancellation signal through nested calls.
3. Release resources when a deadline or cancellation occurs.
4. Return a clear timeout or cancellation error.
5. Test timeout, cancellation, and cleanup paths automatically.
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
- `configure-formatting-and-linting-for-a-repo`
- `cut-a-release-branch-and-backport-a-fix`
