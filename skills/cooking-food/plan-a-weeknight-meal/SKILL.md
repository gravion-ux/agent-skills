---
name: plan-a-weeknight-meal
description: Plan a weeknight meal that fits the time, the equipment and what is already in the kitchen. Use when the user wants a dinner idea that works on a normal weeknight.
domain: cooking-food
tags: [weeknight, meal-plan, quick]
triggers: ["plan a weeknight meal", "what should I cook tonight on a time limit", "quick dinner idea for tonight"]
---

# Plan a weeknight meal that fits the time, the equipment and what is already in the kitchen

## Purpose

Plan a weeknight meal that fits the time, the equipment and what is already in the kitchen.

## When to use

Use when the user wants a dinner idea that works on a normal weeknight.

## When NOT to use

Do not use this for nutrition planning over weeks; use health-wellness instead.

## Inputs required

- The dish, the servings and the equipment
- The dietary constraints and the allergies
- The time available

## Procedure

1. Fix the time available, including the time waiting for the oven or pan.
2. Check which ingredients and equipment are already available.
3. Choose a dish whose steps fit the time with no last-minute additions.
4. Confirm the dietary constraints and call out every allergen in the dish.
5. Give the order of operations so nothing waits on a step that has not started.

## Output contract

A scaled recipe with timings, temperatures, substitutions and the order of operations.

## Validation checklist

- [ ] The quantities scale linearly with the servings
- [ ] Allergens are called out explicitly
- [ ] Food-safety timings are respected

## Safety notes

Never suggest a workaround for a serious allergy, and state when food must be cooked to a safe internal temperature.

## Related skills

- `plan-a-dinner-party-menu`
- `braise-a-meat`
- `build-a-shopping-list-from-a-menu`
