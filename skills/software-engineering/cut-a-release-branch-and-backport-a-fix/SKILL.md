---
name: cut-a-release-branch-and-backport-a-fix
description: Cut a supported release branch and backport a verified fix without introducing unrelated changes. Use when the user needs a fix backported to a maintained release line.
domain: software-engineering
tags: [release-branches, backports, versioning]
triggers: ["cut a release branch and backport", "backport a fix to a release line"]
---

# Cut a supported release branch and backport a verified fix without introducing unrelated changes

## Purpose

Cut a supported release branch and backport a verified fix without introducing unrelated changes.

## When to use

Use when the user needs a fix backported to a maintained release line.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Identify the supported release branches and intended target.
2. Create the branch from the correct release baseline.
3. Port only the reviewed fix and its regression test.
4. Resolve branch differences without copying unrelated changes.
5. Run target-branch tests and packaging checks.
6. Record the backport, release notes, and rollback procedure.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `cut-a-hotfix-release`
- `tag-and-release-a-version`
- `configure-formatting-and-linting-for-a-repo`
