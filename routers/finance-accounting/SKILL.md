---
name: router-finance-accounting
description: Route work in the Finance and accounting domain to the right leaf skill. Use when a task clearly belongs to finance-accounting.
domain: finance-accounting
tags: [router, routing, finance-accounting]
triggers: ["route a finance-accounting task", "which finance-accounting skill should I use"]
---

# Finance and accounting router

## Purpose

List every leaf skill in the finance-accounting domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside finance-accounting and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `audit-spend-for-duplicate-charges` | Use when the user suspects the business is paying twice for the same thing. |
| `build-a-cash-flow-forecast` | Use when the user wants to see whether the business will run out of cash and when. |
| `calculate-a-unit-economics-model` | Use when the user wants to understand the margin on a single sale or customer. |
| `explain-a-profit-and-loss-statement` | Use when the user needs to understand what drove the profit or loss in a period. |
| `post-a-monthly-journal-entry` | Use when the user wants to post a recurring journal entry at the end of a month. |
| `prepare-a-budget-vs-actual-report` | Use when the user wants a report comparing the budget with the actual results. |
| `prepare-a-financial-summary-for-a-board` | Use when the user needs a short financial summary for a board or leadership meeting. |
| `prepare-a-fundraising-data-room` | Use when the user is preparing documents for investors, lenders or due diligence. |
| `prepare-a-monthly-close-checklist` | Use when the user needs a repeatable checklist for closing the books each month. |
| `prepare-a-vat-return` | Use when the user needs to prepare a VAT or sales tax return for a period. |
| `reconcile-a-bank-account` | Use when the user wants to reconcile a bank account against the ledger and find the differences. |
| `resolve-a-payment-dispute` | Use when the user has a customer or supplier disputing a payment. |
| `review-a-balance-sheet` | Use when the user wants to check a balance sheet for accuracy and risk before it is filed or used. |
| `review-a-supplier-contract-payment-terms` | Use when the user wants to check the payment terms in a supplier contract before signing. |
| `set-up-an-expense-approval-workflow` | Use when the user wants a consistent process for approving expenses. |
| `set-up-an-invoice-follow-up-routine` | Use when the user wants to collect overdue invoices without chasing each one by hand. |
| `track-accruals-and-prepayments` | Use when the user wants to manage the timing of income and costs across periods. |
| `write-an-accounts-payable-aging-report` | Use when the user wants to see what the business owes suppliers and how late it is. |
