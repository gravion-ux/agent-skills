---
name: detect-model-degradation-over-time
description: Detect model performance degradation over time and diagnose its likely cause. Use when the user needs to detect and classify performance degradation over time.
domain: ml-model-training
tags: [model-degradation, production-monitoring, performance-metrics]
triggers: ["detect model degradation over time", "track model metric degradation", "weekly model performance monitoring"]
---

# Detect model performance degradation over time and diagnose its likely cause

## Purpose

Detect model performance degradation over time and diagnose its likely cause.

## When to use

Use when the user needs to detect and classify performance degradation over time.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Schedule weekly evaluations against fixed labeled snapshots.
2. Compare metrics with the acceptance baseline and prior periods.
3. Segment changes by class, cohort, input source, and model version.
4. Classify degradation as data, concept, or system related.
5. Open and prioritize a retraining or rollback decision.
6. Archive evaluation data, metrics, and the decision log.

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
