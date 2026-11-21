---
name: prepare-a-vat-return
description: Prepare a VAT return that ties to the underlying records and flags the doubtful items. Use when the user needs to prepare a VAT or sales tax return for a period.
domain: finance-accounting
tags: [vat, tax, compliance]
triggers: ["prepare a vat return", "file my sales tax quarterly return", "vat reconciliation before filing"]
---

# Prepare a VAT return that ties to the underlying records and flags the doubtful items

## Purpose

Prepare a VAT return that ties to the underlying records and flags the doubtful items.

## When to use

Use when the user needs to prepare a VAT or sales tax return for a period.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Reconcile the sales and purchase ledgers to the filed VAT accounts and to the bank.
2. Check the treatment of each category of income and expense against the local rules.
3. Investigate the invoices with missing tax details or disputed amounts.
4. Calculate the net position and check it against the previous period.
5. Review the return with a qualified person before it is filed.

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
- `prepare-a-financial-summary-for-a-board`
- `prepare-a-fundraising-data-room`
