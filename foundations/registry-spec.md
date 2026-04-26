---
id: doc:registry-spec
type: foundation
name: Registry specification
status: draft
since: r3.0
---

# Registry specification

Every navigable node in this catalogue (dimension, capability, business service, solution, business process, scenario architecture, NFR, foundation document) carries a YAML frontmatter block whose `id` field is **the canonical reference target** for that node.

Folder paths can move; IDs do not. External tools (CI, JIRA, partner repos, conformance claims) that reference a node by `id:` continue to resolve after a rename, because the node still has the same `id` after it moves.

This document defines the URN scheme, the per-node-type frontmatter schema, and the rename/redirect policy.

---

## 1. URN scheme

IDs are URNs of the form `<namespace>:<slug>`. Namespaces partition the ID space so `cap:participant-management` and `svc:participant-management` could coexist (they don't, but the namespace prevents accidental collision).

| Namespace | Used for | Example |
|-----------|----------|---------|
| `dim:` | Capability-map dimensions (6 total) | `dim:governance` |
| `cap:` | Capability-map capabilities | `cap:participant-management` |
| `svc:` | Capability-map business services | `svc:onboarding` |
| `simpl:` | Solutions (concrete components, built or planned) | `simpl:onboarding-service` |
| `bp:` | Business processes | `bp:BP03A` |
| `sa:` | Scenario architectures | `sa:SA03` |
| `nfr:` | Non-functional requirements | `nfr:NFR06` |
| `doc:` | Foundation/reference documents | `doc:glossary` |
| `team:` | Owner teams | `team:iaa` |

### Slug rules

- Lower-kebab-case for `dim:`, `cap:`, `svc:`, `simpl:`, `doc:`, `team:` (e.g. `simpl:tier-1-authentication-provider`).
- Verbatim BP/SA/NFR identifier for `bp:`, `sa:`, `nfr:` (e.g. `bp:BP03A`, preserves the source-document casing).
- The slug must NOT encode the path. `simpl:onboarding-service` is correct; `simpl:governance.participant-management.onboarding.onboarding-service` defeats the entire point — when the path moves, the ID would have to move too.

### Stability contract

- **Once allocated, an `id` is immutable.** If the *meaning* of a node changes substantively (e.g. a solution is split into two), allocate a new `id`, mark the old one `deprecated-in` with `replaced-by`, and keep an `aliases` entry pointing at the old slug for grep-ability.
- Renames of the underlying folder do NOT change the id. Only the `name` (display) field tracks the rename.

---

## 2. Frontmatter schema by node type

Every README starts with a YAML frontmatter block (between `---` lines) before the H1.

### 2.1 Dimension (`type: dimension`)

```yaml
---
id: dim:<slug>
type: dimension
name: <display name>
since: r3.0
---
```

Required: `id`, `type`, `name`. `since` is recommended.

### 2.2 Capability (`type: capability`)

```yaml
---
id: cap:<slug>
type: capability
name: <display name>
dimension: dim:<slug>
since: r3.0
---
```

### 2.3 Business service (`type: business-service`)

```yaml
---
id: svc:<slug>
type: business-service
name: <display name>
dimension: dim:<slug>
capability: cap:<slug>
since: r3.0
---
```

### 2.4 Solution (`type: solution`) — full schema

```yaml
---
id: simpl:<slug>
type: solution
name: <display name>

owner:
  team: team:<slug>          # see §4 for the team registry

dimension: dim:<slug>
capability: cap:<slug>
business-service: svc:<slug>

status: built                # built | planned | external | deprecated
release: r3.0                # release in which it currently ships
since: r3.0                  # release in which the id was first allocated
deprecated-in: null
replaced-by: null
aliases: []

participates-in:             # business processes / SAs this solution implements
  - bp:BP03A
realises:                    # capabilities this solution realises (≥1)
  - cap:participant-management
covers-nfrs: []              # optional, populated as NFR scoring lands

provenance:
  source: built              # built | external | fork | placeholder
  upstream: null             # URL of upstream project if source=fork or external
  repos:                     # source-code repositories
    - code.europa.eu/simpl/simpl-open/development/iaa/onboarding
    - code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding
  licence: EUPL-1.2
---
```

`provenance.source` values:

- `built` — implemented by Simpl itself, no upstream.
- `fork` — Simpl maintains a fork of an upstream OSS project (e.g. EDC, Keycloak, Dagster, XFSC). Set `upstream:` to the upstream URL.
- `external` — used as-is, not forked.
- `placeholder` — solution is planned but no code exists yet. Set `status: planned`, `repos: []`.

### 2.5 Business process (`type: business-process`)

```yaml
---
id: bp:<ID>
type: business-process
name: <display name>
since: r3.0
---
```

### 2.6 Scenario architecture (`type: scenario-architecture`)

```yaml
---
id: sa:<ID>
type: scenario-architecture
name: <display name>
since: r3.0
---
```

### 2.7 Dynamic view (`type: dynamic-view`)

`dynamic-view.md` files alongside BP/SA READMEs:

```yaml
---
id: bp:<ID>:dynamic-view       # composite ID — child of the BP
type: dynamic-view
name: <BP name> – Dynamic view
of: bp:<ID>                    # parent
since: r3.0
---
```

### 2.8 NFR (`type: non-functional-requirement`)

```yaml
---
id: nfr:<ID>
type: non-functional-requirement
name: <display name>
since: r3.0
---
```

### 2.9 Foundation document (`type: foundation`)

```yaml
---
id: doc:<slug>
type: foundation
name: <display name>
since: r3.0
---
```

### 2.10 Index README (`type: index`)

For grouping READMEs that don't represent a node themselves (root `README.md`, `foundations/README.md`, `foundations/business-processes/README.md`, `foundations/non-functional-requirements/README.md`):

```yaml
---
id: doc:<slug>-index
type: index
name: <display name>
---
```

---

## 3. Cross-references

Inside markdown body text, links remain *relative paths* for now (so they render correctly on GitHub without tooling). The `id` is the contract for **structured references** in frontmatter (`participates-in:`, `realises:`, `covers-nfrs:`, `replaced-by:`) and for **external consumers** (CI rules, conformance claims, JIRA links).

When a folder moves, two things must change:
1. The relative links in body text (which is the painful retrofit cost the council flagged).
2. Nothing else — IDs are stable, frontmatter references are stable.

Once tooling exists (Phase 2+ in the rollout), the link-rewriter will update body-text links automatically on rename, using the registry to resolve `id` → current path.

---

## 4. Team registry

Owner teams (slugs derived from observed source-repo path segments under `code.europa.eu/simpl/simpl-open/development/`):

| `team:` slug | Display name | Source-repo prefix |
|--------------|--------------|--------------------|
| `team:iaa` | Identity, Authentication & Authorisation | `iaa/` |
| `team:edc` | Eclipse EDC fork (Catalogue & Connector) | `gaia-x-edc/` |
| `team:data1` | Data1 (Schema, SD, Search) | `data1/` |
| `team:contract-billing` | Contract & Billing | `contract-billing/` |
| `team:monitoring` | Monitoring | `monitoring/` |
| `team:infrastructure` | Infrastructure | `infrastructure/` |
| `team:orchestration` | Orchestration Platform (Dagster fork) | `orchestration-platform/` |
| `team:unassigned` | Not yet allocated (planned solutions) | — |

Team boundaries are observational — they reflect today's source-repo layout, not a permanent assignment. When a team renames or solutions move between teams, update `owner.team` in the affected solution frontmatter. The path doesn't change.

---

## 5. Rename / redirect / deprecation policy

When a node moves, splits, merges, or is retired, the `id` outlives the change.

### Folder rename (no semantic change)

1. `git mv` the folder.
2. Update `name:` if the human-readable name changed.
3. Update relative links in body text that pointed at the old path.
4. **Do not change the `id`.** Anything that referenced the id (in frontmatter, external systems) continues to resolve.

### Solution split (one node becomes two)

1. Allocate two new `id`s.
2. The original solution's frontmatter:
   - `status: deprecated`
   - `deprecated-in: r<release>`
   - `replaced-by: [simpl:new-a, simpl:new-b]`
3. Keep the original README in place for at least 2 releases as a tombstone.

### Solution merge (two nodes become one)

1. Pick one `id` to survive (or allocate a new one).
2. The other(s) get `status: deprecated`, `replaced-by: [<survivor>]`.
3. Add the deprecated slugs to the survivor's `aliases:` list for grep-ability.

### Capability or business-service rename

1. Allocate the new `id`.
2. Old node: `status: deprecated`, `replaced-by: <new>`, keep tombstone for 2 releases.
3. Update `capability:` / `business-service:` facets in every affected solution to the new id.
4. Solutions inherit the new placement automatically — the cross-references in their frontmatter are id-based.

### Tombstone

After the deprecation window (≥ 2 releases), the old README may be deleted, but the `aliases:` entry on the survivor must remain so old references can still be located by grep.

---

## 6. What this document does NOT yet specify

- **Tooling.** No registry generator, link-rewriter, or CODEOWNERS generator exists yet. The frontmatter is the prerequisite for that tooling; without the schema applied first, there is nothing to read.
- **CI enforcement.** ID uniqueness, schema conformance, and reference resolution are not yet checked in CI. Until they are, treat this document as the convention; violations will be caught by hand.
- **Generated views.** MAPPING.md, the team-shaped owner view, and the task-indexed README router will be generated from this frontmatter once tooling lands. Until then, MAPPING.md remains hand-maintained.

These are the intended Phase 2+ work items, as outlined in the Round 2 council verdict (see `council/council-report-2026-04-26-1328.html`).
