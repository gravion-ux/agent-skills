---
name: detect-data-leakage-in-a-pipeline
description: Audit a machine learning pipeline and remove features that leak target information. Use when the user suspects target information leaks into a training pipeline.
domain: ml-model-training
tags: [data-leakage, pipeline-audit, feature-engineering]
triggers: ["detect data leakage in pipeline", "find ml data leakage", "audit feature leakage"]
---

# Audit a machine learning pipeline and remove features that leak target information

## Purpose

Audit a machine learning pipeline and remove features that leak target information.

## When to use

Use when the user suspects target information leaks into a training pipeline.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Map every feature to the time it becomes available.
2. Trace preprocessing and target construction through the pipeline.
3. Flag post-outcome, duplicated, and target-derived features.
4. Remove leakage features and rebuild the training split.
5. Compare metrics before and after the correction.
6. Add an automated leakage check to pipeline validation.

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
- `retrain-a-model-on-new-data`
- `run-a-reproducible-training-pipeline`
