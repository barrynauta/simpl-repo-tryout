Source: source repo `data-services/field-level-pseudo-anonymisation` (README.md + documents/user-manual/user-manual.md). FTA spec, §6.5 Data processing capability and §3 change log "anonymisation services added to ACV Static — Data Orchestration Service".

# Field-Level Pseudo-Anonymisation — architecture

## Business view

Privacy-preserving transformation applied at the **field (column) or PII-entity level**. Two operating modes:

- **Structured data** — column-wise pseudonymisation on pandas DataFrames loaded from CSV.
- **Unstructured data** — PII detection and pseudonymisation in free-form text.

Unlike its sibling [Dataframe-Level Anonymisation](../../dataframe-level-anonymisation/doc/architecture.md), field-level pseudonymisation is **reversible**: paired depseudonymisation jobs can recover original values if the protected key material is still available. This makes it suitable for use cases that require linkage or auditing while keeping data outside the scope of GDPR personal-data handling for normal day-to-day processing.

Capability-map placement: Data dimension → Data processing capability → Anonymisation and pseudonymisation business service. Like its sibling, functionally a Data Processing service per FTA; physically a Dagster code-location.

**Business processes supported:**
- [SA02 Data processing services used by a Participant](../../../../foundations/business-processes/SA02-data-processing-services/README.md), sub-process *2.1 Participant pseudonymises a dataset*.

**Pseudonymisation vs anonymisation (per the source user manual):**

| Aspect | Pseudonymisation (this service) | Anonymisation (sibling service) |
|--------|---------------------------------|--------------------------------|
| GDPR scope | **Still personal data** | Out of GDPR scope (irreversible) |
| Reversibility | **Reversible** with key | Irreversible |
| Use cases | Internal linking, longitudinal studies | Public release, regulatory submission |

## Data view

**Inputs** —
- Structured: CSV files / pandas DataFrames; column-wise transformations driven by per-column technique config.
- Unstructured: text documents; spaCy + Scrubadub identify PII spans (PERSON, EMAIL, LOC, ORG, …) before transformation.

**Outputs** —
- Transformed dataset (CSV or text), plus a **metrics output** (Dagster dual-output ops emit data + run metrics).
- For encrypted fields, the **key reference / Vault path** is recorded in metadata for downstream depseudonymisation.

**Per-field techniques:**

| Technique | Reversible | Notes |
|-----------|------------|-------|
| `hash` | No | Deterministic, allows linkage but not recovery |
| `encrypt` | **Yes**, with the Vault key | Most flexible; needs key management |
| `redact` | No | Field replaced with a placeholder |
| `replace` | No | Field replaced with a fixed surrogate |
| `retain` | n/a | Pass-through (used for non-PII columns) |

## Application view

### Internal decomposition

Dagster code-location loaded into the agent's Dagster instance via gRPC (workspace.yaml entry):

```yaml
load_from:
  - grpc_server:
      host: field-level-pseudo-anonymisation
      port: 4000
      location_name: field-level-pseudo-anonymisation
```

**Ops** — column-wise (`hash_column`, `encrypt_column`, `redact_column`, `replace_column`, `retain_column`) and unstructured (`detect_pii_text`, `pseudonymise_text`).

**Jobs** —
- `anonymize_pseudonymize_structured_job` — DataFrame in / DataFrame + metrics out.
- Depseudonymisation jobs that reverse `encrypt_*` operations using keys retrieved from Vault.
- Equivalent text-flavour jobs for unstructured input.

### Key integrations

- [Orchestration Platform](../../../supporting-data-services/data-orchestration/orchestration-platform/doc/architecture.md) — Dagster engine; loads the code location, runs jobs, surfaces in Dagit.
- **HashiCorp Vault** — key management for encrypted (reversible) transformations. The transit engine holds the keys; the code location requests encrypt/decrypt operations through Vault rather than handling raw key material.
- [Asset Orchestrator](../../../supporting-data-services/data-orchestration/asset-orchestrator/README.md) — binds catalogue assets to pseudonymisation jobs.
- spaCy models — bundled per language for unstructured PII detection (18+ languages: English, German, French, Spanish, …).
- [Common Logging (Python)](../../../../cross-cutting/libs/common-logging-python/README.md) — structured logging.

## Technical view

- **Language**: Python 3.12+.
- **Package manager**: `uv` (recommended) — `uv sync --locked` reproduces the lock file exactly.
- **PII detection**: Scrubadub + spaCy.
- **Encryption**: HashiCorp Vault (transit engine).
- **Packaging**: container image hosted in `code.europa.eu:4567` registry; Helm chart deploys it as a Dagster user-code sidecar.
- **Local dev stack** (per source): `docker-compose up -d` from `../dagster-dev-local` brings up Dagster + PostgreSQL + Vault.

**Prerequisites:**

```text
Required
  Python 3.12+
  uv package manager
  Dagster webserver + daemon
  PostgreSQL 12+ (Dagster backend)
  HashiCorp Vault with encryption keys configured
  Access to private GitLab registry (code.europa.eu:4567)

For production
  Kubernetes 1.24+
  Helm 3.9+
  ArgoCD (optional, for GitOps deployments)
```

## Security view

- **Key management** — encryption keys live in **Vault** and are never seen by the code location directly; encrypt/decrypt operations are remote-procedure calls against Vault's transit engine.
- **Reversibility = liability** — pseudonymised data is still personal data under GDPR Article 4(5). The user manual is explicit: the mapping/key must be stored separately and protected by robust controls; access must be logged and strictly limited.
- **Run isolation** — each Dagster run is an ephemeral Kubernetes job.
- **Audit trail** — Dagster dual-output ops emit per-run metrics with technique-by-column counters, allowing offline audit of which fields were transformed how.
- **Logging** — flows into [Monitoring Service](../../../../administration/observability/dashboarding/monitoring-service/README.md) via the Python common-logging library.

Threat model: not yet documented.

Secrets management: HashiCorp Vault, transit engine for encryption keys; agent-level Kubernetes secrets for Vault auth credentials.

## Testing

Strategy: extensive unit-test coverage per op (`tests/test_encrypt_structured.py` etc.); pytest markers (`-m security`, `-m "not slow"`); coverage report via `uv run pytest --cov=src --cov-report=html`. CI/CD pipeline runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
