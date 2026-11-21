---
name: train-a-neural-network-from-scratch
description: Train a neural network from scratch with reproducible data, weights, and checkpoints. Use when the user needs to build and train a neural network without a pre-trained model.
domain: ml-model-training
tags: [neural-networks, deep-learning, model-training]
triggers: ["train neural network from scratch", "build neural network from scratch", "train custom deep learning model"]
---

# Train a neural network from scratch with reproducible data, weights, and checkpoints

## Purpose

Train a neural network from scratch with reproducible data, weights, and checkpoints.

## When to use

Use when the user needs to build and train a neural network without a pre-trained model.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Define tensor shapes, loss, optimizer, and stopping metric.
2. Build separate training, validation, and test loaders.
3. Initialize weights, implement forward and backward passes.
4. Train with checkpoints and early stopping on validation loss.
5. Evaluate once on the untouched test split.
6. Save weights, architecture, seeds, and preprocessing.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `train-a-clustering-model`
- `train-a-first-classification-model`
- `train-a-first-regression-model`
