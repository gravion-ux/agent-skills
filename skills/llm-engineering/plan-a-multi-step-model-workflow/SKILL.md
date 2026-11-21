---
name: plan-a-multi-step-model-workflow
description: Plan a multi-step model workflow with explicit inputs, handoffs, and measurable completion checks. Use when the user wants to design a staged LLM workflow with several dependent model or tool steps.
domain: llm-engineering
tags: [workflow, orchestration, planning, llm]
triggers: ["plan multi step model workflow", "design staged llm workflow", "map model and tool handoffs"]
---

# Plan a multi-step model workflow with explicit inputs, handoffs, and measurable completion checks

## Purpose

Plan a multi-step model workflow with explicit inputs, handoffs, and measurable completion checks.

## When to use

Use when the user wants to design a staged LLM workflow with several dependent model or tool steps.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the workflow outcome and the final acceptance checks.
2. Break the work into steps with one typed input and output per step.
3. Assign each step to a model, tool, or deterministic rule.
4. Add retry, timeout, and fallback behavior for every fallible step.
5. Trace the planned inputs and outputs end to end before implementation.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `plan-a-fallback-model-strategy`
- `build-a-model-router-by-task-difficulty`
- `build-a-retrieval-pipeline-for-a-model`
