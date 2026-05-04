<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Shared libraries inventory</strong><br/>
</p>
</div>

# Shared libraries inventory

Cross-cutting view of every shared library placed in the catalogue: which dimension hosts it, which solutions consume it, and whether it is properly scoped or bundles too many concerns. Libraries are placed alongside their **primary consumer team's dimension** under a `common/` sub-folder, with the `cross-cutting/libs/` umbrella reserved for libraries that genuinely span dimensions or are language-runtime-specific.

## Inventory

| Library | Catalogue path | Hosting dimension | Source repo | Scope | Notes |
|---|---|---|---|---|---|
| **iaa-common** | [security/.../common/iaa-common](../security/access-control-and-trust/common/iaa-common/README.md) | Security | `iaa/common` | IAA team — auth/identity backend primitives | Placed alongside the IAA client stack. |
| **data-services-common** | [data/.../common/data-services-common](../data/supporting-data-services/common/data-services-common/README.md) | Data | `data1/common` | data1 team — 15-package aggregator | ⚠️ **Aggregates 15 unrelated packages** (HTTP/Feign, JWT auth, exceptions, ODRL/SD models, schema-sync clients, utilities). Candidate for upstream modularisation; see solution README. |
| **contract-billing-common** | [governance/.../common/contract-billing-common](../governance/contract-management/common/contract-billing-common/README.md) | Governance | `contract-billing/common` | Contract-billing team — 5-concern aggregator | ⚠️ Bundles exceptions, security/auth, HTTP client, error DTOs, utils. Narrower than data-services-common but still a candidate for finer modularisation. |
| **connector-model-common** | [integration/.../common/connector-model-common](../integration/resource-sharing/resource-sharing-runtime/common/connector-model-common/README.md) | Integration | `data1/common-adapter` | EDC adapter — connector model classes | Properly scoped: shared connector domain models. |
| **tier2-catalogue-client** | [security/.../authentication-provider-federation/common/tier2-catalogue-client](../security/access-control-and-trust/authentication-provider-federation/common/tier2-catalogue-client/README.md) | Security | `data1/common-tier2` | Tier-2 catalogue access client | Properly scoped: a Feign client. |
| **simpl-http-client** | [cross-cutting/libs/simpl-http-client](../cross-cutting/libs/simpl-http-client/README.md) | *Cross-cutting* | `iaa/simpl-http-client` | Secure HTTP/2 client (custom SSL/TLS, CRL validation, ephemeral-proof preflight) | Properly scoped. Used across dimensions. |
| **simpl-vue-components** | [cross-cutting/libs/simpl-vue-components](../cross-cutting/libs/simpl-vue-components/README.md) | *Cross-cutting* | `data1/simpl-vue-components` | Vue 3 design-system library — Tailwind theme, PrimeVue components, typography, icons (`@simpl/vue-components`) | Properly scoped. Used by every Simpl-Open frontend. |

## Placement rule

Libraries sit alongside their primary consumer team's dimension under a `common/` sub-folder. Two libraries qualify for `cross-cutting/libs/` instead — `simpl-http-client` (used by every backend regardless of dimension) and `simpl-vue-components` (used by every frontend). The team-named placement preserves provenance and makes the upstream owner discoverable from the catalogue path.

## Health flags

The two ⚠️-flagged aggregators (`data-services-common`, `contract-billing-common`) violate the modularity principle that Simpl-Open applies to its own runtime services. They are catalogued as single solutions today because the upstream repos are single artefacts; both are tracked as candidates for upstream modularisation. When a split happens, each module would become its own catalogue entry under its appropriate capability and the aggregator entries would be retired. See the per-solution READMEs for the full rationale.

## Cross-references

- [Agent composition](agent-composition.md) — how agents bundle solutions; libraries are linked transitively via the solutions that consume them.
- [Capability map](capability-map.md) — the dimension/capability tree that hosts each library's `common/` parent.
