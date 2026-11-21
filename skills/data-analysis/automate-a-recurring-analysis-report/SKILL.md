---
name: automate-a-recurring-analysis-report
description: Automate a recurring analysis report with validated inputs, scheduled execution, and failure alerts. Use when the user wants a repeatable report delivered on a schedule.
domain: data-analysis
tags: [report-automation, scheduled-analysis, monitoring]
triggers: ["recurring analysis report", "automate weekly analysis report", "schedule analysis with alerts"]
---

# Automate a recurring analysis report with validated inputs, scheduled execution, and failure alerts

## Purpose

Automate a recurring analysis report with validated inputs, scheduled execution, and failure alerts.

## When to use

Use when the user wants a repeatable report delivered on a schedule.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the report metrics, source, recipients, and schedule.
2. Build a reproducible query and templated output.
3. Add checks for freshness, schema, totals, and material changes.
4. Schedule execution and alert on failures or invalid results.
5. Archive each snapshot and delivery log for audit and recovery.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-a-funnel-analysis`
- `run-a-correlation-analysis`
- `write-a-clean-analysis-query`
