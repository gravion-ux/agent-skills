---
name: select-features-with-importance-scores
description: Rank and prune model features using importance scores and held-out validation. Use when the user needs to rank features and justify a simpler model.
domain: ml-model-training
tags: [feature-selection, model-interpretability, tree-models]
triggers: ["select features with importance scores", "model feature importance", "rank features by importance"]
---

# Rank and prune model features using importance scores and held-out validation

## Purpose

Rank and prune model features using importance scores and held-out validation.

## When to use

Use when the user needs to rank features and justify a simpler model.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Select an importance method that matches the model and data.
2. Compute importances on validation or held-out predictions.
3. Check direction, magnitude, and correlated-feature groups.
4. Remove or group features using a declared threshold.
5. Compare performance before and after removal.
6. Save the importance values with the model report.

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
- `encode-categorical-features`
- `evaluate-a-classifier-with-a-confusion-matrix`
