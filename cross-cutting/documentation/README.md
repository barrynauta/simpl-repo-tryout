<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Cross-Cutting</a><br/>
        <strong>Documentation</strong><br/>
</p>
</div>

# Documentation

**Product-level documentation for Simpl-Open as a deployed system.** The two guides under this folder describe how to **install** and **use** a complete Simpl-Open deployment — that is, the integrated set of agents (Consumer, Data Provider, Governance Authority, etc.) running together. They are **not** per-component guides.

> **Scope reminder.** For component-specific deployment, configuration, or upgrade docs, navigate to the relevant solution folder under the capability map (e.g. `governance/contract-management/contract-establishment/contract-manager/doc/`). The guides here sit *one level above* the components — at the agent / product level.

## Guides

- [installation-guide/](installation-guide/README.md) — **D1.6.1 Simpl-Open Installation Guide**: end-to-end procedure for installing Simpl-Open agents in a target environment, prerequisites, infrastructure setup, troubleshooting. SC1 deliverable.
- [user-manual/](user-manual/README.md) — **Simpl-Open User Manual**: how participants use a deployed Simpl-Open system — onboarding, contract negotiation, resource discovery, day-to-day operations from each actor's perspective. SC1 deliverable.

## Why this folder exists

A component README answers *"how do I deploy and configure this one service?"*. A solution README answers *"what does this service do?"*. Neither answers *"how do I install Simpl-Open as a whole?"* or *"how do I, as a participant, use a Simpl-Open data space once it's running?"*. The two guides here fill that product-level gap.

These are catalogue-side **structural pointers** to the upstream guides that live in the dedicated documentation repositories. The authoritative source documents (PDFs, sub-page assets) are not mirrored here — see each sub-folder's `CANONICAL.md` for the upstream URL and `.canonical.yaml` for the machine-readable pointer.
