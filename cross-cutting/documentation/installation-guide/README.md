<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Documentation</a><br/>
            <strong>Installation Guide</strong><br/>
</p>
</div>

# Installation Guide

**D1.6.1 Simpl-Open Installation Guide** — the official SC1 deliverable describing how to install Simpl-Open agents in a target environment.

> **Scope: agent / product level.** This guide covers installing the full Simpl-Open system, not individual components. For component-specific install steps, see the `doc/installation-guide/` folder inside each solution under the capability map.

The guide is maintained in a dedicated upstream repository — see [CANONICAL.md](CANONICAL.md) for the URL and [.canonical.yaml](.canonical.yaml) for the machine-readable pointer.

## What it covers

- Prerequisites (target Kubernetes cluster, network, DNS, certificates).
- Per-actor installation paths: governance-authority, data-provider, consumer, application-provider, infrastructure-provider, with their respective Helm umbrella charts and deployment compositions.
- Common-components bootstrap (Kafka, OpenBao/Vault, PostgreSQL).
- Post-install verification and a troubleshooting reference.

## Source

- Repository: <https://code.europa.eu/simpl/simpl-open/documentation/installation-guide>
- Document title in upstream `README.md`: *D1.6.1 Simpl-Open Installation Guide*.
- Format: Markdown source + generated PDFs under `documents/` in the upstream repo. The PDFs are not mirrored to this catalogue.
