---
name: design-an-experiment-with-a-control-group
description: Design a controlled experiment with explicit hypotheses, assignment, metrics, and stopping rules. Use when the user wants to test a treatment using a control group.
domain: data-analysis
tags: [experiment-design, control-group, randomization]
triggers: ["experiment with control group", "design a controlled experiment", "plan treatment and control"]
---

# Design a controlled experiment with explicit hypotheses, assignment, metrics, and stopping rules

## Purpose

Design a controlled experiment with explicit hypotheses, assignment, metrics, and stopping rules.

## When to use

Use when the user wants to test a treatment using a control group.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the treatment, control, population, and primary outcome.
2. Specify the minimum effect, power, sample size, and allocation ratio.
3. Randomise assignment and prevent treatment contamination.
4. Predefine the analysis plan, guardrails, and data-quality checks.
5. Set the run duration, stopping rule, and interpretation criteria.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `test-a-hypothesis-with-a-significance-test`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`
