---
name: define-a-machine-learning-problem
description: Turn a business request into a scoped prediction task with labels, metrics, and constraints. Use when the user needs to frame a prediction task with measurable success criteria.
domain: ml-model-training
tags: [problem-definition, machine-learning, metrics]
triggers: ["define machine learning problem", "turn business request into prediction task", "define ml objective"]
---

# Turn a business request into a scoped prediction task with labels, metrics, and constraints

## Purpose

Turn a business request into a scoped prediction task with labels, metrics, and constraints.

## When to use

Use when the user needs to frame a prediction task with measurable success criteria.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Write the prediction target, unit of prediction, and intended use.
2. Define the label, available features, and data provenance.
3. Choose a primary metric tied to the real decision cost.
4. Record compute, latency, fairness, and deployment constraints.
5. Write a one-page problem statement with success and stop criteria.

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
- `choose-a-threshold-for-a-classifier`
