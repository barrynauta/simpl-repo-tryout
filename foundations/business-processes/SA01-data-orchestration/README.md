<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA01 — Data orchestration used by a Participant</strong><br/>
</p>
</div>

# SA01 – Data orchestration used by a Participant

## Overview

This supporting activity enables _Providers_ and _Consumers_ to design, execute,
and monitor traceable and repeatable data processing workflows, facilitating
consistent and auditable data transformation activities within the data space.

These workflows orchestrate a sequence of services, allowing _Participants_ to
automate complex data operations in a structured and governed way.

In the case of the _Provider_, the data orchestration capability can also be
used for data preparation workflows that, for example, can include
anonymisation, pseudonymisation, or data cleansing steps.

Once triggered, the workflow executes each defined step in order, processing
selected data sets and delivering outputs to user-defined destinations according
to the configured logic.

The selection and configuration of processing services to be included in each
workflow remain the responsibility of the individual _Participant_, based on
their specific use case and intended outcomes.

## Actors

- _Consumer_
- _Provider_

## Assumptions

- Simpl-Open will not inspect or validate the internal business logic configured by the _Participants_ within their workflows.
- The services that a _Participant_ can use are either built-in to Simpl-Open, defined by the _Participant_ itself, or selected in the application catalogue.

## Prerequisites

- **Participant onboarded** — the _Participant_ should have successfully completed the onboarding business process (BP03A) before they can trigger the orchestration.
- **End-User authentication and authorisation** — the End-User must be authenticated and possess the necessary roles and permissions to execute the process steps (BP03B).

![SA01 figure 1](./media/SA01-figure-1.png)
*SA01 figure 1 — overview diagram*

## Process steps

### Trigger — data orchestration

The _Participant_ initiates the orchestration process. It is triggered by an
End-User who intends to define a new workflow, manage, execute, or monitor an
existing one. This step acts as the entry point to the orchestration lifecycle.

### SA01.01 Create a workflow

The _Participant_ initiates the creation of a new workflow. They define the
logical sequence of services, select the input sources, configure the triggering
mechanism, and specify the expected outputs. Once all parameters are set, the
workflow is available for execution.

### SA01.02 Update a workflow

The _Participant_ selects an existing workflow and modifies its configuration to
meet new requirements. This may include changing the service sequence, updating
data sources or outputs, adjusting the logic, or modifying the trigger. After
applying the changes, the updated workflow replaces the previous version. A
versioning system ensures that each modification is tracked, allowing rollback
to previous states and maintaining an auditable history of changes.

### SA01.03 Delete a workflow

The _Participant_ identifies a workflow that is no longer needed and deletes it
from the system. If the workflow has no active dependencies, it is deleted: the
workflow will no longer be available for future execution, and its definition
will be removed, while past logs and history are retained for auditability and
traceability. If there are any dependencies, deletion is prevented and the
_Participant_ is notified of the existing dependencies.

### SA01.04 Execute a workflow

The _Participant_ triggers the execution of a workflow, either manually or as
per trigger in the workflow. The workflow runs according to its defined logic.
If any of the services included in the workflow need extra information (such as
choosing a file or entering a parameter), the _Participant_ may be asked to
provide it before execution begins. Execution results for each step are logged
and made available for monitoring.

If a workflow is deleted but still referenced (e.g. triggered upon dataset
consumption), an error will be thrown because the workflow cannot be found. In
such cases, no data will be disclosed and the transfer will not occur, but an
error will be returned to the _Consumer_ and/or _Provider_. This ensures that
the middleware remains robust.

### SA01.05 Monitor a workflow execution

The _Participant_ can observe the execution status in real time or access
historical records of past runs. The monitoring functionality includes visual
indicators of the current status (e.g. running, completed, failed) and detailed
logs for each step or service. In the event of failures or bottlenecks, the
End-User can inspect log traces to identify the root cause and take corrective
action.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 1.1 | Participant consults their own data orchestration workflows. | [11-…](./11-participant-consults-their-own-data-orchestration-workflows.md) |
| 1.2 | Participant creates a new data orchestration workflow. | [12-…](./12-participant-creates-new-data-orchestration-workflow.md) |
| 1.3 | Participant creates a new version of a data orchestration workflow. | [13-…](./13-participant-creates-new-version-data-orchestration-workflow.md) |
| 1.4 | Participant deletes a data orchestration workflow. | [14-…](./14-participant-deletes-data-orchestration-workflow.md) |
| 1.5 | Participant executes a data orchestration workflow. | [15-…](./15-participant-executes-data-orchestration-workflow.md) |
| 1.6 | Participant monitors and accesses data orchestration workflow execution logs. | [16-…](./16-participant-monitors-and-accesses-data-orchestration-workflow-execution-logs.md) |

> **Note on numbering:** the source site uses bare `1.x` IDs (and `1x-…` slugs)
> for these HLRs, not `SA01.x`. The local files mirror that.

Detail pages on the public site:

- 1.1 → [11-participant-consults-their-own-data-orchestration-workflows](https://simpl-programme.ec.europa.eu/book-page/11-participant-consults-their-own-data-orchestration-workflows)
- 1.2 → [12-participant-creates-new-data-orchestration-workflow](https://simpl-programme.ec.europa.eu/book-page/12-participant-creates-new-data-orchestration-workflow)
- 1.3 → [13-participant-creates-new-version-data-orchestration-workflow](https://simpl-programme.ec.europa.eu/book-page/13-participant-creates-new-version-data-orchestration-workflow)
- 1.4 → [14-participant-deletes-data-orchestration-workflow](https://simpl-programme.ec.europa.eu/book-page/14-participant-deletes-data-orchestration-workflow)
- 1.5 → [15-participant-executes-data-orchestration-workflow](https://simpl-programme.ec.europa.eu/book-page/15-participant-executes-data-orchestration-workflow)
- 1.6 → [16-participant-monitors-and-accesses-data-orchestration-workflow-execution-logs](https://simpl-programme.ec.europa.eu/book-page/16-participant-monitors-and-accesses-data-orchestration-workflow-execution-logs)

## Source page metadata

- **Author:** Annalie te Hofste
- **Published:** 19 December 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa01-data-orchestration-used-participant](https://simpl-programme.ec.europa.eu/book-page/sa01-data-orchestration-used-participant)

## Touches

- (auto-inferred — verify) [`../../../data/`](../../../data/README.md)
