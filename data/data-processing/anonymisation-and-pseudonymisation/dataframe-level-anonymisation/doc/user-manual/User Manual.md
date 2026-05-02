# Dataframe-Level Anonymisation - User Manual

**Version:** 0.3.1  
**Last Updated:** December 10, 2025  
**Component:** Dataframe-Level Anonymisation Service  
**Part of:** Simpl-open ecosystem

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Available Jobs](#available-jobs)
4. [Operation description](#operation-description)

---

### What is Dataframe-Level Anonymisation?

The Dataframe-Level Anonymisation code location provides privacy-preserving transformations applied at the dataset level, focusing on structured tabular data.
It implements k-anonymity, l-diversity, and t-closeness to ensure that sensitive attributes cannot be used to re-identify individuals within a dataset.
This component is designed specifically for structured datasets, performing anonymisation on pandas DataFrames loaded from these inputs. It does not provide any depseudo-anonymisation or reversible transformation capabilities.

#### Difference Pseudonymisation vs Anonymisation

| Feature | Pseudonymisation (GDPR Article 4(5)) | Anonymisation (GDPR Recital 26) |
| :--- | :--- | :--- |
| **Definition** | Processing data so it can **no longer be attributed** to a specific individual *without the use of additional information* (the key/mapping table). | Processing data so the individual is **no longer identifiable** by any means reasonably likely to be used (irreversible). |
| **GDPR Scope** | **Still considered Personal Data** and must comply with all GDPR principles (lawfulness, security, data minimisation, etc.). | **Falls Outside GDPR Scope** once fully and irreversibly achieved. |
| **Reversibility** | **Reversible.** The original data can be recovered by linking the pseudonym back to the identity using the separate key. | **Irreversible.** The link to the individual is permanently destroyed. |
| **Guarantees** | **Reduced Risk of Harm** from a data breach, as direct identifiers are separated and protected. Still allows for internal linking/longitudinal studies. | **Zero or Negligible Risk of Re-Identification,** as the data is no longer tied to a natural person. |

When preparing data for anonymisation, attributes (columns) must be classified into three categories to determine the appropriate privacy technique:

| Attribute Category | Definition | Key Examples | Best Practice for De-identification |
| :--- | :--- | :--- | :--- |
| **1. Identifier** (Direct) | **Directly and uniquely identifies** a natural person. Data is unequivocally **Personal Data** under GDPR. | **Name,** **Email Address,** **Social Security Number (SSN),** Passport Number, Account IDs linked to a key. | **Remove completely** or replace with an **Irreversible Pseudonym** (e.g., cryptographic hash). If linking is necessary, use a **Reversible Pseudonym** and secure the key separately. |
| **2. Quasi-Identifier** (Indirect) | Does **not uniquely identify** alone, but can be **combined** with other QIs and external data to **re-identify** a person (the "Mosaic Effect"). | **Zip Code/Postcode,** **Date of Birth/Age,** Gender, Race/Ethnicity, Job Title, high-dimensional data patterns. | Apply **Generalisation** (e.g., specific age $\rightarrow$ age range), **Suppression** (remove rare/outlier values). The goal is to meet a standard like **$k$-anonymity**.  |
| **3. Sensitive Attribute** | The data of interest that, if revealed, can cause **significant harm** when linked to an individual. Often overlaps with **GDPR Special Category Data.** | **Medical Condition/Diagnosis,** **Income/Salary,** Political Opinions, Religious Beliefs, Sexual Orientation, Genetic Data. | Apply advanced privacy models like **$l$-diversity** (to ensure variety in sensitive values) or **$tT$-closeness** (to ensure distribution similarity) to prevent inference/homogeneity attacks. **Never remove** this data if it is the target of the analysis. |


#### Overall Best Practice Recommendations

* **Data Minimisation:** **Collect only the minimum set of attributes** required for the stated purpose. If an identifier is not strictly necessary for the analysis, do not collect it or remove it immediately.
* **Context is King:** The classification of an attribute as a Quasi-Identifier is **context-dependent.** An attribute that is safe in one country (e.g., low-density population area) may be highly revealing in another. Always consider the **external data** available to an attacker.
* **Irreversibility:** When aiming for **anonymisation** (to leave the scope of GDPR), ensure that the de-identification process is **practically irreversible** using all means reasonably likely to be used.
* **Holistic Approach:** Do not rely on $k$-anonymity alone. Pair it with **$l$-diversity** or **$t$-closeness** to protect the sensitive attributes from being inferred, even when quasi-identifiers are generalised.

#### Known Limitations and Cautions

All de-identification models involve a **privacy-utility trade-off** and have limitations that users must understand to prevent misuse or failure.

* **Effectiveness Depending on Dataset Size:** In small datasets, unique combinations of quasi-identifiers occur more frequently, forcing higher levels of **suppression** (removing records) or **generalisation** (broadening values). This makes the data less useful and may introduce bias.
* **Suppression Trade-offs:** When records with rare attribute combinations are suppressed to meet a privacy standard (like $K$-anonymity), the resulting dataset can be **skewed**. For instance, removing records for rare diseases may distort the true prevalence in the sample.
* **Distribution Skew:** De-identification techniques can **distort correlations** or summary statistics. If an attribute (like income) is highly correlated with a quasi-identifier (like a unique occupation), generalising or suppressing the quasi-identifier will likely introduce significant bias into the analysis of the sensitive attribute.
* **Model Failure:** Simple $k$-anonymity models are known to be vulnerable to **homogeneity attacks** (if all records in a group have the same sensitive value) and **background knowledge attacks** (if an attacker has external information). Users must be cautioned that meeting $k$-anonymity alone is often **not sufficient** for robust privacy.

### Key Capabilities

- **Structured Dataset Anonymisation**: Designed specifically for CSV datasets transformed into pandas DataFrames
- **Privacy Models Implemented**: 
    - **k-anonymity**: Ensures each quasi-identifier group has at least k indistinguishable rows
    - **l-diversity**: Guarantees diversity of sensitive attributes within each equivalence class
    - **t-closeness**: Ensures the sensitive attribute distribution remains close to the overall dataset distribution.
- **Dagster Integration**: Delivered as a Dagster code location providing reusable ops and jobs, fully orchestratable from the Dagster UI.
- **Metrics Output**: Produces anonymisation quality metrics and reports summarizing the achieved privacy guarantees.


## Getting Started

### Prerequisites

Before using this service, ensure:

1. **Service is installed as a code location within Dagtser**: Follow [Deployment Guide](../deployment-guide/Deployment Guide.md)
2. **Dagster UI accessible**: <http://localhost:3000> (local) or your cluster URL

### Accessing the Service

#### Option 1: Dagster UI (Recommended)

1. Open browser: **<http://localhost:3000>**
2. Navigate to **Jobs** in left sidebar
3. Select a job (e.g., `k_anonymity_job`)
4. Click **Launchpad** to configure and execute

#### Option 2: Python API

```python
from dataframe_level_anonymisation.repository import defs

# Get job definition
job_def = defs.get_job_def("k_anonymity_job")

# Execute with run config
result = job_def.execute_in_process(
    run_config={
        "ops": {
            "read_csv_to_df": {
                "config": {"input_path": "input/data.csv"}
            },
            "apply_k_anonymity": {
                "config": {
                    "ident": ["name"],
                    "sensitive_attributes": ["disease"],
                    "quasi_identifiers": ["gender", "age"],
                    "k": 2,
                    "supp_level": 0.0,
                    "generalisation_hierarchies": {
                        "gender": "simpl_gender",
                        "age": "simpl_age"
                    }
                }
            }
        }
    }
)

```

## Available Jobs

#### 1. `k_anonymity_job`

**Purpose:** Anonymize dataframe using k-anonymity algorithm

**Pipeline:**

```
read_csv_to_df → preview_dataframe → apply_k_anonymity → preview_dataframe → write_df_to_csv
```

**Use Cases:**

- Apply k-anonymity to ensure each record is indistinguishable from at least k others
- Generalize quasi-identifiers (e.g., age ranges, gender categories) to reduce re-identification risk
- Suppress outlier records that cannot meet the desired k-level

**Configuration Example:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "/app/input/input.csv"

  apply_k_anonymity:
    config:
      ident: ["name"]
      sensitive_attributes: ["disease"]
      quasi_identifiers: ["gender","age"]
      k: 4
      supp_level: 0.0
      generalisation_hierarchies:
        gender: "simpl_gender"
        age: "simpl_age"
          
  write_df_to_csv:
    config:
      output_path: "/app/shared/output.csv"

```

#### 2. `l_diversity_job`

**Purpose:** Anonymize dataframe using l-diversity algorithm

**Pipeline:**

```
read_csv_to_df → preview_dataframe → apply_l_diversity → preview_dataframe → write_df_to_csv
```

**Use Cases:**

- Apply l-diversity to ensure that each equivalence class contains at least l well-represented sensitive values
- Protect datasets where sensitive attributes (e.g., medical conditions, income category, behavioural data) must remain diverse to avoid attribute disclosure
- Strengthen privacy beyond k-anonymity by preventing attackers from inferring sensitive information even when groups are sufficiently large

**Configuration Example:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "/app/input/input.csv"

  apply_l_diversity:
    config:
      ident: ["name"]
      sensitive_attribute: "disease"
      quasi_identifiers: ["age"]
      k: 2
      l: 3
      supp_level: 0.0
      generalisation_hierarchies:
        age: "simpl_age"
          
  write_df_to_csv:
    config:
      output_path: "/app/shared/output.csv"

```

#### 3. `t_closeness_job`

**Purpose:** Anonymize dataframe using t-closeness algorithm

**Pipeline:**

```
read_csv_to_df → preview_dataframe → apply_t_closeness → preview_dataframe → write_df_to_csv
```

**Use Cases:**

- Apply t-closeness to ensure that the distribution of sensitive attributes within each equivalence class remains close to the overall dataset distribution
- Prevent attribute disclosure even when attackers know the quasi-identifier group of a subject
- Protect datasets where sensitive values follow meaningful statistical distributions (e.g., disease prevalence, income distribution, risk categories)

**Configuration Example:**

```yaml
ops:
  read_csv_to_df:
    config:
      input_path: "/app/input/input.csv"

  apply_t_closeness:
    config:
      ident: ["name"]
      sensitive_attribute: "disease"
      quasi_identifiers: ["age"]
      k: 2
      t: 0.5
      supp_level: 0.0
      generalisation_hierarchies:
        age: "simpl_age"
          
  write_df_to_csv:
    config:
      output_path: "/app/shared/output.csv"

```

## Operation description

#### 1. `apply_k_anonymity`

**Purpose:** Enforces the k-anonymity privacy model on a structured dataset (a CSV file loaded as a DataFrame).
The goal is to ensure that each record is indistinguishable from at least k–1 other records with respect to the selected quasi-identifiers.
The algorithm works in three main stages:
- Identification of key columns
    - Columns in quasi_identifiers are used to form equivalence classes.
    - Columns in sensitive_attributes contain sensitive values that must remain valid.
    - Columns in ident are treated as direct identifiers and removed or suppressed.
- Generalization
    - Each quasi-identifier is transformed using its associated generalization hierarchy
- Suppression and compliance validation
    If any equivalence class contains fewer than k records, the algorithm attempts:
    - broader generalization levels (if available), or
    - record suppression (within the allowed supp_level).

The final output ensures that every equivalence class meets the k-anonymity requirement, reducing the risk of re-identification.

**Configuration parameters:**

- ident(list[str], required): Direct identifier columns (e.g., name, tax ID). These are removed or suppressed to prevent identity disclosure.
- sensitive_attributes(list[str], required): Columns containing sensitive information (e.g., disease, salary). They are not generalized but are preserved for downstream analysis.
- quasi_identifiers(list[str], required): Columns that may indirectly identify individuals when combined (e.g., age, gender, ZIP code). These form the equivalence classes.
- k(int, required): Minimum group size required for each equivalence class. Higher values provide stronger privacy.
- supp_level(float, required): Maximum fraction of records that can be suppressed (0.0 means no suppression allowed).
- generalisation_hierarchies(dict[str,str], required): Mapping between each quasi-identifier and the generalization hierarchy to apply (e.g., "age": "simpl_age" or "gender": "simpl_gender"). The only available

**Configuration Example:**

```yaml
apply_k_anonymity:
  config:
    ident: ["name"]
    sensitive_attributes: ["disease"]
    quasi_identifiers: ["gender", "age"]
    k: 4
    supp_level: 0.0
    generalisation_hierarchies:
      gender: "simpl_gender"
      age: "simpl_age"

```

**Explanation:**
- Removes the name column (direct identifier).
- Keeps disease as the sensitive attribute.
- Builds equivalence classes from gender + age.
- Applies generalization rules defined in simpl_gender and simpl_age.
- Enforces groups of at least 4 records.
- No suppression is allowed (supp_level = 0.0).

**Example input**

```
| id   | Name    |   age | gender   | disease   |
|:-----|:--------|------:|:---------|:----------|
| 145B | Albert  |    25 | M        | Flu       |
| 245B | Bob     |    26 | M        | Cold      |
| 3245 | Charlie |    27 | M        | Cold      |
| 4324 | David   |    28 | M        | Cold      |
| 5AB7 | Eva     |    36 | F        | Cancer    |
| 6BFF | Franka  |    36 | F        | Flu       |
| 778B | Gracia  |    37 | F        | Cold      |
| 89BB | Hannah  |    37 | F        | Flu       |
| 99BA | Ivan    |    46 | M        | Cancer    |
| 10A5 | Jack    |    47 | M        | Cancer    |
| 99BA | Igor    |    42 | M        | Flu       |
| 10A5 | Jon     |    43 | M        | Cold      |
```

**Example output**

```
| id   | Name   | age      | gender   | disease   |
|:-----|:-------|:---------|:---------|:----------|
| 145B | *      | [20, 30) | M        | Flu       |
| 245B | *      | [20, 30) | M        | Cold      |
| 3245 | *      | [20, 30) | M        | Cold      |
| 4324 | *      | [20, 30) | M        | Cold      |
| 5AB7 | *      | [30, 40) | F        | Cancer    |
| 6BFF | *      | [30, 40) | F        | Flu       |
| 778B | *      | [30, 40) | F        | Cold      |
| 89BB | *      | [30, 40) | F        | Flu       |
| 99BA | *      | [40, 50) | M        | Cancer    |
| 10A5 | *      | [40, 50) | M        | Cancer    |
| 99BA | *      | [40, 50) | M        | Flu       |
| 10A5 | *      | [40, 50) | M        | Cold      |
```

#### 2. `apply_l_diversity`

**Purpose:** Enforces the l-diversity privacy model on datasets processed as DataFrames.
This model extends k-anonymity by protecting against attribute disclosure: even if a group of records is indistinguishable (k-anonymous), the sensitive attribute must still show sufficient diversity within each equivalence class.
The algorithm works in three main stages:
- Equivalence Class Construction
    - Records are grouped by the selected quasi_identifiers (e.g., generalized age ranges).
- Diversity Evaluation
    - For each equivalence class, the sensitive attribute (e.g., disease) must contain at least l distinct values.
- Generalization & Suppression
    If an equivalence class does not meet the required l-diversity level:
    - broader generalization (via the defined hierarchy) is attempted,
    - or, if still insufficient, suppression is applied (within allowed supp_level).

The final output ensures that every equivalence class meets the k-anonymity requirement and the l-divesity requirement.

**Configuration parameters:**

- ident(list[str], required): Direct identifier columns (e.g., name, tax ID). These are removed or suppressed to prevent identity disclosure.
- sensitive_attribute(str, required): The sensitive attribute that must have l distinct values per equivalence class.
- quasi_identifiers(list[str], required): Columns that may indirectly identify individuals when combined (e.g., age, gender, ZIP code). These form the equivalence classes.
- k(int, required): Minimum group size required for each equivalence class. Higher values provide stronger privacy.
- l(int, required): Minimum number of distinct sensitive-attribute values per class (l-diversity).
- supp_level(float, required): Maximum fraction of records that can be suppressed (0.0 means no suppression allowed).
- generalisation_hierarchies(dict[str,str], required): Mapping between each quasi-identifier and the generalization hierarchy to apply (e.g., "age": "simpl_age" or "gender": "simpl_gender"). The only available

**Configuration Example:**

```yaml
apply_l_diversity:
  config:
    ident: ["name"]
    sensitive_attribute: "disease"
    quasi_identifiers: ["age", "gender"]
    k: 2
    l: 3
    supp_level: 0.0
    generalisation_hierarchies:
      age: "simpl_age"
      gender: "simpl_gender"

```

**Explanation:**
- Removes the name column (direct identifier).
- age and gender are the quasi-identifier, generalized using simpl_age and simpl_gender hierarchies.
- The sensitive attribute is disease.
- Each equivalence class must have at least:
  - k = 2 records, and
  - l = 3 distinct disease values.
- No suppression is allowed (supp_level = 0.0), so all generalization attempts must succeed.

**Example input**

```
| id   | Name    |   age | gender   | disease   |
|:-----|:--------|------:|:---------|:----------|
| 145B | Albert  |    25 | M        | Flu       |
| 245B | Bob     |    26 | M        | Cold      |
| 3245 | Charlie |    27 | M        | Cold      |
| 4324 | David   |    28 | M        | Cold      |
| 5AB7 | Eva     |    36 | F        | Cancer    |
| 6BFF | Franka  |    36 | F        | Flu       |
| 778B | Gracia  |    37 | F        | Cold      |
| 89BB | Hannah  |    37 | F        | Flu       |
| 99BA | Ivan    |    46 | M        | Cancer    |
| 10A5 | Jack    |    47 | M        | Cancer    |
| 99BA | Igor    |    42 | M        | Flu       |
| 10A5 | Jon     |    43 | M        | Cold      |
```

**Example output**

```
| id   | Name   | age      | gender   | disease   |
|:-----|:-------|:---------|:---------|:----------|
| 145B | *      | [0, 100) | M        | Flu       |
| 245B | *      | [0, 100) | M        | Cold      |
| 3245 | *      | [0, 100) | M        | Cold      |
| 4324 | *      | [0, 100) | M        | Cold      |
| 5AB7 | *      | [0, 100) | F        | Cancer    |
| 6BFF | *      | [0, 100) | F        | Flu       |
| 778B | *      | [0, 100) | F        | Cold      |
| 89BB | *      | [0, 100) | F        | Flu       |
| 99BA | *      | [0, 100) | M        | Cancer    |
| 10A5 | *      | [0, 100) | M        | Cancer    |
| 99BA | *      | [0, 100) | M        | Flu       |
| 10A5 | *      | [0, 100) | M        | Cold      |
```

#### 3. `apply_t_closeness`

**Purpose:** Enforces the t-closeness privacy model on structured datasets processed as DataFrames.
This model extends l-diversity by not only requiring diversity in the sensitive attribute but also ensuring that the distribution of the sensitive attribute within each equivalence class is statistically close to the global distribution.
The algorithm works in four main stages:
- Equivalence Class Construction
    - Records are grouped by the selected quasi_identifiers (e.g., generalized age ranges).
- Distance Calculation
    - For each group, the algorithm computes a distance metric between:
      - the global distribution of the sensitive attribute, and
      - the distribution within the group.
- Closeness Validation
    A group satisfies t-closeness if the computed distance is ≤ t.
- Generalization & Suppression
    If a group violates t-closeness, the algorithm attempts to fix it by:
      - applying generalizations defined in the hierarchies,
      - merging groups, or
      - applying suppression (limited by supp_level).

The final output ensures that every equivalence class meets the k-anonymity requirement and the t-closeness requirement.

**Configuration parameters:**

- ident(list[str], required): Direct identifier columns (e.g., name, tax ID). These are removed or suppressed to prevent identity disclosure.
- sensitive_attribute(str, required): The sensitive attribute that must have l distinct values per equivalence class.
- quasi_identifiers(list[str], required): Columns that may indirectly identify individuals when combined (e.g., age, gender, ZIP code). These form the equivalence classes.
- k(int, required): Minimum group size required for each equivalence class. Higher values provide stronger privacy.
- t(float, required): Maximum allowed distance between global and local distributions.
- supp_level(float, required): Maximum fraction of records that can be suppressed (0.0 means no suppression allowed).
- generalisation_hierarchies(dict[str,str], required): Mapping between each quasi-identifier and the generalization hierarchy to apply (e.g., "age": "simpl_age" or "gender": "simpl_gender"). The only available

**Configuration Example:**

```yaml
apply_t_closeness:
  config:
    ident: ["name"]
    sensitive_attribute: "disease"
    quasi_identifiers: ["age"]
    k: 2
    t: 0.2
    supp_level: 0.0
    generalisation_hierarchies:
      age: "simpl_age"

```

**Explanation:**
- Removes the name column (direct identifier).
- age is the quasi-identifier, generalized using the simpl_age hierarchy.
- The sensitive attribute is disease.
- Each equivalence class must contain at least 2 records (k = 2).
- The distribution of disease within each group must be within 0.5 distance from the global distribution.
- No suppression is permitted (supp_level = 0.0), so generalization must resolve any violations.

**Example input**

```
| id   | Name    |   age | gender   | disease   |
|:-----|:--------|------:|:---------|:----------|
| 145B | Albert  |    25 | M        | Flu       |
| 245B | Bob     |    26 | M        | Cold      |
| 3245 | Charlie |    27 | M        | Cold      |
| 4324 | David   |    28 | M        | Cold      |
| 5AB7 | Eva     |    36 | F        | Cancer    |
| 6BFF | Franka  |    36 | F        | Flu       |
| 778B | Gracia  |    37 | F        | Cold      |
| 89BB | Hannah  |    37 | F        | Flu       |
| 99BA | Ivan    |    46 | M        | Cancer    |
| 10A5 | Jack    |    47 | M        | Cancer    |
| 99BA | Igor    |    42 | M        | Flu       |
| 10A5 | Jon     |    43 | M        | Cold      |
```

**Example output**

```
| id   | Name   | age      | gender   | disease   |
|:-----|:-------|:---------|:---------|:----------|
| 145B | *      | [0, 100) | M        | Flu       |
| 245B | *      | [0, 100) | M        | Cold      |
| 3245 | *      | [0, 100) | M        | Cold      |
| 4324 | *      | [0, 100) | M        | Cold      |
| 5AB7 | *      | [0, 100) | F        | Cancer    |
| 6BFF | *      | [0, 100) | F        | Flu       |
| 778B | *      | [0, 100) | F        | Cold      |
| 89BB | *      | [0, 100) | F        | Flu       |
| 99BA | *      | [0, 100) | M        | Cancer    |
| 10A5 | *      | [0, 100) | M        | Cancer    |
| 99BA | *      | [0, 100) | M        | Flu       |
| 10A5 | *      | [0, 100) | M        | Cold      |
```