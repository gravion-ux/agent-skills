---
name: test-a-hypothesis-with-a-significance-test
description: Test a prespecified statistical hypothesis and report the result without overstating evidence. Use when the user needs a significance test for a prespecified hypothesis.
domain: data-analysis
tags: [hypothesis-testing, statistical-inference, p-value]
triggers: ["significance test", "test a statistical hypothesis", "calculate p value and effect"]
---

# Test a prespecified statistical hypothesis and report the result without overstating evidence

## Purpose

Test a prespecified statistical hypothesis and report the result without overstating evidence.

## When to use

Use when the user needs a significance test for a prespecified hypothesis.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. State the null hypothesis, alternative, and decision threshold.
2. Confirm the sample design and test assumptions.
3. Calculate the test statistic, effect size, and p-value.
4. Interpret the result alongside a confidence interval.
5. Report limitations and distinguish evidence from a final decision.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `design-an-experiment-with-a-control-group`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`
