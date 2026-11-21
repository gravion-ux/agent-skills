---
name: write-self-documenting-code
description: Make code self-documenting by replacing misleading comments with intent-revealing structure. Use when the user wants stale comments and unclear code replaced with self-explanatory structure.
domain: code-quality
tags: [documentation, readability, comments, code-quality]
triggers: ["self documenting code", "replace stale code comments", "code clarity without comments"]
---

# Make code self-documenting by replacing misleading comments with intent-revealing structure

## Purpose

Make code self-documenting by replacing misleading comments with intent-revealing structure.

## When to use

Use when the user wants stale comments and unclear code replaced with self-explanatory structure.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Identify comments that narrate syntax or contradict the current implementation.
2. Move explanation into names types and small well-named functions.
3. Keep only comments that record rationale constraints or non-obvious trade-offs.
4. Delete comments that no longer describe the code.
5. Run tests and have a reviewer confirm the intent is clear without comments.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `write-a-code-smell-triage-list`
- `remove-dead-dependencies-and-code`
- `remove-duplicated-code`
