# User Guide


## Table of Contents
* [Workflow Observability](Observability.md)
    * [Workflow Execution Logs](Observability.md#workflow-execution-logs)
    * [Workflow Status and Logging on UI](Observability.md#accessing-workflow-execution-status-and-logs-current-and-historical-runs)

* [Workflow Triggering](Triggering.md)
    * [Time-based scheduling](Triggering.md#time-based-scheduling)
    * [Partition scheduling](Triggering.md#calendar-based-partition-scheduling)
    * [Manual Triggering](Triggering.md#manual-triggering)
    * [Event Based - Dataset Change on S3 Storage](S3StorageTriggering.md)

* [Workflow Discovery](Discovery.md)
    * [Dagster UI](Discovery.md#discovering-workflows-via-dagster-ui)
    * [GraphQL API](Discovery.md#discovering-workflows-via-graphql-api)

* [Workflow Details](Details.md)
    * [Dagster UI](Details.md#viewing-workflow-details-via-dagster-ui)
    * [GraphQL API](Details.md#viewing-workflow-details-via-graphql-api)

---

> **Notes**
>
> All user-facing interactions, such as navigating the UI, monitoring jobs, triggering runs and inspecting logs, are performed through the Dagster Webserver.
> Since this repository focuses on deployment configuration and not the Dagster application itself, the full functional usage of Dagster follows the official product documentation:
> - [Dagster Webserver User Manual](https://docs.dagster.io/guides/operate/webserver)
> - [Dagster Official User Guide](https://docs.dagster.io/)
 
