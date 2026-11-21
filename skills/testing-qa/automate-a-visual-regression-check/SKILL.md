---
name: automate-a-visual-regression-check
description: Automate a visual regression check by comparing rendered screenshots against approved baselines. Use when the user wants interface changes caught automatically after a build.
domain: testing-qa
tags: [visual-regression, screenshot-testing, ui-automation]
triggers: ["automate a visual regression check", "screenshot comparison test", "detect ui changes with visual diff"]
---

# Automate a visual regression check by comparing rendered screenshots against approved baselines

## Purpose

Automate a visual regression check by comparing rendered screenshots against approved baselines.

## When to use

Use when the user wants interface changes caught automatically after a build.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Capture the target pages or components at a fixed viewport and browser version.
2. Store the approved screenshots as the baseline for each case.
3. Diff each new capture against its baseline with a fixed pixel tolerance.
4. Fail the check and attach the diff image when a case exceeds the tolerance.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `write-a-regression-test-that-fails-first`
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
