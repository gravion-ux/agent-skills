---
name: substitute-an-ingredient-in-a-recipe
description: Substitute an ingredient in a recipe by matching its function rather than its name. Use when the user is missing an ingredient and wants to know what to use instead.
domain: cooking-food
tags: [substitution, ingredients, adaptation]
triggers: ["substitute an ingredient in a recipe", "what can I use instead of this missing ingredient", "swap an ingredient without ruining the dish"]
---

# Substitute an ingredient in a recipe by matching its function rather than its name

## Purpose

Substitute an ingredient in a recipe by matching its function rather than its name.

## When to use

Use when the user is missing an ingredient and wants to know what to use instead.

## When NOT to use

Do not use this for nutrition planning over weeks; use health-wellness instead.

## Inputs required

- The dish, the servings and the equipment
- The dietary constraints and the allergies
- The time available

## Procedure

1. Identify what the missing ingredient does in the dish, such as thickening, acidity or fat.
2. Choose a replacement that performs that same function in a similar amount.
3. Adjust the seasoning, because substitutes often bring their own salt or sweetness.
4. Reduce the liquid when the replacement releases water, such as fresh instead of canned tomato.
5. Note the change in cooking time if the substitute needs longer to cook through.

## Output contract

A scaled recipe with timings, temperatures, substitutions and the order of operations.

## Validation checklist

- [ ] The quantities scale linearly with the servings
- [ ] Allergens are called out explicitly
- [ ] Food-safety timings are respected

## Safety notes

Never suggest a workaround for a serious allergy, and state when food must be cooked to a safe internal temperature.

## Related skills

- `reduce-food-waste-in-a-kitchen`
- `scale-a-recipe-for-more-people`
- `braise-a-meat`
