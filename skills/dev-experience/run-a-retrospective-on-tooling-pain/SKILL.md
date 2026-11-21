---
name: run-a-retrospective-on-tooling-pain
description: Run a tooling retrospective that identifies recurring friction, ranks causes, and assigns concrete improvements. Use when the user wants to review recent developer tooling pain with the team.
domain: dev-experience
tags: [tooling-retrospective, friction-analysis, team-improvement]
triggers: ["run a retrospective on tooling pain", "review developer tool friction", "improve recurring dev tooling problems"]
---

# Run a tooling retrospective that identifies recurring friction, ranks causes, and assigns concrete improvements

## Purpose

Run a tooling retrospective that identifies recurring friction, ranks causes, and assigns concrete improvements.

## When to use

Use when the user wants to review recent developer tooling pain with the team.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Collect recent friction examples with frequency, severity, and affected workflow.
2. Group duplicate reports into recurring themes and separate symptoms from root causes.
3. Rank themes by impact and confidence using the team's agreed criteria.
4. Choose one improvement with a named owner and measurable outcome.
5. Record remaining issues, decisions, and a follow-up review date.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `review-a-tooling-upgrade-proposal`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
