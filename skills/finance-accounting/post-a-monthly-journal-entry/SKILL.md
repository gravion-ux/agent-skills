---
name: post-a-monthly-journal-entry
description: Post a monthly journal entry with the supporting detail and the approval attached. Use when the user wants to post a recurring journal entry at the end of a month.
domain: finance-accounting
tags: [journal, posting, accrual]
triggers: ["post a monthly journal entry", "month end journal for my accounts", "post recurring monthly accrual entry"]
---

# Post a monthly journal entry with the supporting detail and the approval attached

## Purpose

Post a monthly journal entry with the supporting detail and the approval attached.

## When to use

Use when the user wants to post a recurring journal entry at the end of a month.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. List the accounts to be debited and credited with their amounts.
2. Attach the source document or the calculation that justifies each figure.
3. Check the entry balances and confirm the period is still open.
4. Name the approver and record who posted it and when.
5. Post the entry and verify the resulting ledger balance.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `prepare-a-monthly-close-checklist`
- `build-a-cash-flow-forecast`
- `calculate-a-unit-economics-model`
