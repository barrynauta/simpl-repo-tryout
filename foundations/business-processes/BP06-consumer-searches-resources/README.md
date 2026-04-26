<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Foundations</a><br/>
        <a href="../README.md">Capability: Business Processes</a><br/>
            <strong>Service: BP06 — Consumer Searches Resources</strong><br/>
</p>
</div>

# BP06 – Consumer searches resources in data space catalogues

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram
> showing how this business process executes at runtime, with links
> to each participating solution.

## Overview

This business process covers the situation where a data space Consumer can search resources in the catalogue of one or multiple data spaces. Within the process the Consumer can search for resource descriptions, which can refer to data, application, or infrastructure resources. There are three types of ‘search’ available: quick search, federated search, and advanced search. Quick search: Use one or multiple search terms that are matched against any field in the resource description. Federated search: Perform searches across multiple data spaces simultaneously. Advanced search: Specify values for one or more attributes of the resource description to refine the search results. It includes the following main steps: Search in data space catalogues: The Consumer initiates a search in the data space catalogue using either a quick search, advanced search, or a federated search (searching multiple data space catalogues at once) within the same or another data space. To achieve this, the Consumer inputs the search terms relevant to their intended search. Execute query: The Governance Authority finds resource description matching the provided search terms within the data space's own catalogue or, in case of the federated search, within data space catalogues shared by other data spaces. Access the filtered search results and select one or more resources: The  Governance Authority provides the filtered search results to the participant’s system, showing only the resource description   they are permitted to access. The results of the  search are available to the Consumer , who can access and display the details of selected resource descriptions.

## Actors

The following actors are involved: Governance Authority Consumer

## Assumptions

The following assumptions are made: There is a mechanism in place to perform a quality rating of the resources based on its predefined quality rules.

## Prerequisites

The following prerequisites must be met to enable the process to occur: Dataspace is configured:   The  Governance Authority   has configured the catalogue with the corresponding vocabulary and schemas to have the general structure of a resource description, contract clauses, and other vital components (Business Process 2). Consumer onboarded: Before the Consumer can consume any resources to a data space they should have successfully completed the onboarding business process (Business Process 3A). End-User authenticated & authorised: The  End-User is authenticated and has the appropriate role and permissions to perform the steps in the process (Business Process 3B).

![BP06 figure 2](./media/BP06-figure-2.png)
*BP06 figure 2*

## Sub-processes

- [6.1 - A Consumer consults the returned resources of a search request](./61-consumer-consults-returned-resources-search-request.md)
- [6.2 - Search in data/application/infrastructure catalogue in another federated data space](./62-search-dataapplicationinfrastructure-catalogue-another-federated-data-space.md)
- [6.3 - A Consumer searches resources in the catalogues of a data space](./63-consumer-searches-resources-catalogues-data-space.md)
- [6.4 - The Governance Authority provides resource descriptions matching a search request](./64-governance-authority-provides-resource-descriptions-matching-search-request.md)

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp06-consumer-searches-resources-data-space-catalogues](https://simpl-programme.ec.europa.eu/book-page/bp06-consumer-searches-resources-data-space-catalogues)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
