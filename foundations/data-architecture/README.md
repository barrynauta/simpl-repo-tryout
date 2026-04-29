<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Foundations</a><br/>
        <strong>Data architecture</strong><br/>
</p>
</div>

# Data architecture

The complete data architecture of Simpl-Open: how data is modelled across the platform's open-source components and its custom components, at three levels of abstraction (conceptual, logical, physical). The chapter is split across four files because of its size (~2,500 lines in the source).

This is reference material — when implementing a new solution that persists or transports state, this is where to find the canonical schema, entity relationships, and storage layout. Per-solution data-model details (e.g. the Contract Manager's tables) belong in the solution README; this folder is the cross-cut.

## Contents

- [open-source-components.md](open-source-components.md) — FTA §5.1: data models of the open-source components used by Simpl-Open (PostgreSQL, Neo4j, Apache Jena Fuseki, Apache Kafka, OpenBao, etc.).
- [conceptual-model.md](conceptual-model.md) — FTA §5.2.1: high-level entities and relationships across all custom components, technology-agnostic.
- [logical-model.md](logical-model.md) — FTA §5.2.2: the logical data model — entity attributes, primary/foreign keys, cardinality.
- [physical-model.md](physical-model.md) — FTA §5.2.3: storage-tier physical schema for the custom components, including tablespaces, indexing, and partitioning where relevant.

## Source

This folder reproduces FTA Chapter 5 verbatim, split for navigability. Upstream link: [FTA spec §5](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#5-simpl-open-data-architecture).
