---
name: write-a-reusable-skill
description: Write a reusable skill that captures one repeated task with clear inputs and outputs. Use when the user wants to turn a repeated manual task into a skill other agents can run.
domain: agent-tooling-meta
tags: [skill, authoring, reuse]
triggers: ["write a reusable skill", "turn this repeated task into a skill", "capture this workflow as a skill"]
---

# Write a reusable skill that captures one repeated task with clear inputs and outputs

## Purpose

Write a reusable skill that captures one repeated task with clear inputs and outputs.

## When to use

Use when the user wants to turn a repeated manual task into a skill other agents can run.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect the real examples of the task as it is done today.
2. Write the inputs the task needs and the output it must produce.
3. Write the procedure as ordered steps a reader can follow without guessing.
4. Add the cases where the skill should not be used.
5. Test the skill on the real examples and adjust the steps until each one works.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `write-a-migration-note-for-a-skill-change`
- `write-a-skill-regression-suite`
- `write-a-skill-safety-checklist`
