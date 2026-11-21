---
name: parallelise-a-slow-test-suite
description: Parallelise a slow test suite by isolating suites, balancing workers, and preserving deterministic failures. Use when the user has a test suite whose runtime blocks the development feedback loop.
domain: dev-experience
tags: [test-parallelisation, test-performance, ci-testing]
triggers: ["parallelise a slow test suite", "run test suites in parallel", "speed up the serial test suite"]
---

# Parallelise a slow test suite by isolating suites, balancing workers, and preserving deterministic failures

## Purpose

Parallelise a slow test suite by isolating suites, balancing workers, and preserving deterministic failures.

## When to use

Use when the user has a test suite whose runtime blocks the development feedback loop.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Measure serial test duration and identify independent suite boundaries.
2. Choose a runner that can isolate tests without shared-state conflicts.
3. Distribute tests across available workers and randomise execution order if safe.
4. Keep retries, timeouts, and serial markers explicit for flaky or stateful tests.
5. Compare coverage and failure output with the serial baseline before merging.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `seed-a-database-with-realistic-test-data`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
