---
name: detect-hallucination-in-a-generated-answer
description: Decompose a generated answer into claims and verify each claim against trusted evidence. Use when the user needs to assess unsupported claims in an llm answer.
domain: llm-engineering
tags: [hallucination, fact-checking, verification]
triggers: ["detect llm hallucination", "llm fact check answer", "verify claims in an llm answer"]
---

# Decompose a generated answer into claims and verify each claim against trusted evidence

## Purpose

Decompose a generated answer into claims and verify each claim against trusted evidence.

## When to use

Use when the user needs to assess unsupported claims in an llm answer.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Split the answer into independently checkable factual claims.
2. Retrieve evidence from approved sources or call a trusted verification tool.
3. Mark each claim as supported, contradicted, or unresolved.
4. Rewrite unsupported claims with explicit uncertainty or remove them.
5. Measure detection precision, recall, token cost, latency, and failure modes on a fixed evaluation set.

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
- `ground-a-response-in-retrieved-citations`
- `summarise-a-long-conversation-in-context`
