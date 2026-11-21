---
name: choose-between-a-chain-and-a-router
description: Choose a chain or router by comparing task predictability, routing accuracy, and operating cost. Use when the user needs to select between a fixed LLM pipeline and a model-based router.
domain: llm-engineering
tags: [routing, architecture, model-selection, cost]
triggers: ["chain or router", "choose llm routing architecture", "compare chain and router"]
---

# Choose a chain or router by comparing task predictability, routing accuracy, and operating cost

## Purpose

Choose a chain or router by comparing task predictability, routing accuracy, and operating cost.

## When to use

Use when the user needs to select between a fixed LLM pipeline and a model-based router.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Write representative requests and label the expected route for each.
2. Measure the required number of model calls and data dependencies for a chain.
3. Measure routing accuracy, latency, and cost for a router on the same requests.
4. Select the design that meets quality thresholds at the lowest total cost.
5. Record the decision, thresholds, and cases that require a different design.

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
- `choose-embeddings-for-a-corpus`
- `structure-a-prompt-with-context-and-instructions`
