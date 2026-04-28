<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP06 — Consumer searches resources</strong><br/>
</p>
</div>

# BP06 – Consumer searches resources in data space catalogues

This business process describes how a data space **Consumer** searches for resources (data, applications, or infrastructure) within the catalogues of one or multiple data spaces.

## Actors

-   **Consumer:** The participant seeking resources.
-   **Governance Authority:** The entity managing the catalogue and executing queries.
-   **End-User:** The specific individual acting on behalf of the Consumer.

## Prerequisites

-   **Dataspace Configured:** The Governance Authority has set up the catalogue with appropriate vocabularies and schemas (BP02).
-   **Consumer Onboarded:** The Consumer has successfully completed the onboarding process (BP03A).
-   **End-User Authenticated & Authorised:** The End-User has the necessary roles and permissions (BP03B).

## Assumptions

-   A mechanism exists to perform quality ratings of resources based on predefined rules.

## Detailed Steps

### 1. Trigger resource search

The **Consumer** initiates the search process in the data space catalogues.

### 2. BP06.01: Search in data space catalogues

The **Consumer** inputs search terms. Three types of searches are supported:
-   **Quick search:** Matches terms against any field in the resource description.
-   **Advanced search:** Refines results using specific attribute values.
-   **Federated search:** Searches across multiple data space catalogues simultaneously.

### 3. BP06.02: Add access policy filter parameters

The query is automatically decorated with filters based on access policies. This ensures the **Consumer** (and the specific **End-User**) only sees resource descriptions they are permitted to access.

### 4. BP06.03: Execute query

The **Governance Authority** executes the query against its own catalogue or shared catalogues (in the case of federated search) to find matching resource descriptions.

### 5. BP06.04: Conduct a quality rating

The **Governance Authority** performs a quality rating of the matching resources based on predefined quality rules.

### 6. BP06.05: Access filtered search results

The **Governance Authority** provides the filtered results (including quality ratings) to the **Consumer's** system. The **Consumer** can then display and select specific resource descriptions for further review.

## Outcome

-   **Resources selected for review:** The **Consumer** can consult usage contract templates and decide whether to proceed with consuming the resource (BP08, BP09A, BP09B). If a contract is needed but not yet in place, the Consumer and Provider establish one (BP07).

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp06-consumer-searches-resources-data-space-catalogues](https://simpl-programme.ec.europa.eu/book-page/bp06-consumer-searches-resources-data-space-catalogues)
