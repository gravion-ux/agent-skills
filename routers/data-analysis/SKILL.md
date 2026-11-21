---
name: router-data-analysis
description: Route work in the Data analysis domain to the right leaf skill. Use when a task clearly belongs to data-analysis.
domain: data-analysis
tags: [router, routing, data-analysis]
triggers: ["route a data-analysis task", "which data-analysis skill should I use"]
---

# Data analysis router

## Purpose

List every leaf skill in the data-analysis domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside data-analysis and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `analyse-a-survey-result` | Use when the user needs to interpret responses collected through a survey. |
| `analyse-a-text-corpus` | Use when the user needs to extract patterns from a collection of documents. |
| `analyse-a-time-series` | Use when the user needs to understand patterns in measurements over time. |
| `ask-a-clear-analytical-question` | Use when the user has a vague topic but needs a question that can guide analysis. |
| `automate-a-recurring-analysis-report` | Use when the user wants a repeatable report delivered on a schedule. |
| `build-a-funnel-analysis` | Use when the user needs to understand conversion through an ordered process. |
| `build-a-pivot-table-for-a-question` | Use when the user needs a pivot table organised around a specific analytical question. |
| `build-an-interactive-analysis-dashboard` | Use when the user wants a dashboard that supports repeatable analysis and exploration. |
| `calculate-a-cohort-retention-rate` | Use when the user needs to measure retention across dated cohorts. |
| `choose-the-right-chart-for-a-question` | Use when the user needs to select an appropriate chart for an analytical message. |
| `compare-two-groups-statistically` | Use when the user needs to determine whether two groups differ meaningfully. |
| `design-an-experiment-with-a-control-group` | Use when the user wants to test a treatment using a control group. |
| `detect-outliers-in-a-numeric-column` | Use when the user suspects extreme values may be affecting a numeric analysis. |
| `explore-a-distribution` | Use when the user wants an initial view of how values are distributed. |
| `find-and-remove-duplicate-rows` | Use when the user needs to deduplicate rows without losing legitimate records. |
| `forecast-a-time-series-baseline` | Use when the user needs a transparent baseline forecast and error estimate. |
| `handle-missing-values-in-an-analysis` | Use when the user must handle missing fields in an analysis without hiding data loss. |
| `measure-a-feature-launch-impact` | Use when the user needs to evaluate whether a released feature changed outcomes. |
| `prepare-data-for-a-stakeholder-review` | Use when the user needs to present analytical evidence for a stakeholder decision. |
| `profile-a-dataset-before-analysing` | Use when the user needs to assess a dataset before analysing it. |
| `quantify-uncertainty-in-an-estimate` | Use when the user needs to communicate the uncertainty behind an estimate. |
| `reconcile-two-different-data-sources` | Use when the user needs to reconcile totals or records from two systems. |
| `run-a-correlation-analysis` | Use when the user wants to quantify relationships between variables. |
| `sanity-check-an-aggregate-number` | Use when the user needs to verify that a reported total makes sense. |
| `segment-a-population-by-behaviour` | Use when the user wants to group a population by observed behaviour. |
| `spot-a-misleading-chart` | Use when the user suspects a chart exaggerates or conceals a comparison. |
| `tell-a-data-story-in-a-narrative` | Use when the user wants to communicate an analytical finding as a narrative. |
| `test-a-hypothesis-with-a-significance-test` | Use when the user needs a significance test for a prespecified hypothesis. |
| `validate-an-analysis-result` | Use when the user wants confidence that an analytical output is correct. |
| `write-a-clean-analysis-query` | Use when the user needs SQL that computes an analytical result correctly. |
