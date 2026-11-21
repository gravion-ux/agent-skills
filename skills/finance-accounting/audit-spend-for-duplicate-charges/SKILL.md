---
name: audit-spend-for-duplicate-charges
description: Audit spend for duplicate charges by grouping similar transactions by amount and date. Use when the user suspects the business is paying twice for the same thing.
domain: finance-accounting
tags: [audit, duplicates, spend]
triggers: ["audit spend for duplicate charges", "find duplicate payments in our records", "we might be paying twice for the same invoice"]
---

# Audit spend for duplicate charges by grouping similar transactions by amount and date

## Purpose

Audit spend for duplicate charges by grouping similar transactions by amount and date.

## When to use

Use when the user suspects the business is paying twice for the same thing.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Group the payments by amount and by merchant name to surface near-identical entries.
2. Check each candidate pair for a different invoice number, date or reference.
3. Confirm with the supplier whether one of the two charges is a duplicate.
4. Request the refund or credit in writing and keep the correspondence.
5. Correct the ledger only after the credit is confirmed, and record the cause.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `prepare-a-financial-summary-for-a-board`
- `build-a-cash-flow-forecast`
- `calculate-a-unit-economics-model`
