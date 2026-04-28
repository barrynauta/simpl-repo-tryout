<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Supporting Data Services</a><br/>
            <a href="../README.md">Service: Data Orchestration</a><br/>
                <strong>Solution: Asset Orchestrator</strong><br/>
</p>
</div>

# Asset Orchestrator

Bridge between the Provider Connector and the Workflow Engine (Dagster). Exposes REST APIs to register, validate, and execute workflows associated with catalogue assets, so a Provider can declaratively bind a workflow definition to a self-described resource and have it executed automatically when a Consumer accesses the resource through the connector.

Capability-map placement: `data / supporting-data-services / data-orchestration / asset-orchestrator`. This solution implements the **Data orchestration** business service alongside the [Orchestration Platform](../orchestration-platform/README.md).

Provenance: built by Simpl. Java/Maven service deployed as part of the Provider Agent; participates in connector-driven data flows. Source repository: `code.europa.eu/simpl/simpl-open/development/orchestration-platform/asset-orchestrator`. Licence: EUPL 1.2.

## Key features

- REST API endpoints for workflow definition registration and management.
- Association of catalogue assets with workflows and their configurations.
- Validation of workflow configurations against schema before execution.
- Integration with the Workflow Engine (Dagster) for job submission and tracking.
- Storage and retrieval of workflow run history.
- Error handling using RFC 7807 *Problem Details* with structured logging.
- Dynamic workflow configuration with template variables.

## Typical flow

1. Provider Workflow Designer creates a workflow and a default configuration.
2. Provider creates a self-description for a resource that should trigger the workflow on consumption.
3. Provider creates an association between the resource and the workflow with configuration.
4. Consumer consumes the resource over the connector.
5. Asset Orchestrator submits the job to the orchestration platform.
6. Asset Orchestrator tracks execution status and stores the run history.

## Participates in

- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/README.md)
- [BP09B Consumer receives a data processing service](../../../../foundations/business-processes/BP09B-consume-data-via-application/README.md)
- [SA01 Data orchestration](../../../../foundations/business-processes/SA01-data-orchestration/README.md)

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/asset-orchestrator>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
