#!/usr/bin/env python3
"""
bp-traceability.py — produce a bidirectional BP-to-solution traceability matrix.

Section 1: BP/SA -> solutions that participate in it.
Section 2: solution -> BPs/SAs it supports.

Replaces the BP-coverage portion of MAPPING.md.
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

    bp_to_solutions: dict[str, list[str]] = defaultdict(list)
    solution_to_bps: dict[str, list[str]] = {}

    for _, m in manifests:
        sol = m["simpl_solution"]
        bps = list(m.get("supports_business_processes") or [])
        solution_to_bps[sol] = sorted(bps)
        for bp in bps:
            bp_to_solutions[bp].append(sol)

    lines: list[str] = ["# Business process traceability", ""]
    lines.append(
        "Generated from `.simpl/manifest.yaml` files. "
        "Two views: BP → solutions, and solution → BPs."
    )
    lines.append("")

    lines.append("## BP / SA → solutions")
    lines.append("")
    lines.append("| BP / SA | Solutions |")
    lines.append("|---|---|")
    for bp in sorted(bp_to_solutions):
        sols = ", ".join(sorted(set(bp_to_solutions[bp])))
        lines.append(f"| `{bp}` | {sols} |")
    lines.append("")

    lines.append("## Solution → BPs / SAs")
    lines.append("")
    lines.append("| Solution | BPs / SAs |")
    lines.append("|---|---|")
    for sol in sorted(solution_to_bps):
        bps = solution_to_bps[sol]
        cell = ", ".join(f"`{bp}`" for bp in bps) if bps else "_none declared_"
        lines.append(f"| **{sol}** | {cell} |")
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
