# AGENTS.md

Operating instructions for an agent working **inside this repository**.

## The one rule that matters

`catalog/source/` is the source of truth. `skills/` and `routers/` are **generated**.

Never hand-edit a file under `skills/<domain>/<skill>/SKILL.md` or
`routers/<domain>/SKILL.md`. Edit the matching module in `catalog/source/`, then
regenerate. A hand edit is overwritten by the next generator run and fails the CI drift
gate.

## Adding or changing a skill

1. Find the domain module: `catalog/source/<domain>.py`. One module holds one domain's
   skills; a domain may be split across modules (`<domain>.py` and `<domain>_2.py`) when
   the domain is large. Every module declares `DOMAIN = "<hyphenated-domain>"` so the
   mapping is explicit.
2. Add a `spec(...)` entry following the rules in `docs/CONTRIBUTING_SKILLS.md`.
   - The skill name is the directory name: lowercase ASCII, hyphens only.
   - Names, summaries and trigger phrases must be unique across the whole catalogue.
   - Omit `related` — the generator fills same-domain siblings automatically.
3. Register a new module in `catalog/source/__init__.py` by appending its name to
   `_DOMAIN_MODULES`. Do not reorder the tuple.
4. Regenerate: `python scripts/generate_skills.py`.
5. Run the gate (below).

## The gate

```bash
python scripts/generate_skills.py \
  && python scripts/validate_skills.py \
  && python -m pytest tests/ -q \
  && python -m ruff check src tests scripts \
  && python -m mypy src/agentskills
```

Every one of those commands must exit zero. `scripts/validate_skills.py` enforces the
nine-section structure, the frontmatter keys, the catalogue/index/router consistency and
the uniqueness rules; the test suite enforces the per-domain skill counts.

## Repository map

| Path | Role |
|---|---|
| `catalog/source/` | Hand-authored skill specs — the only place to edit skills |
| `catalog/source/_domains.py` | The 42 domain profiles (framing shared by each domain) |
| `catalog/source/__init__.py` | Module registry (`_DOMAIN_MODULES`) |
| `skills/` | Generated leaf skills, plus the hand-written `skills/master/SKILL.md` |
| `routers/` | Generated per-domain routers |
| `src/agentskills/` | The installable package: spec types, router, generator, validator, CLI |
| `src/agentskills/data/catalog.json` | Generated machine-readable index, shipped in the wheel |
| `scripts/` | `generate_skills.py`, `build_index.py`, `validate_skills.py`, `scan-secrets.py` |
| `catalog/CATALOG.md` | Generated human-readable catalogue mirror |
| `docs/` | Architecture, format, routing and contribution guides |

`skills/master/SKILL.md` is the one file under `skills/` that is **hand-written**. The
generator writes `skills/master/APPENDIX.md` beside it.

## Package boundaries

- The canonical types (`SkillSpec`, `DomainProfile`, `spec()`) live in
  `src/agentskills/spec.py`, inside the installed package.
- `catalog/source/_types.py` is a thin re-export so the authoring modules can use
  `spec()` without importing the installed package by path.
- The installed package **never** imports from `catalog/`. `catalog/` is authoring-only
  and is not shipped in the wheel.
- Runtime dependencies: none. Standard library only, Python 3.11+.

## Style

- `ruff` (line length 100) and `mypy --strict` must pass. No new ignores without a
  reason in the pull request.
- Public functions and classes carry a one-line docstring.
- Tests are plain `pytest` functions, no classes, no fixtures beyond `tmp_path`.
- Comments explain *why*, never restate the code.

## Commits and pull requests

- One logical change per commit; generated files travel with the source change that
  caused them.
- Never commit credentials, tokens or private URLs. `scripts/scan-secrets.py` runs in CI
  and fails the build on a hard-coded secret.
- Run the full gate locally before opening a pull request.
