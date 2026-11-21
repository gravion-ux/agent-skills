---
name: reduce-ci-time-for-pull-requests
description: Reduce pull-request CI time by profiling slow jobs and removing unnecessary work. Use when the user wants pull-request checks to complete faster without losing coverage.
domain: dev-experience
tags: [ci-duration, pull-request-ci, ci-optimization]
triggers: ["reduce CI time for pull requests", "speed up pull request checks", "make PR CI finish faster"]
---

# Reduce pull-request CI time by profiling slow jobs and removing unnecessary work

## Purpose

Reduce pull-request CI time by profiling slow jobs and removing unnecessary work.

## When to use

Use when the user wants pull-request checks to complete faster without losing coverage.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Record duration and queue time for every required pull-request job.
2. Split the slowest job by stage and identify duplicated or irrelevant checks.
3. Run independent checks in parallel and cache reusable outputs.
4. Move long-running or rarely needed jobs to a non-blocking schedule.
5. Compare before-and-after duration and document any changed merge policy.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `cache-dependencies-in-ci`
- `write-a-task-runner-for-a-repo`
- `add-a-health-check-endpoint`
