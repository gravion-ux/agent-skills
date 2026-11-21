---
name: prepare-a-labelled-dataset
description: Assemble a legally usable labelled dataset with consistent labels and documented sources. Use when the user needs to assemble a legally usable dataset with consistent labels.
domain: ml-model-training
tags: [labelled-data, data-preparation, data-provenance]
triggers: ["prepare labelled dataset", "build labelled training data", "assemble labeled dataset"]
---

# Assemble a legally usable labelled dataset with consistent labels and documented sources

## Purpose

Assemble a legally usable labelled dataset with consistent labels and documented sources.

## When to use

Use when the user needs to assemble a legally usable dataset with consistent labels.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Confirm the user's rights and consent for every data source.
2. Define the label schema and write annotation guidelines.
3. Sample records and measure label consistency.
4. Join sources using stable keys and record exclusions.
5. Profile class balance, missingness, and duplicate rates.
6. Export a versioned dataset manifest with labels and provenance.

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
- `apply-regularisation-to-a-model`
- `batch-predict-with-a-trained-model`
