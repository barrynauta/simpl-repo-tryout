Source: functional-and-technical-architecture-specifications.md, sections 4.3.1 (ACV Static — Catalogue Client Service), 4.5.2 (User Interfaces), 6.1.2 (TCV Static — Catalogue Client Service).

# Catalogue Client Application — architecture

## Business view

The Catalogue Client Application is deployed on Consumer and Provider nodes. It is the primary interface through which users search and browse the catalogue.

- **Catalogue Client Application Frontend** presents search fields and options to users. In the case of advanced search, the fields are defined by the schema. It contains:
  - **Quick Search UI** — allows the consumer/provider to perform a quick search on the respective Catalogue.
  - **Advanced Search UI** — allows the consumer/provider to perform an advanced search on the respective Catalogue, with fields auto-generated from the schema.

- **Catalogue Client Application Backend**:
  - Sends policy-filtered queries to the Catalogue component via the Adapter Component. After receiving results, it presents them in a structured format.
  - Transforms the schema definition automatically to frontend files used to generate a custom frontend for defining self-descriptions.

Sub-components deployed alongside the main frontend/backend:

- **Validation Backend** — performs syntax validation for the self-description on the provider side before they are published to the Catalogue. Also validates the resource source address used for registering service offerings in the Connector.

- **Contract Consumption Adapter** — requests an Offering from the Provider (returned with Offering ID and usage/access policies). Once the user accepts the conditions, builds the request to start Contract Negotiation via the EDC Connector Adapter and retrieves the Status of the Contract Negotiation.

Capability-map placement: Integration dimension → Resource discovery capability → Search engine business service.

![ACV Static view — Catalogue Client Service](./media/image42.jpeg)
![UI screenshot — Catalogue Client Application search interface](./media/image72.png)
![UI screenshot — Catalogue Client Application search results](./media/image73.png)
![UI screenshot — Catalogue Client Application resource detail view](./media/image74.png)

## Data view

The Catalogue Client Application does not own a persistent data store. It fetches:

- Schema definitions from the [Schema Management Service](../../../../../data/semantics-and-vocabulary/schema-management/schema-management-service/doc/architecture.md) (via a local schema cache synchronised by the Schema Synch Service) — used to generate advanced search field definitions and validate self-descriptions.
- Self-description results from the [Simpl Catalogue](../../../resource-catalogue/simpl-catalogue/doc/architecture.md) via the Catalogue's API and Query Mapper Adapter.
- Contract negotiation status from the [Connector](../../../../resource-sharing/resource-sharing-runtime/connector/doc/architecture.md) via the EDC Connector Adapter sub-component.

## Application view

### Internal decomposition

- **Catalogue Client Application Backend** — Java backend; query construction, schema-to-form transformation, result formatting.
- **Catalogue Client Application UI** — Angular frontend; Quick Search UI and Advanced Search UI.
- **Validation Backend** — Java backend; syntax validation of self-descriptions and resource source address validation.
- **Contract Consumption Adapter** — Java backend; contract negotiation initiation via EDC Connector Adapter.
- **EDC Connector Adapter** (sub-component of Contract Consumption Adapter) — handles interaction with the EDC Connector for asset registration and contract negotiation.

### Key integrations

- [Simpl Catalogue](../../../resource-catalogue/simpl-catalogue/doc/architecture.md) — the CCA sends queries to the Catalogue; results are returned and presented.
- [Schema Management Service](../../../../../data/semantics-and-vocabulary/schema-management/schema-management-service/doc/architecture.md) — the CCA uses schema definitions for advanced search field generation and self-description validation.
- [Connector](../../../../resource-sharing/resource-sharing-runtime/connector/doc/architecture.md) — the EDC Connector Adapter registers resource offerings and retrieves contract negotiation references.
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — inbound traffic passes through the Tier 1/Tier 2 Gateway. <!-- also relevant to: Security view -->

## Technical view

- **Catalogue Client Application Backend** is implemented as a Java backend application.
- **Catalogue Client Application UI** is implemented as an Angular frontend application.
- **Validation Backend** is implemented as a Java backend application.
- **Contract Consumption Adapter** is implemented as a Java backend application.

The search stack is split into a consumer/provider part and a centralised Governance Authority part. On the consumer/provider side, the CCA holds a local schema cache (synchronised by the Schema Synch Service) allowing it to validate advanced search parameters locally before sending to the Catalogue. A Spring Cloud API Gateway instance (Tier 1 Gateway) secures the connection towards the Governance Authority.

![TCV Static view — Catalogue Client Service](./media/image135.png)

## Security view

- All inbound requests to the CCA pass through the Tier 1/Tier 2 Gateway (Authorisation component).
- The CCA sends policy-filtered queries to the Catalogue — policy filtering happens at the Catalogue side (Policy Filter Service, Query Mapper Adapter).
- The Contract Consumption Adapter uses Tier 2 credentials for agent-to-agent communication when initiating contract negotiation.

Threat model: Status: not yet documented.

Secrets management: Status: not yet documented.

## Testing

Strategy: Status: not yet documented.

PSO validation status: Status: not yet documented.

Requirements traceability: Status: not yet documented.
