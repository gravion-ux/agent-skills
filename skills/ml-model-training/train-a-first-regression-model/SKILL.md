---
name: train-a-first-regression-model
description: Build a regression model and analyze its residuals on an untouched test set. Use when the user needs to train and evaluate a first regression model.
domain: ml-model-training
tags: [regression, model-training, error-metrics]
triggers: ["train first regression model", "first regression model", "train baseline regressor"]
---

# Build a regression model and analyze its residuals on an untouched test set

## Purpose

Build a regression model and analyze its residuals on an untouched test set.

## When to use

Use when the user needs to train and evaluate a first regression model.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Create leakage-safe train, validation, and held-out test splits.
2. Fit the regressor on the training partition only.
3. Tune the regularization strength on validation predictions.
4. Evaluate once on the untouched test split.
5. Record error metrics, residual diagnostics, and target coverage.
6. Save the fitted pipeline, configuration, and model card.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `train-a-first-classification-model`
- `train-a-clustering-model`
- `apply-regularisation-to-a-model`
