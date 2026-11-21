---
name: track-accruals-and-prepayments
description: Track accruals and prepayments so each period carries only its own costs and income. Use when the user wants to manage the timing of income and costs across periods.
domain: finance-accounting
tags: [accruals, prepayments, timing]
triggers: ["track accruals and prepayments", "accrue costs into the right period", "manage prepayments in the ledger"]
---

# Track accruals and prepayments so each period carries only its own costs and income

## Purpose

Track accruals and prepayments so each period carries only its own costs and income.

## When to use

Use when the user wants to manage the timing of income and costs across periods.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. List every invoice that has been received or issued but not yet settled.
2. Determine the period each item belongs to by the service or delivery date.
3. Post the accrual or the prepayment at the period end and release it on settlement.
4. Review the accrual list monthly for items that should no longer be held.
5. Reconcile the remaining balance to the open invoices each period.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `explain-a-profit-and-loss-statement`
- `audit-spend-for-duplicate-charges`
- `build-a-cash-flow-forecast`
