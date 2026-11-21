---
name: tune-hyperparameters-with-a-search
description: Search a bounded hyperparameter space and select the best reproducible configuration. Use when the user needs to search model hyperparameters within a compute budget.
domain: ml-model-training
tags: [hyperparameter-tuning, model-search, validation]
triggers: ["tune hyperparameters with search", "hyperparameter search for ml", "run grid or random search"]
---

# Search a bounded hyperparameter space and select the best reproducible configuration

## Purpose

Search a bounded hyperparameter space and select the best reproducible configuration.

## When to use

Use when the user needs to search model hyperparameters within a compute budget.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Define a bounded search space around the baseline.
2. Set a fixed search budget from the available compute.
3. Use the same split and metric for every trial.
4. Track failed trials instead of silently discarding them.
5. Select the configuration by validation metric and runtime.
6. Evaluate the winner once on the held-out test split.

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
- `evaluate-a-model-with-precision-and-recall`
