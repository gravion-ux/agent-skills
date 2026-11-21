---
name: cross-validate-a-model
description: Cross-validate a model with folds that match the data-generating process. Use when the user needs a robust validation estimate across appropriate folds.
domain: ml-model-training
tags: [cross-validation, model-evaluation, resampling]
triggers: ["cross validate model", "k fold cross validation", "validate model across folds"]
---

# Cross-validate a model with folds that match the data-generating process

## Purpose

Cross-validate a model with folds that match the data-generating process.

## When to use

Use when the user needs a robust validation estimate across appropriate folds.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Choose grouped, stratified, or time-based folds to match the data.
2. Fit preprocessing inside each training fold.
3. Score every fold with the predeclared metric.
4. Report the mean, spread, and per-fold failures.
5. Inspect folds for unusual distributions.
6. Fit the final pipeline on all development data.

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
- `evaluate-a-model-with-precision-and-recall`
