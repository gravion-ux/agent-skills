# tests/test_catalog.py
import json
from pathlib import Path

import pytest

from agentskills.catalog import load_catalogue

ENTRY = {
    "name": "example-skill",
    "domain": "testing",
    "summary": "Do one example thing.",
    "description": "Do one example thing. Use when the user asks for it.",
    "tags": ["example"],
    "triggers": ["do the example thing"],
    "steps": ["Step one", "Step two"],
    "when_to_use": "Use when the user asks for it.",
    "when_not_to_use": "Not for other work.",
    "inputs": ["An input"],
    "output_contract": "An output.",
    "checks": ["A check"],
    "safety": "Be careful.",
    "related": [],
}


def write_index(tmp_path: Path, payload: object) -> Path:
    index = tmp_path / "catalog.json"
    index.write_text(json.dumps(payload), encoding="utf-8")
    return index


def test_load_catalogue_reads_an_index(tmp_path: Path) -> None:
    index = write_index(tmp_path, {"version": "0.1.0", "skills": [ENTRY]})
    catalogue = load_catalogue(index)
    assert catalogue.version == "0.1.0"
    assert len(catalogue.skills) == 1
    assert catalogue.get("example-skill") is not None
    assert catalogue.get("missing-skill") is None
    assert catalogue.domains() == ("testing",)
    assert catalogue.by_domain("testing")[0].name == "example-skill"
    assert catalogue.by_domain("other") == ()


def test_load_catalogue_rejects_a_broken_index(tmp_path: Path) -> None:
    index = tmp_path / "catalog.json"
    index.write_text("not json", encoding="utf-8")
    with pytest.raises(ValueError):
        load_catalogue(index)


def test_load_catalogue_rejects_an_index_without_skills(tmp_path: Path) -> None:
    index = write_index(tmp_path, {"version": "0.1.0"})
    with pytest.raises(ValueError):
        load_catalogue(index)
