<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <strong>Foundations</strong><br/>
</p>
</div>

# Reference

This folder contains foundational artefacts describing what Simpl is and should do — separate from the implementation tree (dimension folders). Use this as the canonical entry point for understanding the system.

---

## Catalogue of the system

- [actors.md](actors.md) — the five canonical Simpl-Open actors (Application Provider, Data Provider, Infrastructure Provider, Consumer, Governance Authority) and which business processes each one touches
- [capability-map.md](capability-map.md) — Level 1 and Level 2 capability map: the six dimensions, all capabilities and business services, deployment model, and Release 3.0 scope
- [business-processes/README.md](business-processes/README.md) — functional requirements catalogue: 13 business processes and 4 scenario architectures, each with a summary, diagrams, and auto-inferred cross-references to the capability map
- [non-functional-requirements/README.md](non-functional-requirements/README.md) — non-functional requirements catalogue: 15 NFRs covering availability, security, modularity, and more, each with measurable thresholds (where published) and cross-references
- [api-catalogue.md](api-catalogue.md) — index of all 42 OpenAPI/AsyncAPI specifications imported from the implementation source, organised by dimension, by kind, and by tier
- [user-interfaces.md](user-interfaces.md) — inventory of every user interface shipped with Simpl-Open (Catalogue Client, Participant Utility, Contract Template Editor, Policy Creator, Dagit, Kibana, Grafana, microfrontend framework)

## Concepts and design vocabulary

- [dataspace-concepts.md](dataspace-concepts.md) — actors, agents, Tier I / Tier II split, anatomy of a Simpl-Open service, built-in vs access-through services, Echo Service template
- [high-level-architecture.md](high-level-architecture.md) — layered building-block view that bridges the data-space concepts with the capability map
- [connector-protocol.md](connector-protocol.md) — Data Space Protocol (DSP / IDSA) concepts as used by every Simpl-Open agent
- [eidas-integration.md](eidas-integration.md) — how the Simpl identity model maps onto eIDAS and the EUDI framework
- [principles.md](principles.md) — the foundational architectural principles of Simpl-Open
- [architectural-patterns.md](architectural-patterns.md) — the architectural patterns used in Simpl-Open
- [interoperability.md](interoperability.md) — minimal mapping of standards used in Simpl in the context of interoperability, mostly Semantic and Technical
- [glossary.md](glossary.md) — the glossary, what is in a name?

## Architecture decisions and traceability

- [assumptions-and-decisions.md](assumptions-and-decisions.md) — architectural assumptions and the Architecture Decision Records (ADRs) that constrain the design
- [functional-traceability.md](functional-traceability.md) — end-to-end mapping from functional requirements to implementing components (FTA §4.6 + Annex 1)

## Deployment, operations, security

- [deployment-model.md](deployment-model.md) — logical (agent-and-cluster) and technical (Kubernetes-and-cloud) deployment views
- [data-architecture/README.md](data-architecture/README.md) — full data architecture chapter: open-source components data model + conceptual / logical / physical models for the custom components
- [technology-roadmap.md](technology-roadmap.md) — forward-looking technology candidates beyond Release 3.0
- [security-architecture/](security-architecture/README.md) — perimeter of intervention, DevSecOps security aspects, functional + technical security architecture; includes stub children for ufw, wireguard, nftables, modsecurity
- [devsecops/](devsecops/README.md) — full DevSecOps approach (cluster planning, provisioning, environment onboarding, security checks, GitOps, testing, monitoring/logging, backup, deprovisioning); includes stub children for gitea, gitlab, helm-charts, trivy, fortify, sonarqube, ansible, spring-cloud-config, gitea-actions
- [interfaces/](interfaces/README.md) — cross-cutting interface technologies (Swagger/OpenAPI, Webpack Module Federation, Spring Cloud Circuit Breaker)
