---
name: summarise-a-long-conversation-in-context
description: Maintain a compact conversation state that preserves decisions, facts, and unresolved requests. Use when the user needs to keep a long chat within the model context limit.
domain: llm-engineering
tags: [conversation-summary, context-window, state-management]
triggers: ["summarise llm conversation context", "llm conversation summary", "compress llm chat history"]
---

# Maintain a compact conversation state that preserves decisions, facts, and unresolved requests

## Purpose

Maintain a compact conversation state that preserves decisions, facts, and unresolved requests.

## When to use

Use when the user needs to keep a long chat within the model context limit.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the request contract and the facts later turns must retain.
2. Extract decisions, confirmed facts, constraints, and open questions from each turn.
3. Replace resolved history with the latest compact state and retain exact identifiers.
4. Redact personal data before storing or sending the conversation state.
5. Check state sufficiency, accuracy, token cost, latency, and documented failure modes on a fixed evaluation set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `chunk-a-long-document-for-a-model`
- `design-a-model-in-the-loop-classifier`
- `detect-hallucination-in-a-generated-answer`
