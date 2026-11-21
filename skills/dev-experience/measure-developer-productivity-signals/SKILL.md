---
name: measure-developer-productivity-signals
description: Measure developer productivity signals without turning individual metrics into performance targets. Use when the user wants evidence about developer workflow efficiency and team friction.
domain: dev-experience
tags: [productivity-metrics, developer-metrics, measurement]
triggers: ["measure developer productivity signals", "track dev team productivity metrics", "measure developer workflow efficiency"]
---

# Measure developer productivity signals without turning individual metrics into performance targets

## Purpose

Measure developer productivity signals without turning individual metrics into performance targets.

## When to use

Use when the user wants evidence about developer workflow efficiency and team friction.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define the recurring friction and the team population affected by it.
2. Collect baseline and follow-up measures such as cycle time, wait time, and task duration.
3. Aggregate results by workflow stage and segment rather than ranking individuals.
4. Pair quantitative signals with short developer feedback about causes.
5. Publish findings, limitations, and the next measurement checkpoint.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `onboard-a-new-developer-in-a-week`
- `publish-an-internal-developer-package`
- `write-a-developer-cli-wrapper`
