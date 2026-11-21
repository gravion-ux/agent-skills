---
name: clean-and-deduplicate-training-data
description: Remove corrupt records, resolve label conflicts, and deduplicate training rows without altering valid examples. Use when the user needs to repair dirty records and remove repeated training examples.
domain: ml-model-training
tags: [data-cleaning, deduplication, label-quality]
triggers: ["clean and deduplicate training data", "deduplicate ml dataset", "clean training rows"]
---

# Remove corrupt records, resolve label conflicts, and deduplicate training rows without altering valid examples

## Purpose

Remove corrupt records, resolve label conflicts, and deduplicate training rows without altering valid examples.

## When to use

Use when the user needs to repair dirty records and remove repeated training examples.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Profile invalid types, impossible values, and missing labels.
2. Quarantine records that cannot be repaired from evidence.
3. Resolve duplicate keys and conflicting labels using source timestamps.
4. Normalize labels to the canonical task schema.
5. Compare row counts and distributions before and after cleaning.
6. Save a cleaning report with every excluded record.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `split-data-for-training-and-evaluation`
- `detect-data-leakage-in-a-pipeline`
- `evaluate-a-model-with-precision-and-recall`
