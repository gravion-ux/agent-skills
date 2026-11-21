# Contributing skills

How to add or change a skill in this catalogue.

## Before you start

Read [SKILL_FORMAT.md](SKILL_FORMAT.md) for the file format and
[ARCHITECTURE.md](ARCHITECTURE.md) for how generation works.

The one rule: **`catalog/source/` is the source of truth.** `skills/` and `routers/`
are generated. Never hand-edit `skills/<domain>/<name>/SKILL.md` or
`routers/<domain>/SKILL.md` — the next generator run overwrites it and CI's drift
gate fails the build.

## Add a skill to an existing domain

1. Open the domain module, e.g. `catalog/source/devops_cloud.py`.

2. Add a `spec(...)` entry, following the field rules in
   [SKILL_FORMAT.md](SKILL_FORMAT.md):

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
   ),
   ```

3. Leave `related` empty. The generator fills same-domain siblings automatically.

4. Regenerate and validate (below).

## Add a skill to a new domain

A new domain needs three things:

1. A `DomainProfile` in `catalog/source/_domains.py`:

   ```python
   "data-engineering": DomainProfile(
       domain="data-engineering",
       title="Data engineering",
       when_not_to_use="Do not use for one-off analysis queries.",
       inputs=("The source systems and their schemas",),
       output_contract="A reproducible pipeline definition and its run instructions.",
       checks=("The pipeline runs end to end on a sample dataset",),
       safety="Never point the pipeline at production data without an approved change.",
   ),
   ```

2. A module `catalog/source/<domain>.py` with `DOMAIN = "<hyphenated-domain>"` and
   the `SKILLS` tuple.

3. A registration in `catalog/source/__init__.py`: append the module name to
   `_DOMAIN_MODULES`. Do not reorder the tuple.

If the domain outgrows one file, split it into `<domain>.py` and `<domain>_2.py`,
give both the same `DOMAIN` value, and register both modules. The generator groups
them into one `skills/<domain>/` tree and one router.

## Change a domain profile

`catalog/source/_domains.py` holds the framing shared by every skill in a domain:
the *When NOT to use* clause, the inputs, the output contract, the validation
checklist and the safety notes.

Changing a profile changes every skill in that domain at once. Regenerate and the
diff will show the change landing in each affected `SKILL.md`. That is intended — it
is why the profile exists.

## Change a skill's own text

Edit the `spec(...)` entry in the module. Never the generated Markdown.

## Rules the validator will enforce

- The skill name equals its directory name: lowercase ASCII letters, digits and
  hyphens only.
- Skill names are unique across the whole catalogue, even across domains.
- Trigger phrases are unique across the whole catalogue — a trigger belongs to
  exactly one skill.
- Summaries are unique across the catalogue (descriptions are derived from them).
- `steps` has 3–7 entries, each imperative and ending in a period.
- `tags` has 3–5 lowercase hyphenated entries.
- `triggers` has 3 entries.
- No placeholder markers: `TBD`, `TODO`, `FIXME`, `XXX`, `lorem`.
- The description stays under 1,024 characters and contains `Use when`.

The validator names the exact problem rather than just failing:

```
ERROR: skills/web-development/...: the nine sections are missing or out of order (missing: Safety notes)
ERROR: src/agentskills/data/catalog.json: duplicate trigger 'prune unreachable code' shared by 'x' and 'y'
```

## The gate

Run this before opening a pull request. Every command must exit zero.

```bash
python scripts/generate_skills.py \
  && python scripts/validate_skills.py \
  && python -m pytest tests/ -q \
  && python -m ruff check src tests scripts \
  && python -m mypy src/agentskills
```

`python scripts/generate_skills.py` prints how many files it wrote. Run it before
`validate_skills.py` — the validator compares the generated tree against the index,
so it will report a stale index if you skip generation.

The test suite asserts the per-domain skill counts. If you deliberately change a
domain's size, update the expected counts in `tests/test_source_counts.py` in the
same commit.

## Style

- `ruff` (line length 100) and `mypy --strict` must pass. No new ignores without a
  reason in the pull request.
- Public functions and classes carry a one-line docstring.
- Tests are plain `pytest` functions, no classes, no fixtures beyond `tmp_path`.
- Comments explain *why*, never restate the code.
- Skill bodies, README and docs are in English.

## Commits and pull requests

- One logical change per commit. Generated files travel with the source change that
  caused them — never commit generated files on their own.
- Never commit credentials, tokens or private URLs.
  `scripts/scan-secrets.py` runs in CI and fails the build on a hard-coded secret.
- Run the full gate locally before opening the pull request.
- In the pull-request description, say which domain you touched and how many skills
  you added or changed.
