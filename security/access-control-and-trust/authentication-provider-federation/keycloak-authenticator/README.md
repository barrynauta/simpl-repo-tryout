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

**Keycloak**-based OpenID Connect identity provider for Tier 1 (human-user) authentication. Manages users, roles, and IdP federation. Extended with a Simpl-built custom Keycloak SPI (`iaa/keycloak-authenticator`) that injects participant context — `client-roles`, `participant_id`, `credential_id`, `identity_attributes` — into Tier 1 JWT tokens.

Capability-map placement: `security / access-control-and-trust / authentication-provider-federation / tier-1-authentication-provider`. This solution and `tier-2-authentication-provider` together implement the **Authentication provider federation** business service (flag d-2: the capmap has a single business service for both tiers).

Provenance: deployed Keycloak (upstream Apache 2.0) **+ Simpl-built authenticator plugin** at `iaa/keycloak-authenticator` (EUPL 1.2). Compatible with **Keycloak 26.4**. The deployed artefact bundles upstream + plugin; downstream the Apache 2.0 governs the runtime, the plugin source is EUPL.

## Custom authenticator plugin (key features)

The plugin is packaged as a JAR loaded into Keycloak as an SPI. It enriches Keycloak authentication flows by:

- Calling the **Authentication Provider** service (Tier 2 backend, API v1) and the **Users & Roles** service (API v1) to resolve participant context.
- Fetching user authentication data from external Simpl services rather than relying solely on Keycloak's local user store.
- **Injecting roles, attributes, participant information, and credential IDs** into the Keycloak session — these become claims in the issued JWT.
- **Multi-realm** configuration support.
- Local development supported via Docker Compose + **Microcks** for mocking the upstream IAA APIs.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0 (Keycloak upstream).

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [BP03B Participant User and Roles Configuration](../../../../foundations/business-processes/BP03B-onboarding-participant-end-user/dynamic-view.md)


## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Custom authenticator plugin (Simpl-built, EUPL 1.2): <https://code.europa.eu/simpl/simpl-open/development/iaa/keycloak-authenticator>
- Upstream Keycloak: <https://github.com/keycloak/keycloak>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
