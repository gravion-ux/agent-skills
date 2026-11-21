---
name: tag-and-release-a-version
description: Prepare and tag a version with passing tests, matching release notes, and a recoverable release record. Use when the user wants to publish a versioned software release.
domain: software-engineering
tags: [versioning, release-engineering, tagging]
triggers: ["tag and release a version", "create an annotated release tag"]
---

# Prepare and tag a version with passing tests, matching release notes, and a recoverable release record

## Purpose

Prepare and tag a version with passing tests, matching release notes, and a recoverable release record.

## When to use

Use when the user wants to publish a versioned software release.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Confirm the version and changelog describe the intended change.
2. Run the complete test suite and packaging checks.
3. Update version metadata and release notes.
4. Create an annotated release tag from the reviewed commit.
5. Publish the artefact and verify its version metadata.
6. Record the tag, artefact checksum, and rollback procedure.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `cut-a-release-branch-and-backport-a-fix`
- `configure-formatting-and-linting-for-a-repo`
- `cut-a-hotfix-release`
