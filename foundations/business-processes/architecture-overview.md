<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Foundations</a><br/>
        <a href="README.md">Business processes</a><br/>
            <strong>Functional architecture overview</strong><br/>
</p>
</div>

# Functional architecture overview

The cross-BP synthesis: how the functional components named in the FTA (Onboarding, IAA, Vocabulary Management, Schema Management, Resource Offering Editor, Federated Catalogue, Search, Data Space Connector, Contract Management, Infrastructure Management, Data Transfer, Observability) interact across every business process. Where the per-BP READMEs in this folder describe one process at a time, this page describes the system end-to-end.

## Source

Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **3.2 Simpl-Open Functional Architecture** (lines 2465–2793 of the source, dated 2026-04-20). Upstream link: [FTA spec §3.2](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#32-simpl-open-functional-architecture).

---

###  3.2. <a name='Simpl-OpenFunctionalArchitecture'></a>Simpl-Open Functional Architecture

The following diagram presents Simpl-Open functional architecture.

An agent per type of participant is represented and the functional
components are represented as ArchiMate services.


Below are described all the functional components presented on the
diagram, how they implement the building blocks from the high-level
architecture, and how they interact between them. These interactions are
highlighted with numbers on the diagram, which are linked to the below
description through the purple numbers between brackets.

The **Onboarding** component implements the Onboarding building block:
it provides the functionalities to submit, review and approve onboarding
requests and deliver to the applicant the necessary security credentials
to join a Data Space.

Both consumers and providers (data/application/infrastructure) can
request to join a Data Space through the **Onboarding** component
(**1**). This component allows the governance authority to control the
required onboarding documents and approve/reject the onboarding request
(**2**). If approved, the onboarding component sets up accesses and
rights into the **IAA** component of the Governance authority (**3**)
and delivers security credentials to the applicant (**4**).

The **IAA** component implements the Identity Provider Federation,
Authorisation, Security Attribute Provider Federation and User Roles
building blocks: it serves as a security intermediary for all
communications between actors and components of Simpl-Open.

Once a participant has received security credentials from
the **Onboarding** component, they install the credentials into their
own **IAA** component (**5**). Once installed, the **IAA** component of
all participants is federated, using the **IAA** component of the
governance authority as trust anchor (**6**). In reality,
the **IAA** component is connected to any single component of Simpl-Open
as any interaction with the agent must be authorised and authenticated.
For the sake of keeping the diagram readable, the relations between
the **IAA** component and all the other components are not represented
on the diagram.

The **Vocabulary Management** component implements part of the Metadata
Description building block: it serves to harmonise the vocabularies in
the Data Space, by providing the definition of metadata representation
and, if required, the data representation standards.

The governance authority defines the vocabularies through the **Vocabulary Management** component (**7**).

The governance authority defines the schemas through the **Schema Management** component (**8**).

The **Schema Management** component implements another part of the
Metadata Description building block: it provides the functionalities
to define the ontologies and schema of the resource description (i.e.
what properties can/should be part of it, what are their types,
constraints and vocabulary).

The **Resource Offering Editor** component implements the last part of
the Metadata Description building block. It provides the functionalities
to create and sign resource descriptions (in the form of
Self-Descriptions). It remains up to date with current metadata
description standards by fetching schemas and vocabularies from the
**Schema Management** and **Vocabulary Management** components (**9**).

The **Federated** **Catalogue** component implements the Resource
Catalogue building block and part of the Search Engine building block.
It provides the functionalities for providers to publish their resources
and for consumer to discover these resources.

The **Search** component implements the remaining part of the Search
Engine building block. It provides the functionalities for consumers to
query and filter catalogue items to find the most suitable resources.

The **Data Space Connector** implements part of the Resource Catalogue,
Usage Contract, Data Orchestration and Simple Data Transfer building
blocks. It provides an implementation of the Data Space Protocol and
acts as an orchestrator between its 3 parts:

1.  Local Assets Catalogue in which the providers register the
    information, related to their own published resources, that is
    required for supporting the contract negotiation and transfer
    process;

2.  Contract Negotiation provides the electronic contract negotiation
    required for consuming any type of resources;

3.  Transfer Process supports the triggering of the data transfer or
    deployment of other types of resources.

Providers (data/application/infrastructure) create and sign resource
description in the **Resource Offering Editor** component (**10**) and
can then register it in the Local Assets Catalogue of their respective
**Data Space Connector** component (**11**). The data registered in the
Local Assets Catalogue of the **Data Space Connector** is the minimal
subset of metadata required to enable the 2 next parts of the DSP:
contract negotiation and transfer process.

Once registered locally, the Resource Offering Editor can publish the
entire resource description (in the form of a Self-Description) to the
**Federated** **Catalogue** component (**12**).

The **Federated Catalogue** validates the submitted
resource descriptions against the schemas and ontologies provided by the
**Schema Management** component (**13**) and against the vocabularies
provided by the **Vocabulary Management** component (**14**).

Consumers can browse the resource offerings published in the **Federated
Catalogue** through the **Search** component (**15**). Instead of having
a search functionality embedded in the **Federated Catalogue**, the
**Search** component is represented as a distinct component of the
consumer agent, connecting to the **Federated Catalogue** in the
governance authority agent (**16**), to enable the 2 tiers approach for
IAA (the consumer end-user connects to the Search component via tier 1
and the Search component connects to the Federated Catalogue via tier
2).

Once consumers have found a resource offering that they would like to
consume, they can request the consumption in the **Search** component
which initiates a contract negotiation with the provider through the
**Data Space Connector** component (**17**). The **Search** component
has obtained from the **Federated Catalogue** the address of the
provider's **Data Space Connector** and the identifier to the resource
offering, and provides these elements to the **Data Space Connector**.
Based on these 2 elements, the consumer's **Data Space Connector**
initiates a contract negotiation with the provider's **Data Space
Connector** (**18**).

Based on the received resource offering identifier, the provider's
**Data Space Connector** can query its Local Assets Catalogue to obtain
the necessary metadata to create a contract (**19**).

The provider's **Data Space Connector** provides the contract to the
consumer's **Data Space Connector** for signature by the consumer
(**20**).

As signing a contract is not explicitly part of the Data Space protocol,
the signature process is not implemented within the Data Space
Connector. Instead, it is externalised to the **Contract Management**
component (**21**).

The **Contract Management** component implements the last part of the
Usage Contract building block. It provides the functionalities to
create, sign and persist usage contracts.

The consumer signs contracts through the **Contract Management**
component (**22**).

Once signed by the consumer, its **Data Space Connector** provides the
contract back to the provider's **Data Space Connector** for the
provider to sign it (**23**). As for the consumer, the signature is
delegated to the **Contract Management** component (**24**) through
which the provider can counter-sign the contract (**25**). The
**Contract Management** component persists the signed contract and
provides a copy to the consumer via their **Data Space Connectors**
(**26**).

The **Contract Management** component of the consumer persists the
signed contract (**27**).

Once a usage contract agreement is established, the **Data Space Connector** 
of the provider can start data and/or infrastructure
consumption.

For standalone infrastructure consumption (see BP 08), the **Data Space Connector** 
of the infrastructure provider triggers the deployment of
the Infrastructure Resource through the **Infrastructure Management**
component (**28**).

The **Infrastructure Management** component implements the
Infrastructure Orchestration, VM Provisioning, Container Provisioning
and Storage Provisioning building blocks. It provides the necessary
features to deploy and configure (incl. policies) infrastructure
resources. It also partly implements the Data Visualisation building
block by providing the functionality to deploy a built-in data
visualisation application on the infrastructure resources. The remaining
part of the Data Visualisation building block is implemented by the
built-in application itself.

The **Infrastructure Management** component deploys and configures the
requested **Infrastructure Resource** (**29**) and provides access
details back to the consumer via the **Data Space Connector** (**30**).

The consumer gets access details from their **Data Space Connector**
(**31**) and can access the **Infrastructure Resource** using these
details (outside of Simpl-Open) (**32**).

For direct data download (see BP 09A), the **Data Space Connector** of
the data provider accesses the **Data Resource** through the **Data
Transfer** component (**33**).

The **Data Transfer** component provides the functionalities to access
various types of data resources and transfer them between participants.
It implements the Data Orchestration and Simple Data Transfer building
blocks. 

The **Data Transfer** component accesses the Data Resource (**34**) and
transfers a copy of it to the consumer via the **Data Space Connector**
(**35**). The consumer's **Data Space Connector** stores the copy of the
**Data Resource** on the consumer side (**36**), which can be accessed
by the consumer (**37**).

For access to data over an application deployed on an infrastructure,
currently, both the data and application resources are already available
in the infrastructure provider and are deployed together with the
infrastructure resource. In a future release, a solution involving the
**Data Space Connectors** of both infrastructure and data providers will
be envisaged.

The **Observability** component implements the Logging building block
and part of the Monitoring building block. It provides the
functionalities to collect and monitor logs and metrics from the other
components of the agent.

In reality, the **Observability** component is connected to any single
component of Simpl-Open as all of them produce logs and are monitored.
For the sake of keeping the diagram readable, the relations between the
**Observability** component and all the other components are not
represented on the diagram.

From the above architecture, 3 functional domains can be distinguished:

1.  **Access Control & Trust** - This domain provides the means to join
    a Data Space and establish trust between participants.

2.  **Publish and consume resources** - This domain is about the essence
    of a Data Space: allow to share resources (datasets, infrastructure,
    applications) between the participants. 

3.  **Management/Operation of Data Space** - This domain provides the
    functionalities that are necessary to manage and operate a Data
    Space.

The table below summarises how the functional components implement the
building blocks from the high-level architecture, and how they map to
the functional domains.

<table>
<thead>
<tr class="header">
<th><strong>Functional architecture component</strong></th>
<th><strong>High-level architecture building block implemented</strong></th>
<th><strong>Functional domain</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Onboarding</td>
<td>Onboarding</td>
<td>Access Control &amp; Trust</td>
</tr>
<tr class="even">
<td>IAA</td>
<td><p>Identity Provider Federation</p>
<p>Authorisation</p>
<p>Security Attribute Provider Federation</p>
<p>Authentication Provider</p>
<p>User Roles</p></td>
<td>Access Control &amp; Trust</td>
</tr>
<tr class="odd">
<td>Vocabulary Management</td>
<td>Metadata Description (partly)</td>
<td>Publish and consumer resources</td>
</tr>
<tr class="even">
<td>Schema Management</td>
<td>Metadata Description (partly)</td>
<td>Publish and consumer resources</td>
</tr>
<tr class="odd">
<td>Resource Offering Editor</td>
<td>Metadata Description (partly)</td>
<td>Publish and consumer resources</td>
</tr>
<tr class="even">
<td>Federated Catalogue</td>
<td><p>Resource Catalogue</p>
<p>Search Engine building block (partly)</p></td>
<td>Publish and consumer resources</td>
</tr>
<tr class="odd">
<td>Search</td>
<td>Search Engine</td>
<td>Publish and consumer resources</td>
</tr>
<tr class="even">
<td>Data Space Connector</td>
<td><p>Resource Catalogue (partly)</p>
<p>Usage Contract (partly)</p>
<p>Data Orchestration (partly)</p>
<p>Simple Data Transfer (partly)</p></td>
<td>Publish and consumer resources</td>
</tr>
<tr class="odd">
<td>Contract Management</td>
<td>Usage Contract (partly)</td>
<td>Publish and consumer resources</td>
</tr>
<tr class="even">
<td>Infrastructure Management </td>
<td><p>Infrastructure Orchestration</p>
<p>VM Provisioning</p>
<p>Container Provisioning</p>
<p>Storage Provisioning</p></td>
<td>Publish and consumer resources</td>
</tr>
<tr class="odd">
<td>Data Transfer</td>
<td><p>Data Orchestration</p>
<p>Simple Data Transfer</p></td>
<td>Publish and consumer resources</td>
</tr>
<tr class="even">
<td>Observability</td>
<td><p>Logging</p>
<p>Monitoring (partly)</p></td>
<td>Management/Operation of Data Space</td>
</tr>
</tbody>
</table>

A mapping between the functional requirements level 2 and the functional
components presented above is provided in annex.

The business processes and the underlying functional requirements are
available from the [Simpl Programme
website](https://simpl-programme.ec.europa.eu/book-page/simpl-requirements).

