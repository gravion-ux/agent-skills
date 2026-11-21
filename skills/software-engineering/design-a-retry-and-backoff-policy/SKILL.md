---
name: design-a-retry-and-backoff-policy
description: Design a bounded retry policy that distinguishes transient failures and respects the caller's deadline. Use when the user wants flaky dependency failures retried without amplifying load.
domain: software-engineering
tags: [retries, backoff, fault-tolerance]
triggers: ["design retry backoff", "bound retries with jitter and deadline"]
---

# Design a bounded retry policy that distinguishes transient failures and respects the caller's deadline

## Purpose

Design a bounded retry policy that distinguishes transient failures and respects the caller's deadline.

## When to use

Use when the user wants flaky dependency failures retried without amplifying load.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Classify failures as transient or permanent.
2. Set a retry count, delay ceiling, and jitter rule.
3. Bound all attempts by the caller deadline.
4. Preserve the final error after attempts are exhausted.
5. Add fault-injection tests for backoff and cancellation.
6. Run the suite and document the policy and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `configure-formatting-and-linting-for-a-repo`
- `cut-a-release-branch-and-backport-a-fix`
- `tag-and-release-a-version`
