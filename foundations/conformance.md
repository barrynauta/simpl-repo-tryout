<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Standards conformance</strong><br/>
</p>
</div>

# Standards conformance

Cross-cutting view of which Simpl-Open solutions claim conformance to which dataspace standards. The intended audience is dataspace owners and integrators evaluating Simpl-Open against external trust frameworks (Gaia-X, IDSA, DSSC, eIDAS).

> **🚧 Placeholder — to be populated.**
>
> This page is the planned home for a per-solution conformance matrix:
>
> - **DSP (Dataspace Protocol, IDSA)** — version supported, profile claimed.
> - **Gaia-X** — Trust Framework alignment, Self-Description schema compliance, Compliance Service interaction.
> - **DSSC (Data Spaces Support Centre)** — interoperability blueprint touchpoints.
> - **eIDAS / EUDI Wallet** — credential format support, attribute exchange.
> - **W3C VC / DID** — verifiable-credential issuance and verification claims.
>
> The data has to be collected per-solution from the relevant upstream repos and the FTA spec, then surfaced as both a top-level matrix on this page and an inline "Standards conformance" section in each connector-touching solution README.
>
> This work is tracked as a TODO in the Notion FTA-migration audit. Update this page once data starts landing.

## Pages that will feed this matrix

The following solutions are the primary candidates for conformance declarations (connectors, catalogue, IAA, signing, wallet):

- [integration/resource-sharing/resource-sharing-runtime/connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) — DSP/IDSA connector implementation (EDC fork).
- [integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) — Simpl adaptation layer.
- [integration/resource-discovery/resource-catalogue/xfsc-federated-catalogue](../integration/resource-discovery/resource-catalogue/xfsc-federated-catalogue/README.md) — Gaia-X federated catalogue.
- [security/access-control-and-trust/authentication-provider-federation/](../security/access-control-and-trust/authentication-provider-federation/README.md) — Tier 1/Tier 2 authentication, mTLS, ephemeral-proof handshake.
- [security/access-control-and-trust/identity-provider-federation/identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) — eIDAS/EUDI alignment.
- [security/credential-management/](../security/credential-management/README.md) — VC issuance, signing, wallet.
- [data/semantics-and-vocabulary/schema-management/](../data/semantics-and-vocabulary/schema-management/README.md) — SD-Tooling, schema validation against Gaia-X SD shapes.

## Cross-references

- [eIDAS integration](eidas-integration.md) — how the Simpl identity model maps onto eIDAS / EUDI.
- [Connector protocol](connector-protocol.md) — DSP/IDSA concepts as used across agents.
- [Interoperability](interoperability.md) — semantic and technical interoperability standards used in Simpl.
