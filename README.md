# Simpl Documentation Catalogue

## What is Simpl

With the ongoing exponential growth of data, there is a pressing need within the European Union to provide access to resilient and competitive data storage and processing capacities for both the private and public sectors. The European Commission aims to address this need through greater data sharing, decentralised data processing, and the establishment of sector-specific Data Spaces — federated ecosystems where organisations pool resources, reduce duplication of effort, and create new cross-sector business value. Simpl is the European Commission's middleware programme delivering the technical foundation on which these data spaces can be built and operated.

The programme's primary technical output is Simpl-Open: an open-source, multi-vendor, modular, and interoperable middleware that powers secure and sovereign data sharing across Europe. Rather than requiring each data space initiative to build interoperability from scratch, Simpl-Open provides a modular, open, and reusable foundation that integrates existing solutions, reducing the time and resources needed to select, develop, and deploy data space components. Simpl-Open stays agnostic to the specifics of any particular data space — it provides common services on which data spaces are built, while leaving domain-specific concerns (data representation standards, quality certifications, peer review rules) to the data space governance authority. Alongside Simpl-Open, the programme includes Simpl-Labs (a testing and validation environment for components and interoperability) and Simpl-Live (production implementations applied to selected European data spaces).

Participants join a data space by deploying a Simpl-Open Agent — a set of integrated software components that acts as a local gateway for data and service interactions. The Agent spans across actor types (Governance Authorities, Providers, Consumers, and their end-users), enabling asset sharing between them. Each actor requiring a distinct role in the data space deploys their own agent instance. Agents are deployment compositions of Simpl-Open modules and are separate from the modular solutions described in this catalogue's capability map.

Simpl-Open not only enables operation within a single data space but creates interoperability between data spaces. As multiple data spaces incorporate Simpl-Open, they become more connected, allowing services and assets to cross data space boundaries. This cross-space interoperability is one of Simpl-Open's distinguishing architectural goals: it is not a standalone platform but a shared backbone for the emerging European data economy. Simpl-Open aligns with and builds upon adjacent EU and international initiatives including Gaia-X (trust model and self-description standards) and the Data Spaces Support Centre (DSSC) interoperability definitions.

[VERIFY]

---

## Business Processes

Business processes describe the operational flows through the Simpl system — the end-to-end sequences of actions that participants, providers, consumers, and governance authorities perform to achieve outcomes such as onboarding, resource sharing, or contract establishment. They are sourced from the public Simpl Requirements site and represent the authoritative behavioural specification of the platform. Each BP and SA folder in this catalogue captures the full hierarchy from the public source, including diagrams and step-level details. The scenario architectures (SA entries) complement the BPs by describing specific deployment or integration patterns that cut across multiple process flows.

<table>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP01-define-dataspace-governance/README.md">
<img src="./foundations/business-processes/media/BP01-tile.png" width="180" /><br>
<b>BP01</b><br>
<sub>Define dataspace governance</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP02-configuration-governance-authority/README.md">
<img src="./foundations/business-processes/media/BP02-tile.png" width="180" /><br>
<b>BP02</b><br>
<sub>Configure data space</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP03A-onboarding-participant-providers/README.md">
<img src="./foundations/business-processes/media/BP03A-tile.png" width="180" /><br>
<b>BP03A</b><br>
<sub>Onboard providers &amp; consumers</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP03B-onboarding-participant-end-user/README.md">
<img src="./foundations/business-processes/media/BP03B-tile.png" width="180" /><br>
<b>BP03B</b><br>
<sub>Onboard end-users</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP05B-provider-manages-resource-descriptions/README.md">
<img src="./foundations/business-processes/media/BP05B-tile.png" width="180" /><br>
<b>BP05B</b><br>
<sub>Manage resource descriptions</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP06-consumer-searches-resources/README.md">
<img src="./foundations/business-processes/media/BP06-tile.png" width="180" /><br>
<b>BP06</b><br>
<sub>Search resources</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP07-establish-usage-contract/README.md">
<img src="./foundations/business-processes/media/BP07-tile.png" width="180" /><br>
<b>BP07</b><br>
<sub>Establish usage contract</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP08-consume-infrastructure-resource/README.md">
<img src="./foundations/business-processes/media/BP08-tile.png" width="180" /><br>
<b>BP08</b><br>
<sub>Consume infrastructure resource</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP09A-consume-data-resource/README.md">
<img src="./foundations/business-processes/media/BP09A-tile.png" width="180" /><br>
<b>BP09A</b><br>
<sub>Consume data resource</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP09B-consume-data-via-application/README.md">
<img src="./foundations/business-processes/media/BP09B-tile.png" width="180" /><br>
<b>BP09B</b><br>
<sub>Consume data via application</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP12B-single-node-logging-monitoring/README.md">
<img src="./foundations/business-processes/media/BP12B-tile.png" width="180" /><br>
<b>BP12B</b><br>
<sub>Single-node logging &amp; monitoring</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/business-processes/BP13-it-administration/README.md">
<img src="./foundations/business-processes/media/BP13-tile.png" width="180" /><br>
<b>BP13</b><br>
<sub>IT administration</sub>
</a>
</td>
</tr>
</table>

> **BP03C** (End-user role request) has no card image on the public index page and is omitted from the tile grid above.

---

## Solution Architectures

No card images exist on the public index page for the SA entries. Text-only links:

| ID | Name | Description |
|----|------|-------------|
| [SA01](./foundations/business-processes/SA01-data-orchestration/README.md) | Data orchestration | Design, execute, and monitor traceable multi-step data processing workflows |
| [SA02](./foundations/business-processes/SA02-data-processing-services/README.md) | Data processing services | Pseudonymisation and anonymisation services for participants |
| [SA03](./foundations/business-processes/SA03-credentials-actions-governance-authority/README.md) | Credentials actions | Governance Authority manages participant credentials: revocation, suspension, renewal |
| [SA04](./foundations/business-processes/SA04-provider-manages-deployment-scripts/README.md) | Deployment scripts | Infrastructure Providers create and manage VM templates and deployment scripts |

See [foundations/business-processes/README.md](./foundations/business-processes/README.md) for the full list and detailed content.

---

## Non-Functional Requirements

Non-functional requirements (NFRs) are the quality attributes the Simpl system must satisfy: accessibility, availability, security, performance, and more. They constrain how the architecture and business processes are designed — a solution may correctly implement a business process yet still fail an NFR if it does not meet the stated thresholds. NFRs are sourced from the public Simpl Requirements site, and measurable thresholds are quoted verbatim from that source wherever they are defined. Each NFR folder in this catalogue documents the requirement in the author's own words alongside the canonical source link and any verbatim threshold statements.

<table>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR01-accessibility/README.md">
<img src="./foundations/non-functional-requirements/media/accessibility-tile.png" width="180" /><br>
<b>NFR01</b><br>
<sub>Accessibility</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR02-availability/README.md">
<img src="./foundations/non-functional-requirements/media/availability-tile.png" width="180" /><br>
<b>NFR02</b><br>
<sub>Availability</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR03-composability-extensibility/README.md">
<img src="./foundations/non-functional-requirements/media/composability-extensibility-tile.png" width="180" /><br>
<b>NFR03</b><br>
<sub>Composability &amp; extensibility</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR04-discoverability/README.md">
<img src="./foundations/non-functional-requirements/media/discoverability-tile.png" width="180" /><br>
<b>NFR04</b><br>
<sub>Discoverability</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR05-federation/README.md">
<img src="./foundations/non-functional-requirements/media/federation-tile.png" width="180" /><br>
<b>NFR05</b><br>
<sub>Federation</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR06-interoperability/README.md">
<img src="./foundations/non-functional-requirements/media/interoperability-tile.png" width="180" /><br>
<b>NFR06</b><br>
<sub>Interoperability</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR07-loose-coupling/README.md">
<img src="./foundations/non-functional-requirements/media/loose-coupling-tile.png" width="180" /><br>
<b>NFR07</b><br>
<sub>Loose coupling</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR08-maintainability/README.md">
<img src="./foundations/non-functional-requirements/media/maintainability-tile.png" width="180" /><br>
<b>NFR08</b><br>
<sub>Maintainability</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR09-modularity/README.md">
<img src="./foundations/non-functional-requirements/media/modularity-tile.png" width="180" /><br>
<b>NFR09</b><br>
<sub>Modularity</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR10-openness-agnosticism/README.md">
<img src="./foundations/non-functional-requirements/media/openness-agnosticism-tile.png" width="180" /><br>
<b>NFR10</b><br>
<sub>Openness &amp; agnosticism</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR11-reliability/README.md">
<img src="./foundations/non-functional-requirements/media/reliability-tile.png" width="180" /><br>
<b>NFR11</b><br>
<sub>Reliability</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR12-resilience/README.md">
<img src="./foundations/non-functional-requirements/media/resilience-tile.png" width="180" /><br>
<b>NFR12</b><br>
<sub>Resilience</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR13-scalability-elasticity/README.md">
<img src="./foundations/non-functional-requirements/media/scalability-elasticity-tile.png" width="180" /><br>
<b>NFR13</b><br>
<sub>Scalability &amp; elasticity</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR14-security-privacy-trust/README.md">
<img src="./foundations/non-functional-requirements/media/security-privacy-trust-tile.png" width="180" /><br>
<b>NFR14</b><br>
<sub>Security, privacy &amp; trust</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./foundations/non-functional-requirements/NFR15-usability/README.md">
<img src="./foundations/non-functional-requirements/media/usability-tile.png" width="180" /><br>
<b>NFR15</b><br>
<sub>Usability</sub>
</a>
</td>
<td></td>
</tr>
</table>

See [foundations/non-functional-requirements/README.md](./foundations/non-functional-requirements/README.md) for the full list and detailed content.

---

## Capability Map

Simpl-Open organises its functionality into six dimensions: Administration, Data, Governance, Infrastructure, Integration, and Security. Each dimension contains one or more capabilities, each capability contains one or more business services, and each business service is realised by one or more solutions. This four-level hierarchy — dimension → capability → business service → solution — is the organising principle of the entire repository tree. The map was defined in the Simpl-Open functional and technical architecture specification and governs how documentation folders are named, nested, and cross-referenced. Every solution folder in this catalogue sits at a path of the form `dimension/capability/business-service/solution/` that corresponds directly to a node in the map.

![L1 Capability Map](./foundations/media/image16.png)
*Figure: The six dimensions of Simpl and their capabilities.*

### Dimensions

- [administration/](./administration/README.md) — platform management and operational services for a Simpl-Open agent node, covering observability and notification and messaging
- [data/](./data/README.md) — data-related platform services covering schema and vocabulary governance, data workflow orchestration, and supporting data services
- [governance/](./governance/README.md) — governance services covering participant lifecycle management, contract management, policy administration, and resource description management
- [infrastructure/](./infrastructure/README.md) — infrastructure provisioning services enabling consumers to request and access compute, storage, and network resources
- [integration/](./integration/README.md) — integration services connecting data space participants for resource discovery, catalogue publication, and resource sharing
- [security/](./security/README.md) — identity, authentication, authorisation, and credential management services implementing a two-tier IAA architecture

See [foundations/capability-map.md](./foundations/capability-map.md) for the full L1 + L2 map with all business services.

---

## How Business Processes, Architecture, and NFRs Relate

*This section is intentionally left as a placeholder. The narrative explaining how business processes, the implementation architecture, and non-functional requirements relate to each other will be authored separately and inserted here. Do not auto-generate this content.*

---

## Foundational Reference

Supporting documents that establish the design vocabulary and governing commitments of Simpl-Open:

- [Architectural principles](./foundations/principles.md) — high-level design commitments informing every architecture decision across Simpl-Open, sourced from the functional and technical architecture document.
- [Architectural patterns](./foundations/architectural-patterns.md) — recurring structural and behavioural design patterns applied across solutions, sourced from the functional and technical architecture document.
- [Glossary](./foundations/glossary.md) — definitional anchor for Simpl terminology, sourced from the official Simpl programme glossary.

---

## Other Contents

- [cross-cutting/](./cross-cutting/README.md) — components that don't map to a single capability
- [interoperability/](./interoperability/README.md) — technical and semantic interoperability index

---

*The `_planning/` folder contains internal generation state and is not part of the documentation product.*
