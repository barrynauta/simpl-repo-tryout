<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Foundations</a><br/>
        <a href="README.md">Data architecture</a><br/>
            <strong>Open-source components data model</strong><br/>
</p>
</div>

# Open-source components data model

> The chapter introduction is reproduced first (FTA §5, lines 6476–6514), followed by FTA §5.1 (lines 6515–6577). Source dated 2026-04-20. Upstream link: [FTA spec §5.1](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#51-open-source-components-data-model).

---

##  5. <a name='Simpl-OpenDataArchitecture'></a>Simpl-Open Data Architecture

Simpl-Open Data Architecture presents data entities and/or collections
and how they are structured within the system.

Given that Simpl-Open combines existing/reusable open-source components
and custom-built components, the following approach is followed:

1.  For open-source components, the dedicated sub-section provides a
    link to the available data model documentation of the component.

2.  For custom components, the dedicated sub-section describes the data
    model per component (as per the microservices approach) through the
    following layers:

<table>
<thead>
<tr class="header">
<th><strong>Layer</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Conceptual</td>
<td>The conceptual data model (CDM) operates at a high level, providing an overarching perspective on the application's data needs. It defines a broad and simplified view of the data to create a shared understanding of the application by capturing the essential concepts. These essential concepts are captured in an Entity Relationship Diagram (ERD) and the accompanying entity definitions.</td>
</tr>
<tr class="even">
<td>Logical</td>
<td><p>The logical data model (LDM) contains representations that fully defines relationships in data, adding the details and structure of essential entities. The LDM remains data platform agnostic because it focuses on business needs, flexibility and portability.</p>
<p>The LDM includes the specific attributes of each entity, the relationships between entities and the cardinality of those relationships.</p></td>
</tr>
<tr class="odd">
<td>Physical</td>
<td>The physical data model (PDM) is a data model that represents relational data objects. It describes the technology-specific and database-specific implementation of the data model and is the last step in transforming from the logical data model to a working database. The physical data model includes all the needed physical details to build the database.</td>
</tr>
</tbody>
</table>

###  5.1. <a name='Open-SourceComponentsDataModel'></a>Open-Source Components Data Model

<table>
<thead>
<tr class="header">
<th><strong>OSS</strong></th>
<th><strong>Data Model</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XFSC Signer</td>
<td>The self-description is wrapped into a verifiable credentials and the proof section of the VC contain the signature. The data model is defined here: <a href="https://www.w3.org/TR/vc-data-model/#proofs-signatures">https://www.w3.org/TR/vc-data-model/#proofs-signatures</a></td>
</tr>
<tr class="even">
<td>XFSC catalogue</td>
<td><p>XFSC catalogue stores the data in three different ways:</p>
<ul>
<li><p>File storage for the JSON-LD serialisation. Definition of the file format can be found <a href="https://json-ld.org/">https://json-ld.org/</a>. The data model itself depends on the schema definition used (defined in Additional Technical Specifications about Capabilities section).</p></li>
<li><p>Graph-DB (Neo4J) used as index to allow semantic queries. The data model of the database also depends on the schema.</p></li>
<li><p>Metadata stored in a relational database (PostgreSQL). Data Model is described in <a href="https://gaia-x.gitlab.io/data-infrastructure-federation-services/cat/architecture-document/architecture/catalogue-architecture.html#_metadata_store">https://gaia-x.gitlab.io/data-infrastructure-federation-services/cat/architecture-document/architecture/catalogue-architecture.html#_metadata_store</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>OpenBao</td>
<td>Secrets data is stored in secret engine <a href="https://openbao.org/docs/internals/architecture/">https://openbao.org/docs/internals/architecture/</a>. The data model depends on the model used currently a Key-Value (KV) Store Data Model is used.</td>
</tr>
<tr class="even">
<td>Keycloak</td>
<td>Keycloak use a "code first" approach to data modelling. There are no data model diagrams available in their documentation, but the data model is described in their code repository: <a href="https://github.com/keycloak/keycloak/tree/main/model">https://github.com/keycloak/keycloak/tree/main/model</a></td>
</tr>
<tr class="odd">
<td>EJBCA</td>
<td>EJBCA data model diagram is located <a href="https://doc.primekey.com/ejbca/ejbca-introduction/ejbca-architecture/internal-architecture">https://doc.primekey.com/ejbca/ejbca-introduction/ejbca-architecture/internal-architecture</a></td>
</tr>
<tr class="even">
<td>Crossplane</td>
<td><p>Resource Definition:</p>
<p><a href="https://docs.crossplane.io/latest/concepts/composite-resource-definitions/">https://docs.crossplane.io/latest/concepts/composite-resource-definitions/</a></p></td>
</tr>
<tr class="odd">
<td>OpenTofu</td>
<td><p>Resource Definition:</p>
<p><a href="https://opentofu.org/docs/language/resources/">https://opentofu.org/docs/language/resources/</a></p></td>
</tr>
<tr class="even">
<td>Kubernetes</td>
<td>Kubernetes objects:<br />
<a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/">https://kubernetes.io/docs/concepts/overview/working-with-objects/</a></td>
</tr>
<tr class="odd">
<td>Ansible</td>
<td><p>Ansible Data Manipulation:</p>
<p><a href="https://docs.ansible.com/ansible/latest/playbook_guide/complex_data_manipulation.html">https://docs.ansible.com/ansible/latest/playbook_guide/complex_data_manipulation.html</a></p></td>
</tr>
<tr class="even">
<td>ArgoCD</td>
<td><p>RBAC Model</p>
<p><a href="https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/#rbac-model-structure">https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/#rbac-model-structure</a></p></td>
</tr>
</tbody>
</table>

