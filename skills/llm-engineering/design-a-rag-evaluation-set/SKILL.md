---
name: design-a-rag-evaluation-set
description: Create a labelled evaluation set that tests retrieval and generation against realistic corpus questions. Use when the user needs a repeatable benchmark for a retrieval-augmented application.
domain: llm-engineering
tags: [rag-evaluation, test-set, retrieval]
triggers: ["llm rag evaluation set", "build rag test set for an llm", "llm retrieval test questions"]
---

# Create a labelled evaluation set that tests retrieval and generation against realistic corpus questions

## Purpose

Create a labelled evaluation set that tests retrieval and generation against realistic corpus questions.

## When to use

Use when the user needs a repeatable benchmark for a retrieval-augmented application.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Write questions that span the corpus and reflect real user requests.
2. Label the answer and the passage evidence required for each question.
3. Add difficult, unanswerable, and distractor-heavy cases.
4. Freeze the set and version its labels for later comparisons.
5. Document the expected quality, token cost, and latency thresholds.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `design-a-model-in-the-loop-classifier`
- `design-a-schema-validated-tool-response`
- `build-a-batch-inference-pipeline`
