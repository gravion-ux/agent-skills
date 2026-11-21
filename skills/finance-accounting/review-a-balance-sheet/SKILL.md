---
name: review-a-balance-sheet
description: Review a balance sheet by testing whether each balance is supported and current. Use when the user wants to check a balance sheet for accuracy and risk before it is filed or used.
domain: finance-accounting
tags: [balance-sheet, review, audit]
triggers: ["review a balance sheet", "check the balance sheet for errors", "sanity check my statement of financial position"]
---

# Review a balance sheet by testing whether each balance is supported and current

## Purpose

Review a balance sheet by testing whether each balance is supported and current.

## When to use

Use when the user wants to check a balance sheet for accuracy and risk before it is filed or used.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. Check that each balance ties to the underlying ledger and to the supporting schedule.
2. Compare the current period with the prior period and investigate every large movement.
3. Test the balances that depend on judgement, such as accruals, provisions and goodwill.
4. Confirm the restricted and non-current balances cannot be used as working capital.
5. Record each issue with the amount, the risk and the action needed to close it.

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
