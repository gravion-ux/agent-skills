---
name: reconcile-a-bank-account
description: Reconcile a bank account by matching every statement line to a ledger entry. Use when the user wants to reconcile a bank account against the ledger and find the differences.
domain: finance-accounting
tags: [reconciliation, banking, ledger]
triggers: ["reconcile a bank account", "match my bank statement to the ledger", "bank reconciliation differences"]
---

# Reconcile a bank account by matching every statement line to a ledger entry

## Purpose

Reconcile a bank account by matching every statement line to a ledger entry.

## When to use

Use when the user wants to reconcile a bank account against the ledger and find the differences.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Import the bank statement and the ledger for the same period.
2. Match each statement line to a ledger entry using date, amount and reference.
3. List every unmatched line on both sides rather than netting them together.
4. Investigate each difference and classify it as a timing item or a genuine error.
5. Record the reconciling items so the balance can be proved at the period end.

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
- `calculate-a-unit-economics-model`
- `explain-a-profit-and-loss-statement`
