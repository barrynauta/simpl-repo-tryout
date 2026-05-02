<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Samples</a><br/>
            <strong>EJBCA Preconfig</strong><br/>
</p>
</div>

# EJBCA Preconfig

> ⚠️ The configuration script provided in this repository is intended for **development and testing only** and is not suited to be used in production.

This repository contains a script designed to automate the deployment and configuration of an EJBCA component within a Governance Authority Agent. It streamlines key setup tasks such as creating CAs, enabling the REST API, configuring end-entity profiles, and obtaining SuperAdmin certificates, all based on EJBCA's official configuration guides. The script is parameterised, packaged in a Docker container, and ensures that EJBCA starts up fully configured. The Docker container can be integrated into Helm-chart installations, and executed via Kubernetes `initContainers` to eliminate manual intervention.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Key features

- Idempotent: re-running on an already-configured EJBCA does nothing.
- Parameterised — driven by environment variables for CA names, profiles, and admin identities.
- Packaged as a Docker container; integrates into Helm charts via Kubernetes `initContainers`.
- Requires a service account with secret-management access for storing the SuperAdmin certificates.

## Used by

- [Identity Provider](../../../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) — the IdP relies on a fully configured EJBCA as its backing CA.
