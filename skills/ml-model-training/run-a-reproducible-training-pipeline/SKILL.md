---
name: run-a-reproducible-training-pipeline
description: Run a training pipeline that reproduces the same model from recorded configuration. Use when the user needs a model training run that can be reproduced exactly.
domain: ml-model-training
tags: [reproducible-training, mlops, pipeline-automation]
triggers: ["run reproducible training pipeline", "reproducible ml training pipeline", "rerun model training from config"]
---

# Run a training pipeline that reproduces the same model from recorded configuration

## Purpose

Run a training pipeline that reproduces the same model from recorded configuration.

## When to use

Use when the user needs a model training run that can be reproduced exactly.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Pin the code revision and declare all runtime dependencies.
2. Fix random seeds and record hardware and accelerator details.
3. Separate data acquisition, preparation, training, and evaluation stages.
4. Fit every learned transformation inside the training stage.
5. Enforce the held-out split and reproducibility checks in automation.
6. Publish the run manifest, model artefacts, metrics, and deployment notes.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `detect-data-leakage-in-a-pipeline`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
