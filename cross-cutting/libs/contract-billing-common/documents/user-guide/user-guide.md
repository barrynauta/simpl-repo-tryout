# User Guide

## Purpose
This guide provides step-by-step instructions and best practices for using the `common` library into production 
or controlled environments, including cloud, on-premises, containers, and Kubernetes. 
It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, 
and recovery procedures.

---

## Component Description

This component provides following functionalities:
1. Exception Handling - provides a unified mechanism for managing and propagating errors across services:
    - BadArgumentException – Thrown when invalid or missing arguments are detected.
    - RecordNotFoundException – Raised when a requested record cannot be found.
    - CustomResponseStatusException, ResponseStatusSingleException, ResponseStatusMultilineException – Custom exception
      wrappers for more expressive API error responses.
    - GlobalExceptionHandler – Centralized handler for mapping exceptions to consistent HTTP responses.

2. Security & Authentication - implements core authentication logic and security configuration shared between services:
    - ApiKeyAuthentication, AuthenticationFilter, AuthenticationService – components enabling API key–based
      authentication and request filtering.
    - SecurityConfig – provides Spring Security configuration for secure endpoints.
    - SecretClientConfig, SecretClientRetriever, SecretRetriever, ClientKey – utilities for managing secret keys
      and retrieving them from external secret stores.

3. External Communication
    - ExternalRequestService – Common HTTP client service for safely performing outbound REST API requests between microservices.

4. Error Model
    - Standardized error transfer objects for consistent API responses:
    - ErrorCode – Enumerates system-wide error identifiers.
    - ErrorTO, ErrorListTO – DTOs for representing single or multiple errors in API responses.

5. Logging Utilities
    - LogUtils – Helper class for structured logging and consistent log formatting across services.

6. Purpose
   The common module acts as a foundational dependency for any backend services in the system which requires it.
   It ensures:
    - Unified error response structure.
    - Consistent authentication logic.
    - Shared security and configuration standards.
    - Reusable communication and logging utilities.

By centralizing these shared elements, the library helps maintain cleaner microservices with less duplicated
boilerplate code and simpler integration.

---

## Prerequisites
- access to git repository for downloading the library

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture, minimum 2 vCPUs, 4GB RAM (production: 4+ vCPUs, 8GB+ RAM recommended).
- **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+, or compatible). Windows.

---

## 2. Configuration Details

- no configuration required

---

## 3. Step-by-Step Deployment

Adding the Dependency: Include the common library in your microservice’s pom.xml:

```
    <dependency>
        <groupId>eu.europa.ec.simpl</groupId>
        <artifactId>COMMON</artifactId>
        <version>${simpl.common.version}</version>
    </dependency>
```

---

## 4. Security Best Practices

- **Network**: This component should only be accessible from trusted networks or as internal cluster service.
- **Updates**: Regularly update base dependency.

---

