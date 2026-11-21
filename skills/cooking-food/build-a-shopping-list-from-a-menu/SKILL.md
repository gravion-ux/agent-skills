---
name: build-a-shopping-list-from-a-menu
description: Build a shopping list from a chosen menu so ingredients are bought once and nothing is missed. Use when the user wants a shopping list for several planned meals.
domain: cooking-food
tags: [shopping, menu, planning]
triggers: ["shopping list from a menu", "buy everything for these meals in one trip", "consolidated grocery list for several recipes"]
---

# Build a shopping list from a chosen menu so ingredients are bought once and nothing is missed

## Purpose

Build a shopping list from a chosen menu so ingredients are bought once and nothing is missed.

## When to use

Use when the user wants a shopping list for several planned meals.

## When NOT to use

Do not use this for nutrition planning over weeks; use health-wellness instead.

## Inputs required

- The dish, the servings and the equipment
- The dietary constraints and the allergies
- The time available

## Procedure

1. Write out each planned dish with its serving count before listing anything.
2. Collect every ingredient each dish needs, including the pantry staples.
3. Merge duplicate ingredients into one line with the combined quantity.
4. Subtract the ingredients already in the kitchen from the combined list.
5. Group the remaining items by aisle so the shop takes one pass.

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
- `cook-a-sourdough-loaf`
