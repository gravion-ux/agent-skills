---
name: design-a-model-in-the-loop-classifier
description: Design a model-based classifier with labeled examples, calibrated thresholds, and a safe fallback. Use when the user wants an LLM to classify incoming records on a fixed taxonomy.
domain: llm-engineering
tags: [classification, thresholds, evaluation, fallbacks]
triggers: ["model in loop classifier", "llm classification prompt", "classify records with confidence"]
---

# Design a model-based classifier with labeled examples, calibrated thresholds, and a safe fallback

## Purpose

Design a model-based classifier with labeled examples, calibrated thresholds, and a safe fallback.

## When to use

Use when the user wants an LLM to classify incoming records on a fixed taxonomy.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define mutually exclusive labels and a written decision rule for each label.
2. Collect representative labeled examples, including common edge cases.
3. Prompt the classifier to return the label and a short supporting reason.
4. Score precision, recall, and confusion pairs on a held-out set.
5. Route low-confidence and ambiguous cases to a fallback rule or reviewer.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-model-router-by-task-difficulty`
- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`
