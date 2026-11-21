---
name: choose-a-threshold-for-a-classifier
description: Choose a classifier threshold that satisfies the operating constraint. Use when the user needs to set a classifier operating threshold.
domain: ml-model-training
tags: [threshold-tuning, classification, decision-threshold]
triggers: ["choose threshold for classifier", "classifier decision threshold", "tune classification threshold"]
---

# Choose a classifier threshold that satisfies the operating constraint

## Purpose

Choose a classifier threshold that satisfies the operating constraint.

## When to use

Use when the user needs to set a classifier operating threshold.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Obtain validation probabilities without touching the test split.
2. Compute precision, recall, and expected cost across candidate thresholds.
3. Choose the threshold that satisfies the stated operating constraint.
4. Document the resulting rates and any rejected constraints.
5. Apply the frozen threshold to the held-out test split.
6. Store the threshold beside the serialized model.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `evaluate-a-classifier-with-a-confusion-matrix`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
