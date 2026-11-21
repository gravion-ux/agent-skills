# Contributing

Thanks for improving the catalogue. Most contributions are **new or improved skills**;
the fastest way to help is to add a skill that a domain is missing.

## Workflow

1. **Fork and clone.**

   ```bash
   git clone https://github.com/<your-fork>/agent-skills.git
   cd agent-skills
   ```

2. **Create a branch.**

   ```bash
   git checkout -b feature/my-skill
   ```

3. **Install the development environment.**

   ```bash
   python -m pip install -e ".[dev]"
   ```

   Python 3.11 or newer. The package has no runtime dependencies.

4. **Add or edit the skill** in `catalog/source/<domain>.py`. Never edit `skills/` or
   `routers/` — they are generated. Read
   [`docs/CONTRIBUTING_SKILLS.md`](docs/CONTRIBUTING_SKILLS.md) for the `spec()` signature,
   the field rules, the quality bar and a complete worked example.

5. **Regenerate the artefacts.**

   ```bash
   python scripts/generate_skills.py
   ```

   This rewrites `skills/<domain>/<skill>/SKILL.md`, `routers/<domain>/SKILL.md`,
   `src/agentskills/data/catalog.json`, `catalog/CATALOG.md` and
   `skills/master/APPENDIX.md`.

6. **Run the gate.**

   ```bash
   python scripts/validate_skills.py \
     && python -m pytest tests/ -q \
     && python -m ruff check src tests scripts \
     && python -m mypy src/agentskills
   ```

   All four must pass. CI runs the same commands, plus a drift check that regenerates the
   catalogue and fails if the committed files differ.

7. **Open a pull request** against `main`. Describe what the skill does and when an agent
   should reach for it.

## What a good pull request looks like

- One domain per pull request, or one coherent theme — easier to review, easier to revert.
- The generated files are included in the same commit as the source change.
- New skills follow the nine-section format and the uniqueness rules.
- No placeholder text. No "TODO". No marketing language.
- The README domain table stays correct: it is written by hand, so update the count in
  `README.md` if you change a domain's skill count.

## Adding a whole domain

A new domain needs four things:

1. A `DomainProfile` in `catalog/source/_domains.py` — the framing shared by every skill
   in that domain.
2. One or more modules in `catalog/source/` with `DOMAIN = "<your-domain>"` and the
   skills.
3. The module name appended to `_DOMAIN_MODULES` in `catalog/source/__init__.py`.
4. The expected count added to `tests/test_source_counts.py`.

Then regenerate and run the gate.

## Changing the package code

The package is small on purpose: no runtime dependencies, standard library only, strict
types. Keep it that way — a new dependency needs a strong reason in the pull request
description.

## Reporting a problem

Open an issue with the skill name, what you expected and what the skill says. For
security issues, follow [`SECURITY.md`](SECURITY.md) instead of the public tracker.

## Code of conduct

Be direct, be kind, and review the work rather than the person. Assume good faith.
