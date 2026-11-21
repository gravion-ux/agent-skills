# Architecture

How the catalogue is authored, generated, validated, routed and shipped.

## The shape of the system

```
catalog/source/*.py          hand-authored SkillSpec entries
catalog/source/_domains.py   42 DomainProfile records (domain-wide framing)
catalog/source/__init__.py   module registry + domain_of()
        │
        │  scripts/generate_skills.py
        ▼
src/agentskills/generation.py  build_skill() + renderers
        │
        ├─► skills/<domain>/<skill-name>/SKILL.md   1,209 leaf skills
        ├─► routers/<domain>/SKILL.md                42 domain routers
        ├─► src/agentskills/data/catalog.json        packaged index
        ├─► catalog/CATALOG.md                       human-readable mirror
        └─► skills/master/APPENDIX.md                generated domain map
        │
        │  scripts/validate_skills.py
        ▼
src/agentskills/validation.py  validate_repository()
```

`skills/master/SKILL.md` is the only file under `skills/` that is written by hand.

## Single source of truth

There is exactly one editable representation of a skill: the `spec(...)` call in
`catalog/source/<module>.py`. Everything else is derived.

| Artefact | Editable? | Producer |
|---|---|---|
| `catalog/source/*.py` | yes | humans |
| `catalog/source/_domains.py` | yes | humans |
| `catalog/source/__init__.py` | yes | humans (registry only) |
| `skills/<domain>/<name>/SKILL.md` | no | `generation.render_skill_markdown` |
| `routers/<domain>/SKILL.md` | no | `generation.render_router_markdown` |
| `src/agentskills/data/catalog.json` | no | `generation.render_index_json` |
| `catalog/CATALOG.md` | no | `generation.render_catalog_markdown` |
| `skills/master/APPENDIX.md` | no | `generation.render_master_appendix` |
| `skills/master/SKILL.md` | **yes** | hand-written |

A hand edit to a generated file is silently overwritten by the next generator run and
caught by the CI drift gate. This is deliberate: one source of truth means the nine
sections of a skill can never drift between the file on disk, the JSON index and the
routers that point at it.

## The authoring model

Two records carry all the content of a catalogue entry.

**`SkillSpec`** (`src/agentskills/spec.py`) — the part that is unique to one skill:
`name`, `summary`, `when`, `steps`, `tags`, `triggers`, and an optional `related`.
Everything a human writes for a single skill lives here.

**`DomainProfile`** (`src/agentskills/spec.py`, data in `catalog/source/_domains.py`) —
the part that is shared by every skill in a domain: `when_not_to_use`, `inputs`,
`output_contract`, `checks`, `safety`, plus the display `title`.

A domain profile exists so that 1,209 skills stay consistent without repeating the
same paragraph 1,209 times, and so that changing a domain's safety framing is one
edit rather than thirty.

`build_skill()` merges the two into a full `Skill` (`src/agentskills/catalog.py`),
which is the single in-memory shape used by the renderers, the router and the CLI.

The `description` shown in frontmatter is derived, never authored:

```
description = f"{summary} Use when {when}."
```

That is what lets the validator enforce a `Use when` clause in every description
without a human having to remember it.

## Module and domain mapping

A domain may be large enough to split across several files. Every module therefore
declares its domain explicitly:

```python
DOMAIN = "devops-cloud"
```

`catalog/source/__init__.py` holds `_DOMAIN_MODULES`, the ordered registry of module
names, and `domain_of()` reads each module's `DOMAIN` attribute (falling back to the
filename). The generator groups entries by the resolved domain, so `devops_cloud.py`
and `devops_cloud_2.py` land in the same `skills/devops-cloud/` tree and the same
`routers/devops-cloud/SKILL.md`.

## Generation

`agentskills.generation.generate()` is a pure function of
`(source modules, domain profiles, version)`. It is idempotent: running it twice on
an unchanged tree produces byte-identical output, which is what makes the CI drift
gate meaningful.

For each domain it:

1. Groups the specs by domain and sorts them by name.
2. Computes deterministic sibling links for each skill (same-domain, ranked by
   shared name tokens, tie-broken alphabetically) so the *Related skills* section is
   never empty and never random.
3. Renders each leaf skill and writes `skills/<domain>/<name>/SKILL.md`.
4. Renders the domain router with a table of every skill in the domain.
5. Writes the JSON index, the catalogue mirror and the master appendix.

All writes use `encoding="utf-8"` and `newline="\n"`, and `.gitattributes` pins LF,
so generation is byte-stable across platforms.

## Validation

`agentskills.validation.validate_repository()` is the single gate. It checks:

- every leaf skill, router and the master skill has valid frontmatter with
  `name`, `description`, `domain`, `tags` and `triggers`;
- the frontmatter `name` matches the directory name;
- the description is within 1,024 characters and contains a `Use when` clause;
- the nine sections are present, in order and non-empty;
- no placeholder markers (`TBD`, `TODO`, `FIXME`, `XXX`, `lorem`) appear;
- skill names are unique;
- the JSON index and `catalog/CATALOG.md` list exactly the skills on disk;
- descriptions and trigger phrases are unique across the catalogue;
- every `related` link resolves to a real skill;
- the routers cover exactly the domains present in the index.

Any error makes `scripts/validate_skills.py` exit non-zero, which fails CI.

## Runtime and packaging

The installed package is `agentskills`, `src`-layout, Python 3.11+, **zero runtime
dependencies** — standard library only.

The canonical types live *inside* the package (`src/agentskills/spec.py`).
`catalog/source/_types.py` is a thin authoring shim that re-exports `spec()` so the
authoring modules do not need the package installed to be importable. The installed
package never imports from `catalog/`; `catalog/` is authoring-only and is not
shipped in the wheel.

The packaged data file is `src/agentskills/data/catalog.json`, included in the
wheel. `load_catalogue()` resolves it through `importlib.resources`, with an
`AGENTSKILLS_CATALOG` environment variable override for pointing the CLI at a
different index (useful for testing a catalogue before publishing it).

## CLI surface

| Command | Reads | Writes |
|---|---|---|
| `agentskills list [--domain D] [--json]` | index | stdout |
| `agentskills show <name>` | index | stdout |
| `agentskills route "<task>" [--top N] [--json]` | index | stdout |
| `agentskills validate [--json]` | the whole repo tree | stdout, exit code |
| `agentskills export --out DIR [--domain D]` | `skills/` | another agent's skills dir |
| `agentskills pack --out FILE.zip` | index, `skills/`, `routers/` | a zip |

`list`, `show` and `route` work against the packaged index and need no repository
checkout. `validate`, `export` and `pack` operate on a repository tree and take
`--root` (default `.`).

## CI

`.github/workflows/ci.yml` runs lint, a strict type check, the test suite across
Python 3.11/3.12/3.13, the skills drift gate and the wheel build.
`.github/workflows/secret-scan.yml` fails the build on a hard-coded secret.
The wheel build is the only place the distribution is verified — the authoring
environment has no package index access, so `python -m build` is CI-only by design.
