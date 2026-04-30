<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Governance Authority Agent</strong><br/>
</p>
</div>

# Governance Authority Agent

Master Helm chart that deploys a complete **Governance Authority** Simpl-Open Agent. Bundles the central-authority modules: onboarding, identity provider (with EJBCA as CA), federated catalogue, schema management, signer, contract template store, monitoring, plus the shared infrastructure (OpenBao, Postgres, Kafka).

Provenance: built by Simpl. Source repository: `agents/governance-authority`. Owner: Cross-team. Licence: EUPL 1.2.

## Modules composed (illustrative)

- [Onboarding](../../../governance/participant-management/onboarding/onboarding-service/README.md)
- [Users & Roles](../../../governance/participant-management/user-roles/users-roles/README.md)
- [Identity Provider](../../../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md)
- [Security Attributes Provider](../../../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md)
- [Authorisation](../../../security/access-control-and-trust/authorisation/authorisation/README.md)
- [Simpl Catalogue (XFSC FC)](../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md)
- [Schema Management Service](../../../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md)
- [Signer Service](../../../security/credential-management/signing/signer-service/README.md)
- [Monitoring Service](../../../administration/observability/dashboarding/monitoring-service/README.md)
- [EJBCA Preconfig](../../utils/ejbca-preconfig/README.md) (init-container)
- [Common Components](../common-components/README.md)

## Documentation

- [deployment-guide.md](deployment-guide.md) — full deployment procedure (ArgoCD and manual paths), prerequisites including the common-components dependency, post-deploy initialisation, and a step-by-step recovery for the **Identity Provider failure** race condition (drop+recreate the EJBCA and identity-provider Postgres DBs). Sourced from `agents/governance-authority/documents/deployment-guide/`.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `iaa-2.11.x/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/agents/governance-authority>
