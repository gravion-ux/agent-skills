---
name: measure-skill-routing-accuracy
description: Measure routing accuracy by checking the selected skill against the labelled correct answer. Use when the user wants to know how often the router picks the right skill.
domain: agent-tooling-meta
tags: [routing, metrics, accuracy]
triggers: ["measure skill routing accuracy", "how often does the router pick correctly", "routing precision and recall check"]
---

# Measure routing accuracy by checking the selected skill against the labelled correct answer

## Purpose

Measure routing accuracy by checking the selected skill against the labelled correct answer.

## When to use

Use when the user wants to know how often the router picks the right skill.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Build a set of requests with the correct skill labelled for each one.
2. Include near-miss requests that should route to a different skill.
3. Run the router over the set and record the selected skill for each request.
4. Calculate the accuracy overall and the accuracy for each domain.
5. List the specific misroutes so the fix targets a known cause.

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
