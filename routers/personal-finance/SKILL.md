---
name: router-personal-finance
description: Route work in the Personal finance domain to the right leaf skill. Use when a task clearly belongs to personal-finance.
domain: personal-finance
tags: [router, routing, personal-finance]
triggers: ["route a personal-finance task", "which personal-finance skill should I use"]
---

# Personal finance router

## Purpose

List every leaf skill in the personal-finance domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside personal-finance and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for company accounting or tax filing; use finance-accounting instead.

## Inputs required

- The income, the bills and the goals
- The time horizon and the risk tolerance
- The jurisdiction for tax and benefit rules

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A prioritised plan with a budget breakdown, an emergency buffer target and the next concrete action.

## Validation checklist

- [ ] The plan balances on the real numbers
- [ ] High-interest debt is addressed first if it exists
- [ ] Tax or benefit claims are flagged for verification

## Safety notes

Never give personalised tax or investment advice as if it were professional advice, and never ask for account numbers or credentials.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `automate-bill-payments` | Use when the user wants recurring bills to be paid automatically and on schedule. |
| `build-a-zero-based-budget` | Use when the user wants a monthly budget that assigns every pound or dollar a purpose. |
| `check-a-fee-and-charger-in-a-subscription` | Use when the user wants to audit a subscription before deciding to keep it. |
| `compare-credit-cards-on-cost` | Use when the user wants to choose between credit cards based on what they will actually pay. |
| `pay-down-debt-with-a-plan` | Use when the user wants a concrete schedule for clearing credit card or other debts. |
| `plan-a-big-purchase-affordably` | Use when the user wants to buy something expensive without overextending their money. |
| `plan-a-sinking-fund` | Use when the user wants to save steadily for a specific planned purchase or renewal. |
| `review-a-monthly-finance-routine` | Use when the user wants a repeatable monthly check on their money. |
| `set-up-an-emergency-fund` | Use when the user wants a buffer to cover unexpected costs or a sudden loss of income. |
| `start-a-first-investment` | Use when the user wants to make their first investment and needs a safe starting point. |
| `track-spending-in-one-place` | Use when the user wants to see all of their spending together instead of scattered across accounts. |
