---
name: resolve-a-payment-dispute
description: Resolve a payment dispute by separating the factual disagreement from the commercial decision. Use when the user has a customer or supplier disputing a payment.
domain: finance-accounting
tags: [dispute, negotiation, receivables]
triggers: ["resolve a payment dispute", "customer disputes an invoice", "supplier refuses to pay a bill"]
---

# Resolve a payment dispute by separating the factual disagreement from the commercial decision

## Purpose

Resolve a payment dispute by separating the factual disagreement from the commercial decision.

## When to use

Use when the user has a customer or supplier disputing a payment.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Get the underlying contract, the invoice and the delivery evidence in one place.
2. List each disputed line with the amount and the specific reason given.
3. Check which lines are factual disagreements and which are commercial positions.
4. Propose a resolution with the options and the cost of each to the business.
5. Agree the outcome in writing and update the ledger only once it is authorised.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `review-a-supplier-contract-payment-terms`
- `build-a-cash-flow-forecast`
- `calculate-a-unit-economics-model`
