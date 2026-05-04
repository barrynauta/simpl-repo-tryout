<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Samples</a><br/>
            <strong>Solution: fe-openapi-clients</strong><br/>
</p>
</div>

# fe-openapi-clients

Holding repository for **REST API definitions** (OpenAPI specs) of the IAA frontend services. Intended use is to serve as the input to a client-generation pipeline that produces typed clients (likely TypeScript / JS, possibly mocks) consumed by Simpl-Open frontends.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Status

Sparse upstream — only LICENSE + GitLab-boilerplate README in the cloned repo. Catalogued under `cross-cutting/samples/` because the repository is a **utility / generator input** rather than a production service: holds API definitions used to *generate* client code, with limited active development. Treat as a reference, not as a deployable component.

## Source

- <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-openapi-clients>
