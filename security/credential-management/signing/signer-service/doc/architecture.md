Source: functional-and-technical-architecture-specifications.md, sections 4.3.1 (ACV Static — Signer Service), 6.1.2 (TCV Static — Signer Service).

# Signer Service — architecture

## Business view

The Signer Service manages the digital signing of self-descriptions and contracts, ensuring their authenticity, integrity, and non-repudiation. When a provider completes a self-description, it is signed using the provider's private key to verify identity and prevent tampering. Once signed, the self-description is ready for distribution and publication to the Catalogue. The Signer Service is also used by the VC Issuer to sign usage contracts cryptographically.

Capability-map placement: Security dimension → Credential management capability → Signing business service.

![ACV Static view — Signer Service](./media/image55.jpeg)

## Data view

The Signer Service processes signing requests and returns signed artefacts. It does not persist signed documents itself — signed self-descriptions are forwarded to the Catalogue; signed contracts are stored in the Wallet via the VC Issuer.

## Application view

### Internal decomposition

**Signer Service:**
- Receives signing requests from callers (SD Tooling, VC Issuer).
- Applies cryptographic signatures using the caller's private key.
- Returns signed artefacts (self-descriptions, contracts) to the requestor.
- Provides non-repudiation and authenticity guarantees for all signed artefacts.

### Key integrations

- [SD Tooling](../../../../../governance/resource-management/metadata-description/sd-tooling/doc/architecture.md) — uses the Signer to apply cryptographic signatures to self-descriptions before publication to the Catalogue; the provider's private key is used to verify identity and prevent tampering.
- [VC Issuer](../../../vc-issuance-verification/vc-issuer/doc/architecture.md) — uses the Signer to apply cryptographic signatures to usage contracts, ensuring non-repudiation and authenticity of issued verifiable credentials.
- [Simpl Catalogue](../../../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/doc/architecture.md) — receives signed self-descriptions published after signing; validates signature integrity as part of the publication process.

## Technical view

- The **Signer Service** component is implemented with XFSC Organisation Credential Manager (OCM).

Source repository: `gaia-x-edc/simpl-signer`.

Deployment: deployed in Provider Nodes (for self-description signing) and Governance Authority Agents / shared infrastructure (for contract signing in the VC Issuer workflow).

![TCV Static view — Signer Service](./media/image145.jpeg)

## Security view

- The Signer Service holds or accesses private keys; key management and secure storage of private key material are critical security concerns.
- Cryptographic signatures applied by the Signer enable tamper-detection: any modification to a signed artefact invalidates its signature.
- Non-repudiation: signed contracts and self-descriptions provide cryptographic proof of originator identity.
- The Signer Service is accessed only by authorised internal components (SD Tooling, VC Issuer); it is not directly exposed via a public API.

Threat model: Status: not yet documented.

Secrets management: Status: not yet documented.

## Testing

Strategy: Status: not yet documented.

PSO validation status: Status: not yet documented.

Requirements traceability: Status: not yet documented.
