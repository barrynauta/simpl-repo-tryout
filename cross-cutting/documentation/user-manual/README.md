<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Documentation</a><br/>
            <strong>User Manual</strong><br/>
</p>
</div>

# User Manual

**Simpl-Open User Manual** — the official SC1 deliverable describing how participants use a deployed Simpl-Open system.

> **Scope: agent / product level.** This manual covers using the Simpl-Open product as a participant, not the inner workings of individual components. For component-specific user docs (e.g. how the contract-manager UI works), see the `doc/user-manual/` folder inside each solution under the capability map.

The manual is maintained in a dedicated upstream repository — see [CANONICAL.md](CANONICAL.md) for the URL and [.canonical.yaml](.canonical.yaml) for the machine-readable pointer.

## What it covers

- Day-to-day usage from each actor's perspective: Governance Authority, Data Provider, Application Provider, Infrastructure Provider, Consumer.
- Onboarding and credential lifecycle (request, approval, install, renewal, revocation).
- Resource publication, discovery, contract negotiation, and consumption flows end-to-end.
- Operational responsibilities split between the participant and the agent.

## Source

- Repository: <https://code.europa.eu/simpl/simpl-open/documentation/user-manual>
- Document title in upstream `README.md`: *Simpl-Open User Manual*.
- Format: Markdown source + generated PDFs under `documents/` in the upstream repo. The PDFs are not mirrored to this catalogue.

## Note on bundled component docs

The upstream `documents/` folder contains PDFs generated from per-component READMEs (e.g. `778_sdtooling-api-be_README.pdf`, `951_common_components_README.pdf`). These are bundled with the user manual for convenience, but the canonical home for each component's docs remains the corresponding solution folder under the capability map. If you need the latest version of a component's docs, navigate via the capability map; the bundles here are snapshots tied to the manual's release.
