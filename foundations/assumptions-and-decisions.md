<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Assumptions and architecture decisions</strong><br/>
</p>
</div>

# Assumptions and architecture decisions

The architectural assumptions and the Architecture Decision Records (ADRs) that constrain the design of Simpl-Open. Every solution in this catalogue inherits these decisions; review this page before proposing a change that contradicts a recorded decision.

## Source

Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **2.11 Assumptions and Architecture Decisions** (lines 2010–2419 of the source, dated 2026-04-20). Upstream link: [FTA spec §2.11](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#211-assumptions-and-architecture-decisions).

---

###  2.11. <a name='AssumptionsandArchitectureDecisions'></a>Assumptions and Architecture Decisions

This information is based on currently available information tailored
for Release 3.0 (December 2025 release) only.

####  2.11.1. <a name='Assumptions'></a>Assumptions

<table>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Topic</strong></th>
<th><strong>Assumptions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ASM-01</td>
<td>Data Space data management (downloading data vs using it)</td>
<td><ol type="1">
<li><p>Infrastructure provider is a mandatory intermediary to enable security of data processing.</p></li>
<li><p>It is the responsibility of the infrastructure provider to setup access control on the provisioned infrastructure tenant for the consumer.</p></li>
<li><p>It is the responsibility of the data provider to setup policy enforcement measures (e.g. restricting download) on the infrastructure tenant for the consumer.</p></li>
<li><p>In the case where data from the data provider is downloaded directly by the consumer (without an infrastructure provider involved), then the "technical enforcement" is replaced by a "legal enforcement".</p></li>
</ol></td>
</tr>
<tr class="even">
<td>ASM-02</td>
<td>Possible data sharing scenarios</td>
<td><p>The following scenarios to share data exist:</p>
<ol type="1">
<li><p>Simple Data Download: <br />
Data Provider is willing to offer the possibility of downloading the dataset to the consumer. <br />
The contract will create some legally binding usage policies. → supported by Simpl-Open.</p></li>
<li><p>The data/app provider offers one, or a bundle of infrastructure instances that host both the data, and the application that can process the data. The consumer still has the possibility of downloading the data, but the contract may prevent it or put limitations/usage policies on it. → currently not in scope (but could be implemented in the future).</p></li>
<li><p>The data/app provider offers a bundle of infrastructure instances that host the data and the application that process the data separately. The access will be provided only to the application (or the infra instance that hosts the application). The consumer cannot access the data, and as part of the contract they shouldn't even try. → supported by Simpl-Open.</p></li>
<li><p>Compute to Data or loading the data in confidential memory enclaves (such as Intel SGX). An advanced version of Scenario 3, with more technical complexities. → currently not in scope (but could be implemented in the future).</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>ASM-03</td>
<td>Actors with multiple participant roles</td>
<td><ol type="1">
<li><p>One agent per participant role (i.e. multiple agents required if a participant plays multiple roles in the Data Space).</p></li>
<li><p>One standard deployment script per type of participant will be provided.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>ASM-04</td>
<td>Distinction between Certificate/Credentials</td>
<td>There is a clear distinction between credentials for securing the Data Space (Tier 1 and 2 IAA) and the credentials for signing SDs and contracts (legally binding signature).</td>
</tr>
<tr class="odd">
<td>ASM-05</td>
<td>Data sharing connector</td>
<td><ol type="1">
<li><p>A connector agnostic "Asset Manager" will be developed, which can access different storage types and handle the data transfer. Currently, existing plugins of the EDC connector are used (such as the S3 object storage extension, that can handle access management and data transfer, in case of contracting). The asset manager will be a module of the agents. </p></li>
<li><p>The combination of the connector (any) and the asset manager will be a part of the agents, for example the consumer and the provider agent. </p></li>
</ol></td>
</tr>
<tr class="even">
<td>ASM-06</td>
<td>Contract signature</td>
<td>Currently, only a simple signature is used (not a legally valid one).</td>
</tr>
<tr class="odd">
<td>ASM-07</td>
<td>Usage of a Data Space connector</td>
<td><p>Any communication/transfer between agents will be done via Data Space connectors. They are responsible to implement the 3 aspects of the Data Space Protocol (DSP):</p>
<ol type="1">
<li><p>registering and requesting service offerings in/from the catalogue;</p></li>
<li><p>negotiation of a contract;</p></li>
<li><p>enabling consumption of service offerings.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>ASM-08</td>
<td>Storage attached to VMs and containers</td>
<td>It is assumed that VMs and containers always have an attached storage.</td>
</tr>
<tr class="odd">
<td>ASM-09</td>
<td>Type of storage supported</td>
<td>It is assumed that Simpl-Open only supports natively S3-compliant storage but is extensible to support other storages (offering an API).</td>
</tr>
<tr class="even">
<td>ASM-10</td>
<td>Deployment and termination of built-in applications</td>
<td>It is assumed that the application is always deployed and terminated together with the infrastructure resource as part of deployment script.</td>
</tr>
<tr class="odd">
<td>ASM-11</td>
<td>Type of built-in application deployment supported</td>
<td>It is assumed that Simpl-Open only supports natively applications deployed on Kubernetes but is extensible to support other platforms (offering an API).</td>
</tr>
<tr class="even">
<td>ASM-12</td>
<td>Supported infrastructure resources</td>
<td><ul>
<li><p>It is assumed that Simpl-Open only supports natively:</p>
<ul>
<li><p>S3-compliant storage</p></li>
<li><p>Kubernetes containers platform</p></li>
<li><p>VMWare virtual machines</p></li>
</ul></li>
</ul>
<p>but is extensible to support other platforms (offering an API).</p></td>
</tr>
</tbody>
</table>

####  2.11.2. <a name='ArchitectureDecisionsRecordADR'></a>Architecture Decisions Record (ADR)

<table>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Title</strong></th>
<th><strong>Context</strong></th>
<th><strong>Decision</strong></th>
<th><strong>Consequence</strong></th>
<th><strong>Date</strong></th>
<th><strong>Decision Maker</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADR-01</td>
<td>API Guidelines</td>
<td>One of the base principles of Simpl is interoperability, and in this respect, REST API guidelines should be established.</td>
<td><p>The decision is to use :</p>
<ul>
<li><p>the <a href="https://www.belgif.be/specification/rest/api-guide/">BelgIF API Guidelines</a> but be pragmatic about it and only address the most important guidelines which have been documented in the APIs section of this document.</p>
<ul>
<li><p>these guidelines are compliant with the European Interoperability Framework (EIF), which promotes Interoperability (one of the core Simpl-Open principles).</p></li>
</ul></li>
<li><p><a href="https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html">OWASP Security cheat sheet</a> and the <a href="https://owasp.org/www-project-api-security/">OWASP API Security project</a></p>
<ul>
<li><p>these additional guidelines will promote Security (another of the core Simpl-Open principles).</p></li>
</ul></li>
<li><p>OpenAPI definitions are stored in GitLab in yaml format.</p></li>
</ul></td>
<td>The guidelines should be implemented for each custom-built component in Simpl-Open.</td>
<td>29 Nov 2024 </td>
<td>DG Connect</td>
</tr>
<tr class="even">
<td>ADR-02</td>
<td>PostgreSQL Deployment Model</td>
<td><p>The different patterns to persist data in the Simpl-Open microservices architecture are:</p>
<ol type="1">
<li><p>a (database) cluster per service</p></li>
<li><p>a database per service (co-hosted on the same database cluster)</p></li>
<li><p>a shared database (with schema or table per service)</p></li>
</ol>
<p>Option 3 has not be further analysed as it creates tight coupling between services and goes against the architecture principles of Simpl-Open.</p></td>
<td><p>The decision is to select option 2 (a database per service) as default option for the development of Simpl-Open.</p>
<p>Note: this decision does not prevent the final data space user to change the deployment model that best fits its interests.</p></td>
<td><p><strong>Pros</strong></p>
<ul>
<li><p>Fault tolerance at node level (loss of a pod is compensated by its replicas);</p></li>
<li><p>Logical data segregation between services;</p></li>
<li><p>Less operational complexity;</p></li>
<li><p>More optimal resource allocation;</p></li>
<li><p>Less expensive;</p></li>
<li><p>Provide loose coupling;</p></li>
<li><p>Provide modularity;</p></li>
<li><p>Allow horizontal scalability.</p></li>
</ul>
<p><strong>Cons</strong></p>
<ul>
<li><p>No fault tolerance at cluster level (lost of the entire StatefulSet impacts all services);</p></li>
<li><p>No physical data segregation between services.</p></li>
</ul></td>
<td>23 Jan 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="odd">
<td>ADR-03</td>
<td>Notification service</td>
<td><p>In certain cases, notifications need to be sent to end-users. E.g. when an onboarding request is created, a notary of the GA should be notified.</p>
<p>It is important to distinguish notifications from asynchronous call-backs.</p>
<p>For notifications, the Simpl-Open custom-built components need a way to generate events.</p>
<p>Assumption: in data spaces the likelihood of asynchronous processing is high due to the federated nature.</p>
<p>Following options have been considered:</p>
<ol type="1">
<li><p><strong>independent and synchronous notification microservice</strong>: In this option, a new independent microservice is built and is triggered synchronously over a REST API.</p></li>
<li><p><strong>independent and asynchronous notification microservice</strong>: In this option, a new independent microservice is built and is reacting asynchronously on messages posted on Kafka.</p></li>
<li><p><strong>notification java library</strong>: In this option, a reusable java library so sends notifications which can be integrated into any application component that needs it. The library should encapsulate the logic for sending notifications and should be injectable as a dependency into other java applications (same model as the one built for the Log4J wrapper).</p></li>
</ol></td>
<td>The decision is to select option 2 (independent and asynchronous notification microservice).</td>
<td><p><strong>Pros</strong></p>
<ul>
<li><p>Fault tolerant by default (message-driven);</p></li>
<li><p>Operational complexity: centralised configuration and credentials management.</p></li>
<li><p>Provide loose coupling;</p></li>
<li><p>Provide modularity;</p></li>
<li><p>Allow horizontal scalability.</p></li>
</ul>
<p><strong>Cons</strong></p>
<ul>
<li><p>Operational complexity: an additional microservice to maintain;</p></li>
<li><p>Interoperability: Kafka producer required to integrate (less standard).</p></li>
</ul></td>
<td>23 Jan 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="even">
<td>ADR-04</td>
<td>Distributed tracing</td>
<td><p>Operating a complex, distributed system like Simpl-Open, with its federated, modular, and loosely coupled architecture, requires deep visibility into how requests travel across its many independent components providing engineers with clear optics into existing flows. This enhanced visibility is enabling teams to rapidly spot bottlenecks, pinpoint errors, and diagnose performance degradation much faster than would otherwise be possible by using a standard logs. Ultimately, effective tracing aims to provide a unified, 360-degree view of all interacting components, consolidated within a single dashboard, improving observability and troubleshooting efficiency across the entire system.</p>
<p>A need for tracing comes from the real-engineering pain-point experienced by a team in Simpl-Open project.</p>
<p>Below are options that were considered for implementation of Tracing in Simpl-Open. All presented options take advantage of modular and resilient architecture of Simpl-Open ensuring Tracing scalability and interoperability:</p>
<ol type="1">
<li><p><strong>In-house implementation of Tracing library: </strong>Implement a library that would provide all necessary elements to effectively collect telemetry data from agents and sent it to Kibana for visualization.</p></li>
<li><p><strong>Integrate OpenTelemetry with Elastic though Elastic Distributions of OpenTelemetry (<a href="https://github.com/elastic/opentelemetry">EDOT</a>) extension: </strong>Elastic integrates with OpenTelemetry, allowing to reuse your existing instrumentation to easily send observability data to the Elastic Stack.</p></li>
<li><p><strong>Integrate Open Telemetry with ELK though Kafka</strong></p></li>
<li><p><strong>Integrate Open Telemetry with ELK though log collector:</strong> Use the OpenTelemetry <a href="https://opentelemetry.io/docs/collector/deployment/agent/">agent</a> together with OpenTelemetry <a href="https://opentelemetry.io/docs/collector/">collector</a> on edge machines to send traces to <a href="https://www.elastic.co/observability/application-performance-monitoring">APM</a> (an existing, free feature in Elastic stack). Traces will be displayed in preconfigured dashboard in Kibana.</p></li>
</ol></td>
<td>The decision is to select option 3 (Integrate Open Telemetry with ELK though log collector).</td>
<td><p><strong>Pros:</strong></p>
<ul>
<li><p>Decoupling of components.</p></li>
<li><p>Scalability.</p></li>
<li><p>Ability to enrich logs on a collector level.</p></li>
<li><p>Production ready.</p></li>
<li><p>Minimal engineering effort if using <a href="https://opentelemetry.io/docs/languages/java/getting-started/#instrumentation">instrumentation</a>. </p></li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
<li><p>Increased system complexity.</p></li>
<li><p>More resource consumption on the edge machine.</p></li>
</ul></td>
<td>17 Apr 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="odd">
<td>ADR-05</td>
<td>Access control inside Simpl-Open Agent</td>
<td><p>Tier 1 communication with Simpl-Open microservices is protected by an API gateway that validates JWT tokens at the edge. The assumption has been that internal communication cannot be accessed by an attacker, so no internal service-to-service traffic security is in place.</p>
<p>However, this model does not align with the<strong> </strong>Zero Trust approach, which assumes that threats may exist within the internal network. To follow this Zero Trust approach, Simpl-Open need to ensure that all service-to-service (east-west) communication is authenticated and authorized, preventing unauthorized access even within the internal network.</p>
<p>Below are options that were considered:</p>
<ol type="1">
<li><p><strong>Microservices to validate OAuth2 JWT roles and scopes: </strong> Tier1 Gateway forwards the User JWT token to agent Microservices (user-facing APIs)<strong>. </strong>Microservices must implement <strong>Role-Based Access Control (RBAC)</strong>, introducing an additional layer of verification beyond the existing Tier 1 RBAC enforcement. Service-to-Service communication must be enforced as follows: each microservice needing to communicate internally will obtain an OAuth2 JWT Access token from Keycloak using Client Credentials Grant. This token contains a list of the <strong>scopes </strong>that indicate the resource and the action the microservice can perform within the agent. The token is transmitted to the target microservice to authenticate the request and enforce access control based on the token’s claims. Scopes can follow a resource-action format (e.g., participant:create, identityattributes:read) to provide fine-grained <strong>Scope Based Access Control (SBAC)</strong>.</p></li>
<li><p><strong>Service mesh (Istio): </strong>Every POD in the Kubernetes (K8s) namespace will be paired with a sidecar container and is part of <em>mesh</em>. Istio can be used to enforce mTLS for secure service-to-service communication. Role and Scope based access control can be enforced using Istio.</p></li>
<li><p><strong>Internal Communication only through the Tier 1 gateway:</strong></p>
<ol type="1">
<li><p><strong>User-Facing APIs:</strong> the Tier1 gateway <strong>must</strong> enforce RBAC policies and forward the request to the agent components. No access control must be implemented in the microservice.</p></li>
<li><p><strong>Service-to-Service Communication:</strong> Each microservice needing to communicate internally will obtain an OAuth2 JWT Access token from Keycloak using Client Credentials Grant. This token contains a list of the <strong>scopes </strong>that indicate the resource and the action that the microservice is allowed to perform within the agent. The token is transmitted to the gateway. The gateway validates the request and enforces access control based on the token’s claims. If the access control and token validity evaluation are successful, the gateway forwards the request to the target microservice. No access control must be implemented in the microservice.</p></li>
</ol></li>
<li><p><strong>Mutual TLS (mTLS) for Service-to-Service Authentication:</strong> Every component will be provided with a private key and a certificate, enabling it to authenticate and encrypt communications using Mutual TLS (mTLS) for secure service-to-service interactions within the system.</p></li>
<li><p><strong>Microservices to validate OAuth2 JWT roles and scopes with optional Istio service mesh: </strong>Tier1 Gateway forwards the User JWT token to agent Microservices (user-facing APIs)<strong>. </strong>Microservices must implement <strong>Role-Based Access Control (RBAC)</strong>, introducing an additional layer of verification beyond the existing Tier 1 RBAC enforcement.<br />
Service-to-Service communication must be enforced as follows: each microservice needing to communicate internally will obtain an OAuth2 JWT Access token from Keycloak using Client Credentials Grant. This token contains a list of the <strong>scopes </strong>that indicate the resource and the action the microservice can perform within the agent. The token is transmitted to the target microservice to authenticate the request and enforce access control based on the token’s claims. Scopes can follow a resource-action format (e.g., participant:create, identityattributes:read) to provide fine-grained <strong>Scope Based Access Control</strong>.<br />
Optionally, every POD in the Kubernetes (K8s) namespace will be paired with a sidecar container and is part of <em>mesh</em>. Istio can be used to enforce mTLS for secure service-to-service communication.</p></li>
</ol></td>
<td>The decision is to select option 5 (Microservices to validate OAuth2 JWT roles and scopes with optional Istio service mesh).</td>
<td><p><strong>Pros:</strong></p>
<ul>
<li><p>Provides Authorization capabilities via Roles and Scopes</p></li>
<li><p>well-supported standard supported by web frameworks</p></li>
<li><p>granular authorization via OAuth2 scopes and roles</p></li>
<li><p>uses existing Simpl Authentication provider (Keycloak)</p></li>
<li><p>without Istio security mesh </p>
<ul>
<li><p>cloud platform agnostic  </p></li>
</ul></li>
<li><p>with Istio security mesh</p>
<ul>
<li><p>Includes channel encryption (mTLS) </p></li>
<li><p>Can enforce additional security policies and manage traffic for open-source components outside our direct control.</p></li>
</ul></li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
<li><p>Increased operational complexity due to OAuth2 token management.</p></li>
<li><p>Need for well-defined scope and role management to prevent over-provisioning of access rights.</p></li>
<li><p>requires implementation on both client and server side</p></li>
<li><p>without Istio security mesh</p>
<ul>
<li><p>Cannot enforce security policies and manage traffic for open-source components outside our direct control (Option 2 or 3 to be considered)</p></li>
</ul></li>
<li><p>with Istio security mesh</p>
<ul>
<li><p>not technology agnostic, works only on Kubernetes,</p></li>
<li><p>Increased technology portfolio</p></li>
<li><p>Resource overhead</p></li>
</ul></li>
</ul></td>
<td>15 May 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="even">
<td>ADR-06</td>
<td>Healthchecks monitoring</td>
<td><p>To monitor the health of Simpl-Open components, a healthcheck mechanism should be implemented.</p>
<p>Below are options that were considered:</p>
<ol type="1">
<li><p><strong>Direct HTTP Push to Log Store:</strong> Each Simple-Open service independently sends its health status directly to a dedicated HTTP endpoint on the Elastic Stack (e.g., a Logstash HTTP input or an Elasticsearch Ingest Node). This is a "<em>push</em>" model where the service initiates the communication. Collected health data is persisted directly in Elasticsearch and visualized in Kibana.</p></li>
<li><p><strong>Elastic Heartbeat to probe for services health:</strong> A Heartbeat component from Elastic, on a predefined schedule, check a status of each of registered service by sending HTTP call. Collected health data is persisted directly in Elastic and visualised in Kibana.</p></li>
<li><p><strong>Enhance Probing with Spring Boot Actuator: </strong>This option builds on the "pull" model from Option 2 by requiring services to use the <strong>Spring Boot Actuator</strong> library. The Actuator exposes a detailed, standardized health endpoint (e.g., /health). A probing tool like Elastic Heartbeat is then configured to poll this specific endpoint. This hybrid approach combines the active probing of Heartbeat with the rich, internal context provided by the Actuator.</p></li>
<li><p><strong>Elastic Heartbeat to probe for services health and pushes it to Kafka:</strong> A Heartbeat component pull health status for predefined list of services via HTTP and pushes data to Kafka. A dedicated Logstash pipeline is configured to read data from a predefined Kafka topic and put it in Elastic for visualization in Kibana.</p></li>
</ol></td>
<td>The decision is to select option 3 (Enhance Probing with Spring Boot Actuator).</td>
<td><p><strong>Pros:</strong></p>
<ul>
<li><p>Deep, Standardized Health Information: Provides rich, out-of-the-box details on the status of dependencies needed for a Simple service to execute on business process.</p></li>
<li><p>Actionable Business-Level Monitoring: Enables the creation of custom health checks tied to critical business processes, providing much more meaningful alerts than a simple uptime check.</p></li>
<li><p>Minimal Implementation Effort: Adding the Actuator is a simple dependency addition in a Spring Boot application. The framework handles the rest (example below).</p></li>
<li><p>Combines Best of Both Worlds: Gets the reliable active probing and Kibana integration from Heartbeat (Option 1) while solving its "<em>Limited Scope</em>" problem by providing deep application insights and readiness to execute on Simple-Open business logic.</p></li>
<li><p>Fully Controllable: Actuator endpoints can be configured to meet a service dependencies and exposed.</p></li>
<li><p>Predefined Implementation: Spring Boot offers predefined set of actuators (<a href="https://docs.spring.io/spring-boot/docs/2.5.6/reference/html/actuator.html#actuator.endpoints">Spring Boot Actuator: Production-ready Features</a>) making is easy for each service to enable only sub-set of actuators best suited for their use cases.</p></li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
<li><p>Minor Service-Side Responsibility: Service owners are responsible for including the spring-boot-starter-actuator dependency and creating custom health indicators where necessary. Effort is not centralized.</p></li>
<li><p>Security Requirement: Exposing detailed health information requires careful security configuration to ensure the endpoints are not publicly accessible. Each service must only enable desired set of actuators.</p></li>
</ul></td>
<td>10 Jul 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="odd">
<td>ADR-07</td>
<td>Terraform Provisioning</td>
<td>As OVH does not have an official Crossplane plugin and the existent one, does not support the provisioning of Virtual Machines, a research was done in order to use Terraform instead.</td>
<td><p>It was confirmed that using an OVH Token, the Infrastructure Provisioner can deploy a Virtual Machine in a similar fashion when compared to the IONOS flow. The changes required related to the Infrastructure Provisioner will be done on the definition of the resource template and on the ArgoCD part. </p>
<p>The chosen technology to support the creation of Virtual Machines using Terraform language is <a href="https://opentofu.org/">OpenTofu</a>. Being a fully open-source solution, community-driven alternative to Terraform, ensuring long-term flexibility, transparency, and independence from proprietary licensing changes, it maintains full compatibility with existing Terraform configurations and supports new infrastructure-as-code configurations through full compatibility with the Terraform environment.</p></td>
<td>The Architecture related to the “BP08” will not have any changes, only the Technology View.</td>
<td>28 May 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="even">
<td>ADR-08</td>
<td>Signer service eIDAS compliance</td>
<td><p>The OCM signer service provides a cryptographic function that binds the organization's identity to the claims within a Verifiable Credential, making it trustworthy and verifiable in a digital environment.</p>
<p>While the OCM performs a digital signature that provides integrity and links the VC to the issuing organization, this process, by default, does not include the eIDAS requirements to achieve the legal equivalence of a handwritten signature (Qualified Electronic Signature).<br />
Requirements such as stringent identity verification, certified hardware/software, and accredited certificate issuance required by eIDAS.</p>
<p>Some data spaces may require achieving the legal equivalence of a handwritten signature (QES) for certain scenarios (e.g. establishing a contract). The EU Digital Signature Service (DSS) offers exactly that by  facilitating the creation and validation of electronic signatures in line with eIDAS regulations. </p>
<p>Unlike the general OCM signer service which focuses on the cryptographic binding for VC integrity, DSS is specifically designed to help implement signing processes that adhere to the legal and technical requirements defined by eIDAS, including working with qualified certificates and signature creation devices when needed to achieve the highest levels of assurance and legal recognition within the European Union. </p>
<p>Below are options that were considered:</p>
<ol type="1">
<li><p><strong>Standalone Service</strong></p></li>
<li><p><strong>Embedded Library</strong></p></li>
</ol></td>
<td>The decision is to select option 1 (Standalone service).</td>
<td><ul>
<li><p><strong>Pros:</strong></p>
<ul>
<li><p><strong>Centralized Access:</strong> Offers a single, accessible service for various internal systems and business processes requiring QES.</p></li>
<li><p><strong>Simplified Management:</strong> Centralizes monitoring, maintenance, updates, and auditing of the QES functionality.</p></li>
<li><p><strong>Clear Separation of Concerns:</strong> Keeps the specialized QES logic distinct from other application code, improving modularity.</p></li>
</ul></li>
<li><p><strong>Considerations:</strong></p>
<ul>
<li><p>Potential for network latency (though often negligible for signing operations).</p></li>
<li><p>Requires dedicated deployment and operational management.</p></li>
</ul></li>
</ul></td>
<td>26 Jun 2025 </td>
<td>DG Connect</td>
</tr>
<tr class="odd">
<td>ADR-09</td>
<td>Infrastructure Consumption Monitoring</td>
<td><p><strong>Key architectural considerations:</strong></p>
<ol type="1">
<li><p>Infrastructure Consumption Monitoring component needs to monitor various type of metrics for different cloud resources including but not limited to: compute (VMs), storage (S3), etc.</p></li>
<li><p>Abstraction layer needs to exist to ensure different type of cloud providers can be integrated. Default implementation must exist for OVH.</p></li>
<li><p>Pull method must be used to extract infrastructure consumption data though APIs from a cloud provider on a configurable schedule (as per #1).</p></li>
<li><p>Information about cloud resources to pull consumption data from come, directly or indirectly, from infrastructure logs in ELK.</p></li>
<li><p>Infrastructure consumption data are transformed into a standard JSON format (same format for all cloud providers) and persisted in a dedicated index in ELK along with infrastructure provider reference.</p></li>
<li><p>Infrastructure consumption monitoring component accesses cloud provider APIs by using secrets (certificates, API keys, etc) stored in ELK (<a href="https://www.elastic.co/guide/en/logstash/current/keystore.html">Secrets keystore for secure settings | Logstash Reference [8.17] | Elastic</a>) or a different, dedicated store.</p></li>
</ol>
<p><strong>Other useful aspects:</strong></p>
<ol type="1">
<li><p>The cloud providers (i.e. OVH) expose dedicated endpoints to get consumption data. Example here: <a href="https://eu.api.ovh.com/console/?section=%2Fcloud&amp;branch=v1#get-/cloud/project/-serviceName-/consumption">OVHcloud API</a>. </p></li>
<li><p>Consumption data is per Service (aka cloud resource).</p></li>
<li><p>Total consumption is often a sum of various sub-offering for a service. For example for a cloud hosting it's would be: instances + storage + snapshots. </p></li>
<li><p>Consumption comes in a form of currency spent per unit.</p></li>
</ol>
<p>Below are options that were considered:</p>
<ol type="1">
<li><p>Use open-source collector agent (i.e. <a href="https://opentelemetry.io/docs/collector/">OpenTelemetry</a> or <a href="https://logz.io/learn/complete-guide-elk-stack/#beats">The Complete Guide to the ELK Stack | Logz.io</a>) directly on the cloud resources.</p></li>
<li><p>Invocation of a hosted script/program through a Logstash plugin to load infrastructure consumption data as part of Logstash processing pipeline.</p></li>
<li><p>A dedicated microservice which gets invoked for a specific cloud resource based on signals stored in a message queue.</p></li>
</ol></td>
<td>The decision is to select option 3 (dedicated microservice).</td>
<td><p><strong>Pros</strong>:</p>
<ul>
<li><p>Full control over the code and functionalities.</p></li>
<li><p>Fully testable with emphasis on shift-to-left/fail-fast.</p></li>
<li><p>Resiliency and high availability achieved by design.</p></li>
<li><p>Abstraction layer for different cloud providers achieved at interfaces layer.</p></li>
<li><p>Secrets management for accessing APIs removed from ELK - separation of concerns.</p></li>
<li><p>Adding support for new cloud providers defined by a set of interfaces to implement.</p></li>
<li><p>Aligned with a principal of separation of concerns. Follows a <a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers">Competing Consumer</a>s cloud pattern for scalability and resiliency. </p></li>
<li><p>Scheduled on demand (i.e. though ELK).</p></li>
<li><p>Not invasive, pull based approach.</p></li>
<li><p>Can be implemented as sync or async solution (design choice depending if a Kafka is needed).</p></li>
<li><p>Less networking configuration needed - each agent only checks consumption of resource it uses.</p></li>
</ul>
<p><strong>Cons</strong>:</p>
<ul>
<li><p>Needs to be fully coded so it will take time.</p></li>
</ul></td>
<td>10 Jul 2025 </td>
<td>DG Connect</td>
</tr>
</tbody>
</table>

