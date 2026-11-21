---
name: encode-categorical-features
description: Convert categorical fields into model-ready representations while preserving unknown-category behavior. Use when the user needs to turn categorical fields into model-ready features.
domain: ml-model-training
tags: [categorical-encoding, feature-engineering, data-preparation]
triggers: ["encode categorical features", "categorical feature encoding", "handle unknown categories in ml"]
---

# Convert categorical fields into model-ready representations while preserving unknown-category behavior

## Purpose

Convert categorical fields into model-ready representations while preserving unknown-category behavior.

## When to use

Use when the user needs to turn categorical fields into model-ready features.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. List each categorical column and its allowed values.
2. Combine rare levels into an explicit other category.
3. Fit an encoder on the training partition only.
4. Choose an explicit unknown-category encoding.
5. Transform validation and serving data with the fitted encoder.
6. Save the category map in the model configuration.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `scale-numeric-features`
- `select-features-with-importance-scores`
- `apply-regularisation-to-a-model`
