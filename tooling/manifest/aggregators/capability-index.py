#!/usr/bin/env python3
"""
capability-index.py — produce a Markdown capability index.

Walks the tree of solution manifests and emits a tree of:

    # Capability index
    ## <Dimension>
    ### <Capability>
    #### <Business service>
    - <solution>  (vX.Y.Z, provenance)

Replaces the solution-listing portion of MAPPING.md.
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
    parser.add_argument(
        "--out", type=Path, default=None, help="Write to file instead of stdout."
    )
    args = parser.parse_args()

    manifests = load_validated_manifests(args.root, args.manifest_glob)

    # dimension -> capability -> business_service -> [(solution, version, provenance)]
    tree: dict[str, dict[str, dict[str, list[tuple[str, str, str]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )

    for _, m in manifests:
        primary = m["capability_map"]["primary"]
        d = primary["dimension"]
        c = primary["capability"]
        bs = primary["business_service"]
        tree[d][c][bs].append(
            (m["simpl_solution"], m["version"], m["provenance"])
        )

    lines: list[str] = ["# Capability index", ""]
    lines.append(
        "Generated from per-solution manifests at `.simpl/manifest.yaml`. "
        "Do not edit by hand."
    )
    lines.append("")

    for dim in sorted(tree):
        lines.append(f"## {dim}")
        lines.append("")
        for cap in sorted(tree[dim]):
            lines.append(f"### {cap}")
            lines.append("")
            for bs in sorted(tree[dim][cap]):
                lines.append(f"#### {bs}")
                lines.append("")
                for sol, ver, prov in sorted(tree[dim][cap][bs]):
                    lines.append(f"- **{sol}** — v{ver} ({prov})")
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
