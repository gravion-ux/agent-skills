import agentskills


def test_version_is_semver() -> None:
    parts = agentskills.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_package_exports_version() -> None:
    assert agentskills.__version__
    assert "__version__" in agentskills.__all__
