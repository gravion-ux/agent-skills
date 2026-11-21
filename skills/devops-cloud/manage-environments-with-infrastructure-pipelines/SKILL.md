---
name: manage-environments-with-infrastructure-pipelines
description: Promote infrastructure changes across environments through one reviewed pipeline. Use when the user wants infrastructure changes promoted from development to production.
domain: devops-cloud
tags: [infrastructure-pipeline, environments, promotion]
triggers: ["manage environments with pipelines", "promote infrastructure across environments", "environment pipeline"]
---

# Promote infrastructure changes across environments through one reviewed pipeline

## Purpose

Promote infrastructure changes across environments through one reviewed pipeline.

## When to use

Use when the user wants infrastructure changes promoted from development to production.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Keep one source of truth for the environment topology and its variables.
2. Separate environment differences into variable files, never into forked code.
3. Apply each environment in order and stop the pipeline at the first failed stage.
4. Capture the plan output as an artefact for every applied environment.
5. Reconcile drift between environments and fix the source rather than the target.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `manage-configuration-across-environments`
- `manage-cost-with-a-scheduled-scale-down`
- `manage-feature-flags-across-environments`
