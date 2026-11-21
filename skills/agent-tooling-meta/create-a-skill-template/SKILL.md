---
name: create-a-skill-template
description: Create a skill template that produces a correctly structured skill every time. Use when the user writes many skills and wants the structure to be identical every time.
domain: agent-tooling-meta
tags: [template, scaffolding, consistency]
triggers: ["create a skill template", "standardise the way skills are written", "template for new skill files"]
---

# Create a skill template that produces a correctly structured skill every time

## Purpose

Create a skill template that produces a correctly structured skill every time.

## When to use

Use when the user writes many skills and wants the structure to be identical every time.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. List the fields every skill must have, in the order the repository expects.
2. Turn each field into a placeholder with a short instruction beside it.
3. Add the rules that are easy to break, such as the uniqueness and the step count.
4. Add a checklist that can be copied into the new skill as the validation section.
5. Test the template by producing one skill from it and checking the result.

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
- `design-a-router-for-a-skill-catalogue`
