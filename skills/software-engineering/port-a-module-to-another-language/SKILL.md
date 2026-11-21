---
name: port-a-module-to-another-language
description: Port a module to another language while preserving its API contract, edge cases, and observable behavior. Use when the user needs an existing module reimplemented in another programming language.
domain: software-engineering
tags: [cross-language, portability, parity]
triggers: ["port a module to another language", "create cross language api parity"]
---

# Port a module to another language while preserving its API contract, edge cases, and observable behavior

## Purpose

Port a module to another language while preserving its API contract, edge cases, and observable behavior.

## When to use

Use when the user needs an existing module reimplemented in another programming language.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Specify the source module's API and behavioral edge cases.
2. Create parity tests from the original module's observable outputs.
3. Implement the target-language API with matching semantics.
4. Compare both implementations on shared and boundary inputs.
5. Run target tests and publish migration guidance.
6. Document rationale, known differences, and rollback.

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
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
