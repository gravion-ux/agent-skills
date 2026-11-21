---
name: write-an-rfc-for-review
description: Write an RFC that makes review easy by stating the decision and the objections early. Use when the user wants to propose a change for structured team review.
domain: technical-writing
tags: [rfc, review, proposal]
triggers: ["write an rfc for review", "request for comments document", "propose a change for team review"]
---

# Write an RFC that makes review easy by stating the decision and the objections early

## Purpose

Write an RFC that makes review easy by stating the decision and the objections early.

## When to use

Use when the user wants to propose a change for structured team review.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State the decision in the title so the reader knows what is being asked.
2. Give the summary and the motivation before the details.
3. State the alternatives and the reason the proposal was chosen.
4. Mark the parts where feedback is specifically wanted.
5. Set the review deadline and say what happens after it.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-runbook-for-an-operational-task`
- `write-an-architecture-decision-record-for-a-reviewer`
- `review-a-technical-document-for-accuracy`
