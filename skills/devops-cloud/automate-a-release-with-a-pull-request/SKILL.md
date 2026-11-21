---
name: automate-a-release-with-a-pull-request
description: Open a release pull request that generates changelog entries, artifacts, and promotion checks. Use when the user wants the release preparation steps to run from a reviewed pull request.
domain: devops-cloud
tags: [release-automation, pull-request, changelog, release]
triggers: ["automate a release with a pull request", "release pull request workflow", "generate a changelog release pr"]
---

# Open a release pull request that generates changelog entries, artifacts, and promotion checks

## Purpose

Open a release pull request that generates changelog entries, artifacts, and promotion checks.

## When to use

Use when the user wants the release preparation steps to run from a reviewed pull request.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Derive the release version from the version files and the commit history since the last tag.
2. Generate the changelog, release notes, and version bump in a dedicated branch.
3. Open a pull request that links each changelog entry to its source commits.
4. Run the artifact build, signature, and scan checks inside the pull request pipeline.
5. Require the release owner to approve and merge before publishing the tag.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `run-a-canary-release-with-metrics`
- `manage-cost-with-a-scheduled-scale-down`
- `set-up-a-cd-pipeline-with-safe-rollouts`
