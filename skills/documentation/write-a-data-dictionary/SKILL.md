---
name: write-a-data-dictionary
description: Describe each dataset field with meaning, type, constraints, lineage, and sensitivity. Use when the user wants a data dictionary that defines a dataset for readers and consumers.
domain: documentation
tags: [data-dictionary, schema, lineage]
triggers: ["data dictionary", "write a data dictionary", "dataset field definitions"]
---

# Describe each dataset field with meaning, type, constraints, lineage, and sensitivity

## Purpose

Describe each dataset field with meaning, type, constraints, lineage, and sensitivity.

## When to use

Use when the user wants a data dictionary that defines a dataset for readers and consumers.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Inventory fields from the current schema and a sample record.
2. Define each field's meaning, type, nullability, and accepted values.
3. Record the upstream source and any transformations for each field.
4. Classify sensitive values and remove real data from examples.
5. Assign an owner to review the definitions when the schema changes.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `write-a-changelog`
- `write-a-checklist-in-a-runbook`
- `write-a-comparison-table-of-options`
