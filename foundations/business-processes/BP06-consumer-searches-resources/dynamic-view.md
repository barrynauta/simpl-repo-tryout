# BP06 Dynamic View

## Source

Extracted from functional-and-technical-architecture-specifications.md, section 4.3.2.

---

## Trace

A Consumer end user searches for resources (datasets, applications, or infrastructure offerings) available in the data space catalogue. Two search modes are supported: quick search (keyword-based) and advanced search (schema-driven structured query). For advanced search, the local Schema Registry must first be synchronised with the Governance Authority's central Schema Registry.

> **Image not available**: The sequence diagram (image62) referenced in the source document is not present in this repository. Embed it here once available, using the pattern `![BP06 sequence diagram](./media/BP06-sequence.png)`.

1. **User Search Request Initiation** — The end user enters search criteria (keywords, filters, or structured parameters) in the Search Client (Catalogue Client Application). For advanced search, the available search fields are defined by the Schema Registry, which drives automatic form generation.

2. **Policy Filter Service** — The validated search request is passed to the Policy Filter Service, which checks the user's access rights against the policies defined in the Policy Creator Component. The service modifies the query to restrict results to only those resources the user is authorised to view.

3. **Query Translation by Adapter Component** — The Query Mapper Adapter receives the policy-filtered request and translates it into the Catalogue's internal query language, embedding access restrictions directly into the query.

4. **Catalogue Component Query Execution** — The Catalogue receives the translated query and executes it via its Search Engine, scanning the database of signed self-descriptions and associated metadata. Results are filtered to ensure compliance with access policies.

5. **Result Return to Search Client** — The Catalogue sends the authorised results back through the Adapter, which re-formats them. The Search Client presents the results to the user with associated metadata.

---

## Participants

- [catalogue-client-application/](../../../integration/resource-discovery/search-engine/catalogue-client-application/README.md) — Catalogue Client Application / Search Client (UI for search input and result display)
- [schema-management-service/](../../../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) — Schema Registry (drives advanced search form fields; provides schema definitions)
- [simpl-catalogue/](../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) — Simpl Catalogue (executes search queries; returns filtered results)
- Policy Filter Service / Query Mapper Adapter — unmatched — verify (no dedicated solution folder found; these components may be embedded within the Catalogue or a separate module not yet documented)
