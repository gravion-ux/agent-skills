---
name: write-an-experiment-log
description: Record training experiments with complete metadata, metrics, artefacts, and decisions. Use when the user needs an auditable record of a training experiment.
domain: ml-model-training
tags: [experiment-tracking, mlops, reproducibility]
triggers: ["write experiment log", "record ml experiment", "track training run metadata"]
---

# Record training experiments with complete metadata, metrics, artefacts, and decisions

## Purpose

Record training experiments with complete metadata, metrics, artefacts, and decisions.

## When to use

Use when the user needs an auditable record of a training experiment.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Assign each run a unique identifier and timestamp.
2. Record the objective, data version, split, and metric definition.
3. Capture configuration, code revision, seed, and environment details.
4. Attach training logs, checkpoints, and evaluation results.
5. Summarize outcomes, failures, and decisions to stop or continue.
6. Store the log in the experiment tracker with links to artefacts.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `serve-a-trained-model-as-an-api`
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
