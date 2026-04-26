"""
Shared helpers for the manifest aggregators.

Kept deliberately small. Each aggregator script imports what it needs from
here; no global state is held.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable, Iterator

import yaml
from jsonschema import Draft202012Validator


SCHEMA_PATH = Path(__file__).resolve().parent.parent / "manifest.schema.json"
DEFAULT_GLOB = "**/.simpl/manifest.yaml"


def load_schema() -> dict:
    with SCHEMA_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def iter_manifest_paths(root: Path, manifest_glob: str = DEFAULT_GLOB) -> Iterator[Path]:
    """Yield manifest file paths under root matching the given glob."""
    if not root.exists():
        raise FileNotFoundError(f"root does not exist: {root}")
    yield from sorted(root.glob(manifest_glob))


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: manifest is not a YAML mapping")
    return data


def load_validated_manifests(
    root: Path, manifest_glob: str = DEFAULT_GLOB
) -> list[tuple[Path, dict]]:
    """Load and schema-validate every manifest under root.

    Aggregators call this when they need the data clean. The validate.py
    script does its own loop because it needs per-file error reporting.
    """
    schema = load_schema()
    validator = Draft202012Validator(schema)
    out: list[tuple[Path, dict]] = []
    errors: list[str] = []
    for path in iter_manifest_paths(root, manifest_glob):
        try:
            manifest = load_manifest(path)
        except Exception as exc:  # pragma: no cover - surface the message
            errors.append(f"{path}: {exc}")
            continue
        validation_errors = sorted(validator.iter_errors(manifest), key=lambda e: e.path)
        if validation_errors:
            for err in validation_errors:
                pointer = "/".join(str(p) for p in err.absolute_path) or "<root>"
                errors.append(f"{path}: {pointer}: {err.message}")
            continue
        out.append((path, manifest))
    if errors:
        msg = "manifest validation failed:\n  " + "\n  ".join(errors)
        raise SystemExit(msg)
    return out


def solution_label(manifest: dict) -> str:
    return manifest["simpl_solution"]
