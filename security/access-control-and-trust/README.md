<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Dimension: Security</a><br/>
        <strong>Capability: Access Control And Trust</strong><br/>
</p>
</div>

# Access control and trust

Two-tier identity, authentication, and authorisation (IAA) for Simpl-Open. Tier 1 covers participant-internal user access (RBAC via Keycloak + Spring Cloud Gateway). Tier 2 covers cross-participant agent-to-agent communication (ABAC via mTLS, X.509 credentials, and ephemeral proofs).

## Business services

- [Authentication provider federation](authentication-provider-federation/README.md) — Tier 1 (Keycloak) and Tier 2 (X.509 mTLS) authentication providers.
- [Authorisation](authorisation/README.md) — Tier 1 (RBAC) and Tier 2 (ABAC) API gateway enforcement via Spring Cloud Gateway.
- [Identity provider federation](identity-provider-federation/README.md) — Governance Authority–managed identity federation and Tier 2 credential issuance.
- [Security attribute provider federation](security-attribute-provider-federation/README.md) — management and assignment of identity attributes used for ABAC policy enforcement.
- [Encryption](encryption/README.md) — cryptographic key and secret management underpinning every secure store and Tier 2 credential. _(Realised by HashiCorp Vault / OpenBao.)_
- [Guaranteed authenticity and integrity](guaranteed-authenticity-integrity/README.md) — mTLS for every cross-participant call against the Tier 2 credential.

- [Common](common/README.md) — shared libraries (e.g. `iaa-common`) consumed by every Access-Control-and-Trust service. Not deployable on its own.

## Detailed specification

- [detailed-spec.md](detailed-spec.md) — full Tier 1 / Tier 2 component model, role catalogue, identity-attribute catalogue, credential formats, and encryption / integrity guarantees (extracted from FTA §6.4.1).

## Concept (FTA §2.3)

> Conceptual overview of how IAA works at a high level. Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **2.3 Access Control & Trust** (lines 1038–1110, source dated 2026-04-20). Upstream link: [FTA spec §2.3](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#23-access-control--trust).

How IAA works at a high level:

1. **Roles** are used to enforce **RBAC** (role-based access control) to end users that access Simpl-Open functionalities in tier 1.
2. **Identity Attributes** are used to enforce **ABAC** (attributes-based access control) in the agent-to-agent (node-to-node) communication in tier 2.
3. **Assignable Identity Attributes** are used to be assigned to **Roles**, enabling end users belonging to those roles to act on behalf of the participant in a certain context.

**Second Tier IAA — X.509 certificates with dynamic attribute provisioning.** For clarification, an example of how Tier II works in practice:

- **1.1** John Doe logs into the Consumer IAA Tier 1 system.
- **1.2** The IAA Tier 1 system retrieves user roles from the Simpl-Open agent's User Roles module and assigns John Doe the rights to access data space functionality through the Consumer's Simpl-Open agent. From this point on, all of John Doe's actions are performed by the Consumer's Simpl-Open agent, which interacts with other agents (Provider and/or data-space built-in capabilities).
- **2.1** John Doe makes the infrastructure request to the Provider's Simpl-Open agent, which validates it against the Access Control and Trust capability.
- **2.2** Provider and Consumer authenticate each other using mutual X.509 TLS authentication.
- **2.3** Provider and Consumer verify the validity of the X.509 certificate through the Identity Provider Federation.
- **2.4** Provider enforces the access-control policy based on embedded identity attributes and authorises the Consumer's Simpl-Open agent.
- **2.5** Consumer requests its own identity-attributes ephemeral proof from the Identity Provider Federation.
- **2.6** Identity Provider Federation responds to the Consumer's ephemeral-proof request with identity attributes.
- **2.7** Consumer sends the ephemeral proof with identity attributes to the Provider.
- **2.8** Provider checks and validates the ephemeral proof, then enforces the access-control policy based on the embedded identity attributes and authorises the Consumer's Simpl-Open agent.
- **3.1** Once verification against Access Control and Trust succeeds, the Provider uses its Infrastructure / User-data services module to fulfil the requests received.
- **3.2** Provider checks the policies by querying the Contracts module.
- **3.3** Provider enforces the retrieved contract policies.
- **3.4** Provider activates the Provisioning module to fulfil the requested resource.
- **4** Provider returns an affirmative response to the Consumer's request.
