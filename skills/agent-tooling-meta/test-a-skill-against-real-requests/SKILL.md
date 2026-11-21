---
name: test-a-skill-against-real-requests
description: Test a skill against the real requests it was written to handle. Use when the user wants to check that a skill works on the requests that motivated it.
domain: agent-tooling-meta
tags: [testing, evaluation, quality]
triggers: ["test a skill against real requests", "check my skill on actual examples", "skill behaves right on real tasks"]
---

# Test a skill against the real requests it was written to handle

## Purpose

Test a skill against the real requests it was written to handle.

## When to use

Use when the user wants to check that a skill works on the requests that motivated it.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect the real requests, taken from actual use rather than invented examples.
2. Run the skill on each one and record the output it produced.
3. Check the output against the skill's own output contract every time.
4. Note the cases where the skill was chosen but should not have been.
5. Adjust the procedure or the when-not-to-use clause until the failures are gone.

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
