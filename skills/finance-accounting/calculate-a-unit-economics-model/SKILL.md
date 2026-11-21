---
name: calculate-a-unit-economics-model
description: Calculate a unit economics model that shows the margin on each unit sold. Use when the user wants to understand the margin on a single sale or customer.
domain: finance-accounting
tags: [unit-economics, margin, modelling]
triggers: ["calculate unit economics", "margin on a single customer or order", "contribution margin and payback model"]
---

# Calculate a unit economics model that shows the margin on each unit sold

## Purpose

Calculate a unit economics model that shows the margin on each unit sold.

## When to use

Use when the user wants to understand the margin on a single sale or customer.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Define the unit, whether it is a transaction, a subscription month or a customer.
2. List every cost that varies with that unit, including support and delivery.
3. Separate the costs that are fixed per period from the ones that scale.
4. Calculate the contribution margin and then the payback period.
5. Test the result against a realistic volume and a realistic price change.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `build-a-cash-flow-forecast`
- `explain-a-profit-and-loss-statement`
- `post-a-monthly-journal-entry`
