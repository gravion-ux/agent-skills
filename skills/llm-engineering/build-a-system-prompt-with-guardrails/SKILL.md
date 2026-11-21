---
name: build-a-system-prompt-with-guardrails
description: Build a system prompt with explicit behavior boundaries, escalation rules, and adversarial checks. Use when the user needs a system prompt that constrains model behavior in production.
domain: llm-engineering
tags: [system-prompt, guardrails, safety]
triggers: ["llm system prompt guardrails", "guardrails for an llm system prompt", "llm policy system prompt"]
---

# Build a system prompt with explicit behavior boundaries, escalation rules, and adversarial checks

## Purpose

Build a system prompt with explicit behavior boundaries, escalation rules, and adversarial checks.

## When to use

Use when the user needs a system prompt that constrains model behavior in production.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the model's role, permitted tasks, and explicit refusal boundaries.
2. State how to handle ambiguity, prohibited requests, and uncertain evidence.
3. Add a safe escalation path for requests outside the allowed scope.
4. Test the prompt with adversarial, privacy-sensitive, and normal request cases.
5. Record violation rate, task accuracy, token cost, latency, and documented failure modes.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `structure-a-prompt-with-context-and-instructions`
- `build-a-batch-inference-pipeline`
- `build-a-model-router-by-task-difficulty`
