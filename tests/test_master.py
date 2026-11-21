# tests/test_master.py
from pathlib import Path

from catalog.source import domain_of

MASTER = Path(__file__).resolve().parents[1] / "skills" / "master" / "SKILL.md"
APPENDIX = Path(__file__).resolve().parents[1] / "skills" / "master" / "APPENDIX.md"


def test_master_skill_exists() -> None:
    assert MASTER.exists()


def test_master_skill_names_the_router_and_the_scorer() -> None:
    text = MASTER.read_text(encoding="utf-8")
    assert "agentskills route" in text
    assert "routers/" in text
    assert "When NOT to use" in text


def test_master_appendix_exists_and_lists_every_domain() -> None:
    text = APPENDIX.read_text(encoding="utf-8")
    for _, domain in domain_of():
        assert f"routers/{domain}/SKILL.md" in text
