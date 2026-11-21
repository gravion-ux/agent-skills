---
name: structure-a-skill-file
description: Structure a skill file so its sections appear in the fixed order the repository expects. Use when the user is writing or repairing the layout of a skill file.
domain: agent-tooling-meta
tags: [structure, format, authoring]
triggers: ["structure a skill file", "correct section order for a skill", "skill file layout and headings"]
---

# Structure a skill file so its sections appear in the fixed order the repository expects

## Purpose

Structure a skill file so its sections appear in the fixed order the repository expects.

## When to use

Use when the user is writing or repairing the layout of a skill file.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Write the frontmatter with the name, description, domain, tags and triggers.
2. Write the purpose and the when-to-use clause first, since they set the frame.
3. Add the when-not-to-use clause so the skill can be ruled out.
4. Write the inputs, the procedure and the output contract in that order.
5. Finish with the validation checklist, the safety notes and the related skills.

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
