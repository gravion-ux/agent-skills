"""Curated source of truth for the skill catalogue."""

from __future__ import annotations

import importlib
from types import ModuleType

from agentskills.spec import DomainProfile, SkillSpec, spec

_DOMAIN_MODULES: tuple[str, ...] = (
    "ai_agents",
    "ai_agents_2",
    "llm_engineering",
    "llm_engineering_2",
    "ml_model_training",
    "data_analysis",
    "research",
    "learning_skills",
    "agent_tooling_meta",
    "software_engineering",
    "software_engineering_2",
    "web_development",
    "web_development_2",
    "mobile_desktop",
    "devops_cloud",
    "devops_cloud_2",
    "dev_experience",
    "code_quality",
    "architecture_design",
    "testing_qa",
    "api_design",
    "observability",
    "networking",
    "databases",
    "data_engineering",
    "data_engineering_2",
    "security",
    "security_2",
    "business_ops",
    "project_management",
    "productivity",
    "communication",
    "sales_marketing",
    "finance_accounting",
    "legal_compliance",
    "hr_recruiting",
    "education",
    "documentation",
    "technical_writing",
    "design_ux",
    "image_visual",
    "video_audio",
    "content_creation",
    "cooking_food",
    "home_diy",
    "travel_lifestyle",
    "health_wellness",
    "personal_finance",
    "relationships_social",
)


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
        domain = str(getattr(module, "DOMAIN", module_name.replace("_", "-")))
        for entry in getattr(module, "SKILLS"):
            pairs.append((entry, domain))
    return tuple(pairs)


__all__ = ["DomainProfile", "SkillSpec", "all_specs", "domain_of", "spec"]
