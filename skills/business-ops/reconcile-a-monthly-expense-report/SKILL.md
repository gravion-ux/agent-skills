---
name: reconcile-a-monthly-expense-report
description: Reconcile a monthly expense report by matching transactions, categories, approvals, and totals. Use when the user needs to reconcile a monthly expense report for review or approval.
domain: business-ops
tags: [expense-reconciliation, month-end, approvals]
triggers: ["reconcile monthly expense report", "match monthly expenses to receipts", "monthly expense reconciliation"]
---

# Reconcile a monthly expense report by matching transactions, categories, approvals, and totals

## Purpose

Reconcile a monthly expense report by matching transactions, categories, approvals, and totals.

## When to use

Use when the user needs to reconcile a monthly expense report for review or approval.

## When NOT to use

Do not use this for a single customer conversation; use communication instead.

## Inputs required

- The process being run
- The inputs and who supplies them
- The service level the process must meet

## Procedure

1. Obtain the approved budget, source transactions, receipts, and prior report total.
2. Match each expense to its receipt, date, amount, category, and approving owner.
3. Investigate duplicates, missing receipts, unsupported amounts, and category errors.
4. Recalculate totals and reconcile the report with source and budget records.
5. Route disputed, financial, tax, or policy exceptions to the accountable owner.
6. Record the reconciled total, variance, exceptions, and sign-off before submission.

## Output contract

A documented operating procedure with owners, inputs, steps and the metrics it is judged on.

## Validation checklist

- [ ] Every step has an owner
- [ ] The failure path is documented
- [ ] The metric that proves the process works is named

## Safety notes

Never change a financial, legal or contractual step without the owner's approval.

## Related skills

- `check-compliance-with-a-process`
- `delegate-a-task-with-a-clear-outcome`
- `document-a-business-process`
