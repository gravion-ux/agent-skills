---
name: fine-tune-a-pre-trained-model
description: Fine-tune a pre-trained model on permitted task data with validation control. Use when the user needs to adapt a pre-trained model to a supervised task.
domain: ml-model-training
tags: [fine-tuning, transfer-learning, pretrained-models]
triggers: ["fine tune pre trained model", "fine tune pretrained model", "adapt foundation model to task"]
---

# Fine-tune a pre-trained model on permitted task data with validation control

## Purpose

Fine-tune a pre-trained model on permitted task data with validation control.

## When to use

Use when the user needs to adapt a pre-trained model to a supervised task.

## When NOT to use

Do not use this for prompting an existing model; use llm-engineering instead.

## Inputs required

- The task, the data and the metric
- The compute budget and the deadline
- The serving constraints and the fairness requirements

## Procedure

1. Confirm the base-model license and permitted data rights.
2. Choose a task template and label formatting for the target task.
3. Create leakage-safe splits before adapting the model.
4. Fine-tune with a small learning rate and validation checkpointing.
5. Compare against the untuned base model on the test split.
6. Save the adapter or weights, configuration, and model card.

## Output contract

A trained or fine-tuned model with its metrics, its evaluation split and its deployment notes.

## Validation checklist

- [ ] The evaluation split is held out from training
- [ ] The metric matches the real objective
- [ ] The model is reproducible from the recorded configuration

## Safety notes

Never train on data the user lacks the right to use, and never deploy a model whose evaluation was skipped.

## Related skills

- `batch-predict-with-a-trained-model`
- `serve-a-trained-model-as-an-api`
- `apply-regularisation-to-a-model`
