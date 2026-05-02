<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Utils</a><br/>
            <strong>SD Schemas Util</strong><br/>
</p>
</div>

# SD Schemas Util

Python tool that generates ontology files and SHACL shape files from YAML definitions. The output feeds the **XFSC Federated Catalogue** so that self-descriptions can be validated against the correct schemas.

Provenance: built by Simpl. Source repository: `data1/sdtooling-sd-schemas`. Licence: EUPL 1.2.

## Key features

- Driven by YAML definition files — schemas, vocabularies, and contracts are described once in YAML.
- Two generation modes:
  - **ontology-generation** — emits ontology and SHACL shapes from a CSV/YAML source. The `contract` directory in YAML input is ignored for ontology generation.
  - Schema/vocabulary CLI commands.
- Output consumed by the [Schema Management Service](../../../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) and the [Simpl Catalogue](../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md).

## Note

The PSO mapping spreadsheet flags this utility for *extraction* from the as-is repo. Sample/default schemas produced by it now live at [`data/semantics-and-vocabulary/schema-management/sdtooling-sd-schemas/`](../../../data/semantics-and-vocabulary/schema-management/sdtooling-sd-schemas/README.md).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/data1/sdtooling-sd-schemas>
