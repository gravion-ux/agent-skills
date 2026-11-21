---
name: structure-a-prompt-with-context-and-instructions
description: Organize a prompt into explicit context, task, instruction, and output sections. Use when the user wants a prompt with unambiguous sections and boundaries.
domain: llm-engineering
tags: [prompt-structure, context, instructions]
triggers: ["structured llm prompt", "llm prompt context and instructions", "organize an llm prompt"]
---

# Organize a prompt into explicit context, task, instruction, and output sections

## Purpose

Organize a prompt into explicit context, task, instruction, and output sections.

## When to use

Use when the user wants a prompt with unambiguous sections and boundaries.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Write the request contract with required inputs and outputs.
2. Separate trusted context from the instructions sent to the model.
3. State the task and the required output format in distinct sections.
4. Define how to handle missing, ambiguous, and conflicting context.
5. Score the structured prompt on a fixed evaluation set and record cost and latency.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-system-prompt-with-guardrails`
- `call-a-model-with-streaming-output`
- `choose-between-a-chain-and-a-router`
