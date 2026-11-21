---
name: build-a-cash-flow-forecast
description: Build a cash flow forecast from expected receipts and payments over the coming weeks. Use when the user wants to see whether the business will run out of cash and when.
domain: finance-accounting
tags: [cash-flow, forecast, liquidity]
triggers: ["build a cash flow forecast", "when will my cash run out", "thirteen week cash forecast"]
---

# Build a cash flow forecast from expected receipts and payments over the coming weeks

## Purpose

Build a cash flow forecast from expected receipts and payments over the coming weeks.

## When to use

Use when the user wants to see whether the business will run out of cash and when.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. List the expected cash receipts with their dates and confidence.
2. List the expected payments with their dates, including the ones that are not yet invoiced.
3. Open the forecast with the cash balance at the start of the period.
4. Extend it far enough to cover the longest payment gap, not just one month.
5. Mark the weeks where the balance goes negative and name the action for each.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `calculate-a-unit-economics-model`
- `explain-a-profit-and-loss-statement`
- `post-a-monthly-journal-entry`
