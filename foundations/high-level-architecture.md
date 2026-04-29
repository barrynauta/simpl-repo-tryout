<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>High-level architecture</strong><br/>
</p>
</div>

# High-level architecture

The layered view of Simpl-Open that bridges the abstract data-space concepts above with the concrete capability map below. It identifies the building blocks that compose the platform and the relationships between them, before any specific technology is named. Read this page alongside [capability-map.md](capability-map.md): the building blocks here become the capabilities and business services there.

## Source

Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **2.6 High-Level Architecture** (lines 1305–1362 of the source, dated 2026-04-20). Upstream link: [FTA spec §2.6](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#26-high-level-architecture).

---

###  2.6. <a name='High-LevelArchitecture'></a>High-Level Architecture

This section elaborates on the High-Level Architecture of Simpl-Open. It
presents the capabilities of Simpl-Open and the building blocks that
support these capabilities. It is important to remark that the high
level architecture lays out the capabilities of Simpl-Open as a whole.
How these capabilities are realised is then described in the following
sections of the document.

The concepts described in this section have been, for a large part,
already developed in the [Architecture Vision
Document](https://ec.europa.eu/newsroom/dae/redirection/document/86241)
of the Simpl Preparatory Study. They are taken over in this document and
updated/complemented where needed to stay up-to-date with the current
developments of Simpl-Open.

Six architectural dimensions describe Simpl-Open: the integration
dimension, the data dimension, the infrastructure dimension, the
administration dimension, the governance dimension and the security
dimension.

1.  The **integration dimension** contains the capabilities that enable
    participants to integrate with each other in a secured and trusted
    manner. This is required for the well-functioning of a Data Space
    integrating Simpl-Open. These capabilities regard security, access
    control and trust and federation management.

2.  The **data dimension** focuses on semantic interoperability, data
    models, data quality and governance of data. It ensures that data
    can be understood, processed, and exchanged consistently across
    participants through standardized vocabularies and quality
    management.

3.  The **infrastructure dimension** allows end users to utilise and
    manage infrastructure resources offered by infrastructure providers.
    Simpl-Open can connect to third-party infrastructure resources,
    enabling end users to execute applications and manage workloads.

4.  The **administration dimension** provides supporting capabilities
    for the well-functioning of the other dimensions as well as
    administration of Simpl-Open. The administration layer allows actors
    to operate their components in the Data Space.

5.  The **governance dimension** establishes and enforces policies,
    manages risks, oversees compliance and provides audit and assurance
    for the entire ecosystem. It supports the implementation of legal
    and organisational interoperability through policy management,
    contract management, participant lifecycle, and audit capabilities.

6.  The **security dimension** ensures that all interactions and data
    exchanges across the Simpl-Open ecosystem are confidential,
    authentic, and tamper-resistant. It focuses on safeguarding
    communications, assets, and operations through technical and
    procedural resilience measures.

Each of these six layers is further detailed in the following
sub-sections.

