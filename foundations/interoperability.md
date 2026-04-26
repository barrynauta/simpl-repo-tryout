---
id: doc:interoperability
type: foundation
name: Interoperability
since: r3.0
---

# Interoperability

Technical and semantic interoperability of Simpl-Open with external systems and data space standards.

## Technical interoperability

| Standard / protocol | Simpl-Open implementation | Solution(s) |
|---------------------|--------------------------|-------------|
| Data Space Protocol (DSP) | Eclipse Dataspace Connector (EDC) | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |
| OpenID Connect (OIDC) | Keycloak + Spring Cloud Gateway | [Tier 1 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md), [Authorisation](../security/access-control-and-trust/authorisation/authorisation/README.md) |
| mTLS (X.509) | EJBCA CA + Tier 2 credential | [Identity Provider](../security/access-control-and-trust/identity-provider/identity-provider/README.md), [Tier 2 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) |
| AsyncAPI v3.0.0 (Kafka) | Notification Service; Contract Manager; Infrastructure Triggering Module | [Notification Service](../administration/notification-and-messaging/notification/notification-service/README.md) |
| W3C Verifiable Credentials | VC Issuer + Wallet | [VC Issuer](../security/credential-management/vc-issuance-verification/vc-issuer/README.md), [Wallet](../security/credential-management/wallet/wallet/README.md) |
| SHACL | Self-description schema validation | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md), [Simpl Catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) |
| SPARQL / RDF (Turtle, JSON-LD) | Schema storage (Jena Fuseki); Self-descriptions (JSON-LD) | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) |

## Semantic interoperability

| Vocabulary / ontology | Usage | Solution(s) |
|----------------------|-------|-------------|
| Gaia-X Trust Framework | Self-description structure and terms | [SD Tooling](../governance/resource-management/metadata-description/sd-tooling/README.md), [Simpl Catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) |
| SKOS thesauri | Vocabulary datastore (ontologies) | [Vocabulary Management](../data/semantics-and-vocabulary/vocabulary-hub/vocabulary-management/README.md) |
| Dublin Core (dct) + OWL | Schema metadata properties | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) |
| Custom SIMPL namespace | simpl:Schema, simpl:SchemaVersion, simpl:status, simpl:resourceType | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) |

Full interoperability documentation: Status: not yet documented in detail. See individual solution `doc/architecture.md` technical views.
