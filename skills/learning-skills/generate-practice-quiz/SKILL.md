---
name: generate-practice-quiz
description: Generate a practice quiz with graded questions from the learner's notes. Use when the user wants an agent to create questions from a set of study notes.
domain: learning-skills
tags: [quiz, practice, assessment]
triggers: ["practice quiz", "generate a practice quiz", "quiz from my study notes"]
---

# Generate a practice quiz with graded questions from the learner's notes

## Purpose

Generate a practice quiz with graded questions from the learner's notes.

## When to use

Use when the user wants an agent to create questions from a set of study notes.

## When NOT to use

Do not use this for producing a training artefact for a team; use technical-writing instead.

## Inputs required

- The learner's level and goal
- The time available
- The practice or assessment that proves learning

## Procedure

1. Extract the learning objectives covered by the notes.
2. Write questions that test recall and practical application.
3. Provide an answer key with a short rationale for each item.
4. Label each question with its difficulty and objective.
5. Check that every answer is supported by the source material.

## Output contract

A study plan with exercises, a checkpoint schedule and a self-test.

## Validation checklist

- [ ] The plan has a measurable outcome
- [ ] Practice starts before the reading ends
- [ ] There is a way to check retention

## Safety notes

Never present unverified claims about a topic as established fact.

## Related skills

- `grade-practice-answers`
- `build-a-two-week-study-plan`
- `build-learning-feedback-loop`
