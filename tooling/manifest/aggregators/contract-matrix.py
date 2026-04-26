#!/usr/bin/env python3
"""
contract-matrix.py — produce a contract owner -> deliverable -> solutions table.

Useful for DG CNECT audit and for spotting solutions with missing
contract metadata.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from _common import DEFAULT_GLOB, load_validated_manifests


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manifest-glob", default=DEFAULT_GLOB)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    manifests = load_validated_manifests(args.root, args.manifest_glob)

    # owner -> deliverable -> [solutions]
    by_owner: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    missing: list[str] = []

    for _, m in manifests:
        sol = m["simpl_solution"]
        contract = m.get("contract") or {}
        owner = contract.get("owner")
        deliverable = contract.get("deliverable")
        if not owner or not deliverable:
            missing.append(sol)
            continue
        by_owner[owner][deliverable].append(sol)

    lines: list[str] = ["# Contract deliverable matrix", ""]
    lines.append(
        "Generated from `.simpl/manifest.yaml` files. "
        "Solutions without a contract block are listed at the bottom."
    )
    lines.append("")

    lines.append("| Contract owner | Deliverable | Solutions |")
    lines.append("|---|---|---|")
    for owner in sorted(by_owner):
        for deliverable in sorted(by_owner[owner]):
            sols = ", ".join(sorted(set(by_owner[owner][deliverable])))
            lines.append(f"| {owner} | `{deliverable}` | {sols} |")
    lines.append("")

    if missing:
        lines.append("## Solutions with no contract metadata")
        lines.append("")
        for sol in sorted(set(missing)):
            lines.append(f"- {sol}")
        lines.append("")

    output = "\n".join(lines).rstrip() + "\n"

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
