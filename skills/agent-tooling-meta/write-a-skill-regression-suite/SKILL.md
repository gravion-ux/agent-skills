---
name: write-a-skill-regression-suite
description: Write a regression suite that locks in the behaviour a catalogue must not lose. Use when the user wants tests that protect the routing and output of the current catalogue.
domain: agent-tooling-meta
tags: [regression, tests, stability]
triggers: ["write a skill regression suite", "tests that protect my catalogue routing", "lock in current skill behaviour"]
---

# Write a regression suite that locks in the behaviour a catalogue must not lose

## Purpose

Write a regression suite that locks in the behaviour a catalogue must not lose.

## When to use

Use when the user wants tests that protect the routing and output of the current catalogue.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect the requests that currently route correctly and are most important.
2. Write one test per request asserting the skill that must be selected.
3. Add tests for the output contract of the skills that are most used.
4. Add the cases that broke before, so the same bug cannot return.
5. Run the suite on every change and treat a failure as a blocking problem.

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
- `write-a-skill-safety-checklist`
