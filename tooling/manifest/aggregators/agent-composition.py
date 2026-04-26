#!/usr/bin/env python3
"""
agent-composition.py — produce a per-agent-role listing of solutions.

For each agent role declared anywhere across the manifests, list the
solutions that declare deployment into that role. Solutions with no
`deployed_in_agents` field appear under a separate "unassigned" group
so reviewers can spot gaps.
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

    by_agent: dict[str, list[str]] = defaultdict(list)
    unassigned: list[str] = []

    for _, m in manifests:
        sol = m["simpl_solution"]
        agents = m.get("deployed_in_agents") or []
        if not agents:
            unassigned.append(sol)
            continue
        for agent in agents:
            by_agent[agent].append(sol)

    lines: list[str] = ["# Agent composition", ""]
    lines.append(
        "Solutions deployed into each agent role. "
        "Generated from `.simpl/manifest.yaml` files."
    )
    lines.append("")

    for agent in sorted(by_agent):
        lines.append(f"## {agent}")
        lines.append("")
        for sol in sorted(set(by_agent[agent])):
            lines.append(f"- {sol}")
        lines.append("")

    if unassigned:
        lines.append("## (no agent declared)")
        lines.append("")
        for sol in sorted(set(unassigned)):
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
