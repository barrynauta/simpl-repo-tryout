# Simpl manifest specification

## Purpose

Every Simpl solution repository declares its capability-map placement, contract ownership, business-process coverage, agent deployment, licence, and provenance in a single per-repo file: `.simpl/manifest.yaml`. This file is the canonical source for that metadata. CI validates it against a JSON schema on every merge, and aggregator scripts walk a tree of solutions to generate the indexes that previously lived in a hand-maintained `MAPPING.md` — capability index, BP traceability, agent compositions, contract deliverable matrix, API catalogue.

The manifest replaces three locations of duplicated truth — folder structure, `MAPPING.md`, and scattered Confluence/spreadsheet references — with one declared, validated, machine-readable file per solution. Folders and indexes become *views* over the manifest, regenerated on each merge. Drift becomes structurally impossible.

This pattern is independent of the repository spine: it works whether the code repos are organised by capability, by team, or any other shape. The folder is one form of the truth; the manifest is another. Adopt the manifest pattern without conceding the spine debate.

## Location

Each solution repository carries one manifest at:

```
.simpl/manifest.yaml
```

The dotfile prefix keeps the file out of `src/` discoverability while remaining trivially globbable by tooling. The `.simpl/` folder is reserved for Simpl-specific machine-readable metadata (manifest, optional `api/openapi.yaml`, future additions).

## Field reference

The manifest is a single YAML document with the fields below. Field names use `snake_case`; all string identifiers (slugs, dimensions, capabilities, business services, team names) use `kebab-case`.

### Required fields

| Field | Type | Allowed values / pattern | Description |
|---|---|---|---|
| `simpl_solution` | string | kebab-case slug, `^[a-z][a-z0-9-]*[a-z0-9]$` | Stable solution identifier. Must match the solution folder name in the documentation catalogue. Once allocated, never changes. |
| `schema_version` | integer | `1` | Version of this manifest schema the file targets. Lock at `1` for the initial schema; bump when breaking changes ship. |
| `version` | string | SemVer 2.0, e.g. `0.3.1` | Current released version of the solution. |
| `product` | enum | `simpl-open`, `simpl-labs`, `simpl-live` | Which Simpl product line the solution belongs to. Simpl-Open is the middleware codebase; Simpl-Labs and Simpl-Live are downstream consumers. |
| `capability_map.primary.dimension` | string | kebab-case, sourced from the capability map | One of `integration`, `data`, `infrastructure`, `administration`, `governance`, `security`. Validated against the canonical capability map by the aggregator (not enumerated in the schema, because the map evolves). |
| `capability_map.primary.capability` | string | kebab-case, sourced from the capability map | The L1 capability under that dimension. |
| `capability_map.primary.business_service` | string | kebab-case, sourced from the capability map | The L2 business service under that capability. |
| `licence` | string | SPDX identifier, `^[A-Za-z0-9.+-]+$` | Licence the solution is published under. `EUPL-1.2` for built solutions; upstream licence preserved for forks/reused. |
| `provenance` | enum | `built`, `forked`, `reused` | Origin of the codebase. `built` = original Simpl code. `forked` = Simpl-maintained fork of an upstream project. `reused` = upstream consumed unmodified. |

### Conditionally required

| Field | Required when | Description |
|---|---|---|
| `upstream_repository` | `provenance ∈ {forked, reused}` | URL of the upstream OSS project. Omitted (or `null`) when `provenance: built`. |

### Optional fields

| Field | Type | Allowed values / pattern | Description |
|---|---|---|---|
| `team` | string | kebab-case slug | Team currently owning the solution. Observational; reflects today's allocation, not a permanent assignment. Authoritative ownership lives in `codeowners`. |
| `repository_url` | string | URL | Canonical source-code URL. Optional because built solutions in early development may not yet have a public repo. The api-catalogue aggregator emits "no repository declared" when missing. |
| `capability_map.touches` | array of `{dimension, capability, business_service}` objects | Same patterns as `primary` | Other capability-map nodes the solution materially interacts with. Used by the capability index to surface secondary placements. |
| `contract.owner` | enum | `PSO`, `SC1`, `SC2`, `SC3`, `SC4`, `SC5` | Contract owner under the Simpl programme procurement. |
| `contract.deliverable` | string | `^D[0-9]+(\.[0-9]+)*[A-Za-z]?$`, e.g. `D3.4`, `D5.2a` | Deliverable identifier the solution satisfies. |
| `contract.framework_contract` | string | free text | Framework contract reference (e.g. `DIGIT/A3/PR/2023/...`). |
| `supports_business_processes` | array of string | `^(BP|SA)[0-9]{2}[A-Z]?$`, e.g. `BP03A`, `SA02` | Business processes and scenario architectures the solution participates in. |
| `deployed_in_agents` | array of enum | `governance-authority`, `provider`, `consumer`, `application-provider` | Agent roles into which this solution is deployed. See open question on canonical list. |
| `codeowners` | array of string | path or team slug | Either GitLab/GitHub-style codeowner specs (e.g. `* @simpl/iaa`) or team slugs. The aggregator does not resolve these; downstream tooling does. |
| `testing.unit_coverage_target` | number | `0`–`100` | Unit-test coverage target, in percent. The aggregator surfaces this; CI does not enforce it. |

### Convention notes

- **Identifiers are kebab-case.** `simpl_solution`, `team`, `dimension`, `capability`, `business_service`, agent roles, BP/SA identifiers (uppercase prefix preserved per the public requirements catalogue).
- **Versions are SemVer 2.0.** `MAJOR.MINOR.PATCH`, optional pre-release/build metadata. Aggregators sort solutions by version where useful.
- **Licences are SPDX.** `EUPL-1.2` is the default for Simpl-built solutions. Forks preserve the upstream licence (Apache-2.0, MIT, GPL family — whichever the upstream uses). Do not substitute EUPL on forks.
- **Capability-map values are validated against a canonical list.** The schema enforces *shape* (kebab-case non-empty strings); the aggregator enforces *membership* against the capability map maintained on Notion. A typo or stale value fails the aggregate stage, not the validate stage.
- **Agent role names are an enum** in the schema for now, but the canonical list is owned by the agent-composition design (see open questions).
- **`schema_version` is mandatory.** It allows the schema itself to evolve without requiring a flag-day migration: the aggregator reads `schema_version` to pick the correct validator.

## Worked examples

Two example manifests live under `./examples/` and are the canonical reference implementation:

- [`examples/simpl-catalogue/.simpl/manifest.yaml`](./examples/simpl-catalogue/.simpl/manifest.yaml) — Simpl-built catalogue solution, EUPL-1.2, multiple BPs, provenance `built`.
- [`examples/edc-connector-extension/.simpl/manifest.yaml`](./examples/edc-connector-extension/.simpl/manifest.yaml) — fork of the Eclipse EDC connector, Apache-2.0, provenance `forked`, populated `upstream_repository`.

Both validate against the schema. The test harness `aggregators/run-against-examples.sh` runs every aggregator against the `examples/` tree as part of its self-check.

## Validation

Schema validation runs on every merge via the GitLab CI pipeline at [`.gitlab-ci.yml`](./.gitlab-ci.yml). The `validate` stage fails the pipeline if any `.simpl/manifest.yaml` in the repository tree does not validate against `manifest.schema.json`.

Local validation:

```sh
python3 aggregators/validate.py --root .
```

Exits non-zero if any manifest fails schema validation. Each failure is reported with the offending file path and the JSON-schema error path.

The validator does *not* check capability-map membership. That happens in the aggregator stage — `capability-index.py` will emit warnings (or fail, configurable) when a manifest references a `dimension`/`capability`/`business_service` that does not appear in the canonical capability map.

## How aggregators consume manifests

Each aggregator is a standalone Python script under `./aggregators/` that:

1. Takes a `--root <dir>` argument pointing at the directory tree to walk.
2. Globs for `**/.simpl/manifest.yaml` under that root (override with `--manifest-glob`).
3. Loads each manifest via PyYAML, validates against the schema once (fail-fast), and projects the fields it needs.
4. Emits Markdown to stdout (or a `--out <file>` path).

The aggregators are deliberately *additive* — adding a new aggregator is a new script in the same folder, no pipeline rewiring needed. They share no state and import only standard library plus `PyYAML` and `jsonschema`.

The five aggregators planned for the first pass:

| Aggregator | Output | Replaces |
|---|---|---|
| `capability-index.py` | Markdown index by `dimension > capability > business_service > solution` | The solution-listing portion of `MAPPING.md` |
| `bp-traceability.py` | Markdown matrix BP→solutions and solution→BPs | The BP-coverage portion of `MAPPING.md` |
| `agent-composition.py` | Markdown listing per agent role of the solutions deployed into it | Currently maintained ad-hoc in slides |
| `contract-matrix.py` | Markdown table contract owner → deliverable → solutions | Currently maintained ad-hoc in spreadsheets |
| `api-catalogue.py` | Markdown index linking each solution's `repository_url` and the conventional location of its OpenAPI spec | The `api-catalogue/` root index, today written by hand |

Plus one self-check tool:

| Tool | Purpose |
|---|---|
| `validate.py` | Walks the tree, validates every manifest against the schema, exits non-zero on any failure. Used by CI's `validate` stage. |

## Open questions

These could not be resolved from the source material in this pass. They are deferred to the maintainer (or to a follow-up workshop) and are not silently decided in code:

1. **Aggregator output destination.** This pass treats aggregator output as CI artefacts (uploaded by the `aggregate` stage, downloadable from the pipeline). The alternative — committing into a `generated/` folder on the catalogue repo — couples the aggregator to write access on the catalogue and adds noise to git history. The simpler choice (artefacts) is captured in `.gitlab-ci.yml`. Revisit if a stable URL for downstream consumers is needed.
2. **Manifest location.** This spec uses `.simpl/manifest.yaml`. Andrei's original v1 proposal used the same path. If the dotfile causes issues with any tooling (Windows Explorer hiding, GitLab UI rendering, etc.), the alternative is `simpl-manifest.yaml` at repo root. Decision: defer until evidence of a real problem.
3. **Canonical agent role list.** This spec enumerates `governance-authority`, `provider`, `consumer`, `application-provider` as a starting set. The canonical list belongs in the agent-composition design and is not on the design Notion page. Treat the schema enum as a starting point; expand or correct based on the agent-composition design when it lands.
4. **Capability-map canonical source for the aggregator.** The schema does not enumerate dimensions/capabilities/business services — they are validated by the aggregator against the canonical capability map (Notion, Confluence v85). The aggregator currently does *not* fetch that list (no network). For now the validator is shape-only; membership-validation is deferred. Options: (a) ship a snapshot of the capability map with the tooling and refresh manually; (b) generate it from the catalogue folder structure; (c) call out to Notion at CI time. None obviously right.
5. **`team` vs `codeowners`.** The spec keeps both: `team` as a single observational owner, `codeowners` as the operational routing for review. They will drift unless one is generated from the other. The intended direction is that `codeowners` is generated *from* `team` plus a programme-wide team-to-CODEOWNERS mapping; that generator is out of scope for this pass.
6. **Status of the registry-spec id system.** The cleanup pass stripped frontmatter from every README in the catalogue, including the `id` / `type` / `name` / `since` fields defined in `foundations/registry-spec.md`. The registry-spec document itself is now orphaned: its convention is no longer applied anywhere. Either retire `foundations/registry-spec.md`, or rebuild the id system as part of the manifest (e.g. promote `simpl_solution` to a global URN and add equivalent ids for non-solution nodes). Defer to the maintainer.
7. **`schema_version` semantics.** This spec introduces `schema_version: 1` as a required integer. The semantics — when to bump, what counts as a breaking change, how the aggregator dispatches across versions — are not formalised. Acceptable for v1; needs a policy by v2.
