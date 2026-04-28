# Installation Guide

## Overview
This guide will help you install and run **schemasyncadapter** on a fresh system. Follow the steps for your operating system and refer to troubleshooting if you encounter issues.

---

## Prerequisites

- **Java**: JDK 17 or higher
- **Maven**: 3.8.x or higher
- **Git**: Latest stable version
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for downloading dependencies

> **Note:** Ensure your `JAVA_HOME` and `MAVEN_HOME` environment variables are set correctly.

---

## Step-by-Step Installation

### 1. Clone the Repository

```
git clone https://code.europa.eu/simpl/simpl-open/development/data1/schemasyncadapter.git
cd schemasyncadapter
```

### 2. Build the Project

#### Windows
Run:
```
#build_and_release.bat
```

#### macOS/Linux
Run:
```
chmod +x #build_and_release.bat
./#build_and_release.bat
```

_Alternatively, use Maven directly:_
```
mvn clean install
```

### 3. Run the Application

Refer to the documentation or run the generated JAR/WAR file as per your deployment needs.

---

### 4. Verify Installation

To verify the application is running correctly, call the `/status` endpoint:

```
curl http://localhost:<port>/status
```

Replace `<port>` with the actual port number configured for the application.

---

## Example Output

After a successful build, you should see output similar to:
```
[INFO] BUILD SUCCESS
```

---

## Configuration

The application behaviour is controlled through configuration parameters.
Configuration values can be provided via:

- Environment variables
- Helm values (if deployed via Kubernetes)
- application.yml overrides

### Configuration Parameters
##### Core Service Configuration
###### This section defines the core runtime settings of the service, including ports, domain resolution and environment identifiers.
---------------
| Parameter name | Description                     | Default value | Allowed values/range | Minimum version | Status |
| -------------- | ------------------------------- | ------------- | -------------------- | --------------- | ------ |
| servicePort    | Service port exposed internally | 8080          | integer (1–65535)    | 1.1.0           | Active |
| containerPort  | Container listening port        | 8080          | integer (1–65535)    | 1.1.0           | Active |

##### Logging Configuration
###### This section defines logging behaviour, including log levels and dynamic configuration reload.
---------------
| Parameter name        | Description                            | Default value           | Allowed values/range            | Minimum version | Status |
| --------------------- | -------------------------------------- | ----------------------- | ------------------------------- | --------------- | ------ |
| log4j.config          | Path to log4j2 configuration file      | file:/config/log4j2.xml | valid file path                 | 1.1.0           | Active |
| log4j.monitorInterval | Log4j config reload interval (seconds) | 10                      | integer ≥ 0                     | 1.1.0           | Active |
| log4j.level.root      | Root logging level                     | INFO                    | TRACE, DEBUG, INFO, WARN, ERROR | 1.1.0           | Active |
| log4j.level.app       | Application logging level              | INFO                    | TRACE, DEBUG, INFO, WARN, ERROR | 1.1.0           | Active |
| log4j.level.feign     | Feign client logging level             | INFO                    | TRACE, DEBUG, INFO, WARN, ERROR | 1.1.0           | Active |

##### OpenAPI configuration
###### This section defines OpenAPI/Swagger exposure settings used for API documentation and service discovery.
---------
| Parameter name        | Description                                                 | Default value                                                                                      | Allowed values/range | Minimum version | Status |
| --------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------- | --------------- | ------ |
| openapiConfig.servers | Comma-separated list of server URLs used by Swagger/OpenAPI | [https://schema-sync-adapter.dev.simpl-europe.eu](https://schema-sync-adapter.dev.simpl-europe.eu) | valid URL(s)         | 1.1.0           | Active |

##### Observability (Open Telemetry)
###### This section defines telemetry and distributed tracing configuration for monitoring and observability.
---------
| Parameter name                      | Description                | Default value                                                                                  | Allowed values/range | Minimum version | Status |
| ----------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | --------------- | ------ |
| openTelemetry.disabled              | Disable OpenTelemetry SDK  | true                                                                                           | true/false           | 1.1.0           | Active |
| openTelemetry.environment           | Logical environment name   | local-dev                                                                                      | string               | 1.1.0           | Active |
| openTelemetry.service               | Logical service identifier | schema-sync-adapter                                                                            | string               | 1.1.0           | Active |
| openTelemetry.otlpExporter.endpoint | OTLP collector endpoint    | [http://collector.common01.dev.simpl-europe.eu](http://collector.common01.dev.simpl-europe.eu) | valid URL            | 1.1.0           | Active |
| openTelemetry.otlpExporter.protocol | OTLP protocol              | http/protobuf                                                                                  | http/protobuf, grpc  | 1.1.0           | Active |
| openTelemetry.propagators           | Context propagation type   | tracecontext                                                                                   | tracecontext         | 1.1.0           | Active |

##### Storage configuration
###### This section defines persistent storage configuration for schema management and file storage.
---------
| Parameter name                   | Description                                 | Default value                | Allowed values/range  | Minimum version | Status |
| -------------------------------- | ------------------------------------------- | ---------------------------- | --------------------- | --------------- | ------ |
| schemaVolumeClaim                | PersistentVolumeClaim ID for schema storage | nfs-storage-pvc              | valid PVC name        | 1.1.0           | Active |
| schemaPvcMountPath               | Mount path for schema storage               | /home/simpluser/data         | valid filesystem path | 1.1.0           | Active |
| schemaSyncService.repositoryPath | Path to synced schema repository            | /home/simpluser/data/schemas | valid filesystem path | 1.1.0           | Active |

##### Security Configuration
###### This section defines security-related configuration, including CORS and JWT enforcement.
---------
| Parameter name                   | Description                        | Default value      | Allowed values/range         | Minimum version | Status |
| -------------------------------- | ---------------------------------- | ------------------ | ---------------------------- | --------------- | ------ |
| web.mvc.cors.allowedOrigins      | Allowed CORS origins               | ""                 | comma-separated list or *    | 1.1.0           | Active |
| web.mvc.bearerToken.required     | Require JWT Bearer token           | true               | true/false                   | 1.0.0           | Active |
| web.mvc.bearerToken.allowedPaths | Paths excluded from JWT validation | /actuator/health/* | comma-separated ant patterns | 1.1.0           | Active |

##### Kafka Configuration
###### This section defines Kafka connectivity and authentication parameters.
---------
| Parameter name                  | Description                            | Default value                                           | Allowed values/range                | Minimum version | Status |
| ------------------------------- | -------------------------------------- | ------------------------------------------------------- | ----------------------------------- | --------------- | ------ |
| kafka.auth.type                 | Kafka authentication type              | SASL_PLAINTEXT                                          | PLAINTEXT, SASL_PLAINTEXT, SASL_SSL | 1.1.0           | Active |
| kafka.auth.mechanism            | Kafka authentication mechanism         | PLAIN                                                   | PLAIN, SCRAM-SHA-256, SCRAM-SHA-512 | 1.1.0           | Active |
| kafka.auth.loginModuleClass     | Login module class                     | org.apache.kafka.common.security.plain.PlainLoginModule | valid class name                    | 1.1.0           | Active |
| kafka.auth.username             | Kafka username                         | tbd                                                     | string                              | 1.1.0           | Active |
| kafka.auth.password             | Kafka password                         | tbd                                                     | string                              | 1.1.0           | Active |
| kafka.bootstrapServers          | Kafka bootstrap servers                | kafka.common01.svc.cluster.local:9092                   | host:port                           | 1.1.0           | Active |
| kafka.consumer.groupId          | Kafka consumer group ID                | schema-sync-adapter                                     | string                              | 1.1.0           | Active |
| kafka.fatalIfBrokerNotAvailable | Fail application if broker unavailable | true                                                    | true/false                          | 1.1.0           | Active |
| kafka.topic.processSchemaEvent  | Kafka topic name for schema events     | schema-sync-adapter                                     | string                              | 1.1.0           | Active |

##### Database Configuration
###### This section defines database connectivity for schema persistence.
---------
| Parameter name    | Description         | Default value                                                  | Allowed values/range | Minimum version | Status |
| ----------------- | ------------------- | -------------------------------------------------------------- | -------------------- | --------------- | ------ |
| postgres.url      | JDBC connection URL | jdbc:postgresql://localhost:5432/schema_sync_adapter?ssl=false | valid JDBC URL       | 1.1.0           | Active |
| postgres.username | Database username   | tbd                                                            | string               | 1.1.0           | Active |
| postgres.password | Database password   | tbd                                                            | string               | 1.1.0           | Active |

##### External service connectivity
###### This section defines URLs and routing configuration for dependent internal services.
---------
| Parameter name           | Description                   | Default value                                                                          | Allowed values/range | Minimum version | Status |
| ------------------------ | ----------------------------- | -------------------------------------------------------------------------------------- | -------------------- | --------------- | ------ |
| schemaManager.serviceUrl | URL of Schema Manager service | [http://localhost:8080/mock/schema-manager](http://localhost:8080/mock/schema-manager) | valid URL            | 1.1.0           | Active |

---
## Troubleshooting

- **Java not found**: Ensure Java is installed and `JAVA_HOME` is set.
- **Maven not found**: Install Maven and add it to your PATH.
- **Permission denied (macOS/Linux)**: Run `chmod +x #build_and_release.bat`.
- **Dependency download errors**: Check your internet connection and proxy settings.

---

## Automated Options

- Use the provided `#build_and_release.bat` script for automated build and release.
- For Dockerized deployments, check for a `Dockerfile` or related scripts in the repository.

---

## Version Information

- **schemasyncadapter**: v1.0.0 or higher
- **Java**: 17+
- **Maven**: 3.8+
