<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Resource Management</a><br/>
            <a href="../README.md">Service: Metadata Description</a><br/>
                <strong>Solution: Sd Tooling</strong><br/>
</p>
</div>

# SD Tooling

REST + UI services that let providers create, validate, and publish **self-descriptions** for their resources, leveraging schemas from the [Schema Management Service](../../../../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md). Exposes the active SHACL schema to the frontend so that input forms can be rendered dynamically per resource type.

Capability-map placement: `governance / resource-management / metadata-description / sd-tooling`. This solution implements the **Metadata description** business service.

Provenance: built by Simpl. Source repositories: `data1/sdtooling-api-be` (backend, Java 21 / Maven 3.9+) + `gaia-x-edc/simpl-sd-ui` (Astro-based frontend). SD Creation Tool is built on XFSC SD Tooling (Eclipse XFSC). Licence: EUPL 1.2.

## Key features

- REST endpoints for **generation, validation, and publication** of self-descriptions.
- **Schema-driven UI** — backend exposes the SHACL schema, the frontend renders fields dynamically against it.
- **Access and usage policies** — APIs to define ODRL policies attached to assets.
- **Resource Address management** — capture the source-side endpoint where the asset physically lives.
- **Asset registration on the Provider Connector** — once a self-description is validated, technical attributes (DID, asset ID, dataspace endpoint) are added and the asset is registered.
- **Automated publication** — validated SDs are pushed to the [Simpl Catalogue](../../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md).
- Logging, audit, error handling.

## Publication flow (UI)

The SD UI walks the user through the form, then on submit performs three sequential calls — all over the **Tier-1 Gateway**:

1. **`enrichAndValidate`** — backend validates the document and populates derived fields.
2. **`signing`** — the validated document is signed by the [Signer Service](../../../../security/credential-management/signing/signer-service/README.md).
3. **`publishing`** — the signed document is published to the catalogue.

## Frontend configuration

| Variable | Purpose |
|----------|---------|
| `PUBLIC_AUTH_KEYCLOAK_SERVER_URL` / `_REALM` / `_CLIENT_ID` | Keycloak OAuth (Tier 1 IdP) |
| `PUBLIC_CREATION_WIZARD_API_URL` (+ `_API_VERSION` = `v2`) | SD Tooling backend behind Tier-1 Gateway |
| `PUBLIC_SIGNER_URL` | Signer endpoint behind Tier-1 Gateway |

(No trailing slashes.)

## Deployment topology

Deployed on the **Provider Agent**. The backend communicates with the **Tier-2 Gateway on the Governance Authority Agent** to execute the publication step, and locally with the **Provider Connector** (via the [EDC Connector Adapter](../../../../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md)) to register the asset before publication.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)

## Source code

- Backend: <https://code.europa.eu/simpl/simpl-open/development/data1/sdtooling-api-be>
- Frontend: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-sd-ui>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
