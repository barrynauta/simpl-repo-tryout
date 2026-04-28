# Installation Guide

## Overview

This guide will help you install and run **asset-orchestrator** on a fresh system. 
Follow the steps for your operating system and refer to troubleshooting if you encounter issues.

---

## Prerequisites

- **Java**: JDK 21 or higher
- **Maven**: 3.9.x or higher
- **Git**: Latest stable version
- **Docker**: 20.10+ (optional, for containerized development)
- **PostgreSQL**: 13+
- **Kafka**: Required at runtime
- **Dagster**: Required at runtime
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for downloading dependencies

> **Note:** Ensure your `JAVA_HOME` and `MAVEN_HOME` environment variables are set correctly.

---

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://code.europa.eu/simpl/data-orchestrator/asset-orchestrator.git
cd asset-orchestrator
```

### 2. Configure Environment

Copy the example environment file and configure your local settings:

```bash
cp .env.example .env
```

#### Docker vs Local execution

The provided `.env.example` file is **Docker-oriented**.  
When running the application locally, some values must be overridden.

| Variable                    | Docker value                | Local value                   |
|-----------------------------|-----------------------------|-------------------------------|
| DB_HOST                     | postgres                    | localhost                     |
| MAIL_HOST                   | mailpit                     | localhost                     |
| WORKFLOW_ENGINE_GRAPHQL_URL | http://dagster:3000/graphql | http://localhost:3000/graphql |
| KAFKA_BOOTSTRAP_SERVERS     | kafka:19092                 | localhost:9092                |
| OTEL_EXPORTER_OTLP_ENDPOINT | http://otel-collector:4318  | http://localhost:4318         |

Minimal local overrides:

```properties
DB_HOST=localhost
MAIL_HOST=localhost
WORKFLOW_ENGINE_GRAPHQL_URL=http://localhost:3000/graphql
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

### 3. Set Up Local Infrastructure

#### Option A: Using Docker Compose (Recommended)

##### Docker network

All provided Docker Compose files rely on an external Docker network.

Create it once before starting Docker services:

```bash
docker network create dagster_network
```

##### Start infrastructure services

Start PostgreSQL, Mailpit, Kafka and OpenTelemetry Collector:

```bash
cd scripts/docker
docker compose up -d postgres zookeeper kafka kafka-ui otel-collector
docker compose -f docker-compose-mailpit.yaml up -d
```

Create the database schema:

```bash
docker exec -it postgres psql -U postgres -c "CREATE DATABASE asset_orchestrator;"
docker exec -it postgres psql -U postgres -d asset_orchestrator -c "CREATE SCHEMA IF NOT EXISTS \"asset-orchestrator\";"
```

#### Option B: Manual infrastructure Setup

Install and start the required components locally:

- PostgreSQL 13+
- Kafka

Create the PostgreSQL database:

```sql
CREATE DATABASE asset_orchestrator;

\c asset_orchestrator

CREATE SCHEMA IF NOT EXISTS "asset-orchestrator";
```

---

### 4. Build the Project

#### Project version requirement

The project version is resolved from the following Maven expression:

```xml
<version>${env.PROJECT_RELEASE_VERSION:unknown}</version>
```

For local builds, choose **one** of the following options.

##### Option A: Set environment variable (recommended)

```bash
export PROJECT_RELEASE_VERSION=0.1.0
mvn clean install
```

##### Option B: Temporary local change to `pom.xml`

Edit `pom.xml` and replace the version with a fixed value:

```xml
<version>0.1.0-SNAPSHOT</version>
```

> This change must **not** be committed.

##### Build command

```bash
mvn clean install
```

---

### 5. Run the Application

#### Option A: Using Maven Spring Boot Plugin

```bash
mvn spring-boot:run
```

#### Option B: Using Docker Compose

```bash
cd scripts/docker
docker compose up -d simpl-asset-orchestrator
```

#### Option C: Using the JAR File

```bash
java -jar target/asset-orchestrator-*.jar
```

---

## 6. Verify Installation

### Check Application Health

To verify the application is running correctly, call the health endpoints:

```bash
# Liveness check
curl http://localhost:8080/v1/actuator/health/liveness

# Readiness check
curl http://localhost:8080/v1/actuator/health/readiness

# Full health details
curl http://localhost:8080/v1/actuator/health
```

Expected response:

```json
{
  "status": "UP"
}
```

---

### Access API Documentation

Open your browser and navigate to:

- **Swagger UI**: http://localhost:8080/v1/swagger-ui.html
- **OpenAPI Docs**: http://localhost:8080/v1/api-docs
- **OpenAPI Specification**: See `openapi/openapi-asset-orchestrator-v1.yaml`

### Test API Endpoints

Get available workflows:

```bash
curl -X GET http://localhost:8080/v1/workflows
```

Expected response:

```json
{
  "codeLocations": [
    {
      "id": "location-1",
      "name": "user_code",
      "loadStatus": "LOADED"
    }
  ],
  "total": 1
}
```

Create a workflow definition:

```bash
curl -X POST http://localhost:8080/v1/workflowDefinitions \
  -H "Content-Type: application/json" \
  -d '{
    "assetId": "asset-001",
    "assetType": "dataset",
    "assetDescription": "Customer analytics dataset",
    "providerEmail": "provider@example.com",
    "repositoryName": "my_repository",
    "codeLocation": "user_code",
    "jobName": "data_pipeline",
    "yamlConfiguration": {
      "ops": {
        "process_data": {
          "config": {
            "url": "${APP_URL}"
          }
        }
      }
    }
  }'
```

Expected response (201 Created):

```json
{
  "id": 1,
  "assetId": 1,
  "assetType": "dataset",
  "assetDescription": "Customer analytics dataset",
  "providerEmail": "provider@example.com",
  "repositoryName": "my_repository",
  "codeLocation": "user_code",
  "jobName": "data_pipeline",
  "associationTitle": "definition",
  "isActive": true,
  "yamlConfiguration": "ops:\n  process_data:\n    config:\n      url: ${APP_URL}"
}
```

---

## Example Output

After a successful build, you should see output similar to:

```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  2.456 s
[INFO] Finished at: 2025-12-01T10:30:00Z
[INFO] ------------------------------------------------------------------------
```

When the application starts successfully:

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::               (v3.5.7)

2025-12-01 10:30:15.123  INFO 12345 --- [           main] e.e.e.s.a.AssetOrchestratorApplication  : Starting AssetOrchestratorApplication
2025-12-01 10:30:16.456  INFO 12345 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http)
2025-12-01 10:30:16.789  INFO 12345 --- [           main] e.e.e.s.a.AssetOrchestratorApplication  : Started AssetOrchestratorApplication in 2.345 seconds
```

---

## Troubleshooting

### Common Issues

#### Java not found

**Error**: `java: command not found`

**Solution**:

- Install Java 21 or higher
- Set `JAVA_HOME` environment variable:
  ```bash
  # macOS/Linux
  export JAVA_HOME=/path/to/java21
  export PATH=$JAVA_HOME/bin:$PATH
  
  # Windows
  set JAVA_HOME=C:\path\to\java21
  set PATH=%JAVA_HOME%\bin;%PATH%
  ```

#### Maven not found

**Error**: `mvn: command not found`

**Solution**:

- Install Maven 3.9+ and add it to your PATH

#### Database Connection Failed

**Error**: `Unable to create initial connections of pool`

**Solution**:

- Verify PostgreSQL is running: `pg_isready` or `docker ps | grep postgres`
- Check database credentials in `.env` file
- Ensure database and schema exist:
  ```sql
  CREATE DATABASE asset_orchestrator;
  CREATE SCHEMA "asset-orchestrator";
  ```

### Kafka Connection Failed

**Error**: application fails to start or logs show Kafka connection errors

**Solution**:

- Verify Kafka is running:
  ```bash
  docker ps | grep kafka
  ```
- Check Kafka bootstrap server in `.env`:
  ```properties
  KAFKA_BOOTSTRAP_SERVERS=localhost:9092
  ```
- Verify broker connectivity:
  ```bash
  nc -z localhost 9092
  ```

#### Port Already in Use

**Error**: `Port 8080 is already in use`

**Solution**:

- Stop the process using port 8080:
  ```bash
  # macOS/Linux
  lsof -ti:8080 | xargs kill -9
  
  # Windows
  netstat -ano | findstr :8080
  taskkill /PID <pid> /F
  ```
- Or change the port in `.env`:
  ```properties
  SERVER_PORT=8081
  ```

#### Flyway Migration Errors

**Error**: `FlywayException: Unable to obtain connection from database`

**Solution**:

- Verify database connection parameters
- Check if schema exists: `SELECT schema_name FROM information_schema.schemata;`
- Clear Flyway history if needed (development only):
  ```sql
  DROP TABLE IF EXISTS "asset-orchestrator".flyway_schema_history;
  ```

#### Dependency Download Errors

**Error**: `Failed to execute goal on project: Could not resolve dependencies`

**Solution**:

- Check your internet connection
- Configure Maven proxy settings if behind a corporate firewall
- Clear Maven cache: `rm -rf ~/.m2/repository`
- Retry build: `mvn clean install -U`

---

## Development Setup

### IDE Configuration

#### IntelliJ IDEA

1. Open the project: `File > Open` → select `pom.xml`
2. Enable annotation processing: `Settings > Build, Execution, Deployment > Compiler > Annotation Processors`
3. Install Lombok plugin: `Settings > Plugins > Marketplace` → search "Lombok"
4. Set Java 21 SDK: `File > Project Structure > Project SDK`

#### Eclipse

1. Import as Maven project: `File > Import > Maven > Existing Maven Projects`
2. Install Lombok: Download `lombok.jar` and run `java -jar lombok.jar`
3. Set Java 21: `Project > Properties > Java Build Path > Libraries`

#### VS Code

1. Install extensions:
    - Extension Pack for Java
    - Spring Boot Extension Pack
    - Lombok Annotations Support
2. Open project folder
3. Configure Java home in settings: `java.configuration.runtimes`

### Running Tests

```bash
# Run all tests
mvn test

# Run specific test class
mvn test -Dtest=AssetOrchestratorTest

# Run with coverage
mvn clean test jacoco:report
```

---

## Next Steps

After successful installation:

1. **Review API Documentation**: Explore available endpoints at `/swagger-ui.html` or `/v1/api-docs`
2. **Deploy to Kubernetes**: Follow the [Deployment Guide](../deployment-guide/deployment-guide.md)

---

## Additional Resources

- [Deployment Guide](../deployment-guide/deployment-guide.md) - Production deployment instructions
- [API Documentation](http://localhost:8080/swagger-ui.html) - Interactive API docs (Swagger UI)
- [OpenAPI Specification](http://localhost:8080/v1/api-docs) - OpenAPI 3.0 JSON specification
- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/html/) Official Spring Boot documentation
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) Official PostgreSQL documentation
- [Kafka Documentation](https://kafka.apache.org/documentation/) Official Kafka documentation
- [Docker Documentation](https://docs.docker.com/) Official Docker documentation
