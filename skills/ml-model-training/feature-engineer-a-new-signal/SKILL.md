---
name: feature-engineer-a-new-signal
description: Design a predictive feature that is available at inference time and adds measurable value. Use when the user needs a new feature that improves prediction without leakage.
domain: ml-model-training
tags: [feature-engineering, signal-design, leakage-prevention]
triggers: ["feature engineer new signal", "engineer predictive feature", "add a leakage safe ml feature"]
---

# Design a predictive feature that is available at inference time and adds measurable value

## Purpose

Design a predictive feature that is available at inference time and adds measurable value.

## When to use

Use when the user needs a new feature that improves prediction without leakage.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Choose a signal tied to the stated prediction objective.
2. Compute the feature only from information available at prediction time.
3. Fit any transformation parameters on training data only.
4. Measure the incremental metric on validation data.
5. Remove the feature if it adds no consistent value.
6. Document the feature formula and serving dependencies.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `retrain-a-model-on-new-data`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
