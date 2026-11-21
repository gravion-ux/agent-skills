---
name: automate-a-repetitive-admin-task
description: Turn a repeated administrative chore into a rule the agent runs on a schedule. Use when the user repeats the same administrative chore and wants it handled automatically.
domain: productivity
tags: [automation, admin, scheduling]
triggers: ["automate a repetitive admin task", "set up a recurring admin automation", "run this chore automatically"]
---

# Turn a repeated administrative chore into a rule the agent runs on a schedule

## Purpose

Turn a repeated administrative chore into a rule the agent runs on a schedule.

## When to use

Use when the user repeats the same administrative chore and wants it handled automatically.

## When NOT to use

Do not use this for a shared team workflow; use project-management instead.

## Inputs required

- The tasks or commitments in scope
- The time and attention available
- The deadline or habit being targeted

## Procedure

1. List the exact trigger event, the fixed inputs and the expected output artefact.
2. Write the steps the agent must perform as an ordered instruction list.
3. Define the output location, file name and format for each run.
4. Add a validation check that rejects incomplete or malformed output.
5. Schedule the run frequency and name the condition that stops it.
6. Test the rule on one real example and review the artefact before enabling it.

## Output contract

A prioritised, time-boxed plan with the next concrete action stated.

## Validation checklist

- [ ] The first action can start immediately
- [ ] The plan fits the available time
- [ ] Each item has an explicit done condition

## Safety notes

Never schedule rest, health or recovery time away to fit more work in.

## Related skills

- `capture-a-task-in-one-line`
- `delegate-a-task-with-a-check-in-date`
- `finish-a-task-that-drags`
