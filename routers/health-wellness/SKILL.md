---
name: router-health-wellness
description: Route work in the Health and wellness domain to the right leaf skill. Use when a task clearly belongs to health-wellness.
domain: health-wellness
tags: [router, routing, health-wellness]
triggers: ["route a health-wellness task", "which health-wellness skill should I use"]
---

# Health and wellness router

## Purpose

List every leaf skill in the health-wellness domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside health-wellness and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a medical diagnosis or an acute emergency; use a qualified clinician instead.

## Inputs required

- The goal and the current baseline
- The time, equipment and mobility available
- Any constraints the user has stated

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A realistic plan with weekly structure, a simple tracking method and clear stopping conditions.

## Validation checklist

- [ ] The plan matches the stated baseline and constraints
- [ ] Progression is gradual and reversible
- [ ] The plan says when to seek professional advice

## Safety notes

Never diagnose, prescribe or set medical targets, and never encourage a routine that contradicts a clinician's advice.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `build-a-sleep-routine` | Use when the user wants to improve their sleep by changing their evening and morning routine. |
| `build-a-stress-relief-routine` | Use when the user wants a repeatable way to manage everyday stress. |
| `build-a-sustainable-exercise-routine` | Use when the user wants a regular exercise habit that will not collapse after a week. |
| `do-a-safe-indoor-workout-check` | Use when the user is about to exercise indoors and wants to make sure the space is safe. |
| `eat-well-on-a-budget` | Use when the user wants to eat nutritious food without spending much money. |
| `improve-sleep-hygiene` | Use when the user wants practical changes that will improve the quality of their sleep. |
| `plan-a-home-workout` | Use when the user wants a workout routine they can do at home. |
| `plan-a-week-of-meals` | Use when the user wants a meal plan for the week ahead. |
| `prepare-a-healthy-weeknight-dinner` | Use when the user wants a healthy dinner that is quick on an ordinary evening. |
| `prepare-for-a-doctor-appointment` | Use when the user wants to get ready for an appointment with a clinician. |
| `reduce-sedentary-time` | Use when the user sits for long periods and wants to move more during the day. |
| `review-a-supplement-or-diet-claim` | Use when the user has seen a health claim and wants it checked before they try it. |
| `set-a-realistic-fitness-milestone` | Use when the user wants a fitness target that will not be unrealistic or vague. |
| `start-a-walking-program` | Use when the user wants to begin walking regularly as exercise. |
| `take-a-screen-break-that-works` | Use when the user wants a break from screen work that reduces fatigue instead of adding to it. |
| `track-a-fitness-goal` | Use when the user wants to track progress towards a fitness goal over weeks or months. |
| `track-a-symptom-diary` | Use when the user wants to record symptoms to find a pattern over time. |
| `warm-up-before-exercise` | Use when the user wants a warm-up routine before a workout or a sport. |
