---
name: scale-numeric-features
description: Standardize or normalize numeric features consistently for training and inference. Use when the user needs consistent numeric scaling between training and serving.
domain: ml-model-training
tags: [feature-scaling, preprocessing, numerical-features]
triggers: ["scale numeric features", "numeric feature scaling", "standardize ml inputs"]
---

# Standardize or normalize numeric features consistently for training and inference

## Purpose

Standardize or normalize numeric features consistently for training and inference.

## When to use

Use when the user needs consistent numeric scaling between training and serving.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Inspect feature ranges, units, and skew before scaling.
2. Fit the scaler on the training partition only.
3. Choose standardization or normalization from the training distribution.
4. Apply the fitted scaler to validation and serving data.
5. Record the scaler parameters with the model.
6. Check that inverse transforms recover expected units.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `encode-categorical-features`
- `select-features-with-importance-scores`
- `apply-regularisation-to-a-model`
