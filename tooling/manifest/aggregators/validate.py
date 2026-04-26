#!/usr/bin/env python3
"""
validate.py — walk a directory tree, validate every .simpl/manifest.yaml
against manifest.schema.json, and exit non-zero on any failure.

Used by CI's `validate` stage. Reports each failure with the offending
file path and the schema path of the violation.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from _common import (
    DEFAULT_GLOB,
    iter_manifest_paths,
    load_manifest,
    load_schema,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Directory tree to walk (default: current directory).",
    )
    parser.add_argument(
        "--manifest-glob",
        default=DEFAULT_GLOB,
        help=f"Glob pattern for manifest files (default: {DEFAULT_GLOB}).",
    )
    args = parser.parse_args()

    schema = load_schema()
    validator = Draft202012Validator(schema)

    total = 0
    failures = 0
    for path in iter_manifest_paths(args.root, args.manifest_glob):
        total += 1
        try:
            manifest = load_manifest(path)
        except Exception as exc:
            failures += 1
            print(f"FAIL {path}: cannot load: {exc}", file=sys.stderr)
            continue
        errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.absolute_path))
        if errors:
            failures += 1
            for err in errors:
                pointer = "/".join(str(p) for p in err.absolute_path) or "<root>"
                print(f"FAIL {path}: {pointer}: {err.message}", file=sys.stderr)
        else:
            print(f"OK   {path}")

    print(f"\n{total} manifest(s) checked, {failures} failure(s).")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
