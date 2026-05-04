<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Participant management</a><br/>
            <a href="../README.md">Service: User roles</a><br/>
                <strong>Solution: fe-users-roles</strong><br/>
</p>
</div>

# fe-users-roles

Frontend (Angular) for the **User-roles** business service. UI used by Provider/Consumer operators and applicants to manage end-user roles, request roles, map identity attributes, and create applicant accounts during onboarding.

> **Scope note.** This folder represents the frontend solution. Most documentation under `doc/` and `api/` was originally bundled with the backend repository (`iaa/users-roles`) and is preserved here for reference until a dedicated backend solution folder is added — see [Source code](#source-code) below for the upstream backend repository.

Capability-map placement: `governance / participant-management / user-roles / fe-users-roles`. This solution implements the frontend half of the **User-roles** business service.

Provenance: built by Simpl. Source repositories: `iaa/users-roles` (backend, Java 21 / Maven 3.9+) and `iaa/fe-users-and-roles` (frontend). Licence: EUPL 1.2.

## Key features

- **Lifecycle management** for users, roles, and role-requests: create, update, search/filter/paginate.
- **Role-request workflow** for end-users to request a new role within a participant.
- **Identity-attribute mapping**: manage assignable identity attributes associated with each role.
- **User-role assignment**: track which users carry which roles, and apply attribute-based propagation.
- Java 21 + Spring stack; Helm 3.19 for deployment; Postgres for persistence.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [BP03B Participant User and Roles Configuration](../../../../foundations/business-processes/BP03B-onboarding-participant-end-user/dynamic-view.md)
- [BP03C End User Role Request](../../../../foundations/business-processes/BP03C-end-user-role-request/dynamic-view.md)


## API

[`api/`](api/README.md) — 3 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `frontend/` (4 files), `iaa-2.11.x/` (1 file), `installation-guide/` (2 files), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Frontend (this folder): <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-users-and-roles>
- Backend (upstream — no dedicated catalogue folder yet): `code.europa.eu/simpl/simpl-open/development/iaa/users-roles`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
