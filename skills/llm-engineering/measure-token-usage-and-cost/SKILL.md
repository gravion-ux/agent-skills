---
name: measure-token-usage-and-cost
description: Attribute model tokens, latency, and monetary cost to requests and features from provider metadata. Use when the user needs visibility into llm usage and spending.
domain: llm-engineering
tags: [token-usage, cost-accounting, observability]
triggers: ["measure llm token usage", "llm cost per request", "llm token budget tracking"]
---

# Attribute model tokens, latency, and monetary cost to requests and features from provider metadata

## Purpose

Attribute model tokens, latency, and monetary cost to requests and features from provider metadata.

## When to use

Use when the user needs visibility into llm usage and spending.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Capture provider-reported input and output token counts for every request.
2. Attach request, feature, model, and environment labels without logging prompt contents.
3. Convert token counts into cost with a versioned provider price table.
4. Aggregate cost and latency by feature and compare them with the cost ceiling.
5. Report unusual usage patterns and the resulting budget risks.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `choose-between-a-chain-and-a-router`
- `log-model-inputs-and-outputs-safely`
- `measure-retrieval-quality`
