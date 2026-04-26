# Simpl manifest tooling

This folder contains the schema, aggregators, and CI sketch for the Simpl manifest pattern. Every Simpl solution repository declares its capability-map placement, contract ownership, BP coverage, agent deployment, licence, and provenance in `.simpl/manifest.yaml`. CI validates that file against `manifest.schema.json`. Aggregator scripts walk a tree of solutions and produce the Markdown indexes that previously lived in a hand-maintained `MAPPING.md`.

## Layout

```
tooling/manifest/
├── SPEC.md                       # human-readable specification
├── manifest.schema.json          # JSON Schema (draft 2020-12)
├── README.md                     # this file
├── .gitlab-ci.yml                # validate + aggregate pipeline sketch
├── examples/
│   ├── simpl-catalogue/.simpl/manifest.yaml
│   └── edc-connector-extension/.simpl/manifest.yaml
└── aggregators/
    ├── _common.py                # shared loader / validator
    ├── validate.py               # CI gate: schema-check every manifest
    ├── capability-index.py       # dimension > capability > service > solution
    ├── bp-traceability.py        # BP <-> solution matrix (both directions)
    ├── agent-composition.py      # solutions per agent role
    ├── contract-matrix.py        # contract owner > deliverable > solutions
    ├── api-catalogue.py          # repo URL + conventional OpenAPI path
    └── run-against-examples.sh   # exercises every aggregator on examples/
```

## Run locally

Requires Python 3.11+ and two dependencies:

```sh
pip install pyyaml jsonschema
```

Validate every manifest under the current directory:

```sh
python3 tooling/manifest/aggregators/validate.py --root .
```

Generate one index to stdout:

```sh
python3 tooling/manifest/aggregators/capability-index.py --root .
```

Generate every index to files under `./generated/`:

```sh
mkdir -p generated
python3 tooling/manifest/aggregators/capability-index.py --root . --out generated/capability-index.md
python3 tooling/manifest/aggregators/bp-traceability.py    --root . --out generated/bp-traceability.md
python3 tooling/manifest/aggregators/agent-composition.py  --root . --out generated/agent-composition.md
python3 tooling/manifest/aggregators/contract-matrix.py    --root . --out generated/contract-matrix.md
python3 tooling/manifest/aggregators/api-catalogue.py      --root . --out generated/api-catalogue.md
```

Self-check the tooling against the bundled examples:

```sh
tooling/manifest/aggregators/run-against-examples.sh
```

This walks `examples/`, schema-validates the two manifests, and prints every aggregator's output. Exits 0 on success.

## CI wiring

The pipeline at `.gitlab-ci.yml` has two stages:

- **validate** — runs `validate.py` against the repository tree. Fails the pipeline if any `.simpl/manifest.yaml` does not validate.
- **aggregate** — runs every aggregator on default-branch merges and uploads the Markdown output as GitLab artefacts under `generated/`. Output is **not** committed back to the catalogue repo (see [SPEC.md, Open questions §1](./SPEC.md#open-questions)).

The pipeline is a sketch — it runs as written, but adopters should adapt the `rules:` blocks to programme-wide conventions, swap the base image if needed, and decide whether to switch to a commit-back model.

## Where to read more

- [`SPEC.md`](./SPEC.md) — full field reference, conventions, and open questions.
- [Manifest pattern — design and tooling](https://www.notion.so/34e273daab3981c39346c934d277a77d) — the design rationale on Notion.
- [Repository restructuring](https://www.notion.so/31a273daab398175a5adecf13d964f4e) — the broader context the manifest pattern was extracted from.
