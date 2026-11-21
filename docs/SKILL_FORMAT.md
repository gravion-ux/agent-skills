# Skill format

Every leaf skill is one Markdown file at `skills/<domain>/<skill-name>/SKILL.md`.
It has YAML-subset frontmatter and exactly nine body sections, in a fixed order.

## Frontmatter

```yaml
---
name: review-a-pull-request
description: Review a pull request for correctness, scope and risk. Use when the user wants a change reviewed before merge.
domain: software-engineering
tags: [code-review, pull-request, quality]
triggers: ["review this pull request", "check my changes before merge"]
---
```

| Key | Rule |
|---|---|
| `name` | Must equal the directory name. Lowercase ASCII letters, digits and hyphens only. |
| `description` | Derived as `"{summary} Use when {when}."` — never authored directly. Must stay under 1,024 characters and must contain `Use when`. |
| `domain` | The hyphenated domain slug. Must match the router directory. |
| `tags` | Lowercase, hyphen-separated. Used for BM25 scoring at weight 2. |
| `triggers` | Natural phrases a user might type. Must be unique across the whole catalogue. Used for BM25 scoring at weight 3. |

The frontmatter parser (`src/agentskills/frontmatter.py`) supports exactly
`key: value` and `key: [a, b, c]`. It is not a general YAML parser, and it must not
grow into one.

## The nine sections

The order is fixed and enforced by the validator.

### 1. Purpose

One or two sentences on what the skill does. This is the skill's `summary`, and it
is the H1 title of the file with the trailing period removed.

### 2. When to use

The trigger clause, rendered as `Use when {when}.`. Write it as a situation, not a
command: "the user wants to release infrastructure changes through a blue-green
deployment", not "release infrastructure changes".

### 3. When NOT to use

Comes from the domain profile. This is the clause the master skill checks to rule
a candidate out, so it must actually exclude something real.

### 4. Inputs required

A bullet list of what must be known before the procedure can run. From the domain
profile, so all skills in a domain demand the same baseline.

### 5. Procedure

The numbered steps. Each step is imperative, self-contained and ends with a period.
Write steps that a reader can execute in order without guessing the next one.

```markdown
1. Deploy the green stack alongside the unchanged blue stack.
2. Prove the rollback command restores traffic to the blue stack.
3. Shift five percent of traffic to the green stack and watch error rates.
```

### 6. Output contract

What the skill must produce. From the domain profile — one sentence describing the
shape of the deliverable.

### 7. Validation checklist

Checkbox items the caller runs before accepting the result. From the domain profile.

### 8. Safety notes

The domain's guardrails: what must never happen, what needs confirmation. From the
domain profile.

### 9. Related skills

Links to sibling skills, rendered as `` - `skill-name` ``. The generator fills these
deterministically from same-domain skills ranked by shared name tokens, so leave
`related` empty when authoring unless you have a specific link in mind.

## What a skill author writes

A skill is authored as a `spec(...)` call, not as Markdown:

```python
spec(
    "implement-blue-green-traffic-shifting",
    summary="Shift production traffic between blue and green stacks with weighted routing and a tested rollback.",
    when="the user wants to release infrastructure changes through a blue-green deployment",
    steps=(
        "Deploy the green stack alongside the unchanged blue stack.",
        "Prove the rollback command restores traffic to the blue stack.",
        "Shift five percent of traffic to the green stack and watch error rates.",
        "Ramp to full traffic only while the error budget holds.",
        "Record the rollback command and the ramp thresholds in the runbook.",
    ),
    tags=("blue-green", "traffic-shift", "load-balancer", "release"),
    triggers=("blue green traffic shifting", "shift traffic to the green stack", "blue-green deployment routing"),
)
```

`spec()` is the only sanctioned way to build an entry. It lives in
`src/agentskills/spec.py` and is re-exported by `catalog/source/_types.py`.

## Field rules

| Field | Rule |
|---|---|
| `name` | The directory name and the key used everywhere. Unique across the catalogue. |
| `summary` | One sentence, third person, no trailing "This skill". Unique across the catalogue (the derived description inherits this). |
| `when` | A situation clause starting with "the user wants to" or similar. |
| `steps` | 3–7 steps, imperative mood, each ending in a period. |
| `tags` | 3–5 lowercase hyphenated tags. |
| `triggers` | 3 natural-language phrases. Each one unique across the whole catalogue. |
| `related` | Optional. Leave empty; the generator fills same-domain siblings. |

## Uniqueness

Two things must be unique across all 1,209 skills, and the validator fails the build
if they are not:

- **Skill names.** Two skills may not share a name, even in different domains.
- **Trigger phrases.** A trigger may belong to exactly one skill. This is what makes
  a trigger usable as a lookup key, so "prune unreachable code" cannot be a trigger
  for two different skills.

Descriptions are checked too, since they are derived from `summary`.

## Routers

Each domain gets one generated router at `routers/<domain>/SKILL.md`. It carries the
same nine-section structure and ends with a table of every skill in the domain:

```markdown
| Skill | Use when |
|---|---|
| `implement-blue-green-traffic-shifting` | Use when the user wants to release infrastructure changes through a blue-green deployment. |
```

The router is the second routing layer: it narrows a domain to a handful of
neighbouring skills without loading the whole catalogue. See
[ROUTING.md](ROUTING.md).

## The master skill

`skills/master/SKILL.md` is hand-written and follows the same nine-section format,
with one addition: it references the generated `skills/master/APPENDIX.md`, which
carries the domain map, the router path for each domain, the skill count per domain
and the scoring reference.

## Checking your work

```bash
python scripts/generate_skills.py    # write skills/, routers/, index, mirrors
python scripts/validate_skills.py    # structure, uniqueness, consistency
```

The validator names the exact problem, for example:

```
ERROR: skills/web-development/...: the nine sections are missing or out of order (missing: Safety notes)
```

To add a skill to the catalogue, follow
[CONTRIBUTING_SKILLS.md](CONTRIBUTING_SKILLS.md).
