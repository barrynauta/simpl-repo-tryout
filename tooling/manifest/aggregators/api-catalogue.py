#!/usr/bin/env python3
"""
api-catalogue.py — produce a Markdown index of solution repositories
and the conventional location of their OpenAPI specifications.

Convention: each repo's OpenAPI lives at `.simpl/api/openapi.yaml`. The
aggregator does not fetch it (no network); it links the path so a
downstream tool or human reviewer can resolve it.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _common import DEFAULT_GLOB, load_validated_manifests


OPENAPI_CONVENTION = ".simpl/api/openapi.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manifest-glob", default=DEFAULT_GLOB)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    manifests = load_validated_manifests(args.root, args.manifest_glob)

    rows: list[tuple[str, str, str, str]] = []
    for _, m in manifests:
        sol = m["simpl_solution"]
        repo = m["repository_url"]
        provenance = m["provenance"]
        # Best-effort URL to the conventional OpenAPI location. We keep
        # this as a string hint; the aggregator does not verify it exists.
        openapi_hint = f"{repo.rstrip('/')}/-/blob/main/{OPENAPI_CONVENTION}"
        rows.append((sol, repo, openapi_hint, provenance))

    lines: list[str] = ["# API catalogue", ""]
    lines.append(
        f"Each solution publishes its OpenAPI specification at the "
        f"conventional path `{OPENAPI_CONVENTION}`. The link below is a "
        "best-effort URL; existence is not verified by this aggregator."
    )
    lines.append("")
    lines.append("| Solution | Repository | OpenAPI (conventional) | Provenance |")
    lines.append("|---|---|---|---|")
    for sol, repo, openapi_hint, provenance in sorted(rows):
        lines.append(
            f"| **{sol}** | [{repo}]({repo}) | [`{OPENAPI_CONVENTION}`]({openapi_hint}) | {provenance} |"
        )
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
