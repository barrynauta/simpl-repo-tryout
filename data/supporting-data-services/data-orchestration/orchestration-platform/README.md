# Orchestration Platform

Executes data workflows for data processing and pre-processing using custom or built-in data services (such as data anonymisation). Acts as a data plane bridge between data sources and consumer destinations. Based on Dagster with a custom Asset Orchestrator component developed for Simpl-Open.

Capability-map placement: `data / supporting-data-services / data-orchestration / orchestration-platform`. This solution implements the **Data orchestration** business service.

Provenance: built on upstream **Dagster** (Apache 2.0) with a custom Simpl-built Asset Orchestrator and Auth Proxy. The Simpl fork lives at `orchestration-platform/dagster`. Licence: Apache 2.0 (Dagster upstream). Simpl-specific components (Asset Orchestrator, Auth Proxy) may carry separate provenance — see LICENCE notes.

Note: the architecture spec frames this component both as a Connector extension/data-plane bridge (§4.3.1) and as a data-orchestration capability (capmap). The capmap placement is followed per precedence rule 2 (flag d-5 from step 3 checkpoint).

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0 (Dagster upstream).

## Source code

- Simpl fork: `code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster`
- Upstream Dagster: `https://github.com/dagster-io/dagster`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
