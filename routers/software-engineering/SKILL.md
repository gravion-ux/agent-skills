---
name: router-software-engineering
description: Route work in the Software engineering domain to the right leaf skill. Use when a task clearly belongs to software-engineering.
domain: software-engineering
tags: [router, routing, software-engineering]
triggers: ["route a software-engineering task", "which software-engineering skill should I use"]
---

# Software engineering router

## Purpose

List every leaf skill in the software-engineering domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside software-engineering and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-structured-logging-to-a-code-path` | Use when the user wants a code path to emit searchable logs without exposing sensitive data. |
| `add-timeouts-and-cancellation` | Use when the user needs operations to stop reliably at a deadline. |
| `adopt-type-checking-in-an-untyped-codebase` | Use when the user wants to add type safety to an untyped codebase. |
| `apply-solid-principles-to-a-class` | Use when the user wants a class redesigned around solid design principles. |
| `automate-a-repetitive-code-change` | Use when the user wants a repeated repository-wide code edit handled by an agent or script. |
| `bisect-a-regression-to-one-commit` | Use when the user needs a known-good and known-bad revision narrowed to one commit. |
| `cache-a-computed-result-safely` | Use when the user wants repeated computation reduced without serving stale results. |
| `configure-formatting-and-linting-for-a-repo` | Use when the user wants consistent formatting and static lint checks enforced in a codebase. |
| `cut-a-hotfix-release` | Use when the user needs a critical production defect fixed for immediate release. |
| `cut-a-release-branch-and-backport-a-fix` | Use when the user needs a fix backported to a maintained release line. |
| `deduplicate-repeated-logic` | Use when the user wants copy-pasted application logic reduced into one maintained implementation. |
| `deprecate-a-public-function` | Use when the user wants to deprecate a widely used public function. |
| `design-a-retry-and-backoff-policy` | Use when the user wants flaky dependency failures retried without amplifying load. |
| `eliminate-a-race-condition` | Use when the user sees intermittent failures only under concurrent execution. |
| `estimate-a-change-before-starting-it` | Use when the user wants a delivery estimate before implementation begins. |
| `extract-a-shared-helper` | Use when the user wants repeated code replaced by one reusable helper. |
| `fix-a-memory-leak` | Use when the user reports steadily growing memory during repeated execution. |
| `fix-an-off-by-one-error` | Use when the user wants an inclusive or exclusive range boundary corrected. |
| `hand-over-code-to-the-next-owner` | Use when the user must transfer an active codebase change to another maintainer. |
| `handle-merge-conflicts-in-a-feature-branch` | Use when the user has merge conflicts between a feature branch and its target. |
| `implement-a-feature-from-a-ticket` | Use when the user wants a repository change delivered from an agreed ticket. |
| `introduce-a-feature-flag` | Use when the user wants new behavior released gradually through a controlled code flag. |
| `make-a-blocking-call-non-blocking` | Use when the user needs a blocking operation removed from an event loop or latency path. |
| `make-a-script-safe-to-run-twice` | Use when the user wants a maintenance script to be safe across accidental reruns. |
| `migrate-code-to-a-new-language-version` | Use when the user wants to migrate a repository to a newer language version. |
| `pin-a-build-to-reproducible-output` | Use when the user needs software builds to be reproducible across machines. |
| `plan-a-multi-day-migration` | Use when the user wants a risky repository migration divided across several days. |
| `plan-the-code-change-before-editing` | Use when the user wants a code-change plan before any repository files are edited. |
| `port-a-module-to-another-language` | Use when the user needs an existing module reimplemented in another programming language. |
| `prepare-a-pull-request-for-review` | Use when the user wants a completed repository change made ready for reviewer approval. |
| `prepare-code-for-a-code-freeze` | Use when the user needs a codebase stabilized for a release freeze. |
| `profile-a-slow-function` | Use when the user wants to find why a repository function is slow. |
| `raise-useful-errors-from-a-library` | Use when the user wants a library failure to explain its cause and recovery path. |
| `reduce-coupling-between-modules` | Use when the user wants one code module to depend less on another. |
| `reduce-the-blame-of-a-failing-test-suite` | Use when the user wants a noisy failing test suite reduced to actionable root causes. |
| `refactor-a-long-function` | Use when the user wants an existing function simplified while its behavior stays compatible. |
| `remove-a-dependency-safely` | Use when the user wants an unused package removed from a maintained project. |
| `remove-a-hot-path-allocation` | Use when the user wants to lower allocation pressure in a frequently executed path. |
| `remove-dead-code-safely` | Use when the user wants unused code removed without deleting active behavior or user data. |
| `rename-a-symbol-across-the-codebase` | Use when the user wants a code symbol renamed consistently across a repository. |
| `reproduce-a-bug-in-a-local-sandbox` | Use when the user needs a reported software defect reproduced safely outside production. |
| `retire-a-feature-flag-after-rollout` | Use when the user wants an expired feature flag removed from production code. |
| `review-a-pull-request-as-a-pair` | Use when the user wants a two-person review of a proposed repository change. |
| `revive-a-stale-pull-request` | Use when the user wants an old pull request updated and reconsidered for review. |
| `run-a-weekly-code-maintenance-session` | Use when the user wants to schedule recurring repository maintenance work. |
| `set-up-a-build-system-for-a-new-service` | Use when the user wants a new service to have a reliable local and CI build. |
| `set-up-pre-commit-hooks` | Use when the user wants local git hooks to catch quality failures before review. |
| `speed-up-a-slow-build` | Use when the user wants a slow repository build made faster without changing its result. |
| `split-a-large-pull-request` | Use when the user wants a pull request too large for review split into coherent units. |
| `split-a-monolith-into-modules` | Use when the user wants a large module divided into maintainable parts. |
| `split-an-oversized-module` | Use when the user wants one oversized source module divided without changing its contract. |
| `support-a-library-consumer` | Use when the user is supporting a downstream consumer of a published library. |
| `tag-and-release-a-version` | Use when the user wants to publish a versioned software release. |
| `tidy-a-noisy-git-history` | Use when the user wants a local branch history cleaned before review. |
| `trace-a-production-stack-trace` | Use when the user has a production stack trace that needs a code-level cause. |
| `triage-a-bug-report-with-a-reproducer` | Use when the user wants a defect report converted into actionable engineering work. |
| `upgrade-a-dependency-without-breaking-anything` | Use when the user wants a package upgraded without breaking the application. |
| `use-property-based-testing-for-edge-cases` | Use when the user wants broader edge-case coverage than example-only tests. |
| `validate-input-at-the-system-boundary` | Use when the user wants external requests or files validated before processing. |
| `verify-a-third-party-library-integration` | Use when the user wants to validate a new or upgraded external library dependency. |
| `work-in-a-legacy-codebase-without-tests` | Use when the user needs a change in legacy code that lacks reliable automated tests. |
| `write-a-changelog-entry` | Use when the user wants a release changelog entry for shipped changes. |
| `write-a-postmortem-for-a-defect` | Use when the user wants a production defect analyzed and prevention actions assigned. |
| `write-a-technical-debt-register` | Use when the user wants a practical register of outstanding code debt. |
| `write-an-executable-design-note` | Use when the user wants a technical design captured in an implementation-ready repository artefact. |
| `write-an-idempotent-background-job` | Use when the user wants a background job to tolerate duplicate delivery safely. |
