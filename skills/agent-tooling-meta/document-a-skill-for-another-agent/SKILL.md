---
name: document-a-skill-for-another-agent
description: Document a skill for another agent so it can be loaded and applied without asking a question. Use when the user wants a skill documented for consumption by a different agent.
domain: agent-tooling-meta
tags: [documentation, handoff, agents]
triggers: ["document a skill for another agent", "write a skill spec an agent can follow", "handoff instructions for a skill"]
---

# Document a skill for another agent so it can be loaded and applied without asking a question

## Purpose

Document a skill for another agent so it can be loaded and applied without asking a question.

## When to use

Use when the user wants a skill documented for consumption by a different agent.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. State the skill's purpose and the exact situation it applies to.
2. Write the inputs as a list another agent can gather before starting.
3. Write the procedure as ordered steps with the decision at each branch.
4. State the output contract so the caller knows what to expect.
5. State the safety limits and what the agent must ask the user before proceeding.

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
