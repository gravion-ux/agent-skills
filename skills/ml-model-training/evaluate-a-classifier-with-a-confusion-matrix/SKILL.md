---
name: evaluate-a-classifier-with-a-confusion-matrix
description: Diagnose classifier errors with a class-labelled confusion matrix. Use when the user needs to diagnose classifier errors by class.
domain: ml-model-training
tags: [confusion-matrix, classification, model-evaluation]
triggers: ["evaluate classifier with confusion matrix", "classifier confusion matrix", "inspect classification error cells"]
---

# Diagnose classifier errors with a class-labelled confusion matrix

## Purpose

Diagnose classifier errors with a class-labelled confusion matrix.

## When to use

Use when the user needs to diagnose classifier errors by class.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Collect predictions and labels from the held-out split.
2. Define the positive class before counting outcomes.
3. Count true and false positives and negatives.
4. Inspect class support and identify the largest error cells.
5. Link error counts to the model's decision threshold.
6. Record the matrix with metric context and class labels.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `evaluate-a-model-with-precision-and-recall`
- `batch-predict-with-a-trained-model`
- `choose-a-threshold-for-a-classifier`
