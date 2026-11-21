---
name: write-a-skill-usage-guide
description: Write a usage guide that shows a user how to get the right result from a skill. Use when the user wants a guide explaining how to use a skill they have built.
domain: agent-tooling-meta
tags: [guide, documentation, usage]
triggers: ["write a skill usage guide", "explain to users how to use my skill", "guide for calling a skill"]
---

# Write a usage guide that shows a user how to get the right result from a skill

## Purpose

Write a usage guide that shows a user how to get the right result from a skill.

## When to use

Use when the user wants a guide explaining how to use a skill they have built.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Describe the outcome the skill produces in one sentence.
2. Show a real request that the skill handles well.
3. Show the inputs the user must supply and how to phrase them.
4. Explain what the user will receive back and what they can change.
5. List the requests that should go to a different skill instead.

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
- `write-a-reusable-skill`
- `write-a-skill-regression-suite`
