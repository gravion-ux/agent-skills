---
name: router-ml-model-training
description: Route work in the Machine learning and model training domain to the right leaf skill. Use when a task clearly belongs to ml-model-training.
domain: ml-model-training
tags: [router, routing, ml-model-training]
triggers: ["route a ml-model-training task", "which ml-model-training skill should I use"]
---

# Machine learning and model training router

## Purpose

List every leaf skill in the ml-model-training domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside ml-model-training and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `apply-regularisation-to-a-model` | Use when the user needs to reduce a confirmed overfitting gap. |
| `batch-predict-with-a-trained-model` | Use when the user needs to score a large dataset with a fixed model version. |
| `choose-a-threshold-for-a-classifier` | Use when the user needs to set a classifier operating threshold. |
| `clean-and-deduplicate-training-data` | Use when the user needs to repair dirty records and remove repeated training examples. |
| `cross-validate-a-model` | Use when the user needs a robust validation estimate across appropriate folds. |
| `define-a-machine-learning-problem` | Use when the user needs to frame a prediction task with measurable success criteria. |
| `detect-data-leakage-in-a-pipeline` | Use when the user suspects target information leaks into a training pipeline. |
| `detect-model-degradation-over-time` | Use when the user needs to detect and classify performance degradation over time. |
| `diagnose-overfitting` | Use when the user sees training performance exceed evaluation performance. |
| `diagnose-underfitting` | Use when the user sees a model underperform both the baseline and its training data. |
| `encode-categorical-features` | Use when the user needs to turn categorical fields into model-ready features. |
| `evaluate-a-classifier-with-a-confusion-matrix` | Use when the user needs to diagnose classifier errors by class. |
| `evaluate-a-clustering-result` | Use when the user needs to judge whether discovered clusters are useful and stable. |
| `evaluate-a-model-with-precision-and-recall` | Use when the user needs to compare classifier error rates for a business decision. |
| `feature-engineer-a-new-signal` | Use when the user needs a new feature that improves prediction without leakage. |
| `fine-tune-a-pre-trained-model` | Use when the user needs to adapt a pre-trained model to a supervised task. |
| `handle-class-imbalance-in-training` | Use when the user needs to train on imbalanced classes without hiding minority errors. |
| `handle-missing-values-in-a-dataset` | Use when the user needs a safe imputation strategy for incomplete training features. |
| `interpret-a-tree-based-model` | Use when the user needs to explain a tree model's splits and predictions. |
| `monitor-model-drift-in-production` | Use when the user needs a scheduled monitor for production model drift. |
| `prepare-a-labelled-dataset` | Use when the user needs to assemble a legally usable dataset with consistent labels. |
| `retrain-a-model-on-new-data` | Use when the user needs to refresh a deployed model with newly collected data. |
| `run-a-reproducible-training-pipeline` | Use when the user needs a model training run that can be reproduced exactly. |
| `scale-numeric-features` | Use when the user needs consistent numeric scaling between training and serving. |
| `select-a-baseline-model` | Use when the user needs a credible reference model before complex experiments. |
| `select-features-with-importance-scores` | Use when the user needs to rank features and justify a simpler model. |
| `serve-a-trained-model-as-an-api` | Use when the user needs to expose a trained model through a production API. |
| `split-data-for-training-and-evaluation` | Use when the user needs reproducible train, validation, and held-out partitions. |
| `train-a-clustering-model` | Use when the user needs to discover unlabeled groups in training data. |
| `train-a-first-classification-model` | Use when the user needs to train and evaluate a first classification model. |
| `train-a-first-regression-model` | Use when the user needs to train and evaluate a first regression model. |
| `train-a-neural-network-from-scratch` | Use when the user needs to build and train a neural network without a pre-trained model. |
| `tune-hyperparameters-with-a-search` | Use when the user needs to search model hyperparameters within a compute budget. |
| `write-an-experiment-log` | Use when the user needs an auditable record of a training experiment. |
