---
name: monitor-model-drift-in-production
description: Detect production feature and prediction drift through scheduled reference checks. Use when the user needs a scheduled monitor for production model drift.
domain: ml-model-training
tags: [model-drift, production-monitoring, data-distribution]
triggers: ["monitor model drift in production", "production model drift monitor", "detect feature prediction drift"]
---

# Detect production feature and prediction drift through scheduled reference checks

## Purpose

Detect production feature and prediction drift through scheduled reference checks.

## When to use

Use when the user needs a scheduled monitor for production model drift.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Capture feature, prediction, and label distributions from production.
2. Define reference windows and alert thresholds per segment.
3. Run scheduled drift checks on a consistent time window.
4. Route breached thresholds to an incident queue with evidence.
5. Track acknowledged drift and mitigation status over time.
6. Save dashboards, threshold versions, and response notes.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
- `cross-validate-a-model`
