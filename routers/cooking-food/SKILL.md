---
name: router-cooking-food
description: Route work in the Cooking and food domain to the right leaf skill. Use when a task clearly belongs to cooking-food.
domain: cooking-food
tags: [router, routing, cooking-food]
triggers: ["route a cooking-food task", "which cooking-food skill should I use"]
---

# Cooking and food router

## Purpose

List every leaf skill in the cooking-food domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside cooking-food and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for nutrition planning over weeks; use health-wellness instead.

## Inputs required

- The dish, the servings and the equipment
- The dietary constraints and the allergies
- The time available

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A scaled recipe with timings, temperatures, substitutions and the order of operations.

## Validation checklist

- [ ] The quantities scale linearly with the servings
- [ ] Allergens are called out explicitly
- [ ] Food-safety timings are respected

## Safety notes

Never suggest a workaround for a serious allergy, and state when food must be cooked to a safe internal temperature.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `batch-cook-for-the-week` | Use when the user wants to prepare several meals at once for the coming week. |
| `braise-a-meat` | Use when the user wants to cook a tough cut of meat slowly in a braising liquid. |
| `build-a-shopping-list-from-a-menu` | Use when the user wants a shopping list for several planned meals. |
| `cook-a-sourdough-loaf` | Use when the user wants to bake an open-crumb sourdough loaf at home. |
| `cook-rice-perfectly` | Use when the user wants reliably fluffy rice rather than mushy or scorched rice. |
| `fix-a-sauce-that-broke` | Use when the user wants to rescue a sauce that split, curdled or turned grainy. |
| `make-a-pizza-dough` | Use when the user wants to make pizza dough from scratch for a home oven. |
| `plan-a-dinner-party-menu` | Use when the user wants to host a dinner and needs a menu that works as a whole. |
| `plan-a-weeknight-meal` | Use when the user wants a dinner idea that works on a normal weeknight. |
| `prep-vegetables-efficiently` | Use when the user wants to batch-prep vegetables without wasting time or water. |
| `reduce-food-waste-in-a-kitchen` | Use when the user wants to cut the food waste in their household kitchen. |
| `scale-a-recipe-for-more-people` | Use when the user wants to cook a recipe for a different number of servings. |
| `sharpen-a-knife` | Use when the user wants to sharpen a blunt kitchen knife properly. |
| `substitute-an-ingredient-in-a-recipe` | Use when the user is missing an ingredient and wants to know what to use instead. |
