"""Curated source of truth for the skill catalogue."""

from __future__ import annotations

import importlib
from types import ModuleType

from agentskills.spec import DomainProfile, SkillSpec, spec

_DOMAIN_MODULES: tuple[str, ...] = ()


def _load_module(name: str) -> ModuleType:
    return importlib.import_module(f"catalog.source.{name}")


def all_specs() -> tuple[SkillSpec, ...]:
    """Return every skill spec across every domain module, in module order."""
    collected: list[SkillSpec] = []
    for module_name in _DOMAIN_MODULES:
        module = _load_module(module_name)
        collected.extend(getattr(module, "SKILLS"))
    return tuple(collected)


def domain_of() -> tuple[tuple[SkillSpec, str], ...]:
    """Return every skill spec paired with the hyphenated domain that owns it."""
    pairs: list[tuple[SkillSpec, str]] = []
    for module_name in _DOMAIN_MODULES:
        module = _load_module(module_name)
        for entry in getattr(module, "SKILLS"):
            pairs.append((entry, module_name.replace("_", "-")))
    return tuple(pairs)


__all__ = ["DomainProfile", "SkillSpec", "all_specs", "domain_of", "spec"]
