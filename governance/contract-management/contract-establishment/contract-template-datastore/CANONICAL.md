# Canonical Location

This is an **interim placement** — implemented by a generic static-file server while the dedicated contract-template datastore is on the roadmap.

The interim implementation lives at:

<https://code.europa.eu/simpl/simpl-open/development/data1/simpl-files>

Per the PSO mapping spreadsheet, this app-service is labelled `contract-template-datastore-temporary` with the note: *"Workaround to make the SD Tooling work while waiting for the real contract template datastore."* The static NGINX server hosts contract and SLA template JSON files consumed by the SD-Tooling frontend during self-description creation.

When the dedicated datastore is built, this `CANONICAL.md` and the sibling `.canonical.yaml` should flip to the new repository's URL.

Status: `prototype-interim`.
