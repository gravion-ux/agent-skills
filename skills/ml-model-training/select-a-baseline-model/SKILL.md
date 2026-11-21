---
name: select-a-baseline-model
description: Choose and record a simple baseline that provides a credible reference score. Use when the user needs a credible reference model before complex experiments.
domain: ml-model-training
tags: [baseline-model, model-selection, metrics]
triggers: ["select baseline model", "choose baseline classifier or regressor", "baseline model for ml"]
---

# Choose and record a simple baseline that provides a credible reference score

## Purpose

Choose and record a simple baseline that provides a credible reference score.

## When to use

Use when the user needs a credible reference model before complex experiments.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Encode and scale the training data using training-only transformations.
2. Train the simplest model that matches the task and metric.
3. Evaluate on the held-out evaluation split.
4. Record the metric, runtime, and training configuration.
5. Set the baseline score as the minimum improvement threshold.
6. Publish the baseline predictions for later comparison.

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
- `cross-validate-a-model`
