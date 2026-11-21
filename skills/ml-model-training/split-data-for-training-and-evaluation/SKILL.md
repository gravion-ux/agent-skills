---
name: split-data-for-training-and-evaluation
description: Create leakage-safe train, validation, and test partitions with reproducible split rules. Use when the user needs reproducible train, validation, and held-out partitions.
domain: ml-model-training
tags: [data-splitting, validation-split, leakage-prevention]
triggers: ["split training and evaluation data", "create leakage safe data split", "make train validation test split"]
---

# Create leakage-safe train, validation, and test partitions with reproducible split rules

## Purpose

Create leakage-safe train, validation, and test partitions with reproducible split rules.

## When to use

Use when the user needs reproducible train, validation, and held-out partitions.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Separate the held-out evaluation rows before any fitting or imputation.
2. Use a time-based split when rows arrive chronologically.
3. Freeze group identifiers before splitting grouped observations.
4. Record the split logic, seed, and row counts.
5. Verify no entity, record, or derived feature crosses partitions.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `clean-and-deduplicate-training-data`
- `choose-a-threshold-for-a-classifier`
- `detect-data-leakage-in-a-pipeline`
