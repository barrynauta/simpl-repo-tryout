# Field-Level Pseudo-Anonymisation - User Manual

**Version:** 0.3.0  
**Last Updated:** November 12, 2025  
**Component:** Field-Level Pseudo-Anonymisation Service  
**Part of:** Simpl-open ecosystem

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Available Jobs](#available-jobs)
4. [Anonymization Techniques](#anonymization-techniques)
5. [Working with Structured Data](#working-with-structured-data)
6. [Working with Unstructured Data](#working-with-unstructured-data)
7. [Configuration Reference](#configuration-reference)
8. [Examples and Use Cases](#examples-and-use-cases)

---

## Introduction

### What is Field-Level Pseudo-Anonymisation?

The Field-Level Pseudo-Anonymisation service provides privacy-preserving transformations for sensitive data at the field (column) or entity (PII) level. It supports:

- **Structured Data**: CSV files and pandas DataFrames with column-wise transformations
- **Unstructured Data**: Text documents with automatic PII detection and anonymization

#### Difference Pseudonymisation vs Anonymisation

| Feature | Pseudonymisation (GDPR Article 4(5)) | Anonymisation (GDPR Recital 26) |
| :--- | :--- | :--- |
| **Definition** | Processing data so it can **no longer be attributed** to a specific individual *without the use of additional information* (the key/mapping table). | Processing data so the individual is **no longer identifiable** by any means reasonably likely to be used (irreversible). |
| **GDPR Scope** | **Still considered Personal Data** and must comply with all GDPR principles (lawfulness, security, data minimisation, etc.). | **Falls Outside GDPR Scope** once fully and irreversibly achieved. |
| **Reversibility** | **Reversible.** The original data can be recovered by linking the pseudonym back to the identity using the separate key. | **Irreversible.** The link to the individual is permanently destroyed. |
| **Guarantees** | **Reduced Risk of Harm** from a data breach, as direct identifiers are separated and protected. Still allows for internal linking/longitudinal studies. | **Zero or Negligible Risk of Re-Identification,** as the data is no longer tied to a natural person. |

##### Best Practices for Safe and Correct Use

Applying field-Level Pseudo-Anonymisation requires careful consideration of the data context and the desired privacy level.

* **1. Attribute Classification:** **Clearly classify** every field as an **Identifier** or a **Sensitive Attribute** before applying any transformation.
    * *Identifiers* should be the primary target for pseudonymisation (or removal).
    * **Note:** Since this service does not use $k$-anonymity, fields that could act as **Quasi-Identifiers** (like Age, Zip Code) should be treated as **Identifiers** or **removed** if they pose a re-identification risk.
* **2. Separate the Key:** For **Pseudonymisation**, the mapping key or table that links the pseudonym back to the original identity **must be stored separately** and protected by robust technical and organisational security measures (GDPR Article 32). Access should be logged and strictly limited.


##### Known Limitations and Cautions

Users must understand that solely relying on field-level transformations has specific limitations, especially regarding re-identification risk.

* **High Risk of Re-identification:** Since this service **does not use advanced models** like $k$-anonymity, field-level anonymisation **does not protect linking via quasi-identifiers**. Fields like **Zip Code, Age, and Gender** can still be combined by an attacker to re-identify records.
* **Context Dependency of Anonymisation:** What is deemed anonymous must be judged against the **external data available to an attacker**. If a record has a unique combination of field values, it is not truly anonymous.
* **Vulnerability to Inference:** Removing an identifier and leaving unique sensitive data intact can still lead to re-identification if the sensitive data is unique to an individual (e.g., a rare medical condition).
* **Unstructured Data Challenges:** PII detection in unstructured text is never 100% accurate. Relying solely on automatic PII detection may **miss nuanced or domain-specific identifiers**, requiring manual review or custom rules for high-risk datasets.
* **Linking Risk (Pseudonymisation):** Although the risk is reduced, pseudonymised data **remains Personal Data**. If the pseudonym is compromised or linked to another data set through a key, the full identity is re-established.

### Key Capabilities

- **Multiple Techniques**: Hash, encrypt, redact, replace, retain
- **Reversible Encryption**: Using OpenBao-managed Fernet keys
- **Multi-language PII Detection**: 18+ languages supported via spaCy
- **Dagster Integration**: Orchestrated workflows with metadata tracking
- **Dual Output**: Both anonymized data and metrics/reports

### When to Use This Service

Use field-level pseudonymisation when:

- ✅ You need to protect specific columns (e.g., SSN, email, phone)
- ✅ You want reversible anonymization (encryption with key management)
- ✅ You're processing unstructured text with embedded PII
- ✅ You need compliance with GDPR, HIPAA, or similar regulations
- ✅ You want to share data while preserving privacy

**Note:** For statistical anonymization (k-anonymity, l-diversity), use the `dataframe-level-anonymisation` service.

---

## Getting Started

### Prerequisites

Before using this service, ensure:

1. **Service is installed**: Follow [Installation Guide](../installation-guide/installation-guide.md)
2. **Vault is running**: OpenBao accessible at configured address
3. **Encryption keys created**: At least one Fernet key stored in Vault (for encryption techniques)
4. **Dagster UI accessible**: <http://localhost:3000> (local) or your cluster URL

### Accessing the Service

#### Option 1: Dagster UI (Recommended)

1. Open browser: **<http://localhost:3000>**
2. Navigate to **Jobs** in left sidebar
3. Select a job (e.g., `anonymize_pseudonymize_structured_job`)
4. Click **Launchpad** to configure and execute

#### Option 2: Dagster CLI

```powershell
# List available jobs
dagster job list -f src/field_level_pseudo_anonymisation/repository.py

# Execute a job with config
dagster job execute -f src/field_level_pseudo_anonymisation/repository.py \
  -j anonymize_pseudonymize_structured_job \
  -c config.yaml
```

#### Option 3: Python API

```python
from field_level_pseudo_anonymisation.repository import defs

# Get job definition
job_def = defs.get_job_def("anonymize_pseudonymize_structured_job")

# Execute with run config
result = job_def.execute_in_process(
    run_config={
        "ops": {
            "read_csv_to_df": {
                "config": {"input_path": "input/data.csv"}
            },
            "anonymize_pseudonymize_structured": {
                "config": {
                    "used_function": [
                        {
                            "technique": {
                                "hash": {
                                    "columns": ["EMAIL", "PERSON"],
                                    "algorithm": "sha256"
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
)
```

---

## Available Jobs

### Structured Data Jobs

#### 1. `anonymize_pseudonymize_structured_job`

**Purpose:** Anonymize/pseudonymize columns in CSV/DataFrame

**Pipeline:**

```
read_csv_to_df → preview_dataframe → anonymize_pseudonymize_structured → preview_dataframe → write_df_to_csv
```

**Use Cases:**

- Hash email addresses for analytics
- Encrypt SSN for secure storage
- Redact sensitive fields before sharing
- Replace real names with placeholders

**Configuration Example:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "input/customers.csv"
  
  anonymize_pseudonymize_structured:
    config:
      used_function:
        - technique:
            hash:
              columns: ["EMAIL"]
              algorithm: "sha256"
        
        - technique:
            encrypt:
              columns: ["PERSON", "CREDIT_CARD"]
              key_name: "pii_encryption_key"
  
  write_df_to_csv:
    config:
      output_path: "output/customers_anonymized.csv"
```

---

#### 2. `depseudonymize_structured_job`

**Purpose:** Reverse pseudonymization (decrypt encrypted fields)

**Pipeline:**

```
read_csv_to_df → preview_dataframe → depseudonymize_structured → preview_dataframe → write_df_to_csv
```

**Use Cases:**

- Restore original values from encrypted data
- Authorized access to sensitive information
- Data recovery for compliance audits

**Configuration Example:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "output/customers_anonymized.csv"
  
  depseudonymize_structured:
    config:
      used_function:
        - technique:
            type: "decrypt"
            columns: ["PERSON", "CREDIT_CARD"]
            key_name: "pii_encryption_key"
  
  write_df_to_csv:
    config:
      output_path: "output/customers_restored.csv"
```

---

#### 3. `anonymize_pseudonymize_depseudonymize_structured_job`

**Purpose:** Test round-trip encryption/decryption

**Pipeline:**

```
read_csv → preview → anonymize_pseudonymize → preview → depseudonymize → preview
```

**Use Cases:**

- Validate encryption/decryption workflow
- Test key management setup
- Verify data integrity after transformations

---

### Unstructured Data Jobs

#### 4. `anonymize_pseudonymize_unstructured_job`

**Purpose:** Detect and anonymize PII in text documents

**Pipeline:**

```
read_txt_to_string → preview_txt → anonymize_pseudonymize_unstructured → preview_txt → write_string_to_txt
```

**Use Cases:**

- Remove names from medical records
- Redact emails from support tickets
- Anonymize customer feedback
- Protect PII in legal documents

**Configuration Example:**

```yaml
ops:
  read_txt_to_string:
    config:
      input_path: "input/medical_notes.txt"
  
  anonymize_pseudonymize_unstructured:
    config:
      language: "en"
      used_function:
        - technique:
            redact:
              pii: ["PERSON", "EMAIL", "PHONE_NUMBERS", "CREDIT_CARD"]
        
        - technique:
            hash:
              pii: ["PERSON"]
              algorithm: "sha256"
  
  write_string_to_txt:
    config:
      output_path: "output/medical_notes_anonymized.txt"
```

---

#### 5. `depseudonymize_unstructured_job`

**Purpose:** Restore original PII from encrypted text

**Pipeline:**

```
read_txt_to_string → preview_txt → depseudonymize_unstructured → preview_txt → write_string_to_txt
```

**Configuration Example:**

```yaml
ops:
  read_txt_to_string:
    config:
      input_path: "output/notes_encrypted.txt"
  
  depseudonymize_unstructured:
    config:
      language: "en"
      used_function:
        - technique:
            type: "decrypt"
            key_name: "pii_encryption_key"
```

---

## Anonymization Techniques

### 1. Hash

**Description:** Irreversible one-way hashing using SHA-256 or SHA-512

**Characteristics:**

- ✅ Irreversible (cannot decrypt)
- ✅ Deterministic (same input → same hash)
- ✅ Fast and efficient
- ❌ Vulnerable to rainbow table attacks for small domains

**Use Cases:**

- User identifiers for analytics
- Email addresses for tracking without revealing identity
- Join keys between anonymized datasets

**Configuration:**

```yaml
technique:
  hash:
    columns: ["EMAIL"]
    algorithm: "sha256"  # Options: "sha256", "sha512"
```

**Example:**

| Original | Hashed (SHA-256) |
|----------|------------------|
| <john.doe@example.com> | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| <jane.smith@example.com> | 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae |

**Best Practices:**

- Use SHA-256 for most cases
- Use SHA-512 for high-security requirements
- Consider adding salt for additional security (custom implementation)

---

### 2. Encrypt

**Description:** Reversible encryption using Fernet (symmetric encryption)

**Characteristics:**

- ✅ Reversible with correct key
- ✅ Vault-managed keys (secure key storage)
- ✅ AES-128 CBC with authentication
- ❌ Requires key management infrastructure

**Use Cases:**

- Temporary anonymization for analytics
- Data that may need restoration
- Compliance with "right to erasure" (key deletion)

**Configuration:**

```yaml
technique:
  encrypt:
    columns: ["PERSON", "CREDIT_CARD", "passport"]
    key_name: "production_pii_key"  # Key path in Vault
```

**Vault Key Setup:**

```bash
# Generate Fernet key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Output: gAAAAABh... (44 characters)

# Store in Vault
vault kv put secret/encryption_keys/production_pii_key key="<generated-key>"
```

**Example:**

| Original | Encrypted |
|----------|-----------|
| 123-45-6789 | gAAAAABnMxY8kJ... (long base64 string) |
| 4532-1234-5678-9010 | gAAAAABnMxY9pL... |

**Best Practices:**

- Use descriptive key names (e.g., `pii_2025_q1`, `healthcare_phi`)
- Implement key rotation policies
- Store key metadata (creation date, purpose)
- Back up Vault encryption keys securely

---

### 3. Redact

**Description:** Complete removal, replaced with `[REDACTED]`

**Characteristics:**

- ✅ Irreversible
- ✅ Visible indicator of removed data
- ✅ Preserves data structure (column still exists)
- ❌ Loses all information

**Use Cases:**

- Highly sensitive data with no analytical value
- Compliance with strict data minimization
- Testing environments

**Configuration:**

```yaml
technique:
  redact:
    columns: ["password", "api_key", "security_answer"]
```

**Example:**

| Original | Redacted |
|----------|----------|
| MyP@ssw0rd123 | [REDACTED] |
| sk-1234567890abcdef | [REDACTED] |

**Unstructured Text Example:**

```
Original:
"Patient John Doe (SSN: 123-45-6789) visited on 2025-11-11."

Redacted:
"Patient [REDACTED] (SSN: [REDACTED]) visited on 2025-11-11."
```

---

### 4. Replace

**Description:** Substitute with a fixed value

**Characteristics:**

- ✅ Irreversible
- ✅ Maintains consistent replacement value
- ✅ Useful for testing with realistic formats
- ❌ Loses original information

**Use Cases:**

- Generate test data with realistic formats
- Placeholder values for demos
- Consistent anonymization across datasets

**Configuration:**

```yaml
technique:
  replace:
    columns: ["PHONE_NUMBERS", "address"]
    new_value: "PLACEHOLDER"
```

**Example:**

| Original | Replaced |
|----------|----------|
| +1-212-555-0100 | PLACEHOLDER |
| 123 Main St, City | PLACEHOLDER |

**Custom Replacements:**

```yaml
# Different replacements per column (requires multiple technique blocks)
used_function:
  - technique:
      replace:
        columns: ["EMAIL"]
        new_value: "anonymous@example.com"
  
  - technique:
      replace:
        columns: ["PHONE_NUMBERS"]
        new_value: "+1-000-000-0000"
```

---

### 5. Retain

**Description:** No transformation, pass through unchanged

**Note:** The `retain` technique is **only available for unstructured data**. For structured data (CSV/DataFrames), simply don't include columns you want to keep unchanged in any technique configuration - they will be automatically retained.

**For Unstructured Data:**

**Characteristics:**

- ✅ Original PII preserved in text
- ✅ Useful for selective anonymization
- ✅ Combined with other techniques

**Use Cases:**

- Explicitly mark non-sensitive PII to keep
- Selective anonymization workflows
- Configuration clarity

**Configuration (Unstructured Only):**

```yaml
technique:
  retain:
    pii: ["DATE_OF_BIRTH", "URL"]
```

**For Structured Data:**

Simply omit columns from technique configurations to retain them:

```yaml
# Only anonymize sensitive columns - other columns are automatically retained
used_function:
  - technique:
      hash:
        columns: ["EMAIL"]  # Only email is hashed
# customer_id, order_date, etc. are automatically retained unchanged
```

---

## Working with Structured Data

### Input Format

**Supported Formats:**

- CSV files (`.csv`)
- Pandas DataFrames (in-memory)

**Requirements:**

- UTF-8 encoding
- Header row with column names
- Consistent delimiters (comma by default)

**Example CSV:**

```csv
customer_id,name,email,ssn,order_date,amount
CUST-001,John Doe,john.doe@example.com,123-45-6789,2025-11-01,299.99
CUST-002,Jane Smith,jane.smith@example.com,987-65-4321,2025-11-05,449.50
CUST-003,Bob Johnson,bob.j@example.com,555-12-3456,2025-11-10,199.00
```

### Configuration Structure

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "input/data.csv"
      # Optional parameters:
      delimiter: ","
      encoding: "utf-8"
      header: 0  # Row number for column names
  
  anonymize_pseudonymize_structured:
    config:
      used_function:
        - technique:
            type: "<technique_type>"
            columns: ["col1", "col2"]
            # Technique-specific parameters
  
  write_df_to_csv:
    config:
      output_path: "output/anonymized.csv"
      # Optional parameters:
      index: false  # Don't write row indices
```

### Multiple Techniques Example

Apply different techniques to different columns:

```yaml
ops:
  anonymize_pseudonymize_structured:
    config:
      used_function:
        # Hash email for analytics
        - technique:
            hash:
              columns: ["EMAIL"]
              algorithm: "sha256"
        
        # Encrypt reversible PII
        - technique:
            encrypt:
              columns: ["PERSON", "CREDIT_CARD"]
              key_name: "pii_key"
        
        # Redact highly sensitive data
        - technique:
            redact:
              columns: ["password", "security_answer"]
        
        # Note: Columns not mentioned in any technique are automatically retained
```

### Processing Order

Techniques are applied **in the order specified** in the configuration:

```yaml
used_function:
  - technique:  # Applied FIRST
      type: "encrypt"
      columns: ["EMAIL"]
      key_name: "key1"
  
  - technique:  # Applied SECOND
      type: "hash"
      columns: ["PHONE_NUMBERS"]
      algorithm: "sha256"
```

**Important:** Be careful with overlapping columns - later techniques overwrite earlier ones.

### Output

**Structure:** Same as input (same columns, same order)

**Example Output:**

```csv
customer_id,name,email,ssn,order_date,amount
CUST-001,[REDACTED],e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,gAAAAABnMxY8...,2025-11-01,299.99
CUST-002,[REDACTED],2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae,gAAAAABnMxY9...,2025-11-05,449.50
```

### Metrics Output

Each job produces metadata:

```python
{
    "rows_processed": 1000,
    "columns_transformed": 3,
    "techniques_applied": ["hash", "encrypt", "redact"],
    "execution_time_seconds": 2.45
}
```

View in Dagster UI: **Run Details** → **Outputs** → `metrics`

---

## Working with Unstructured Data

### Input Format

**Supported Formats:**

- Plain text files (`.txt`)
- String data (in-memory)

**Requirements:**

- UTF-8 encoding
- Supported language (see [Supported Languages](#supported-languages))

**Example Text:**

```
Patient Name: John Doe
SSN: 123-45-6789
Email: john.doe@hospital.org
Phone: +1-212-867-5309

Medical History:
The patient presented with symptoms on November 10, 2025.
Previous consultation with Dr. Jane Smith on October 15, 2025.
```

### PII Entity Types

The service automatically detects the following PII types:

> **⚠️ IMPORTANT:** Use the **exact enum member name** as shown in the "Enum Member" column when configuring PII detection in YAML. These are case-sensitive.

| Enum Member | Description | Examples |
|-------------|-------------|----------|
| `PERSON` | Person names | John Doe, Jane Smith, Dr. Brown |
| `EMAIL` | Email addresses | john@example.com |
| `PHONE_NUMBERS` | Phone numbers | +1-212-555-0100, (617) 253-1000 |
| `CREDIT_CARD` | Credit card numbers | 4532-1234-5678-9010 |
| `URL` | URLs | https://example.com |
| `DATE_OF_BIRTH` | Birth dates | 1990-01-15 |
| `CREDENTIALS` | Username/password pairs | login: admin, password: secret |
| `X_SOCIAL` | Twitter/X usernames | @username |

### Configuration Structure

```yaml
ops:
  read_txt_to_string:
    config:
      input_path: "input/document.txt"
  
  anonymize_pseudonymize_unstructured:
    config:
      language: "en"  # ISO 639-1 code
      
      used_function:
        - technique:
            <technique_name>:
              pii: ["PERSON", "EMAIL", "PHONE_NUMBERS"]
              # Technique-specific parameters
  
  write_string_to_txt:
    config:
      output_path: "output/anonymized.txt"
```

**Supported PII enum members:**
- `PERSON` - Names of people
- `EMAIL` - Email addresses
- `PHONE_NUMBERS` - Phone numbers  
- `CREDIT_CARD` - Credit card numbers
- `URL` - Web URLs
- `DATE_OF_BIRTH` - Dates of birth
- `CREDENTIALS` - Login credentials
- `X_SOCIAL` - Twitter/X usernames

> **📞 Phone Number Detection Note:**  
> Phone detection validates against real phone number formats. Purely fictional numbers like `555-123-4567` (555-only area code) will NOT be detected. Use valid area codes with 555 exchange (e.g., `212-555-0100`, `415-555-0123`) or real numbers for testing.

### Language Support

Specify the language for optimal PII detection:

```yaml
anonymize_pseudonymize_unstructured:
  config:
    language: "de"  # German
    used_function:
      - technique:
          redact:
            pii: ["PERSON", "EMAIL"]
```

**Supported Languages:**

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | `en` | Italian | `it` |
| German | `de` | Dutch | `nl` |
| French | `fr` | Polish | `pl` |
| Spanish | `es` | Portuguese | `pt` |
| Swedish | `sv` | Norwegian | `no` |
| Danish | `da` | Finnish | `fi` |
| Greek | `el` | Lithuanian | `lt` |
| Romanian | `ro` | Russian | `ru` |
| Ukrainian | `uk` | Chinese | `zh` |

### Example: Multi-technique Unstructured

```yaml
anonymize_pseudonymize_unstructured:
  config:
    language: "en"
    used_function:
      # Redact names completely
      - technique:
          redact:
            pii: ["PERSON"]
      
      # Hash SSNs for tracking
      - technique:
          hash:
            pii: ["PERSON"]
            algorithm: "sha256"
      
      # Encrypt emails (reversible)
      - technique:
          encrypt:
            pii: ["EMAIL", "PHONE_NUMBERS"]
            key_name: "contact_info_key"
```

### Output Example

**Original:**

```
Patient Name: John Doe
SSN: 123-45-6789
Email: john.doe@hospital.org
Phone: +1-212-867-5309
```

**Anonymized:**

```
Patient Name: [REDACTED]
SSN: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Email: gAAAAABnMxY8kJ...
Phone: [REDACTED]
```

### Metrics Report

Unstructured jobs generate detailed PII reports:

```markdown
## PII Anonymization Report

### Summary
- **Total PII Detected**: 15
- **Original Length**: 450 chars
- **Anonymized Length**: 520 chars
- **Language**: en

### PII by Type
| Entity Type | Count |
|-------------|-------|
| name        | 3     |
| email       | 2     |
| phone       | 1     |
| ssn         | 1     |
| date_of_birth | 2   |

### Techniques Applied
- redact: name (3 instances)
- hash: ssn (1 instance)
- encrypt: email, phone (3 instances)
```

View in Dagster UI: **Run Details** → **Outputs** → `metrics`

---

## Configuration Reference

### Global Configuration Parameters

#### Vault Configuration

```yaml
# Environment variables (not in YAML config)
VAULT_ADDR: "http://vault:8200"
VAULT_TOKEN: "s.1234567890abcdef"
```

#### Dagster Configuration

```yaml
# dagster.yaml (workspace-level)
run_coordinator:
  module: dagster.core.run_coordinator
  class: QueuedRunCoordinator

run_launcher:
  module: dagster.core.launcher
  class: DefaultRunLauncher
```

### Op-Specific Configuration

> **Important: Technique Configuration Format**  
> This service uses Dagster's **discriminated union** configuration. Each technique type (hash, encrypt, redact, replace, retain) is specified as a **key** under `technique`, not as a `type` field.
>
> **Correct format:**
> ```yaml
> technique:
>   hash:  # Technique name as key
>     columns: ["EMAIL"]
>     algorithm: "sha256"
> ```
>
> **Incorrect format (will fail):**
> ```yaml
> technique:
>   type: "hash"  # ❌ Wrong - don't use 'type' field
>   columns: ["EMAIL"]
> ```
>
> **Exception:** For `depseudonymize_structured`, decrypt uses a flat structure with `type: "decrypt"`.

#### read_csv_to_df

```yaml
read_csv_to_df:
  config:
    input_path: "input/data.csv"  # Required
    delimiter: ","                # Optional (default: ",")
    encoding: "utf-8"             # Optional (default: "utf-8")
    header: 0                     # Optional (default: 0)
```

#### write_df_to_csv

```yaml
write_df_to_csv:
  config:
    output_path: "output/result.csv"  # Required
    index: false                     # Optional (default: false)
    encoding: "utf-8"                # Optional (default: "utf-8")
```

#### read_txt_to_string

```yaml
read_txt_to_string:
  config:
    input_path: "input/document.txt"  # Required
    encoding: "utf-8"                # Optional (default: "utf-8")
```

#### write_string_to_txt

```yaml
write_string_to_txt:
  config:
    output_path: "output/anonymized.txt"  # Required
    encoding: "utf-8"                   # Optional (default: "utf-8")
```

### Technique-Specific Parameters

#### Hash Technique

```yaml
# For structured data:
technique:
  hash:
    columns: ["col1", "col2"]
    algorithm: "sha256"  # Optional: "sha256" (default) or "sha512"

# For unstructured data:
technique:
  hash:
    pii: ["PERSON", "EMAIL"]
    algorithm: "sha256"  # Optional
```

#### Encrypt Technique

```yaml
# For structured data:
technique:
  encrypt:
    columns: ["PERSON"]
    key_name: "my_encryption_key"  # Required: Vault key name

# For unstructured data:
technique:
  encrypt:
    pii: ["EMAIL"]
    key_name: "my_encryption_key"  # Required
```

**Key Path in Vault:** `secret/encryption_keys/<key_name>`

#### Decrypt Technique

```yaml
# For structured data:
technique:
  type: "decrypt"
  columns: ["PERSON"]
  key_name: "my_encryption_key"  # Required: Must match encryption key
```

**Note:** For unstructured decrypt, the structure is different - only `key_name` is required (no `pii` field):

```yaml
# For unstructured data:
technique:
  decrypt:
    key_name: "my_encryption_key"  # Decrypts all encrypted content
```

#### Redact Technique

```yaml
# For structured data:
technique:
  redact:
    columns: ["password"]

# For unstructured data:
technique:
  redact:
    pii: ["PERSON", "PERSON"]
```

#### Replace Technique

```yaml
# For structured data:
technique:
  replace:
    columns: ["PHONE_NUMBERS"]
    new_value: "PLACEHOLDER"  # Required

# For unstructured data:
technique:
  replace:
    pii: ["EMAIL"]
    new_value: "PLACEHOLDER"  # Required
```

#### Retain Technique

**Note:** Only available for unstructured data. For structured data, simply omit columns from configurations.

```yaml
# For unstructured data only:
technique:
  retain:
    pii: ["DATE_OF_BIRTH", "URL"]
```

---

## Examples and Use Cases

### Example 1: E-commerce Customer Data

**Scenario:** Anonymize customer database for analytics team

**Input CSV:**

```csv
customer_id,name,email,phone,address,city,order_total
C001,John Doe,john@example.com,212-555-0100,123 Main St,Boston,299.99
C002,Jane Smith,jane@example.com,617-555-0178,456 Oak Ave,Seattle,449.50
```

**Configuration:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "input/customers.csv"
  
  anonymize_pseudonymize_structured:
    config:
      used_function:
        # Hash email for user tracking without PII
        - technique:
            hash:
              columns: ["EMAIL"]
              algorithm: "sha256"
        
        # Redact personal identifiers
        - technique:
            redact:
              columns: ["PERSON", "PHONE_NUMBERS", "address"]
        
        # Note: customer_id, city, and order_total are automatically retained
  
  write_df_to_csv:
    config:
      output_path: "output/customers_analytics.csv"
```

**Output:**

```csv
customer_id,name,email,phone,address,city,order_total
C001,[REDACTED],96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7,[REDACTED],[REDACTED],Boston,299.99
C002,[REDACTED],6d5f807e23db210bc254a28aa2f5e9e41f2d73c6cfcc29a69e84b9ac86beff69,[REDACTED],[REDACTED],Seattle,449.50
```

**Benefits:**

- Analytics team can track user behavior by hashed email
- Personal identifiers removed
- Geographic and revenue data preserved

---

### Example 2: Healthcare Records

**Scenario:** Anonymize patient notes for research

**Input Text:**

```
Patient: John Doe (SSN: 123-45-6789)
DOB: 1980-05-15
Contact: john.doe@email.com, +1-212-555-0100

Diagnosis: Patient presented with symptoms on 2025-11-10.
Prescribed medication X. Follow-up scheduled with Dr. Jane Smith.
```

**Configuration:**

```yaml
ops:
  read_txt_to_string:
    config:
      input_path: "input/patient_notes.txt"
  
  anonymize_pseudonymize_unstructured:
    config:
      language: "en"
      used_function:
        # Encrypt reversible PII (in case of audit)
        - technique:
            encrypt:
              pii: ["PERSON", "PERSON"]
              key_name: "healthcare_phi_key"
        
        # Redact contact info
        - technique:
            redact:
              pii: ["EMAIL", "PHONE_NUMBERS"]
        
        # Hash dates for temporal analysis
        - technique:
            hash:
              pii: ["DATE_OF_BIRTH"]
              algorithm: "sha256"
  
  write_string_to_txt:
    config:
      output_path: "output/patient_notes_anonymized.txt"
```

**Output:**

```
Patient: gAAAAABnMxY8... (SSN: gAAAAABnMxZ1...)
DOB: 8d5e957f297893487bd98fa830fa6413a1e5e24c6d9e6e6a7e5e5e5e5e5e5e5e
Contact: [REDACTED], [REDACTED]

Diagnosis: Patient presented with symptoms on 2025-11-10.
Prescribed medication X. Follow-up scheduled with Dr. gAAAAABnMxZ2...
```

**Benefits:**

- Patient identity protected but recoverable (encrypted)
- Research can use temporal patterns (hashed DOB)
- Contact info completely removed
- Audit trail maintained via encryption

---

### Example 3: Round-trip Encryption

**Scenario:** Test encryption/decryption workflow

**Configuration (Anonymize):**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "input/sensitive_data.csv"
  
  anonymize_pseudonymize_structured:
    config:
      used_function:
        - technique:
            encrypt:
              columns: ["PERSON", "CREDIT_CARD"]
              key_name: "test_key"
  
  write_df_to_csv:
    config:
      output_path: "temp/encrypted.csv"
```

**Configuration (De-anonymize):**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "temp/encrypted.csv"
  
  depseudonymize_structured:
    config:
      used_function:
        - technique:
            type: "decrypt"
            columns: ["PERSON", "CREDIT_CARD"]
            key_name: "test_key"
  
  write_df_to_csv:
    config:
      output_path: "output/restored.csv"
```

**Verification:**

```powershell
# Compare original and restored files
diff input/sensitive_data.csv output/restored.csv
# Should be identical
```

---

### Example 4: Multi-language Text Processing

**Scenario:** Anonymize multilingual customer feedback

**German Input:**

```
Kunde: Hans Müller
E-Mail: hans.mueller@beispiel.de
Telefon: +49-30-12345678

Feedback: Der Service war ausgezeichnet. Ich habe am 15. November 2025 bestellt.
```

**Configuration:**

```yaml
ops:
  read_txt_to_string:
    config:
      input_path: "input/feedback_de.txt"
  
  anonymize_pseudonymize_unstructured:
    config:
      language: "de"  # German
      used_function:
        - technique:
            redact:
              pii: ["PERSON", "EMAIL", "PHONE_NUMBERS"]
  
  write_string_to_txt:
    config:
      output_path: "output/feedback_de_anonymized.txt"
```

**Output:**

```
Kunde: [REDACTED]
E-Mail: [REDACTED]
Telefon: [REDACTED]

Feedback: Der Service war ausgezeichnet. Ich habe am 15. November 2025 bestellt.
```

---

## Additional Resources

### Documentation

- **Installation Guide:** `documents/installation-guide/installation-guide.md`
- **Upgrade Guide:** `documents/upgrade-guide/upgrade-guide.md`
- **API Reference:** Source code docstrings in `src/`

### External Links

- [Dagster Documentation](https://docs.dagster.io/)
- [OpenBao Documentation](https://openbao.org/docs/)
- [Scrubadub Documentation](https://scrubadub.readthedocs.io/)
- [spaCy Documentation](https://spacy.io/usage)
- [Fernet Encryption Specification](https://github.com/fernet/spec/blob/master/Spec.md)

### Support

- **Maintainer:** Data 2 team
- **Issue Tracker:** <https://code.europa.eu/simpl/simpl-open/development/data-services/field-level-pseudo-anonymisation/-/issues>
- **Confluence:** <https://confluence.simplprogramme.eu/>

---

**Document Version:** 1.0  
**Last Reviewed:** November 17, 2025  
**Next Review:** February 11, 2026
