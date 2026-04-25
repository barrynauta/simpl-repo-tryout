# BP09A Dynamic View

## Source

> **See also: [Business process overview](./README.md)** — narrative
> description of this business process, including actors, prerequisites,
> outcomes, and the full hierarchy of sub-processes.

Extracted from functional-and-technical-architecture-specifications.md, section 4.3.2.

---

## Trace

This dynamic view covers the direct data download scenario: the Consumer accesses a dataset offered by a Provider, with a usage contract (BP07) governing legally binding policies. This is the only data sharing scenario included in the current release. Technical policy enforcement is applied where possible; for downloaded data, the contract provides legal enforcement.

**Preconditions:**
- The Provider has registered the resource at the Connector and published a self-description to the Catalogue.
- The Consumer is authenticated and has identified the dataset via the Catalogue (BP06).
- A usage contract exists between Consumer and Provider, or one will be established in this flow.
- The Consumer has compatible storage available.

> Note (current release): The existence of a contract is not checked during execution.

![BP09A sequence diagram](./media/BP09A-sequence.jpeg)
*Figure: Components involved in consuming a data resource via direct download.*

1. **Dataset Selection by the Consumer** — The Consumer selects a dataset in the Catalogue Client Application. A "Request Consumption of Data Asset" message is sent to the Contract Negotiation Adapter.

2. **Creation of Request Bundle** — The Contract Negotiation Adapter compiles a Request Bundle (dataset ID and negotiation parameters) and forwards it to the Consumer's Connector Control Plane.

3. **Requesting an Offering from the Provider** — The Consumer's Connector Control Plane sends a "Request Offering" message to the Provider's Connector Control Plane.

4. **Asset Validation by the Provider's Connector** — The Provider's Connector checks the Asset Catalogue for the requested dataset:
   - If not found: a "Resource Not Found" message is returned to the Consumer, halting the process.
   - If found: the workflow proceeds to contract negotiation.

5. **Contract Negotiation Between Connectors** — The Consumer and Provider Connectors negotiate usage terms (access conditions, compliance requirements, obligations), producing a draft contract.

6. **Policy Evaluation on the Provider's Side** — The draft contract is evaluated by the Provider's Policy Engine:
   - If the policy check fails: the Consumer is notified of the violation and the process halts.
   - If the policy check succeeds: the contract is approved.

7. **Notification of Policy Check Results** — The result (success or failure) is sent to the Consumer's Connector. On failure, the Contract Negotiation Adapter notifies the Consumer with details.

8. **Finalisation of Contract Agreement** — The contract is formalised within both Connectors' Control Planes, creating a binding agreement.

9. **Initiation of File Transfer Request** — The Consumer's Data Plane Extension for S3 sends a "Request File Transfer" message — including the contract agreement ID — to the Provider's Data Plane Extension for S3.

10. **Processing the File Transfer** — The Provider's Data Plane Extension verifies the request against the contract agreement ID and transfers the dataset securely to the Consumer.

---

## Participants

- [catalogue-client-application/](../../../integration/resource-discovery/search-engine/catalogue-client-application/README.md) — Catalogue Client Application (Consumer's interface for dataset selection)
- [connector/](../../../integration/resource-sharing/resource-sharing-runtime/connector/README.md) — Connector (contract negotiation control plane on both Consumer and Provider sides; includes Contract Negotiation Adapter and Data Plane Extension for S3)
- [simpl-catalogue/](../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) — Simpl Catalogue (Provider's Asset Catalogue consulted during asset validation)
- Policy Engine — unmatched — verify (evaluates draft contract against governance rules; may be embedded in the Connector or a separate module not yet documented)
