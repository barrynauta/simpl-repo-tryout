# User Guide

## Purpose
This guide is describing how the `simpl-contract` component is used with examples.

## Key Capabilities

### 1. Contract Lifecycle Management
The service manages the full lifecycle of a contract agreement:
- Creating contract agreement data (`/credentials/agreements/{id}/definitions/{id}/create`)
- Issuing a verifiable credential representing contract creation (`/credentials/.../issue`)
- Confirming contract signing (`/agreements/{id}/definitions/{id}/status`)
- Retrieving stored contract agreements (`/agreements/{id}`)
- Retrieving stored contract agreement files (`/agreements/{id}/file`)
- Searching for existing agreements (`/agreements/{negotiationId}/search`)

### 2. Verifiable Credentials (W3C VC)
- Issue credential documents (`/credentials/.../issue`)
- Verify provided Verifiable Credentials (`/verifications/{id}`)

### 3. Health Monitoring
A standard Spring Boot actuator-compatible health endpoint (`/health`).

---

## Authentication
All operations require an API Key

---

## Main Endpoints Overview

| Area | Endpoint | Purpose |
|------|----------|---------|
| Health | `GET /health` | Check service liveness and readiness. |
| Contract creation | `POST /credentials/agreements/{agreementId}/definitions/{definitionId}/create` | Prepare contract data before signing. |
| VC issue | `POST /credentials/agreements/{agreementId}/definitions/{definitionId}/issue` | Issue a Verifiable Credential for the contract. |
| Contract signing | `PATCH /agreements/{agreementId}/definitions/{definitionId}/status` | Confirm final signature. |
| Contract retrieval | `GET /agreements/{agreementId}` | Retrieve contract metadata. |
| Contract file | `GET /agreements/{agreementId}/file` | Retrieve contract file from storage. |
| Contract search | `POST /agreements/{negotiationId}/search` | Search for a contract by parameters. |
| VC verification | `POST /verifications/{negotiationId}` | Validate a Verifiable Credential. |

---

# Usage Examples

## Example 1 — Creating a Contract Agreement

**Endpoint:**
```
POST /credentials/agreements/{contractAgreementId}/definitions/{contractDefinitionId}/create
```

**Request body:**
```json
{
  "contractNegotiationId": "C1-12",
  "assetId": "As5",
  "providerId": "PR1",
  "consumerId": "CNS44",
  "contractOfferId": "C1-12-33"
}
```

**Response:**
```json
{
  "contractAgreementId": "677186f6-1179-4cf1-b845-68d1c00c185f",
  "contractDefinitionId": "777186f6-1179-4cf1-b845-68d1c00c185f",
  "status": "INITIATED"
}
```

---

## Example 2 — Finalizing Contract Signature

**Endpoint:**
```
PATCH /agreements/{agreementId}/definitions/{definitionId}/status
```

**Request body:**
```json
{
  "status": "FINALIZED"
}
```

**Response:**
```json
{
  "contractAgreementId": "677186f6-1179-4cf1-b845-68d1c00c185f",
  "contractDefinitionId": "777186f6-1179-4cf1-b845-68d1c00c185f",
  "status": "FINALIZING"
}
```

---

## Example 3 — Issuing a Verifiable Credential

**Endpoint:**
```
POST /credentials/agreements/{agreementId}/definitions/{definitionId}/issue
```

**Request body:**
```json
{
  "contractNegotiationId": "0ec61c92-677b-4e97-aef1-ed542e37183b",
  "assetId": "MyResource1",
  "providerId": "FirstProvider",
  "consumerId": "Cons2000",
  "contractOfferId": "32c61c92-677b-4e97-aef1-ed542e371234"
}
```

**Response:**
```json
{
  "contractAgreementId": "677186f6-1179-4cf1-b845-68d1c00c185f",
  "contractDefinitionId": "777186f6-1179-4cf1-b845-68d1c00c185f",
  "status": "INITIATED"
}
```

---

# Additional Notes

### Contract Status Values
```
INITIATED
CREATED
FINALIZING
FINALIZED
TERMINATED
```

### Retrieving a Stored Contract
```
GET /agreements/{contractAgreementId}
```

### Retrieving Contract File
```
GET /agreements/{contractAgreementId}/file
```

---

