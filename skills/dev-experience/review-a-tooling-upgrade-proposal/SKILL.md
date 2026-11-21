---
name: review-a-tooling-upgrade-proposal
description: Review a tooling upgrade proposal against compatibility, migration effort, and developer impact. Use when the user is evaluating a proposed upgrade to shared developer tooling.
domain: dev-experience
tags: [tooling-upgrade, migration-review, developer-experience]
triggers: ["review a tooling upgrade proposal", "assess a dev tool upgrade", "approve or reject a tooling migration"]
---

# Review a tooling upgrade proposal against compatibility, migration effort, and developer impact

## Purpose

Review a tooling upgrade proposal against compatibility, migration effort, and developer impact.

## When to use

Use when the user is evaluating a proposed upgrade to shared developer tooling.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Summarize the current version, target version, and change affecting developers.
2. Check compatibility with repository dependencies, supported runtimes, and automations.
3. Estimate migration work using a small representative upgrade in a branch.
4. Identify breaking defaults and require a migration note for shared behavior changes.
5. Recommend adoption, deferral, or a pilot with explicit success criteria.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `run-a-retrospective-on-tooling-pain`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
