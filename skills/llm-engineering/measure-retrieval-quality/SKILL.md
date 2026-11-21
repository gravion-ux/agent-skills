---
name: measure-retrieval-quality
description: Measure whether relevant evidence is found and ranked before judging the generated answer. Use when the user needs objective metrics for retrieval quality.
domain: llm-engineering
tags: [retrieval-metrics, relevance, evaluation]
triggers: ["measure llm retrieval quality", "llm retrieval metrics", "evaluate retrieved chunks for an llm"]
---

# Measure whether relevant evidence is found and ranked before judging the generated answer

## Purpose

Measure whether relevant evidence is found and ranked before judging the generated answer.

## When to use

Use when the user needs objective metrics for retrieval quality.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Run the retrieval stack against the fixed labelled evaluation set.
2. Compute recall at the selected cutoffs for every query.
3. Compute ranking metrics such as mean reciprocal rank and normalized discounted cumulative gain.
4. Slice the results by query type and document to expose failure modes.
5. Compare relevance gains with query token cost and latency before accepting a change.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-retrieval-pipeline-for-a-model`
- `measure-token-usage-and-cost`
- `score-output-quality-with-rubrics`
