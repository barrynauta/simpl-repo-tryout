# Workflow Triggering on Input Dataset Change on S3 Storage

This guide provides explaination on how Dagster workflows can be automatically triggered when input datasets change in S3-compatible Object Storage and guidance on how to implement a Dagster Sensor that monitors dataset updates and triggers workflows accordingly.

This description explains:
- How automatic workflow triggering works in Dagster
- The role of Dagster sensors
- How to monitor S3-compatible object storage
- How to implement a polling-based dataset sensor
- How to avoid duplicate triggers
- How to configure storage access and runtime parameters

## 1. Automatic Workflow Triggering in Dagster

Dagster allows workflows (jobs) to be triggered automatically by Sensors.
A Sensor is a lightweight function that runs periodically and:
1. Polls an external system
2. Checks whether a condition is satisfied
3. Optionally launches one or more workflow runs

Sensors are commonly used to react to:
- Dataset updates
- File uploads
- Database changes
- External API events

In the context of data pipelines, sensors allow the implementation of data-driven workflows, where processing starts automatically when new data arrives.

## 2. Monitoring Dataset Changes in Object Storage
Many data pipelines store input datasets in S3-compatible Object Storage, such as:

- Amazon S3
- MinIO
- Garage
- Other S3-compatible systems

Typical dataset change scenarios include:

- A new file is uploaded
- An existing dataset is replaced
- A dataset is updated with a new version

The desired behavior is:  
*When a dataset stored in object storage changes, a Dagster workflow automatically processes the updated dataset.*

## 3. Event-Based vs Polling-Based Triggers

Some object storage systems support event notifications, but these are not always available or easily integrated with Dagster.  
For this reason, the most portable solution is polling-based sensors.

**Polling Strategy**  
The sensor periodically:
1. Queries object storage
2. Retrieves object metadata
3. Compares metadata with the previous state
4. Detects new or modified datasets
5. Triggers workflow runs

This approach works with any S3-compatible system.

## 4. Overview of Dagster Sensors

A Dagster sensor is defined using the `@sensor` decorator.

Example:
``` python
from dagster import sensor

@sensor(
    job_name="my_job",
    minimum_interval_seconds=30
)
def my_sensor(context):
    ...
```
Key properties:
| Parameter | Description |
| --- | --- |
| `job_name` | Job triggered by the sensor |
| `minimum_interval_seconds` | Minimum evaluation interval |
| `required_resource_keys` | External resources needed |

Sensors return one of the following:
| Return Type | Meaning |
| --- | --- |
| `RunRequest` | Trigger a workflow run |
| `SkipReason` | Skip execution |

## 5. Architecture for S3 Dataset Monitoring

The architecture consists of the following components:

```text
Object Storage (S3 / MinIO / Garage)
        │
        │ List objects
        ▼
Dagster Sensor
        │
        │ Detect dataset changes
        ▼
RunRequest
        │
        ▼
Dagster Job
        │
        ▼
Dataset Processing
```

## 6. Detecting Changes in Object Storage

Object storage systems do not provide direct information about dataset updates in a way that can be easily consumed by Dagster sensors. Instead, changes must be inferred by comparing **object metadata** retrieved from the storage API.

Each object stored in S3-compatible object storage exposes metadata fields that can be used to detect whether the dataset has changed.

### Available Object Metadata

The most relevant metadata fields exposed by S3-compatible storage systems are:

| Field | Description |
|---|---|
| `Key` | The unique object path within the bucket |
| `LastModified` | Timestamp indicating when the object was last modified |
| `ETag` | Hash representing the object content |
| `Size` | Object size in bytes |

These metadata values can be retrieved using the `list_objects_v2` API provided by S3-compatible services.

### Change Detection Strategies

Different strategies can be used to determine whether a dataset has changed.

| Strategy | Pros | Cons |
|---|---|---|
| `LastModified` | Simple and easy to compare | Timestamp may change without actual content change |
| `Size` | Fast comparison | Cannot detect changes when file size remains the same |
| `ETag` | Detects content changes reliably | Multipart uploads may generate non-standard ETags |
| Combined strategy | Most reliable approach | Slightly higher comparison cost |

Recommended Strategy:  
`ETag + LastModified + Size`

## 7. Sensor State Management
Dagster sensors maintain state using a **cursor**.
```text
context.cursor
```
Example state:
```json
{
  "incoming/file1.csv": {
    "etag": "abc123",
    "last_modified": "2025-03-01T10:00:00",
    "size": 2048
  }
}
```
Sensor execution flow:
1. Retrieve current object metadata
2. Load previous state from cursor
3. Compare metadata
4. Identify changed objects
5. Update cursor
6. Emit `RunRequest`

## 8. Configuring Access to S3-Compatible Storage
Dagster interacts with object storage via Python resources.  
Example resource definition:

```python
import boto3
import os
from dagster import resource

@resource
def object_storage_resource():
    """Provides a boto3 S3 resource connected to an object storage."""
    
    return boto3.resource(
        "s3",
        endpoint_url=os.environ.get("S3_ENDPOINT_URL"),
        aws_access_key_id=os.environ.get("S3_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("S3_SECRET_KEY"),
    )
```
Example environment variables:
```bash
S3_ENDPOINT_URL=http://minio:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
```
This configuration works with:
- AWS S3
- MinIO
- Garage
- Any S3-compatible storage

## 9. Implementing a Dagster Sensor for Dataset Monitoring
Below is a basic example of a sensor that monitors a bucket prefix and triggers processing jobs when objects change.
```python
from dagster import sensor, RunRequest, SkipReason
import json

@sensor(
    job_name="process_dataset_job",
    required_resource_keys={"object_storage_resource"},
    minimum_interval_seconds=30,
)
def s3_prefix_sensor(context):

    bucket_name = "data-bucket"
    prefix = "incoming/"

    s3_client = context.resources.object_storage_resource.meta.client

    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=prefix,
    )

    contents = response.get("Contents", [])

    if not contents:
        return SkipReason("No objects found under monitored prefix.")

    current_state = {
        obj["Key"]: {
            "etag": (obj.get("ETag") or "").strip('"'),
            "last_modified": obj["LastModified"].isoformat(),
            "size": obj.get("Size", 0),
        }
        for obj in contents
        if not obj["Key"].endswith("/")
    }

    previous_state = json.loads(context.cursor) if context.cursor else {}

    changed_objects = []

    for key, metadata in current_state.items():
        old_metadata = previous_state.get(key)

        if old_metadata is None:
            changed_objects.append(key)
            continue

        if (
            old_metadata.get("etag") != metadata.get("etag")
            or old_metadata.get("last_modified") != metadata.get("last_modified")
            or old_metadata.get("size") != metadata.get("size")
        ):
            changed_objects.append(key)

    if not changed_objects:
        return SkipReason("No new or modified objects detected.")

    context.update_cursor(json.dumps(current_state))

    return [
        RunRequest(
            run_key=f"{bucket_name}:{key}:{current_state[key]['etag']}",
            run_config={
                "ops": {
                    "process_object": {
                        "config": {
                            "bucket_name": bucket_name,
                            "object_key": key,
                        }
                    }
                }
            },
            tags={
                "source": "object_storage",
                "bucket": bucket_name,
                "key": key,
            },
        )
        for key in changed_objects
    ]
```

## 10. Avoiding Duplicate Workflow Triggers
Dagster provides two mechanisms to prevent duplicate runs.

### 1. Sensor Cursor

The cursor stores previously processed metadata.  
This ensures that objects are processed only when they change.

### 2. Run Keys

RunRequest.run_key ensures that identical runs are not triggered multiple times.  
Example:
```text
run_key = bucket + object_key + etag
```
If the same key is emitted twice, Dagster ignores duplicates.

## 11. Handling Configuration Parameters
Sensors may need configurable parameters such as:

- bucket name
- monitored prefix
- polling interval

These can be provided through:

- environment variables
- Dagster resources
- configuration files

Example:
```python
bucket_name = os.getenv("INPUT_BUCKET")
prefix = os.getenv("INPUT_PREFIX", "incoming/")
```

## 13. Best Practices

Recommended best practices:

### Use Prefix-Based Monitoring

Monitor specific dataset folders instead of entire buckets.  
Example:
```text
incoming/datasets/
```
### Avoid Too Frequent Polling

Typical sensor interval:
```text
30–120 seconds
```
### Use Metadata Comparison

Combine:

- `ETag`
- `LastModified`
- `Size`

### Use One Run Per Dataset

Each changed dataset should produce a separate `RunRequest`.