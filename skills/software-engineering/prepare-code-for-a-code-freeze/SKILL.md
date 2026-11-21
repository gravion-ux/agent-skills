---
name: prepare-code-for-a-code-freeze
description: Prepare a repository for a code freeze by isolating risk, approving exceptions, and proving the release state. Use when the user needs a codebase stabilized for a release freeze.
domain: software-engineering
tags: [code-freeze, release-readiness, risk-control]
triggers: ["prepare code for a freeze", "stabilize a repository for release freeze"]
---

# Prepare a repository for a code freeze by isolating risk, approving exceptions, and proving the release state

## Purpose

Prepare a repository for a code freeze by isolating risk, approving exceptions, and proving the release state.

## When to use

Use when the user needs a codebase stabilized for a release freeze.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inventory unmerged changes and known release risks.
2. Freeze nonessential refactors and dependency upgrades.
3. Run the full test suite and packaging checks.
4. Document each exception with approver, scope, and expiry.
5. Prepare release notes, rollback steps, and escalation owners.
6. Record the frozen revision and outstanding risk status.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `prepare-a-pull-request-for-review`
- `add-structured-logging-to-a-code-path`
- `automate-a-repetitive-code-change`
