---
name: explain-a-technical-concept-to-a-senior-reader
description: Explain a technical concept to a senior reader in terms of decision and risk. Use when the user needs to explain a technical subject to someone who will decide about it.
domain: technical-writing
tags: [explainer, senior, decision]
triggers: ["explain a technical concept to a senior reader", "brief an exec on this design", "technical summary for leadership"]
---

# Explain a technical concept to a senior reader in terms of decision and risk

## Purpose

Explain a technical concept to a senior reader in terms of decision and risk.

## When to use

Use when the user needs to explain a technical subject to someone who will decide about it.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Identify the decision the reader will have to make after reading.
2. State the problem in one sentence before any detail.
3. Give the two or three implications that affect the decision.
4. Name the cost, the risk and the uncertainty plainly.
5. End with the recommendation and what would change it.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `explain-a-tradeoff-with-numbers`
- `review-a-technical-document-for-accuracy`
- `write-a-technical-abstract`
