---
id: sa:SA04
type: scenario-architecture
name: SA04 - Provider manages deployment scripts
since: r3.0
---

<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA04 — Provider Manages Deployment Scripts</strong><br/>
</p>
</div>

# SA04 - Provider manages deployment scripts

## Overview

This supporting activity covers the management of deployment scripts by a Provider, which supports the management of resource descriptions (BP05B) when adding or updating resource type specific metadata of an infrastructure resource. Upon the consumption of such an infrastructure resource (BP08), the deployment script is used for the provisioning and configuration of the infrastructure resource on a dedicated environment for the Consumer. During the post configuration process, the deployment script is used for actions such as deploying an application or loading data resources. Simpl-Open supports Infrastructure Providers in the management of deployment scripts by allowing them to: Consult and download the available deployment scripts. Consult the available VM templates. Create, update or delete a deployment script directly. Create or update a VM template by specifying its building blocks such as cloud environment configurations and post provisioning configurations (see SA04.01 for more details). This automatically generates a deployment script based on the provided building blocks. Delete a VM template: This automatically deletes the related deployment script, and hence makes it unavailable to link to a resource description. With the use of VM templates to create a deployment script, Simpl-Open hence provides mechanisms to configure and automatically provision VMs in multiple cloud providers, and provide a parametrisable approach to easily configure VMs to Infrastructure and Application Providers participating in the data space.

## Actors

The following actors are involved:   Infrastructure Provider

## Assumptions

None.

## Prerequisites

The following prerequisites must be fulfilled: Provider onboarded:  The  Provider  must be successfully onboarded (Business Process 3A).

## Sub-processes

- [4.1 - A Provider consults their own VM templates](./41-provider-consults-their-own-vm-templates.md)
- [4.2 - A Provider consults their own deployment scripts](./42-provider-consults-their-own-deployment-scripts.md)
- [4.3 - A Provider creates a new VM template](./43-provider-creates-new-vm-template.md)
- [4.4 - A Provider creates a new deployment script](./44-provider-creates-new-deployment-script.md)

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa04-provider-manages-deployment-scripts](https://simpl-programme.ec.europa.eu/book-page/sa04-provider-manages-deployment-scripts)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
