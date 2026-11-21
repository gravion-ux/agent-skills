---
name: handle-class-imbalance-in-training
description: Train a classifier on imbalanced data while protecting minority-class performance. Use when the user needs to train on imbalanced classes without hiding minority errors.
domain: ml-model-training
tags: [class-imbalance, classification, resampling]
triggers: ["handle class imbalance in training", "imbalanced classification training", "balance minority classes"]
---

# Train a classifier on imbalanced data while protecting minority-class performance

## Purpose

Train a classifier on imbalanced data while protecting minority-class performance.

## When to use

Use when the user needs to train on imbalanced classes without hiding minority errors.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Measure class frequencies and the cost of each error type.
2. Choose stratified splits that preserve minority support.
3. Compare class weighting, resampling, and threshold shifts.
4. Tune the balancing method on validation data only.
5. Evaluate precision, recall, and minority metrics on the test split.
6. Record the final strategy and any sampling assumptions.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `handle-missing-values-in-a-dataset`
- `clean-and-deduplicate-training-data`
- `detect-data-leakage-in-a-pipeline`
