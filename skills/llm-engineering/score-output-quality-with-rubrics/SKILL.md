---
name: score-output-quality-with-rubrics
description: Score generated outputs against explicit rubrics that define quality dimensions and pass thresholds. Use when the user needs a consistent way to grade open-ended LLM outputs.
domain: llm-engineering
tags: [rubrics, quality, grading, evaluation]
triggers: ["score outputs with rubrics", "llm output rubric", "grade generated answers"]
---

# Score generated outputs against explicit rubrics that define quality dimensions and pass thresholds

## Purpose

Score generated outputs against explicit rubrics that define quality dimensions and pass thresholds.

## When to use

Use when the user needs a consistent way to grade open-ended LLM outputs.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define two to four quality dimensions relevant to the task.
2. Write observable scoring levels for each dimension with one example per level.
3. Set a pass threshold and a rule for handling missing or malformed output.
4. Score the blind outputs and record evidence for every assigned level.
5. Review disagreements and revise ambiguous rubric wording before finalising.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `call-a-model-with-streaming-output`
- `build-a-system-prompt-with-guardrails`
- `constrain-a-model-output-to-json-schema`
