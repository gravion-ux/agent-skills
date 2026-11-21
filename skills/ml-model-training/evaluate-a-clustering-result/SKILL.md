---
name: evaluate-a-clustering-result
description: Assess cluster usefulness, separation, stability, and actionable membership patterns. Use when the user needs to judge whether discovered clusters are useful and stable.
domain: ml-model-training
tags: [clustering-evaluation, model-evaluation, unsupervised-learning]
triggers: ["evaluate clustering result", "assess cluster quality", "cluster silhouette evaluation"]
---

# Assess cluster usefulness, separation, stability, and actionable membership patterns

## Purpose

Assess cluster usefulness, separation, stability, and actionable membership patterns.

## When to use

Use when the user needs to judge whether discovered clusters are useful and stable.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Use labeled outcomes when available to score cluster usefulness.
2. Compute silhouette scores and nearest-centroid distances.
3. Compare cluster metrics across candidate feature sets.
4. Inspect membership examples and boundary cases.
5. Test stability under a seeded resample.
6. Document which clusters are actionable and why.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `evaluate-a-classifier-with-a-confusion-matrix`
- `evaluate-a-model-with-precision-and-recall`
- `train-a-clustering-model`
