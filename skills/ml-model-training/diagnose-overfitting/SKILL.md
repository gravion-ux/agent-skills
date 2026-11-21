---
name: diagnose-overfitting
description: Diagnose overfitting from metric gaps, learning curves, and model complexity. Use when the user sees training performance exceed evaluation performance.
domain: ml-model-training
tags: [overfitting, model-diagnosis, generalization]
triggers: ["diagnose model overfitting", "overfitting diagnosis", "close train validation gap"]
---

# Diagnose overfitting from metric gaps, learning curves, and model complexity

## Purpose

Diagnose overfitting from metric gaps, learning curves, and model complexity.

## When to use

Use when the user sees training performance exceed evaluation performance.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Compare training, validation, and held-out metric curves.
2. Inspect learning curves for a widening generalization gap.
3. Check sample size, noise, feature count, and training duration.
4. Reduce capacity or add regularization and data augmentation.
5. Re-evaluate with the same split and metric.
6. Record the diagnosis and the corrected configuration.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `diagnose-underfitting`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
