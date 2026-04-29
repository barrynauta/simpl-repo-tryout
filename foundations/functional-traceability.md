<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Functional traceability</strong><br/>
</p>
</div>

# Functional traceability

The end-to-end mapping from functional requirements to the components that implement them. Two FTA sections describe this mapping at different levels of detail: §4.6 is the architecture-level traceability statement (which architectural components address which requirements), and §9.1 (Annex 1) is the requirement-by-requirement table. Both are reproduced below; treat the §9.1 annex as authoritative and §4.6 as commentary.

## Architectural traceability — FTA §4.6

> Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, lines 6360–6475 (source dated 2026-04-20). Upstream link: [FTA spec §4.6](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#46-traceability-from-the-functional-architecture).

###  4.6. <a name='Traceabilityfromthefunctionalarchitecture'></a>Traceability from the functional architecture

The following table presents a mapping between the components from the
functional architecture and the ones from the application architecture.

<table>
<thead>
<tr class="header">
<th><strong>Functional Component</strong></th>
<th><strong>Application Component</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Onboarding</td>
<td>Onboarding</td>
</tr>
<tr class="even">
<td>IAA</td>
<td>Authorisation</td>
</tr>
<tr class="odd">
<td></td>
<td>Tier 1 Authentication Provider</td>
</tr>
<tr class="even">
<td></td>
<td>Tier 2 Authentication Provider</td>
</tr>
<tr class="odd">
<td></td>
<td>Identity Provider</td>
</tr>
<tr class="even">
<td></td>
<td>Security Attributes Provider</td>
</tr>
<tr class="odd">
<td></td>
<td>User &amp; Roles</td>
</tr>
<tr class="even">
<td></td>
<td>Credential Database/Vault</td>
</tr>
<tr class="odd">
<td>Vocabulary Management</td>
<td>Vocabulary Management</td>
</tr>
<tr class="even">
<td>Schema Management</td>
<td>Schema Management</td>
</tr>
<tr class="odd">
<td></td>
<td>Schema Registry</td>
</tr>
<tr class="even">
<td>Service Offering Editor</td>
<td>SD Tooling</td>
</tr>
<tr class="odd">
<td></td>
<td>Signer Service</td>
</tr>
<tr class="even">
<td></td>
<td>Wallet</td>
</tr>
<tr class="odd">
<td></td>
<td>Policy Template Datastore</td>
</tr>
<tr class="even">
<td>Federated Catalogue</td>
<td>Catalogue</td>
</tr>
<tr class="odd">
<td>Search</td>
<td>Catalogue Client Application</td>
</tr>
<tr class="even">
<td>Data Space Connector</td>
<td>Connector</td>
</tr>
<tr class="odd">
<td>Contract Management</td>
<td>Contract Manager Orchestrator</td>
</tr>
<tr class="even">
<td></td>
<td>Contract Manager Backend</td>
</tr>
<tr class="odd">
<td></td>
<td>Contract Template Datastore</td>
</tr>
<tr class="even">
<td>Data Transfer</td>
<td>Connector</td>
</tr>
<tr class="odd">
<td>Infrastructure Management</td>
<td>Triggering Module</td>
</tr>
<tr class="even">
<td></td>
<td>Infrastructure Provisioner</td>
</tr>
<tr class="odd">
<td>Observability</td>
<td>Monitoring Module</td>
</tr>
</tbody>
</table>


---

## Annex 1 — Mapping between functional requirements and components — FTA §9.1

> Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, lines 18108 to end-of-document (source dated 2026-04-20). Upstream link: [FTA spec §9.1](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#91-annex-1---mapping-between-functional-requirements-and-components).

##  9. <a name='Annexes'></a>Annexes

###  9.1. <a name='Annex1-Mappingbetweenfunctionalrequirementsandcomponents'></a>Annex 1 - Mapping between functional requirements and components

While L2 requirements are mapped to functional requirements through the
use of components in Jira, the table below provides an extract from this
mapping.

<table>
<thead>
<tr class="header">
<th>Requirement ID</th>
<th>Summary</th>
<th>Component/s</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SIMPL-402</td>
<td>Create usage policy</td>
<td>Resource Offering Editor</td>
</tr>
<tr class="even">
<td>SIMPL-409</td>
<td>Assign usage policy</td>
<td>Resource Offering Editor</td>
</tr>
<tr class="odd">
<td>SIMPL-415</td>
<td>Enforce usage policies</td>
<td>Contract Management, Data Space Connector</td>
</tr>
<tr class="even">
<td>SIMPL-469</td>
<td>Quick Search</td>
<td>Federated Catalogue, Search</td>
</tr>
<tr class="odd">
<td>SIMPL-500</td>
<td>Semantic Validation</td>
<td>Federated Catalogue, Vocabulary Management</td>
</tr>
<tr class="even">
<td>SIMPL-503</td>
<td>Access policy publication</td>
<td>Resource Offering Editor</td>
</tr>
<tr class="odd">
<td>SIMPL-514</td>
<td>Assign Contract Template</td>
<td>Contract Management, Resource Offering Editor</td>
</tr>
<tr class="even">
<td>SIMPL-1610</td>
<td>Defining preconfigured attributes</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1612</td>
<td>Tier 2 identity attributes configuration</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1613</td>
<td>Tier 2 attributes management - services</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1616</td>
<td>Authentication between participant agents</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1619</td>
<td>Handling different versions of application</td>
<td>Federated Catalogue, Resource Offering Editor</td>
</tr>
<tr class="odd">
<td>SIMPL-1629</td>
<td>Unified Orchestration Mechanism</td>
<td>Infrastructure Management</td>
</tr>
<tr class="even">
<td>SIMPL-1630</td>
<td>Cross-Platform Service Management</td>
<td>Infrastructure Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1655</td>
<td>Participant offboard operations</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1658</td>
<td>Implement monitoring actions</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-1672</td>
<td>View the onboarding process documentation and initiate the onboarding</td>
<td>Onboarding</td>
</tr>
<tr class="even">
<td>SIMPL-1673</td>
<td>Register onboarding application</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-1674</td>
<td>Onboarding request - tracking by applicant</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1675</td>
<td>Onboarding requests - automated tracking and monitoring</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-1676</td>
<td>Onboarding requests - verification support</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1677</td>
<td>Onboarding requests - manual approval support</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1679</td>
<td>Onboarding requests - rejection support</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1681</td>
<td>Attribute selection</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1682</td>
<td>Create credential request</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1683</td>
<td>Credential creation</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1684</td>
<td>Credential request - tracking by participant</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1685</td>
<td>Credential request - notification of completion</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-1686</td>
<td>Credentials installation and review - services</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1687</td>
<td>Credentials installation and review - status and information</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1688</td>
<td>Credentials installation and review - identity attributes check</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1689</td>
<td>Users and roles configuration</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1696</td>
<td>Mandatory quality rules</td>
<td>Federated Catalogue</td>
</tr>
<tr class="even">
<td>SIMPL-1698</td>
<td>Validation of a resource description - feedback to the provider</td>
<td>Federated Catalogue, Schema Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1699</td>
<td>Syntax Validation</td>
<td>Federated Catalogue, Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-1704</td>
<td>Creating a resource description</td>
<td>Resource Offering Editor</td>
</tr>
<tr class="odd">
<td>SIMPL-1705</td>
<td>Uploading a resource description</td>
<td>Federated Catalogue, Resource Offering Editor</td>
</tr>
<tr class="even">
<td>SIMPL-1715</td>
<td>Access policy definition</td>
<td>Resource Offering Editor</td>
</tr>
<tr class="odd">
<td>SIMPL-1719</td>
<td>Advanced Search</td>
<td>Federated Catalogue, Search</td>
</tr>
<tr class="even">
<td>SIMPL-1728</td>
<td>Attributes of a self-description for a dataset</td>
<td>Federated Catalogue</td>
</tr>
<tr class="odd">
<td>SIMPL-1729</td>
<td>Attributes of a self-description for an application</td>
<td>Federated Catalogue</td>
</tr>
<tr class="even">
<td>SIMPL-1730</td>
<td>Support for sharing across the Federated Dataspace</td>
<td>Federated Catalogue</td>
</tr>
<tr class="odd">
<td>SIMPL-1731</td>
<td>Adding a vocabulary</td>
<td>Vocabulary Management</td>
</tr>
<tr class="even">
<td>SIMPL-1734</td>
<td>Advance search - Search parameters compliant with constraints and vocabularies</td>
<td>Schema Management, Vocabulary Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1739</td>
<td>Triggering Mechanism</td>
<td>Data Space Connector, Infrastructure Management</td>
</tr>
<tr class="even">
<td>SIMPL-1740</td>
<td>data space IAA Tier 2 customization</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1741</td>
<td>End user authentication process - services</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1743</td>
<td>Identity provider federation initialisation</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1744</td>
<td>Ensure RBAC compliance</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1745</td>
<td>Roles management operations</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1746</td>
<td>Identity provider federation configuration</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1747</td>
<td>Identity provider federation APIs</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-1748</td>
<td>End user authentication process - api</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-1749</td>
<td>Adding attributes of a self-description for a dataset/application/infrastructure</td>
<td>Federated Catalogue, Vocabulary Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1751</td>
<td>Update vocabulary</td>
<td>Vocabulary Management</td>
</tr>
<tr class="even">
<td>SIMPL-1752</td>
<td>Remove vocabulary</td>
<td>Vocabulary Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1753</td>
<td>Updating attributes of a self-description for a dataset/application/infrastructure</td>
<td>Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-1754</td>
<td>Selecting shared entries</td>
<td>Federated Catalogue</td>
</tr>
<tr class="odd">
<td>SIMPL-1755</td>
<td>Selecting dataspaces for catalogue sharing</td>
<td>Federated Catalogue</td>
</tr>
<tr class="even">
<td>SIMPL-1756</td>
<td>Publishing shared entries to selected dataspace</td>
<td>Federated Catalogue</td>
</tr>
<tr class="odd">
<td>SIMPL-1757</td>
<td>Quality dimension and Quality Rules</td>
<td>Federated Catalogue, Resource Offering Editor</td>
</tr>
<tr class="even">
<td>SIMPL-1758</td>
<td>Calculation of Quality Score</td>
<td>Federated Catalogue</td>
</tr>
<tr class="odd">
<td>SIMPL-1772</td>
<td>Storing results</td>
<td>Search</td>
</tr>
<tr class="even">
<td>SIMPL-1784</td>
<td>Data sharing</td>
<td>Data Space Connector, Data Transfer</td>
</tr>
<tr class="odd">
<td>SIMPL-1787</td>
<td>Duplication of source before applying data processing</td>
<td>Data Transfer</td>
</tr>
<tr class="even">
<td>SIMPL-1788</td>
<td>Template and Policy Engine for VM</td>
<td>Infrastructure Management</td>
</tr>
<tr class="odd">
<td>SIMPL-1789</td>
<td>Integration with Cloud APIs through Crossplane</td>
<td>Infrastructure Management</td>
</tr>
<tr class="even">
<td>SIMPL-2882</td>
<td>Log infrastructure consumption metrics in the provider agent</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2884</td>
<td>Metrics to log during Infrastructure resource consumption</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2889</td>
<td>Monitoring infrastructure consumption</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2894</td>
<td>Simpl shall log metrics when data is transferred through the Simpl-Open agent</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2902</td>
<td>Monitoring data consumption</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2904</td>
<td>Log all the metrics in a central repository per agent</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2906</td>
<td>Logging amount and type of data transferred through Simpl-Open agent</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2907</td>
<td>Logging the reason for transferring data</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2914</td>
<td>Logs and traces compliant with EU regulations and with the rules set for the audit process</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2916</td>
<td>Pre-configured monitoring dashboard</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2917</td>
<td>Participant to configure custom dashboards</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2919</td>
<td>Monitoring Simpl-Open agent software components technical logs</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2921</td>
<td>Monitoring Simpl-Open agent infrastructure metrics</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2924</td>
<td>Healthcheck endpoint for all of application components</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2926</td>
<td>Application healthchecks in the monitoring dashboard</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2929</td>
<td>Send alert when a component is unhealthy</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2930</td>
<td>Store the alerts</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2932</td>
<td>Make all logged information retrievable in real time from a reporting module</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2941</td>
<td>Simpl shall store technical logs of agent (software) components in a log repository</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2945</td>
<td>Store technical logs of the infrastructure on which Simpl-Open is deployed in a log repository</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2946</td>
<td>Log Simpl agent infrastructure metrics</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2949</td>
<td>Simpl shall log all business actions in the central logs repository</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2966</td>
<td>Simpl shall log the usage of data/application resource on a provider's infrastructure by a consumer</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-2969</td>
<td>Simpl shall log all Tier I accesses to the agent</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-2970</td>
<td>Simpl shall log all security events generated by its components</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-3180</td>
<td>Alert thresholds definition</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-3182</td>
<td>Alert triggering</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-3382</td>
<td>The Usage Contract Agreement stored in human readable format</td>
<td>Contract Management</td>
</tr>
<tr class="even">
<td>SIMPL-3835</td>
<td>Monitoring Simpl-Open agent Tier II transactions</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-3886</td>
<td>Monitoring Simpl business logs</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-3995</td>
<td>Define the onboarding process documentation</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-4417</td>
<td>Automated deployment of Simpl-Open pre-configured monitoring dashboard</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-4421</td>
<td>Simpl shall log all Tier II transactions</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-4422</td>
<td>Monitoring Simpl-Open agent infrastructure technical logs</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-4423</td>
<td>Monitoring Simpl-Open agent Tier I accesses</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-4424</td>
<td>Monitoring Simpl-Open agent security events</td>
<td>Observability</td>
</tr>
<tr class="even">
<td>SIMPL-4428</td>
<td>Monitor Simpl agent infrastructure components health</td>
<td>Observability</td>
</tr>
<tr class="odd">
<td>SIMPL-4494</td>
<td>Sorting search results</td>
<td>Search</td>
</tr>
<tr class="even">
<td>SIMPL-4495</td>
<td>Filter search result based on access policy</td>
<td>Federated Catalogue, Search</td>
</tr>
<tr class="odd">
<td>SIMPL-4889</td>
<td>Publishing a resource description</td>
<td>Federated Catalogue, Resource Offering Editor</td>
</tr>
<tr class="even">
<td>SIMPL-5396</td>
<td>Request a data resource</td>
<td>Data Space Connector, Data Transfer</td>
</tr>
<tr class="odd">
<td>SIMPL-6100</td>
<td>Requesting an infrastructure resource</td>
<td>Infrastructure Management</td>
</tr>
<tr class="even">
<td>SIMPL-6109</td>
<td>Access policy enforcement</td>
<td>Data Space Connector</td>
</tr>
<tr class="odd">
<td>SIMPL-6122</td>
<td>Data Visualization</td>
<td>Data Transfer, Infrastructure Management</td>
</tr>
<tr class="even">
<td>SIMPL-10173</td>
<td>Configure a ruleset for the automatic validation of onboarding request documents</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-10174</td>
<td>Define identity attributes for an Onboarding Procedure Template</td>
<td>Onboarding, IAA</td>
</tr>
<tr class="even">
<td>SIMPL-10489</td>
<td>Onboarding request automated document validation</td>
<td>Onboarding</td>
</tr>
<tr class="odd">
<td>SIMPL-10572</td>
<td>Governance Authority - Credentials actions</td>
<td>IAA</td>
</tr>
<tr class="even">
<td>SIMPL-10594</td>
<td>Participant - Credential Renewal and Deployment</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-11315</td>
<td>Governance Authority‚ retrieving schemas and schema versions</td>
<td>Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-11316</td>
<td>Governance Authority‚ creating a new schema for a new resource type</td>
<td>Schema Management</td>
</tr>
<tr class="odd">
<td>SIMPL-11318</td>
<td>Governance Authority‚ creating a new version of an existing schema for a resource type</td>
<td>Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-11320</td>
<td>Governance Authority‚ revoking a schema</td>
<td>Schema Management</td>
</tr>
<tr class="odd">
<td>SIMPL-11321</td>
<td>Governance Authority‚ retaining a revoked schema for existing resource descriptions</td>
<td>Resource Offering Editor, Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-11322</td>
<td>Governance Authority‚ ensuring that a revoked schema is not available for publishing a new resource description</td>
<td>Resource Offering Editor, Schema Management</td>
</tr>
<tr class="odd">
<td>SIMPL-11323</td>
<td>Governance Authority‚ validating a schema‚ syntax, semantics, and default properties</td>
<td>Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-11328</td>
<td>Governance Authority - publishing a validated schema</td>
<td>Schema Management</td>
</tr>
<tr class="odd">
<td>SIMPL-11333</td>
<td>Governance Authority‚ notifying Providers about schema changes</td>
<td>Schema Management</td>
</tr>
<tr class="even">
<td>SIMPL-12197</td>
<td>Governance Authority - Identity attributes assignment to participants</td>
<td>IAA</td>
</tr>
<tr class="odd">
<td>SIMPL-12898</td>
<td>A Provider consults an overview of its Resource descriptions</td>
<td>Federated Catalogue, Search</td>
</tr>
<tr class="even">
<td>SIMPL-12903</td>
<td>A Provider consults the details of one of its own resource descriptions</td>
<td>Federated Catalogue, Search</td>
</tr>
<tr class="odd">
<td>SIMPL-12904</td>
<td>A Provider consults the version history of one of its own resource descriptions</td>
<td>Resource Offering Editor</td>
</tr>
</tbody>
</table>
