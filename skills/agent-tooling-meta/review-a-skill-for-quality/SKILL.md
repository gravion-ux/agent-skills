---
name: review-a-skill-for-quality
description: Review a skill for quality by checking whether its steps actually decide anything. Use when the user wants a critical review of a skill before it is published.
domain: agent-tooling-meta
tags: [review, quality, audit]
triggers: ["review a skill for quality", "critique this skill before publishing", "what is weak about this skill"]
---

# Review a skill for quality by checking whether its steps actually decide anything

## Purpose

Review a skill for quality by checking whether its steps actually decide anything.

## When to use

Use when the user wants a critical review of a skill before it is published.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Check that each step names an artefact, a command or a threshold rather than an intention.
2. Check that the when-not-to-use clause would exclude a real neighbouring task.
3. Check that the output contract could be checked by someone who did not write it.
4. Check that the triggers would not also fit a different skill.
5. Write the list of changes ranked by how much they would reduce the failure rate.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `design-a-router-for-a-skill-catalogue`
- `design-a-skill-for-a-multi-domain-task`
- `design-a-skill-for-a-repeated-task`
