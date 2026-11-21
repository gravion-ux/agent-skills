---
name: handle-missing-values-in-a-dataset
description: Impute or handle missing feature values in a way that matches the training and serving paths. Use when the user needs a safe imputation strategy for incomplete training features.
domain: ml-model-training
tags: [missing-data, imputation, feature-engineering]
triggers: ["handle missing values in dataset", "impute missing training features", "missing value strategy for ml"]
---

# Impute or handle missing feature values in a way that matches the training and serving paths

## Purpose

Impute or handle missing feature values in a way that matches the training and serving paths.

## When to use

Use when the user needs a safe imputation strategy for incomplete training features.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Profile missingness by feature, group, and target.
2. Distinguish structural missingness from random missingness.
3. Fit imputers on the training partition only.
4. Add missingness indicators when the signal is predictive.
5. Apply the same imputation pipeline to serving data.
6. Compare performance with and without the imputation strategy.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `detect-data-leakage-in-a-pipeline`
- `handle-class-imbalance-in-training`
- `prepare-a-labelled-dataset`
