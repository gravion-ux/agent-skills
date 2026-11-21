---
name: apply-regularisation-to-a-model
description: Reduce overfitting by selecting and validating an appropriate regularization strength. Use when the user needs to reduce a confirmed overfitting gap.
domain: ml-model-training
tags: [regularization, model-training, generalization]
triggers: ["apply regularization to model", "regularize overfit model", "choose l1 l2 or weight decay"]
---

# Reduce overfitting by selecting and validating an appropriate regularization strength

## Purpose

Reduce overfitting by selecting and validating an appropriate regularization strength.

## When to use

Use when the user needs to reduce a confirmed overfitting gap.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Confirm overfitting with a generalization-gap analysis.
2. Choose a regularization parameter appropriate to the model family.
3. Search the parameter on validation data only.
4. Compare validation metrics and training cost across trials.
5. Evaluate the selected model once on the held-out split.
6. Save the parameter and training configuration.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `batch-predict-with-a-trained-model`
- `cross-validate-a-model`
- `evaluate-a-model-with-precision-and-recall`
