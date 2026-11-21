---
name: build-spaced-repetition-deck
description: Build a spaced-repetition deck with atomic cards and review intervals. Use when the user wants an agent to turn study notes into reviewable flashcards.
domain: learning-skills
tags: [flashcards, repetition, automation]
triggers: ["flashcard deck", "build a flashcard deck", "spaced repetition flashcard deck"]
---

# Build a spaced-repetition deck with atomic cards and review intervals

## Purpose

Build a spaced-repetition deck with atomic cards and review intervals.

## When to use

Use when the user wants an agent to turn study notes into reviewable flashcards.

## When NOT to use

Do not use this for producing a training artefact for a team; use technical-writing instead.

## Inputs required

- The learner's level and goal
- The time available
- The practice or assessment that proves learning

## Procedure

1. Extract atomic facts from the approved study notes.
2. Write one clear question and answer per card.
3. Remove duplicates and flag ambiguous or unsupported cards.
4. Schedule each card at expanding review intervals.
5. Save review outcomes with each card for later adjustment.

## Output contract

A study plan with exercises, a checkpoint schedule and a self-test.

## Validation checklist

- [ ] The plan has a measurable outcome
- [ ] Practice starts before the reading ends
- [ ] There is a way to check retention

## Safety notes

Never present unverified claims about a topic as established fact.

## Related skills

- `build-a-two-week-study-plan`
- `build-learning-feedback-loop`
- `create-learning-concept-map`
