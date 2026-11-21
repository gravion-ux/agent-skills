---
name: implement-a-multi-turn-tool-conversation
description: Implement a multi-turn conversation that carries tool results back into the model context. Use when the user wants an LLM chat flow to use results from earlier tool calls.
domain: llm-engineering
tags: [conversation, tool-calls, context, agents]
triggers: ["multi turn tool conversation", "continue llm conversation after tool call", "carry tool results across turns"]
---

# Implement a multi-turn conversation that carries tool results back into the model context

## Purpose

Implement a multi-turn conversation that carries tool results back into the model context.

## When to use

Use when the user wants an LLM chat flow to use results from earlier tool calls.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Maintain an ordered message list with one role per turn.
2. Append each requested tool call and its validated result to the list.
3. Keep the running context within the configured token budget.
4. Stop when the model returns a final response without another tool call.
5. Record the turn count, tokens used, and any unresolved tool error.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-tool-calling-loop`
- `design-a-schema-validated-tool-response`
- `plan-a-multi-step-model-workflow`
