Source: source repo `data-services/dataframe-level-anonymisation` (README.md + documents/user-manual/User Manual.md). Functional and Technical Architecture spec, §6.5 Data processing capability and the change-log entry "anonymisation services added to ACV Static — Data Orchestration Service".

# Dataframe-Level Anonymisation — architecture

## Business view

Privacy-preserving transformation applied at the **dataset (DataFrame) level**. Designed for structured tabular data (CSV → pandas), it implements the three canonical statistical-disclosure-control models — **k-anonymity**, **l-diversity**, **t-closeness** — to ensure that sensitive attributes cannot be used to re-identify individuals within a dataset. Anonymisation is **irreversible** by design: there is no de-anonymisation counterpart in this code location.

Capability-map placement: Data dimension → Data processing capability → Anonymisation and pseudonymisation business service. Functionally a Data Processing service per the FTA spec; physically a Dagster code-location deployed alongside the [Orchestration Platform](../../../supporting-data-services/data-orchestration/orchestration-platform/doc/architecture.md) on Provider and/or Consumer Agents.

**Business processes supported:**
- [SA02 Data processing services used by a Participant](../../../../foundations/business-processes/SA02-data-processing-services/README.md), sub-process *2.2 Participant anonymises a dataset*.

**Privacy-model summary:**

| Model | Guarantees | Failure mode |
|-------|------------|--------------|
| **k-anonymity** | Each quasi-identifier group has ≥ k indistinguishable rows | Vulnerable to homogeneity and background-knowledge attacks if used alone |
| **l-diversity** | At least *l* well-represented sensitive values per equivalence class | Mitigates homogeneity but not skewness |
| **t-closeness** | Sensitive-attribute distribution within each class is within *t* of the global distribution | Most robust of the three; computationally heaviest |

The user manual is explicit about the **privacy/utility trade-off** and known cautions: small datasets force aggressive suppression/generalisation; suppressed records skew distributions; correlations between quasi-identifiers and sensitive attributes can survive de-identification. K-anonymity alone is *not* sufficient — pair with l-diversity or t-closeness.

## Data view

**Input** — pandas DataFrame loaded from CSV at a configurable input path. Attributes must be classified into:

- **Identifiers** — direct uniques (name, SSN, email). Removed or pseudonymised before anonymisation.
- **Quasi-identifiers** — indirect (zip, DoB, gender). Generalised or suppressed.
- **Sensitive attributes** — protected values (medical condition, salary). Subject to l-diversity / t-closeness guarantees.

**Output** — anonymised DataFrame written back to CSV at a configurable output path, plus an **anonymisation metrics report** summarising the achieved privacy guarantees.

**Generalisation hierarchies** — supplied per quasi-identifier (e.g. `gender → simpl_gender`, `age → simpl_age`) and applied to broaden values when needed to meet the configured *k*.

## Application view

### Internal decomposition

The repository is a **Dagster code-location** packaged as a Docker image and loaded into the agent's Dagster instance at runtime via the workspace gRPC protocol.

Three jobs, each a sequence of Dagster ops:

- **`k_anonymity_job`** — `read_csv_to_df → preview_dataframe → apply_k_anonymity → preview_dataframe → write_df_to_csv`
- **`l_diversity_job`** — same shape with `apply_l_diversity` in the middle.
- **`t_closeness_job`** — same shape with `apply_t_closeness` in the middle.

Each algorithmic op accepts an explicit configuration block: identifier columns, sensitive attributes, quasi-identifiers, the privacy parameter (k / l / t), suppression level, and generalisation hierarchies.

### Key integrations

- [Orchestration Platform](../../../supporting-data-services/data-orchestration/orchestration-platform/doc/architecture.md) — Dagster engine that loads this code location, runs the jobs, and surfaces them in the Dagit UI.
- [Asset Orchestrator](../../../supporting-data-services/data-orchestration/asset-orchestrator/README.md) — binds catalogue assets to anonymisation jobs so they fire automatically on Consumer access.
- Object storage (MinIO / S3) — primary input/output sink; bound to the Agent at deploy time.
- [Common Logging (Python)](../../../../cross-cutting/libs/common-logging-python/README.md) — structured-log emission into the Monitoring Service stream.

## Technical view

- **Language**: Python 3.12+.
- **Framework**: Dagster (ops + jobs); pandas for DataFrame manipulation.
- **Packaging**: container image + Dagster `workspace.yaml` that points the Dagster daemon at the code-location's gRPC server.
- **Deployment**: Helm chart adding the code location as a sidecar to the main Dagster deployment via CI/CD.

**Prerequisites** (per source guide):

```text
Kubernetes cluster with Helm 3.9+
Argo / ArgoCD for deployment management
Docker registry access (image build/pull)
PostgreSQL (Dagster metadata DB)
kubectl with proper context
```

The full deployment procedure lives in `documents/deployment-guide/Deployment Guide.md` in source.

## Security view

- **Run isolation** — each Dagster run executes as an ephemeral Kubernetes job; no shared mutable state between runs.
- **Provenance** — every run is tagged to the container-image digest of the deployed code-location, giving full audit traceability.
- **No reversible material** — by definition this code location does not store or use any key that would allow re-identification. (The pseudonymisation counterpart is the [Field-Level Pseudo-Anonymisation](../../field-level-pseudo-anonymisation/doc/architecture.md) code location.)
- **Logging** — error handling, validation failures, and completion metrics flow into the agent's [Monitoring Service](../../../../administration/observability/dashboarding/monitoring-service/README.md) via the Python common-logging library.

Threat model: not yet documented.

Secrets management: not applicable for the anonymisation jobs themselves; storage credentials inherited from the Dagster deployment.

## Testing

Strategy: unit tests over each algorithmic op (k-anonymity / l-diversity / t-closeness) plus integration tests via the Dagster `execute_in_process` test harness. CI/CD pipeline runs unit tests, SAST (SonarQube), and security tests (Fortify) on every commit.

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
