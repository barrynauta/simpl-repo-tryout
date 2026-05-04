<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <strong>Cross-Cutting</strong><br/>
</p>
</div>

# Cross-cutting

Components that don't belong to a single capability in the Simpl-Open capability map: shared libraries used across multiple services, command-line and one-shot utilities, and reference samples that demonstrate integration patterns. Mirrors the `supporting-services/` group used in the as-is → to-be repository mapping spreadsheet.

## Sub-folders

- [agents/](agents/README.md) — actor-specific master Helm charts that compose modules from across the capability map into deployable Simpl-Open Agents (Consumer, Data Provider, Governance Authority, etc.).
- [documentation/](documentation/README.md) — **agent / product-level guides** for installing and using a complete Simpl-Open deployment (D1.6.1 Installation Guide, User Manual). Distinct from per-component docs which live alongside each solution under the capability map.
- [libs/](libs/README.md) — shared libraries (Java, Python, frontend) consumed by multiple solutions across the capability map.
- [samples/](samples/README.md) — reference implementations and demo nodes — including microfrontend skeletons, the IAA echo service, and the eIDAS demo node — used as starting points or for integration testing.
- [utils/](utils/README.md) — operational utilities and command-line tools used during deployment and pre-configuration of components.

## Why this folder exists

The capability map (six dimensions, capabilities, business services, solutions) describes *what Simpl-Open does*. The contents of this folder either (a) span several capabilities, (b) are development artefacts rather than runtime services, or (c) are samples that aren't meant to be deployed in production. Per the as-is → to-be PSO mapping, they live under `simpl/simpl-open/development/supporting-services/`; in this catalogue they live here.
