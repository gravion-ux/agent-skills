---
name: write-a-changelog
description: Record product changes by version, date, and user impact in a consistent format. Use when the user needs a changelog that tracks releases and explains what changed.
domain: documentation
tags: [changelog, release-history, versioning]
triggers: ["software changelog", "write a changelog", "version changelog entries"]
---

# Record product changes by version, date, and user impact in a consistent format

## Purpose

Record product changes by version, date, and user impact in a consistent format.

## When to use

Use when the user needs a changelog that tracks releases and explains what changed.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Collect commits and release records for the target version.
2. Group each change as added, changed, fixed, deprecated, or removed.
3. Describe the user-visible impact instead of listing internal commits.
4. Link each entry to its issue, pull request, or release record.
5. Compare the changelog with the packaged release notes.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `write-a-checklist-in-a-runbook`
- `write-a-comparison-table-of-options`
- `write-a-conceptual-explanation`
