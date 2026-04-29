<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Dimension: Security</a><br/>
        <a href="README.md">Capability: Access Control And Trust</a><br/>
            <strong>Detailed technical specification</strong><br/>
</p>
</div>

# Detailed technical specification — Identification, Authentication & Authorisation

This page reproduces the IAA section of the functional and technical architecture specification (FTA §6.4.1). It is the canonical reference for the Tier 1 / Tier 2 component model, the role catalogue, the identity-attribute catalogue, the credential formats, and the encryption and integrity guarantees of agent-to-agent communication. Each solution under this capability — [authentication-provider-federation](authentication-provider-federation/README.md), [authorisation](authorisation/README.md), [identity-provider](identity-provider/README.md), and [security-attribute-provider-federation](security-attribute-provider-federation/README.md) — implements one or more of the components listed below.

> **Sub-section numbering note.** The source document uses placeholder numbers `2.27.x` for the sub-sections of §6.4.1. The numbering is preserved here verbatim from the source; treat those as anchors, not as a separate top-level section.

## Source

This content is extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **6.4.1 Identification, Authentication & Authorisation** (lines 11811–12652 of the source document, dated 2026-04-20).

Upstream link: [Functional and Technical Architecture Specifications](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#641-identification-authentication--authorisation).

---

####  6.4.1. <a name='IdentificationAuthenticationAuthorisation'></a>Identification, Authentication & Authorisation

The IAA 2-Tier approach in Simpl-Open is already described in the **Data Spaces Concepts section of the Simpl-Open High-Level Overview.**

Because of the 2-Tier approach, the components are grouped into Tier 1
and Tier 2.

#####  2.27.1. <a name='Tier1IAAComponents'></a>Tier 1 IAA Components

Tier 1 is meant to be under the control of the governance of the
organisation that became a Participant of a Dataspace, its components
are local to the participant agent and are dedicated to enabling and
controlling the access of the organisation's end users to the
resources/functionalities offered by the Simpl-Open agent and are:

###### Identification and Authentication 

The component responsible for identification and authentication is the
**Tier 1 Authentication Provider** realised using an extended version of
Keycloak (OpenID Connect Identity Provider) integrated with the **User &
Roles** component.

###### User & Roles

The User and Roles component is used to define roles used by the
**Authorisation Tier 1**, manage roles assignment of **Tier 1
Authentication Provider** end users and assign identity attributes to
roles (described in Identity Attributes and *User Roles* sections below)

###### Authorisation Tier 1

This component manages permissions, determining what actions each end
user is authorised to perform on a specific Agent resource. It plays a
critical role in maintaining system security by ensuring that only the
necessary users have limited access to specific functions, realised
through an **API Gateway,** more specifically **Spring Cloud Gateway**
and relies on **Tier1 Authentication Provider** to retrieve roles of
authenticated end users to enforce **RBAC (Role Based Access Control)
policies** to authorise or deny the access to the requested agent
resource.

**RBAC** policies will be applied to check if the end user has the
authorisation to access the requested agent resource/functionality based
upon its assigned roles.

#####  2.27.2. <a name='Tier1Credential'></a>Tier 1 Credential

The tier 1 credential consists of an OpenID Connect (OAuth 2.0)
[AccessToken](https://oauth.net/2/access-tokens/) issued by the **Tier 1
Authentication Provider**, in the form of a JWT
([rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)) that contains
standard
[claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims)
extended with the following four custom claims:

###### Client Roles

The client roles is an array containing the list of roles assigned to
the end user through the functionalities of the **User & Roles**
component:

client-roles : \[ "NOTARY", "ONBOARDER\_M"\]

this will also be included in every tier 1 access token with the claim
name "**client-roles**" of the JWT
([rfc7519](https://datatracker.ietf.org/doc/html/rfc7519))

###### Participant ID

The participant ID is the unique and immutable ID used to identify the
participant in the tier 2 IAA process. It is represented by
a **GUID** formatted as shown in the following example:

participant\_id : "02309243-2f77-456a-a1db-d8e8bb006f74"

this will also be included in every tier 1 access token with the claim
name "**participant\_id**" of the JWT
([rfc7519](https://datatracker.ietf.org/doc/html/rfc7519))

Note that the participant ID will never change in time.

###### Credential ID

The credential ID is the unique ID used to identify the current
credential participant in the tier 2 IAA process. It is represented by
the **Base58BTC**
([https://digitalbazaar.github.io/base58-spec](https://digitalbazaar.github.io/base58-spec/))
of the **HASH** (sha384) of the **Participant x509 Certificate** used to
communicate in the data space as shown in the following example:

credential\_id :
"z8A3E8X4NkhgnFrczqy54SZjrnoiz6At3rqLosWN75WCkKQEgxmkA3yqpCPtPqHSnS9"

this will also be included in every tier 1 access token with the claim
name "**credential\_id**" of the JWT
([rfc7519](https://datatracker.ietf.org/doc/html/rfc7519))

Note that the credential ID will change in time: e.g. when a credential
is compromised a new issuance of credentials must occur.

###### Identity Attributes

Participant identity attributes are used to enable the specification of
access to a subset of functionalities for a participant. In the context
of Tier 2 communication, the presence of Identity Attributes ensures
ABAC compliance. Specifically, services provided by dataspace
participants to other participants can be protected by one or more
Attributes. 

A subset of those attributes can be assigned to Tier 1 roles (see Tier 1
User Roles) meaning that every end user belonging to this role owns it
and is represented as in the following example; 

identity\_attributes : \[ "DATA\_CONSUMER", "DATA\_ACCESS\_LEVL1"\]

this will also be included in every tier 1 access token with the claim
name "**identity\_attributes**" of the JWT
([rfc7519](https://datatracker.ietf.org/doc/html/rfc7519))

#####  2.27.3. <a name='Tier1UserRoles'></a>Tier 1 User Roles

Tier 1 roles are the core elements on which the RBAC policies are
enforced and are also used by the participant governance to assign a
subset of Participant Identity Attributes (see Identity Attributes) to
its end users.

Here is the updated list of Roles that are used inside Simpl-Open:

<table>
<thead>
<tr class="header">
<th><strong>Human Readable Role Name</strong></th>
<th><strong>Role Value</strong></th>
<th><strong>Description</strong></th>
<th><strong>Predefined</strong></th>
<th><strong>Participant</strong></th>
<th><strong>Assigned Identity Attributes</strong></th>
<th><strong>Id Component</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Tier 2 authorisation manager</td>
<td>T2IAA_M</td>
<td>In the Dataspace Governance Authority is the one who is in charge of defining and changing the onboarding procedure itself, like setting up the mandatory documents and the rules that will be followed by the onboarding process. </td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td><p>IAA-ONB-FE</p>
<p>IAA-ONB-BE</p></td>
</tr>
<tr class="even">
<td>Tier 2 authorisation operator</td>
<td>NOTARY</td>
<td>tier 2 authorisation operator, the one who is in charge of taking care of onboarding requests and follow their process. It will ask for further documents, it will comment on the onboarding requests and reject/approve the requests</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td><p>IAA-ONB-FE</p>
<p>IAA-ONB-BE</p></td>
</tr>
<tr class="odd">
<td>Tier 2 setup administration role</td>
<td>ONBOARDER_M</td>
<td>tier 2 setup administrator role, the one who is in charge of finalising the tier 2 setup of an agent installation.</td>
<td>true</td>
<td>All Participant</td>
<td></td>
<td><p>IAA-U&amp;R-FE</p>
<p>IAA-U&amp;R-BE</p></td>
</tr>
<tr class="even">
<td>Tier 2 identity attributes manager</td>
<td>IATTR_M</td>
<td>This role is present only in the Dataspace Governance Authority and its duties are to cover the whole lifecycle of Identity Attributes, from the creation and management to the assignment to participants</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td><p>IAA-SAP-FE</p>
<p>IAA-SAP-BE</p></td>
</tr>
<tr class="odd">
<td>Tier 1 user and role manager</td>
<td>T1UAR_M</td>
<td>Tier 1 user and roles manager. In the Dataspace Governance Authority, this role will manage local roles and dataspace identity attributes (defining them and assigning them to participant types + defining their assignability). In any dataspace participant, this role will manage local roles and identity attributes assignment to local roles</td>
<td>true</td>
<td>All Participant</td>
<td></td>
<td><p>IAA-U&amp;R-FE</p>
<p>IAA-U&amp;R-BE</p></td>
</tr>
<tr class="even">
<td>Applicant Representative</td>
<td>APPLICANT</td>
<td>end user responsible for onboarding an applicant dataspace participant who sign up the public dataspace onboarding site to manage the onboarding request. Applicant's primary scope is to create an onboarding request and react on the Tier 2 authorisation operator (NOTARY) interaction to get the onboarding request approved</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td><p>IAA-ONB-FE</p>
<p>IAA-ONB-BE</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Ro-MU-CA</td>
<td>Role defined in XFSC Federated Catalogue: Catalogue Administrator</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Ro-MU-A</td>
<td>Role defined in XFSC Federated Catalogue: Participant Administrator</td>
<td>true</td>
<td>Providers</td>
<td><p>DATA_PROVIDER_PUBLISHER</p>
<p>APP_PROVIDER_PUBLISHER</p>
<p>INFRA_PROVIDER_PUBLISHER</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Ro-SD-A</td>
<td>Role defined in XFSC Federated Catalogue: Self-Description Administrator</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Ro-Pa-A</td>
<td>Role defined in XFSC Federated Catalogue: Participant User Administrator</td>
<td>true</td>
<td>Providers</td>
<td><p>DATA_PROVIDER_PUBLISHER</p>
<p>APP_PROVIDER_PUBLISHER</p>
<p>INFRA_PROVIDER_PUBLISHER</p></td>
<td></td>
</tr>
<tr class="odd">
<td>Researcher</td>
<td>RESEARCHER</td>
<td>Researcher who is able to access research only datasets</td>
<td>false</td>
<td>Consumer</td>
<td>DATA_SEARCHER</td>
<td></td>
</tr>
<tr class="even">
<td>SD Publisher</td>
<td>SD_PUBLISHER</td>
<td>Role defined for the user who is responsible for creating and publishing the self-description on the catalogue</td>
<td>true</td>
<td>Providers</td>
<td><p>DATA_PROVIDER_PUBLISHER</p>
<p>DATA_SEARCHER</p></td>
<td></td>
</tr>
<tr class="odd">
<td>SD Consumer</td>
<td>SD_CONSUMER</td>
<td>Tier-1 Role for Consumer</td>
<td>true</td>
<td>Consumer</td>
<td>CONSUMER</td>
<td></td>
</tr>
<tr class="even">
<td>Schema Manager Admin</td>
<td>GA_SCHEMA_ADMIN</td>
<td>Tier-1 Role for Schema Admin</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Schema Manager Viewer</td>
<td>GA_SCHEMA_VIEWER</td>
<td>Tier-1 Role for Schema Viewer</td>
<td>true</td>
<td>Governance Authority</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Kibana Business User</td>
<td>KIBANA_BUSINESS_USER</td>
<td>Role for accessing Kibana as a business user (binded to local Kibana user)</td>
<td>true</td>
<td>All Participant</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Kibana Admin</td>
<td>KIBANA_ADMIN</td>
<td>Role for accessing Kibana as an admin (binded to local Kibana user)</td>
<td>true</td>
<td>All Participant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Data Orchestration Developer</td>
<td>ORCH_DEVELOPER</td>
<td>Role for developing workfows and services for data orchestration</td>
<td>true</td>
<td><p>Consumer</p>
<p>Provider</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Data Orchestration Admin</td>
<td>ORCH_ADMIN</td>
<td>Role for administration and management of the orchestration, like setting schedules, retry of Workflows or Monitoring</td>
<td>true</td>
<td><p>Consumer</p>
<p>Provider</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Infrastructure Provider Admin</td>
<td>INFRA_ADMIN</td>
<td>Role defined for management of all the Infrastructure Provider's cloud resources.</td>
<td>true</td>
<td>Provider</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Infrastructure Provider Deployer</td>
<td>INFRA_DEPLOYER</td>
<td>Role defined for deactivation and triggering of the Infrastructure Provider's cloud resources.</td>
<td>true</td>
<td>Consumer</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#####  2.27.4. <a name='Tier2IAAComponents'></a>Tier 2 IAA Components

Tier 2 is meant to be under the control of the Dataspace Governance
Authority and is used by all participant agents to ensure secured and
encrypted communications (see *Encryption* and *Guaranteed
Authenticity/Integrity* sections below), its components are both
centralised (in the Authority Agent) and decentralised (local to all
agents) 

###### Centralised

*Identity Provider Federation*

This component includes functionalities about identity information and
Tier 2 credential creation, validation and management.

Starting from the onboarding process, the Identity Provider will be used
for:

-   Create the credential: when an applicant participant is onboarded by
    approving its onboarding request, a Tier 2 credential is created by
    the identity provider. The participant installs the credential
    within its own agent.

-   Validate the credential: the identity provider verifies the received
    identity Tier 2 credentials.

-   Management: during the lifecycle of a credential, it can be either
    renewed or revoked by the Dataspace Governance Authority.

*Security Attribute Provider Federation*

To implement ABAC policies, which are used in agent-to-agent
communications, a set of valid and known Identity Attributes are needed
and will be assigned to each dataspace participant by the Governance
Authority.

The Security Attribute Provider component implements several
functionalities:

-   Identity Attributes management (create, delete and modify identity
    attributes) 

-   Identity Attributes Participant assignment (both during the
    Onboarding and after)

-   Temporary attestation of the participant's identity attributes in
    the form of a *signed ephemeral proof* 

###### Decentralised

*Tier 2 Authentication Provider*

This component is responsible for keeping the Tier 2 Credential received
during the onboarding process and implements all Tier 2 Identification
and Authentication functionalities such as:

-   Keep safely store the participant agent Tier 2 Credential and its
    keypair

-   Check and Validate any Tier 2 credentials coming from other
    participant agents during the mTLS Authentication against the
    **Identity Provider Federation**.

-   Check and Validate the ephemeral proof received from other
    participant agents after the successful mTLS Authentication process.

-   Check and validate the Tier 1 credential forwarded by other
    participant agents against the ephemeral proof (that contains also
    the caller **Tier 1 Authentication Provider** public key)

-   Request ephemeral proof to the **Security Attribute Provider
    Federation** to be used in secured communications with other
    participant agents

*Authorisation Tier 2*

This component is realised through an **API Gateway,** more specifically
**Spring Cloud Gateway** and relies on the **Tier 2 Authentication
Provider** to check Tier 2 credentials and ephemeral proof received
during the mTLS Authentication process to enforce **ABAC (Attribute
Based Access Control) policies** to authorise or deny access to the
requested agent resource.

ABAC policies will be enforced in any agent-to-agent communication, by
verifying whether the requestor's attributes are permitted to access the
requested resource and if needed the enforcement of ABAC policies can be
done also in both Tier 1 and Tier 2 credentials (to check if the
identity attribute is also present in the Tier 1 credential used by the
end user of the caller participant agent)

#####  2.27.5. <a name='Tier2Credential'></a>Tier 2 Credential

The Tier 2 credential has the form of an X509 Certificate and is issued
by a Certificate Authority embedded in the **Identity Provider
Federation**.

###### Identity Attributes

Identity attributes are the most powerful and versatile tool at the
disposal of the Dataspace Governance Authority to "design" the
governance and the rules in the interactions between Dataspace
participants. Some attributes are **built in** Simpl-Open (**Built-in =
true**) and cannot be modified/removed.

Two important properties can be used in the definition of Identity
attributes:

**Assignable**: if **true** means that any governance of a Participant
that receives this identity attribute can assign it to any Tier 1 roles
to then give it to its end users, if **false** means that this identity
attribute is **Participant wide** and is to be considered as assigned to
all the end users of the participant.

**IsRight**: if **true** means that the identity attribute should be
considered as a special centralised right.

Here is the updated list of Identity Attributes that are used inside
Simpl-Open:

<table>
<thead>
<tr class="header">
<th><strong>Human Readable Attribute Name</strong></th>
<th><strong>Identity Attribute Value</strong></th>
<th><strong>Description</strong></th>
<th><strong>Built-in</strong></th>
<th><strong>Assignable</strong></th>
<th><strong>IsRight</strong></th>
<th><strong>Id Component</strong></th>
<th><strong>Component &amp; Endpoint</strong></th>
<th><strong>Location of configuration</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Consumer</td>
<td>CONSUMER</td>
<td>Identity attribute used to tag the consumer participant</td>
<td>true</td>
<td>false</td>
<td>false</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="even">
<td>Data Provider</td>
<td>DATA_PROVIDER</td>
<td>Identity attribute used to tag the data provider participant</td>
<td>true</td>
<td>false</td>
<td>false</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="odd">
<td>Application Provider</td>
<td>APP_PROVIDER</td>
<td>Identity attribute used to tag the application provider participant</td>
<td>true</td>
<td>false</td>
<td>false</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="even">
<td>Infrastructure Provider</td>
<td>INFRA_PROVIDER</td>
<td>Identity attribute used to tag the infrastructure provider participant</td>
<td>true</td>
<td>false</td>
<td>false</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="odd">
<td>Data Provider Publisher</td>
<td>DATA_PROVIDER_PUBLISHER</td>
<td>Identity attribute needed for publishing Data Catalogue</td>
<td>true</td>
<td>true</td>
<td>true</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="even">
<td>Application Provider Publisher</td>
<td>APP_PROVIDER_PUBLISHER</td>
<td>Identity attribute needed for publishing Application Catalogue</td>
<td>true</td>
<td>true</td>
<td>true</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="odd">
<td>Infrastructure Provider Publisher</td>
<td>INFRA_PROVIDER_PUBLISHER</td>
<td>Identity attribute needed for publishing Infrastructure</td>
<td>true</td>
<td>true</td>
<td>true</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
<tr class="even">
<td>Data searcher</td>
<td>DATA_SEARCHER</td>
<td>Identity Attributes used for tagging an end user able to act only as a searcher in the catalogue, but he can't start a contract negotiation or transfer process</td>
<td>true</td>
<td>true</td>
<td>true</td>
<td></td>
<td>Should be put in tier2-gateway  configuration within GA agent as ABAC configuration</td>
<td>tier2-gateway <br />
<strong>→</strong> spring-configmap.yaml</td>
</tr>
</tbody>
</table>

Built-in identity attributes will be available by default in every
Simpl-Open dataspace and cannot be modified by the Governance Authority.
The Governance Authority can add custom (not built-in) identity
attributes based on specific needs. For **example**, if a Governance
Authority needs to define access levels to resources, they could
introduce three new identity attributes such as:

<table>
<thead>
<tr class="header">
<th><strong>Human Readable Attribute Name</strong></th>
<th><strong>Identity Attribute Value</strong></th>
<th><strong>Description</strong></th>
<th><strong>Built-in</strong></th>
<th><strong>Assignable</strong></th>
<th><strong>IsRight</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Basic Access Level</td>
<td>ACCESS_LEVEL_BASIC</td>
<td>Basic Access Level</td>
<td>false</td>
<td>true</td>
<td>true</td>
</tr>
<tr class="even">
<td>Medium Access Level</td>
<td>ACCESS_LEVEL_MEDIUM</td>
<td>Medium Access Level </td>
<td>false</td>
<td>true</td>
<td>true</td>
</tr>
<tr class="odd">
<td>Full Access Level</td>
<td>ACCESS_LEVEL_FULL</td>
<td>Full Access Level</td>
<td>false</td>
<td>true</td>
<td>true</td>
</tr>
</tbody>
</table>

###### Encryption

In mTLS (mutual Transport Layer Security) communication, **encryption of
in-transit data** ensures that the information exchanged between a
client and a server is protected from interception or tampering. This
encryption is achieved through the following process:

1.  **TLS Handshake**: Both the client and server initiate a TLS
    handshake, during which they exchange public keys and agree on
    encryption algorithms.

2.  **Mutual Authentication**: Unlike regular TLS, in mTLS both the
    client and server authenticate each other by exchanging digital
    certificates, confirming the identity of both parties.

3.  **Symmetric Encryption**: After authentication, a symmetric
    encryption key is established and used to encrypt all subsequent
    data transmitted between the client and server.

Through this process, **data in transit is securely encrypted**,
preventing unauthorised access or modification, while ensuring that both
the client and server are trusted entities.

###### Guaranteed Authenticity / Integrity

Supports the measures in place to ensure end-to-end data integrity, such
that Simpl-Open agents can validate the authenticity of the delivered
information.

This capability is achieved by implementing mTLS communication between
agents, ensuring that communication can be established only between
trusted and known participants from the Authority.   
The Governance Authority during the onboarding processes creates unique
Identity Credentials for each participant of the Dataspace. Then the
participant uses the credential during the mTLS communication.

###### Components

This section is dedicated to listing all components divided by Frontend
FE and Backend BE

<table>
<thead>
<tr class="header">
<th><strong>Id Component</strong></th>
<th><strong>Component</strong></th>
<th><strong>Participant</strong></th>
<th><strong>Endpoints published on tier1-gateway</strong></th>
<th><strong>Endpoints published on tier2-gateway</strong></th>
<th><strong>Configuration URL</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IAA-IDPRO-FE</td>
<td>Identity provider FE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>IAA-IDPRO-BE</td>
<td>Identity provider BE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td>IAA-SAP-FE</td>
<td>Security Attribute Provider FE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>IAA-SAP-BE</td>
<td>Security Attribute Provider BE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td>IAA-ONB-FE</td>
<td>Onboarding FE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>IAA-ONB-BE</td>
<td>Onboarding BE</td>
<td>Governance Authority</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="odd">
<td>IAA-U&amp;R-FE</td>
<td>User &amp; Roles FE</td>
<td>All Participant</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>IAA-U&amp;R-BE</td>
<td>User &amp; Roles BE</td>
<td>All Participant</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="odd">
<td>IAA-AUTH-FE</td>
<td>Authentication Provider FE</td>
<td>All Participant</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>IAA-AUTH-BE</td>
<td>Authentication Provider BE</td>
<td>All Participant</td>
<td>YES</td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>xsfc-advsearch-be</td>
<td>Providers, Consumers</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>simpl-edc</td>
<td>Providers, Consumers</td>
<td>NO</td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>sd-creator-backend</td>
<td>Providers</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>xsfc-catalogue</td>
<td>Governance Authority</td>
<td>NO</td>
<td>YES </td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>catalogue-query-mapper</td>
<td>Governance Authority</td>
<td>NO</td>
<td>YES </td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Infra. Deployment Script Management FE</td>
<td>Providers</td>
<td>YES</td>
<td>NO</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Infra. Deployment Script Management BE</td>
<td>Providers</td>
<td><strong>YES</strong></td>
<td>NO</td>
<td><a href="https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be/-/tree/develop?ref_type=heads#configure-tier1-and-tier2-business-logs">https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be/-/tree/develop?ref_type=heads#configure-tier1-and-tier2-business-logs</a></td>
</tr>
<tr class="even">
<td></td>
<td>schema-sync-adapter</td>
<td>Providers, Consumers</td>
<td><strong> NO</strong></td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>asset-orchestrator</td>
<td>Providers</td>
<td><strong>YES</strong></td>
<td><strong>NO</strong></td>
<td><a href="https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/asset-orchestrator/-/blob/feature/add-tags-to-workflow-list/README.md?ref_type=heads#tier1-configuration">https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/asset-orchestrator/-/blob/feature/add-tags-to-workflow-list/README.md?ref_type=heads#tier1-configuration</a></td>
</tr>
<tr class="even">
<td></td>
<td>dagster</td>
<td>Providers</td>
<td><strong>YES</strong></td>
<td><strong>NO</strong></td>
<td><a href="https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster/-/blob/feature/oauth2-proxy-integration/README.md?ref_type=heads#tier1-gateway-configuration-participant">https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster/-/blob/feature/oauth2-proxy-integration/README.md?ref_type=heads#tier1-gateway-configuration-participant</a></td>
</tr>
</tbody>
</table>

