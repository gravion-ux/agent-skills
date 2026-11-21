---
name: keep-skill-outputs-consistent
description: Keep skill outputs consistent by defining one shape that every skill in a group returns. Use when the user wants several skills to produce results that can be handled the same way.
domain: agent-tooling-meta
tags: [consistency, contract, output]
triggers: ["keep skill outputs consistent", "same output format from every skill", "standardise the shape of skill results"]
---

# Keep skill outputs consistent by defining one shape that every skill in a group returns

## Purpose

Keep skill outputs consistent by defining one shape that every skill in a group returns.

## When to use

Use when the user wants several skills to produce results that can be handled the same way.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Choose the sections or fields that every skill in the group must return.
2. Write the shared contract once and reference it from each skill.
3. Define the optional fields and what a skill does when it has nothing to put in them.
4. Add a check that a produced output matches the contract before it is handed on.
5. Add an example output for each shape so the intent is unambiguous.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `add-a-citation-to-a-skill`
- `build-a-skill-evaluation-harness`
- `create-a-skill-template`
