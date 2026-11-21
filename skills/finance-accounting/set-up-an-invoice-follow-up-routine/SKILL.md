---
name: set-up-an-invoice-follow-up-routine
description: Set up an invoice follow-up routine that chases overdue invoices on a predictable schedule. Use when the user wants to collect overdue invoices without chasing each one by hand.
domain: finance-accounting
tags: [invoicing, collections, automation]
triggers: ["invoice follow up routine", "chase overdue invoices on a schedule", "automatic payment reminders for invoices"]
---

# Set up an invoice follow-up routine that chases overdue invoices on a predictable schedule

## Purpose

Set up an invoice follow-up routine that chases overdue invoices on a predictable schedule.

## When to use

Use when the user wants to collect overdue invoices without chasing each one by hand.

## When NOT to use

Do not use this for a budget spreadsheet for a small team; use personal-finance instead.

## Inputs required

- The transactions, invoices or ledger in scope
- The accounting rules and the reporting period
- The reconciliation tolerance

## Procedure

1. List every invoice with its due date, amount, contact and current status.
2. Agree the reminder schedule, such as before due, on due, and every week after.
3. Write one reminder message that states the amount, the due date and the payment details.
4. Escalate to a phone call or a formal notice after the agreed number of reminders.
5. Record every contact so the next person to handle the account knows the history.

## Output contract

A reconciled ledger or report with every difference explained and flagged.

## Validation checklist

- [ ] The totals tie to the source records
- [ ] Every adjustment is traceable to a rule or an approval
- [ ] Rounding differences are within tolerance

## Safety notes

Never post, approve or pay a transaction without explicit authorisation, and never alter a closed period.

## Related skills

- `set-up-an-expense-approval-workflow`
- `write-an-accounts-payable-aging-report`
- `audit-spend-for-duplicate-charges`
