"""Scan the repository for hardcoded secrets."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _path in (ROOT, ROOT / "src"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
SELF = Path(__file__).resolve()

HARD_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("aws-access-key-id", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    (
        "aws-secret-access-key",
        re.compile(r"(?i)\baws_secret_access_key\b\s*[=:]\s*['\"]([^'\"\s]{40})['\"]"),
    ),
    (
        "private-key-header",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
    ),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("github-fine-grained-token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("generic-password", re.compile(r"(?i)\bpassword\b\s*[=:]\s*['\"]([^'\"\s]{8,})['\"]")),
    ("generic-api-key", re.compile(r"(?i)\bapi[_-]?key\b\s*[=:]\s*['\"]([^'\"\s]{12,})['\"]")),
)

PLACEHOLDER_HINTS: tuple[str, ...] = (
    "your",
    "example",
    "placeholder",
    "changeme",
    "redacted",
    "dummy",
)

SKIP_DIRS: frozenset[str] = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "build",
        "dist",
    }
)

SKIP_SUFFIXES: frozenset[str] = frozenset(
    {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".whl", ".gz", ".wav", ".mp3"}
)


def _is_placeholder(value: str) -> bool:
    lowered = value.strip().lower()
    return not value or any(hint in lowered for hint in PLACEHOLDER_HINTS)


def iter_files(root: Path) -> list[Path]:
    """Return every text-candidate file, skipping binary and generated paths."""
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        files.append(path)
    return files


def scan(root: Path) -> list[str]:
    """Return one message per suspected secret."""
    findings: list[str] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in HARD_PATTERNS:
                match = pattern.search(line)
                if match is None:
                    continue
                if match.groups() and _is_placeholder(match.group(1)):
                    continue
                findings.append(f"{path.relative_to(root)}:{number}: {label}")
    return findings


def main() -> int:
    findings = scan(ROOT)
    for finding in findings:
        print(finding)
    if findings:
        print(f"\n{len(findings)} potential secret(s) found.")
        return 1
    print("No secrets found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
