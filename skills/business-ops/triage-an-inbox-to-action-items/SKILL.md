---
name: triage-an-inbox-to-action-items
description: Triage an inbox into owned, prioritized actions without losing the source context. Use when the user needs to convert a busy inbox into a clear action list.
domain: business-ops
tags: [inbox-triage, request-routing, task-capture]
triggers: ["triage inbox action items", "turn inbox into action items", "route urgent inbox requests"]
---

# Triage an inbox into owned, prioritized actions without losing the source context

## Purpose

Triage an inbox into owned, prioritized actions without losing the source context.

## When to use

Use when the user needs to convert a busy inbox into a clear action list.

## When NOT to use

Do not use this for a single customer conversation; use communication instead.

## Inputs required

- The process being run
- The inputs and who supplies them
- The service level the process must meet

## Procedure

1. Scan the connected mailbox for messages that request work, a decision, or an answer.
2. Attach each source link to every extracted inbox action.
3. Classify each item as an action, a decision, an answer, or no response needed.
4. Assign an owner and due date to each action using urgency and commitment level.
5. Route decisions and answers to the named accountable person.
6. Update the action tracker after each reply and report overdue items.

## Output contract

A documented operating procedure with owners, inputs, steps and the metrics it is judged on.

## Validation checklist

- [ ] Every step has an owner
- [ ] The failure path is documented
- [ ] The metric that proves the process works is named

## Safety notes

Never change a financial, legal or contractual step without the owner's approval.

## Related skills

- `write-meeting-minutes-with-action-items`
- `map-a-process-from-start-to-finish`
- `onboard-a-new-hire-to-the-business`
