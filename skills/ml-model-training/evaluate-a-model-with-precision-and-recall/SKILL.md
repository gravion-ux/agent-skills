---
name: evaluate-a-model-with-precision-and-recall
description: Assess classifier errors with precision, recall, and their underlying counts. Use when the user needs to compare classifier error rates for a business decision.
domain: ml-model-training
tags: [precision-recall, classification, model-evaluation]
triggers: ["evaluate model with precision and recall", "precision recall evaluation", "classifier precision and recall"]
---

# Assess classifier errors with precision, recall, and their underlying counts

## Purpose

Assess classifier errors with precision, recall, and their underlying counts.

## When to use

Use when the user needs to compare classifier error rates for a business decision.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Set the positive class and cost of false positives and negatives.
2. Compute precision and recall with their exact denominators.
3. Report class support and the confusion counts behind each rate.
4. Compare results with the baseline and decision threshold.
5. Flag cases where one rate hides a material error.
6. Save the metric definitions with the evaluation results.

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
- `evaluate-a-classifier-with-a-confusion-matrix`
- `apply-regularisation-to-a-model`
