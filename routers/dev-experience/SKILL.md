---
name: router-dev-experience
description: Route work in the Developer experience domain to the right leaf skill. Use when a task clearly belongs to dev-experience.
domain: dev-experience
tags: [router, routing, dev-experience]
triggers: ["route a dev-experience task", "which dev-experience skill should I use"]
---

# Developer experience router

## Purpose

List every leaf skill in the dev-experience domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside dev-experience and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-a-health-check-endpoint` | Use when the user needs a lightweight readiness signal for a locally run or deployed service. |
| `add-editor-support-files-to-a-repo` | Use when the user wants a repository to open consistently in the team's editors. |
| `adopt-a-new-linter-rule-safely` | Use when the user wants to enable a lint rule without disrupting unrelated development work. |
| `cache-dependencies-in-ci` | Use when the user wants CI builds to reuse dependencies without producing stale artifacts. |
| `clean-up-stale-preview-environments` | Use when the user needs to reclaim resources from abandoned pull-request previews. |
| `configure-a-repository-template` | Use when the user wants a reusable baseline for newly created repositories. |
| `create-a-code-snippet-library` | Use when the user wants to capture reusable code examples for recurring developer tasks. |
| `document-a-local-setup-step` | Use when the user needs a reproducible setup instruction in the developer documentation. |
| `manage-multiple-package-versions` | Use when the user must support more than one version of a package or API simultaneously. |
| `measure-developer-productivity-signals` | Use when the user wants evidence about developer workflow efficiency and team friction. |
| `onboard-a-new-developer-in-a-week` | Use when the user wants a new developer to contribute meaningfully within one week. |
| `parallelise-a-slow-test-suite` | Use when the user has a test suite whose runtime blocks the development feedback loop. |
| `provide-a-debug-configuration` | Use when the user wants a consistent local debugging configuration for a repository. |
| `provide-a-one-command-start-script` | Use when the user needs a dependable single command to start the local application stack. |
| `provision-preview-environments-per-branch` | Use when the user wants every pull-request branch to receive a disposable preview environment. |
| `publish-an-internal-developer-package` | Use when the user wants to distribute a reusable package to developers inside the organization. |
| `reduce-ci-time-for-pull-requests` | Use when the user wants pull-request checks to complete faster without losing coverage. |
| `reset-a-broken-local-environment` | Use when the user's local development environment is broken or inconsistent. |
| `review-a-tooling-upgrade-proposal` | Use when the user is evaluating a proposed upgrade to shared developer tooling. |
| `run-a-retrospective-on-tooling-pain` | Use when the user wants to review recent developer tooling pain with the team. |
| `scaffold-a-new-service-repository` | Use when the user is starting a new service repository that should follow team conventions. |
| `seed-a-database-with-realistic-test-data` | Use when the user needs repeatable test data for local development or automated checks. |
| `set-up-a-local-development-environment` | Use when the user needs a consistent local environment for a repository. |
| `speed-up-the-inner-development-loop` | Use when the user experiences slow feedback while editing code in the repository. |
| `version-and-publish-a-shared-library` | Use when the user is preparing a versioned release of a shared code library. |
| `write-a-developer-cli-wrapper` | Use when the user wants a repository-specific command-line tool that simplifies a developer workflow. |
| `write-a-developer-onboarding-checklist` | Use when the user is preparing an onboarding checklist for a new engineering hire. |
| `write-a-good-commit-message` | Use when the user wants a concise commit message for a completed code change. |
| `write-a-task-runner-for-a-repo` | Use when the user wants recurring repository tasks wrapped in predictable commands. |
| `write-an-internal-tooling-adoption-plan` | Use when the user wants teams to adopt a new internal developer tool successfully. |
