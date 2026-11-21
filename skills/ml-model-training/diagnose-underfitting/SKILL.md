---
name: diagnose-underfitting
description: Diagnose underfitting from training performance, error patterns, and model capacity. Use when the user sees a model underperform both the baseline and its training data.
domain: ml-model-training
tags: [underfitting, model-diagnosis, model-capacity]
triggers: ["diagnose model underfitting", "underfitting diagnosis", "improve weak model fit"]
---

# Diagnose underfitting from training performance, error patterns, and model capacity

## Purpose

Diagnose underfitting from training performance, error patterns, and model capacity.

## When to use

Use when the user sees a model underperform both the baseline and its training data.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Compare training and validation metrics with the baseline.
2. Inspect residual or error patterns by subgroup and class.
3. Increase capacity, features, or optimization steps.
4. Verify the learning rate and convergence history.
5. Re-evaluate using the unchanged split and metric.
6. Record the diagnosis and updated model configuration.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `diagnose-overfitting`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
