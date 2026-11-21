---
name: write-an-accounts-payable-aging-report
description: Write an accounts payable aging report that buckets what is owed by how overdue it is. Use when the user wants to see what the business owes suppliers and how late it is.
domain: finance-accounting
tags: [payables, aging, reporting]
triggers: ["accounts payable aging report", "how much do we owe suppliers and for how long", "payables by days overdue"]
---

# Write an accounts payable aging report that buckets what is owed by how overdue it is

## Purpose

Write an accounts payable aging report that buckets what is owed by how overdue it is.

## When to use

Use when the user wants to see what the business owes suppliers and how late it is.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. List every open payable with the supplier, the invoice date and the due date.
2. Bucket the balances by days overdue, such as not yet due, one to thirty and thirty plus.
3. Flag the balances that are disputed or on hold separately from the rest.
4. Total each bucket and compare the total with the payables control account.
5. Rank the buckets by the amount at risk and note the action for the largest.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `prepare-a-budget-vs-actual-report`
- `set-up-an-expense-approval-workflow`
- `set-up-an-invoice-follow-up-routine`
