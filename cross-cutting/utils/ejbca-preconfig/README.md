<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Utils</a><br/>
            <strong>EJBCA Preconfig</strong><br/>
</p>
</div>

# EJBCA Preconfig

Dockerised script that bootstraps a fresh EJBCA instance inside a Governance Authority Agent: creates Certification Authorities, enables the REST API, configures end-entity profiles, and obtains SuperAdmin certificates. Designed to run as a Kubernetes **initContainer** alongside the EJBCA pod; the script is idempotent and is a no-op once EJBCA is already configured.

> ⚠️ Intended for **development and testing only** — not suited for production deployments.

Provenance: built by Simpl. Source repository: `iaa/ejbca-preconfig`. Owner: IAA team. Licence: EUPL 1.2.

## Key features

- Idempotent: re-running on an already-configured EJBCA does nothing.
- Parameterised — driven by environment variables for CA names, profiles, and admin identities.
- Packaged as a Docker container; integrates into Helm charts via Kubernetes `initContainers`.
- Requires a service account with secret-management access for storing the SuperAdmin certificates.

## Used by

- [Identity Provider](../../../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) — the IdP relies on a fully configured EJBCA as its backing CA.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `iaa-2.11.x/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/iaa/ejbca-preconfig>
