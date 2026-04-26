<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access Control And Trust</a><br/>
            <a href="../README.md">Service: Authentication Provider Federation</a><br/>
                <strong>Solution: Tier 1 Authentication Provider</strong><br/>
</p>
</div>

# Tier 1 Authentication Provider

Keycloak-based OpenID Connect identity provider for Tier 1 (human user) authentication. Manages users, roles, and IdP federation. Extended with a custom Keycloak SPI that adds custom claims (client-roles, participant_id, credential_id, identity_attributes) to Tier 1 JWT tokens.

Capability-map placement: `security / access-control-and-trust / authentication-provider-federation / tier-1-authentication-provider`. This solution and `tier-2-authentication-provider` together implement the **Authentication provider federation** business service (flag d-2 in step 3 checkpoint: the capmap has a single business service for both tiers).

Provenance: built on top of upstream **Keycloak** (Apache 2.0) with a Simpl-built custom authenticator plugin (`iaa/keycloak-authenticator`). Licence: Apache 2.0 (Keycloak upstream). Provenance: [TO VERIFY] — the overall solution is Keycloak-based; the custom plugin is EUPL. The Keycloak upstream licence governs the deployed artefact.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0 (Keycloak upstream).

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [BP03B Participant User and Roles Configuration](../../../../foundations/business-processes/BP03B-onboarding-participant-end-user/dynamic-view.md)

## Source code

- Custom authenticator plugin: `code.europa.eu/simpl/simpl-open/development/iaa/keycloak-authenticator`
- Upstream Keycloak: `https://github.com/keycloak/keycloak`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
