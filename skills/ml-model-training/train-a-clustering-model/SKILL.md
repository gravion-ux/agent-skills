---
name: train-a-clustering-model
description: Fit a clustering model and document the structure of its discovered groups. Use when the user needs to discover unlabeled groups in training data.
domain: ml-model-training
tags: [clustering, unsupervised-learning, model-training]
triggers: ["train clustering model", "fit clustering model", "cluster training data"]
---

# Fit a clustering model and document the structure of its discovered groups

## Purpose

Fit a clustering model and document the structure of its discovered groups.

## When to use

Use when the user needs to discover unlabeled groups in training data.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Define the business meaning of a cluster before fitting.
2. Select features that are available and meaningful at scoring time.
3. Scale the selected features and choose a clustering algorithm.
4. Fit on the development data and assign cluster labels.
5. Inspect cluster sizes, centroids, and separation.
6. Save the fitted scaler, model, and cluster profile.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `train-a-first-classification-model`
- `train-a-first-regression-model`
- `apply-regularisation-to-a-model`
