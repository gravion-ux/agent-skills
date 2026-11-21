---
name: design-a-router-for-a-skill-catalogue
description: Design a router that narrows a large catalogue to a small candidate set without hiding options. Use when the user wants to build the selection layer over a large set of skills.
domain: agent-tooling-meta
tags: [router, design, routing]
triggers: ["design a router for a skill catalogue", "build the selection layer over many skills", "how to group skills for selection"]
---

# Design a router that narrows a large catalogue to a small candidate set without hiding options

## Purpose

Design a router that narrows a large catalogue to a small candidate set without hiding options.

## When to use

Use when the user wants to build the selection layer over a large set of skills.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Group the catalogue into domains that a user would also describe that way.
2. Write the one-line signal for each domain that identifies it from the task alone.
3. Choose the number of candidates the router returns and keep it small.
4. Make the router show its reasons so a wrong choice can be diagnosed.
5. Test the router against requests that belong to two domains at once.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `design-a-skill-for-a-multi-domain-task`
- `design-a-skill-for-a-repeated-task`
- `audit-a-catalogue-for-gaps`
