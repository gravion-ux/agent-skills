---
name: write-a-changelog-entry
description: Write a concise changelog entry that explains user-visible changes and links each change to its source. Use when the user wants a release changelog entry for shipped changes.
domain: software-engineering
tags: [changelog, release-notes, documentation]
triggers: ["write a changelog entry", "document user visible release changes"]
---

# Write a concise changelog entry that explains user-visible changes and links each change to its source

## Purpose

Write a concise changelog entry that explains user-visible changes and links each change to its source.

## When to use

Use when the user wants a release changelog entry for shipped changes.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Collect merged changes since the previous release.
2. Group changes by added, changed, fixed, and removed behaviour.
3. Write one user-facing sentence per meaningful change.
4. Link each entry to its issue, pull request, or commit.
5. Check the wording against the implemented behaviour.
6. Compare the entry with the release version and publish notes.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `write-a-postmortem-for-a-defect`
- `write-a-technical-debt-register`
- `add-structured-logging-to-a-code-path`
