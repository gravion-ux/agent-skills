---
name: hand-over-code-to-the-next-owner
description: Hand over code with a current-state map, verified commands, open risks, and an owner acknowledgement. Use when the user must transfer an active codebase change to another maintainer.
domain: software-engineering
tags: [handover, ownership-transfer, documentation]
triggers: ["hand over code to next owner", "transfer active code change", "prepare maintainer handoff"]
---

# Hand over code with a current-state map, verified commands, open risks, and an owner acknowledgement

## Purpose

Hand over code with a current-state map, verified commands, open risks, and an owner acknowledgement.

## When to use

Use when the user must transfer an active codebase change to another maintainer.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Confirm the current branch, diff, ticket scope, and verified test results.
2. Document setup, build, test, and review commands from a clean environment.
3. List unresolved decisions, known failures, risky areas, and next actions.
4. Prepare a rollback note and any migration or flag cleanup obligations.
5. Walk the next owner through the change and record their acknowledgement.

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
- `migrate-code-to-a-new-language-version`
- `plan-the-code-change-before-editing`
