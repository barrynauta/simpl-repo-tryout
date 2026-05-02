<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Changelog</strong><br/>
</p>
</div>

# Changes with respect to the previous FTA version

The version-by-version delta of the Functional and Technical Architecture Specification, lifted from FTA §1.3. Useful for reviewers tracking what is new since the last revision.

## Source

Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **1.3 Changes with respect to the previous version** (lines 248–733 of the source, dated 2026-04-20). Upstream link: [FTA spec §1.3](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#13-changes-with-respect-to-the-previous-version).

---

###  1.3. <a name='Changeswithrespecttothepreviousversion'></a>Changes with respect to the previous version

####  1.3.1. <a name='Mar2026'></a>06 Mar 2026

-   Updated *"ACV Static - Data Orchestration Service"* to include the
    auth proxy and made the asset orchestrator part of release.

-   Updated *"TCV Static - Data Orchestration Service"* to include the
    auth proxy and made the asset orchestrator part of release.

####  1.3.2. <a name='Feb2026'></a>13 Feb 2026

-   Updated *"LDM - Domain 1 - Access Control & Trust"* to include the
    Role entity in Users & Roles component.

-   Updated *"PDM - Domain 1 - Access Control & Trust"* to include the
    Role table in Users & Roles component.

-   Updated "*ACV Dynamic - BP 03B – Participant User and Roles
    Configuration*" to include enable/disable functionality 

-   Updated "ACV Dynamic - BP 03C - End User Role Request" to include
    Role Request review functionality in the frontend

####  1.3.3. <a name='Jan2026'></a>23 Jan 2026

-   Update "APIs" to include new Onboarding v2 API and Authentication
    Provider syncronization API

####  1.3.4. <a name='Dec2025'></a>19 Dec 2025

-   Update "ACV Static - Tier 1 Authentication Service" to include the
    external identity provider

-   Update "TCV Static - Tier 1 Authentication Service" to include the
    external identity provider

-   Update "ACV Dynamic - BP 03B – Participant User and Roles
    Configuration" to include users and roles management

-   Update "TCV Dynamic - BP 03B - Participant User and Roles
    Configuration" to include users and roles management

-   Added "ACV Dynamic - BP 03C - End User Role Request" for end user
    role request

-   Added "TCV Dynamic - BP 03C - End User Role Request" for end user
    role request

-   Update "APIs" to include new Onboarding and Users&Roles API
    description

-   Update "CDM - Domain 1 - Onboarding & IAA" to include roles request
    in Users&Roles data model

-   Update "LDM - Domain 1 - Onboarding & IAA" to include roles request
    in Users&Roles data model

-   Update "PDM - Domain 1 - Onboarding & IAA" to include roles request
    in Users&Roles data model

-   Update "*ACV Static - Catalogue Client Service*" to remove EDC
    Connector adapter

-   Update "*TCV Static - Catalogue Client Service*" to remove EDC
    Connector adapter

-   Update "*ACV Static - Resource Offering Service*" to remove EDC
    Connector adapter

-   Update "*TCV Static - Resource Offering Service*" to remove EDC
    Connector adapter

-   Update "*ACV Static - Connector Service*" to add EDC Connector
    adapter

-   Update "*TCV Static - Connector Service*" to add EDC Connector
    adapter

-   Update "User Interfaces" to mark Identity Provider frontend as a
    released component

-   Update "ACV Static - Tier 1 Authentication Service" to include the
    authenticator plugin

-   Update "TCV Static - Tier 1 Authentication Service" to include the
    authenticator plugin

-   Update "APIs" to include Users And Roles v2 APIs

-   Fixed descriptions of entities and attributes "LDM - Domain 1 -
    Onboarding & IAA" 

-   Updated "Simpl-Open Application Architecture" with Data
    Orchestration Service

-   Update "ACV - Domain 2 - Publish and consume resources" to include
    the Sync Schema Adapter, Schema Management Service and Data
    Orchestration Service

-   Update "ACV Static - Schema Management Service" to include more
    description and the schema synch adapter

-   Added the anonymisation services to "ACV Static - Data Orchestration
    Service"

-   Update "ACV Dynamic - BP 06 – Consumer searches resources in data
    space catalogues" to include the Sync Schema Adapter

-   Update "ACV Dynamic - BP 05B - Provider manages resource
    descriptions" to include the Sync Schema Adapter

-   Updated "User Interfaces" to add Schema Management UI and Data
    Orchestration UI

-   Updated "APIs" to add Data Orchestration Interfaces and update
    Schema Management and Synch Schema Service

-   Updated "Technology Deployment View" to include the Schema
    Management Service

-   Updated "Identification, Authentication & Authorisation" to reflect
    Roles & Identity Attributes for Schema Management and Data
    Orchestration

-   Updated "Simpl-Open Technology Choices" to reflect Apache Fuseki and
    Dagster 

-   Updated "Custom Components Data Model" to reflect Conceptual,
    Logical and Physical Data Models for the Sync Schema Adapter

-   Updated *"Simpl-Open Application Architecture"* to explain the
    difference between mandatory and optional services

-   Updated *"Simpl-Open Functional Architecture"* to rename domain 1
    into Access Control & Trust

-   Updated *"ACV - Domain 1 - Access Control & Trust"* to rename domain
    1 into Access Control & Trust

-   Updated *"CDM - Domain 1 - Access Control & Trust"* to rename domain
    1 into Access Control & Trust

-   Updated *"LDM - Domain 1 - Access Control & Trust"* to rename domain
    1 into Access Control & Trust

-   Updated *"PDM - Domain 1 - Access Control & Trust"* to rename domain
    1 into Access Control & Trust

-   Updated *"TCV - Domain 1 - Access Control & Trust"* to rename domain
    1 into Access Control & Trust

-   Updated *"*LDM - Domain 2 - Publish and consumer resources*"* to
    update the Infrastructure Provider Storage

-   Update "*APIs*" to include Infrastructure Provider API description

-   Updated *"*High-Level Architecture*"* to reflect the new
    capabilities map structure and removed "*Annex 1 - Architecture
    Building Blocks*" as this is now described in the high-level
    architecture itself

-   Updated *"*Simpl-Open Application Architecture*"* to refer to the
    website for NFRs instead of the legacy annex and removed "*Annex 3 -
    Non-Functional Requirements*"

-   Updated *"*Assumptions and Architecture Decisions*"* to include
    missing decisions

-   Updated *"ACV - Domain 3 - Management/Operation of Data Space"* with
    new overview diagram using application services and individual
    service static views

-   Updated *"TCV - Domain 3 - Management/Operation of Data Space"* with
    new structure and individual service static views

-   Added "TCV Dynamic - BP 02C - Manage resource description schemas"

-   Added "TCV Static - Schema Management Service"

-   Updated "ACV Static - Schema Management Service" with description

-   Added "ACV Dynamic - BP 02C - Manage resource description schemas"

-   Updated "CDM - Domain 2 - Publish and consume resources" to include
    the Schema Sync Service

-   Updated "LDM - Domain 2 - Publish and consume resources" to include
    the Schema Sync Service

-   Updated "PDM - Domain 2 - Publish and consume resources" to include
    the Schema Sync Service

-   Added "ACV Static - Schema Sync Service"

-   Added "TCV Static - Schema Sync Service"

-   Added Schema Management to "Detailed Technical Specifications"

-   Updated "User Interfaces" to add Infrastructure UI for deployment
    script VM templates

####  1.3.5. <a name='Nov2025'></a>07 Nov 2025 

-   Update *"ACV Dynamic - BP 12C – Credentials actions by the
    Governance Authority"* to include the Identity Provider Frontend as
    officially available

-   Update *"ACV Static - Identity Provider Service"* to include
    Identity Provider Frontend as officially available

-   Update *"CDM - Domain 1 - Onboarding & IAA"* to update the data
    model of Identity Provider and Authentication Provider

-   Update *"LDM - Domain 1 - Onboarding & IAA"* to update the data
    model of Identity Provider and Authentication Provider

-   Update *"PDM - Domain 1 - Onboarding & IAA"* to update the data
    model of Identity Provider and Authentication Provider

-   Update "APIs" to include the new auto renewal APIs for the
    authentication provider component

####  1.3.6. <a name='26Sep2025'></a> 26 Sep 2025 

-   Update section *"Simpl-Open Application Architecture"* to reflect
    the new structure of the section

-   Update section *"ACV - Domain 2 - Publish and consume resources"*
    with new overview diagram using application services

-   Add section *"ACV - Domain 2 - Publish and consume resources -
    Static Views"* containing individual service static views

-   Add section *"ACV - Domain 2 - Publish and consume resources -
    Dynamic Views"* to reorganise the already existing dynamic views

-   Update section *"Simpl-Open Technology Architecture"* to reflect the
    new structure of the section

-   Update section *"TCV - Domain 1 - Onboarding & IAA"* to reflect the
    new structure of the section

-   Add section *"TCV - Domain 1 - Onboarding & IAA - Static Views"*
    containing individual service static views

-   Add section *"TCV - Domain 1 - Onboarding & IAA - Dynamic Views"* to
    reorganise the already existing dynamic views

-   Update section *"TCV - Domain 2 - Publish and consume resources"* to
    reflect the new structure of the section

-   Add section *"TCV - Domain 2 - Publish and consume resources -
    Static Views"* containing individual service static views

-   Add section *"TCV - Domain 2 - Publish and consume resources -
    Dynamic Views"* to reorganise the already existing dynamic views

-   Removed hyperlinks from section *"User Interfaces"*.

-   Update section "*LDM - Domain 1 - Onboarding & IAA"* to update the
    data model for the security attributes provider and authentication
    provider components

-   Update section *"PDM - Domain 1 - Onboarding & IAA"* to update the
    data model for the security attributes provider and authentication
    provider components

-   Update section *"APIs"* to update Security Attributes Provider Tier1
    and Tier2 v2 APIs, Identity Provider Tier1 and Tier2 v2 APIs,
    Identity Provider Tier1 v2 APIs

-   Update section "*ACV Static - Tier2 Authentication Service" *to
    include the communication with Security Attributes Provider and
    Identity Provider

####  1.3.7. <a name='Sep2025'></a>05 Sep 2025 

-   Update section *"APIs"* to include Security Attributes Provider
    Tier1 and Tier2 v2 APIs, Identity Provider Tier1 and Tier2 v2 APIs,
    Identity Provider Tier1 v2 APIs

-   Update section *"User Interfaces"* to include participant management
    functionalities in the Onboarding frontend

-   Update section *"User Interfaces"* to include credential renewal
    functionalities in the participant utility frontend

-   Update section *"CDM - Domain 1 - Onboarding & IAA"* to update the
    data model for identity provider and authentication provider
    components

-   Update section "*LDM - Domain 1 - Onboarding & IAA"* to update the
    data model for identity provider, security attributes provider and
    authentication provider components

-   Update section *"PDM - Domain 1 - Onboarding & IAA"* to update the
    data model for identity provider, security attributes provider and
    authentication provider components

-   Update section *"ACV - Domain 1 - Onboarding & IAA"* to include
    credential renewal flows

-   Create section *"ACV Dynamic - BP 12C – Credentials actions by the
    Governance Authority"*

-   Update section *"TCV - Domain 1 - Onboarding & IAA"* to include
    credential renewal flow

-   Create section *"TCV Dynamic - BP 12C – Credentials actions by the
    Governance Authority"*

-   Update section *"ACV Dynamic - BP 07 - Consumer and Provider
    establish a usage contract for selected catalogue items"* to include
    traceability to the business process on the diagram

-   Update section *"ACV Dynamic - WF 12B - Local Node Logging and
    Monitoring"* to include traceability to the business process on the
    diagram

-   Update section *"ACV Dynamic - BP 09A - Consumer consumes a data
    resource from a Provider"* to include traceability to the business
    process on the diagram

-   Update section *"ACV Dynamic - BP 09B - Consumer receives a data
    processing service on a data resource via an application"* to
    include traceability to the business process on the diagram

-   Update section *"Application Components Views"* to reflect the new
    structure of the section

-   Update section *"ACV - Domain 1 - Onboarding & IAA"* with new
    overview diagram using application services

-   Add section *"ACV - Domain 1 - Onboarding & IAA - Static Views"*
    containing individual service static views

-   Add section *"ACV - Domain 1 - Onboarding & IAA - Dynamic Views"* to
    reorganise the already existing dynamic views

-   Added first version of orchestration platform to *"ACV - Domain 2 -
    Publish and consume resources"*

-   Update section *"ACV Dynamic - BP 08 - Consumer consumes an
    infrastructure resource from a Provider"* to add traceability to BPs

####  1.3.8. <a name='D1.3.2D1.3.3'></a>D1.3.2 → D1.3.3

-   Update section "*PDM - Domain 1 - Onboarding & IAA*" 

-   Update section "*LDM - Domain 1 - Onboarding & IAA*"

-   Update section "*CDM - Domain 1 - Onboarding & IAA*" 

-   Update section "*ACV - Domain 1 - Onboarding & IAA*" to include
    Document Validation and Hashicorp Vault technology

-   Update section "*TCV - Domain 1 - Onboarding & IAA*" to include
    Document Validation and Hashicorp Vault technology

-   Update section "*TCV Dynamic - BP 03A - Onboarding of a
    participant - Tier II*"

-   Update section "TCV Dynamic - BP 03B - Onboarding Tier 1 -
    Organisation Local IDP(Directory) Connection/Mapping" to include
    Document Validation and Hashicorp Vault technology

-   Update section "*ACV Dynamic - BP 03A - Onboard a Participant*" to
    include ArchiMate Refactoring, traceability with BP03A and Document
    Validation Service

-   Update section "*ACV Dynamic - BP 03B - Connect/map Organisation
    Local IDP (Directory)*" to include ArchiMate cleanup and
    traceability with BP03B

-   Update section "*APIs*" to include IAA OpenAPI definition, AsyncAPI
    definition, API descriptions

-   Update section "*Data Space Concepts*" to include a the new "Anatomy
    of a Simpl-Open service" section

-   Update section: "*ACV - Domain 2 - Publish and consume resources*"
    with new components & APIs to include EDC Connector Adapter,
    Validation Service and Contract Consumption Adapter

-   Update section: "*ACV Dynamic - BP 05 - Add or Update Resource
    (Publish) on Catalogue*"

-   Update section: "*ACV Dynamic - BP 09A - Consumer consumes a data
    resource from the provider*"

-   Update section: "*ACV Dynamic - BP 09B - Consumer receives data
    processing service over a dataset via an Application*"

-   Update section: "*TCV - Domain 2 - Publish and consume resources*"
    with new components & APIs to include EDC Connector Adapter,
    Validation Service and Contract Consumption Adapter

-   Update section: "*TCV Dynamic - BP 05 - Add or Update Resource
    (Publish) on Catalogue*"

-   Update section: "*TCV Dynamic - BP 09A - Consumer consumes a data
    resource from the provider*"

-   Update section: "*TCV Dynamic - BP 09B - Consumer receives data
    processing service over a dataset via an Application*"

-   Update section: "*APIs*" to include EDC Connector Adapter,
    Validation Service and Contract Consumption Backend 

-   Update section: "*ACV Dynamic - BP 08 - Consumers select and use an
    Infrastructure Catalogue Resource from the Infrastructure Provider*"

-   Update section: "*TCV Dynamic - BP 08 - Consumers select and use an
    Infrastructure Catalogue Resource from the Infrastructure Provider*"

-   Update section: "*Technology Deployment View*"

-   Add "*Architecture Patterns*" section into the "*Architecture
    Framework"* and remove "*Annex 4 - Architecture Patterns*"

-   Remove section "*List of Business Processes*" and referred to the
    website instead

-   Update section "*Self-Description Tooling*" to remove the Flow
    Diagram (duplication with ACV Dynamic)

-   Update section "*Simpl-Open Application Architecture*"

-   Update section: "*APIs*" to include post-configuration and
    decommissioning

-   Update section: "*Simpl-Open Technology Choices*" to include
    Terraform related technologies

-   Update section: "*User Interfaces*" with the Infrastructure
    Deployment Script Management UI

-   Update section: "*Infrastructure Provisioning*"

-   Updated section "*Annex 2 - Mapping between functional requirements
    and components*" with latest list of requirements

-   Update section: "*Open-Source Components Data Model*" to include
    OpenTofu

-   Add section "*Digital Identities integration with EU Digital
    Identity Framework - eIDAS*" in the "*Data Spaces Concepts*" section

-   Update section: "*Simpl-Open Security Architecture*" with updated
    diagrams

-   Update section: "*LDM - Domain 2 - Publish and consume resources*"
    with updated Infrastructure Provider fields

-   Update section: "*PDM - Domain 2 - Publish and consume resources*"
    with updated Infrastructure Provider fields

-   Update "*Architecture Decisions Record*" with latest decisions

-   Updated *"ACV Dynamic - BP 05B - Publish and consume"* according to
    BP and renamed to *"ACV Dynamic - BP 05B - Manage resources"*

-   Removed (and replaced by *"ACV Dynamic - BP 05B - Manage
    resources"*) sections: 

    -   *"ACV Dynamic - BP 05B - Request sd"*

    -   *"ACV Dynamic - BP 05B - Retrieve status"*

    -   *"ACV Dynamic - BP 05B - Update SD status"*

####  1.3.9. <a name='D1.3.1D1.3.2'></a>D1.3.1 → D1.3.2

-   Add section *"User Interfaces"* into the "*Simpl-Open Application
    Architecture"*

-   Add section *"Custom Components Data Model"* into the "Simpl-Open
    Data Architecture"

-   *"Simpl-Open Security Architecture"* enhanced

-   *"UI/UX Style Guide"* referenced in the *UIs* section

-   Added Health checks and Tracing for Monitoring component

