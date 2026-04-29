<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Actors</strong><br/>
</p>
</div>

# Actors

An actor is an entity or participant that interacts with the Simpl-Open platform. Actors can be users, applications, or Simpl-Open agents themselves. Each actor plays specific roles and holds distinct permissions within the data space ecosystem.

The five actors below are the canonical participant categories defined in the Simpl-Open functional and technical architecture. Every business process, capability, and solution in this catalogue addresses one or more of them.

> *The original FTA spec includes a context diagram (`image21.png` in the source document) showing the five actor types and their interactions. The figure has not yet been imported into this catalogue; refer to section 3.1 of the [functional and technical architecture specification](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#3-simpl-open-business-architecture) for the diagram.*

## Application Provider

Data space actors offering applications to consumers or any other type of participant. The term "application" is used in a broad sense and covers any sort of executables — including applications and algorithms such as a trained AI model that users can leverage to analyse their data. Application providers can also define the access control policies regarding their resources and bill the users for their usage.

**Touches**: [BP05B](business-processes/BP05B-provider-manages-resource-descriptions/README.md), [BP07](business-processes/BP07-establish-usage-contract/README.md), [BP09B](business-processes/BP09B-consume-data-via-application/README.md).

## Data Provider

Data space actors offering data to consumers. They can share one or more datasets and regulate access and usage over the data with policies. To compensate for data usage, data providers can also bill data space consumers. Example: an energy network operator sharing data on the energy grid load to energy production facilities (acting as consumers) for use in a production-optimisation application.

**Touches**: [BP05B](business-processes/BP05B-provider-manages-resource-descriptions/README.md), [BP07](business-processes/BP07-establish-usage-contract/README.md), [BP09A](business-processes/BP09A-consume-data-resource/README.md), [BP09B](business-processes/BP09B-consume-data-via-application/README.md), [SA02](business-processes/SA02-data-processing-services/README.md).

## Infrastructure Provider

Data space actors offering infrastructure resources and services to consumers (or to any other participant) so they can process the data provided by data providers. They can launch virtual machines or containers and run applications, algorithms, or other executables on top of the underlying infrastructure. Like data providers, infrastructure providers can define access control policies for their resources and bill participants for their usage.

**Touches**: [BP07](business-processes/BP07-establish-usage-contract/README.md), [BP08](business-processes/BP08-consume-infrastructure-resource/README.md), [SA04](business-processes/SA04-provider-manages-deployment-scripts/README.md).

## Consumer

Participants whose aim is to use data, applications, and infrastructure shared by providers. They can search for resources and use them as allowed by the policies. For data, this means typically either using it online by leveraging the infrastructure and applications provided by application and infrastructure providers, or — if policy allows — downloading it for local usage.

**Touches**: [BP03B](business-processes/BP03B-onboarding-participant-end-user/README.md), [BP03C](business-processes/BP03C-end-user-role-request/README.md), [BP06](business-processes/BP06-consumer-searches-resources/README.md), [BP07](business-processes/BP07-establish-usage-contract/README.md), [BP08](business-processes/BP08-consume-infrastructure-resource/README.md), [BP09A](business-processes/BP09A-consume-data-resource/README.md), [BP09B](business-processes/BP09B-consume-data-via-application/README.md).

## Governance Authority

The data space participant that is accountable for creating, developing, operating, maintaining, and enforcing the governance framework for a particular data space.<sup>1</sup>

**Touches**: [BP01](business-processes/BP01-define-dataspace-governance/README.md), [BP02](business-processes/BP02-configuration-governance-authority/README.md), [BP03A](business-processes/BP03A-onboarding-participant-providers/README.md), [BP03B](business-processes/BP03B-onboarding-participant-end-user/README.md), [BP12B](business-processes/BP12B-single-node-logging-monitoring/README.md), [BP13](business-processes/BP13-it-administration/README.md), [SA03](business-processes/SA03-credentials-actions-governance-authority/README.md).

---

## End-users vs participants

In addition to the five participant categories above, every participant has its own end-users — the people who actually interact with the agent's user interfaces. End-users are scoped to a single participant; their roles and permissions are governed by that participant's IAA Tier 1 (RBAC), while participant-to-participant communication is governed by Tier 2 (ABAC). See [security/access-control-and-trust/](../security/access-control-and-trust/README.md) for the full Tier 1 / Tier 2 model and [security/access-control-and-trust/detailed-spec.md](../security/access-control-and-trust/detailed-spec.md) for the full role and identity-attribute catalogue.

---

## Source

Extracted from `Functional-and-Technical-Architecture-Specifications.md`, section 3.1 Actors. The footnote definition of *Governance Authority* is sourced from the [DSSC Glossary v2.0](https://dssc.eu/space/Glossary/176553985/DSSC+Glossary+%7C+Version+2.0+%7C+September+2023).
