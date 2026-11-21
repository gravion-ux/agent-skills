---
name: add-a-citation-to-a-skill
description: Add a citation to a skill so the claims in it can be traced back to their source. Use when the user wants a skill to record where its guidance came from.
domain: agent-tooling-meta
tags: [citation, sources, provenance]
triggers: ["add a citation to a skill", "record where my skill guidance came from", "reference sources inside a skill"]
---

# Add a citation to a skill so the claims in it can be traced back to their source

## Purpose

Add a citation to a skill so the claims in it can be traced back to their source.

## When to use

Use when the user wants a skill to record where its guidance came from.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. List the claims in the skill that depend on external information.
2. Find the primary source for each claim and record its title and URL.
3. Put the source next to the step it supports rather than in a list at the end.
4. Add the date the source was checked, because external guidance changes.
5. Remove or rewrite any claim that has no source behind it.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `migrate-a-skill-to-a-new-format`
- `build-a-skill-evaluation-harness`
- `create-a-skill-template`
