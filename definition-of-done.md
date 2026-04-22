# Definition of done — solution documentation

A solution folder is considered **documentation-complete** when all of the following are true:

## Required files

- [ ] `README.md` — one-paragraph description, capability-map placement, provenance line, contents table linking each doc file, source code repo link.
- [ ] `LICENSE` — correct licence file: EUPL 1.2 for Simpl-built solutions; upstream OSS licence for reused/forked components.
- [ ] `doc/architecture.md` — six-view architecture document with provenance line (source sections).
- [ ] `doc/guides.md` *(optional)* — installation and usage guide. Only create when substantive content exists; do not create stub files.
- [ ] `doc/api.md` *(optional)* — API overview, only when real endpoints or interface content is documented. For solutions with multiple APIs, use an `api/` folder with per-API OpenAPI/AsyncAPI files and an `api/README.md`. Do not create stub API files.

## Content requirements per view

| View | Minimum content |
|------|----------------|
| Business view | What the component does, for whom, and why; business process involvement; capability-map placement. |
| Data view | Data model overview, data flows, ownership. |
| Application view | Internal decomposition (named sub-components); key integrations with relative links to target `doc/architecture.md` files. |
| Technical view | Technology stack; deployment topology; source repositories. |
| Security view | AuthN/AuthZ approach; certificate or secrets handling; known threat surface notes. |
| Testing | Strategy, coverage, PSO validation status. |

## Cross-reference quality

- [ ] All relative links in `doc/architecture.md` resolve to existing files.
- [ ] All external URLs are also listed in the top-level `references.md`.

## Stubs

Stub files (`doc/api.md`, `doc/guides.md`, top-level `eif.md`) are no longer created. When no source content exists for a file type, the file is simply omitted and not linked from the solution README. Section-level stubs *within* `doc/architecture.md` remain acceptable (e.g. "Testing — Status: not yet documented"); content is NOT invented.

## Not required for documentation-complete

- Filled Testing section (stubs acceptable for all solutions in the current release).
- Threat model or secrets management documentation (stubs acceptable).
- Roadmap duplication (Notion is the source of truth; link only).
