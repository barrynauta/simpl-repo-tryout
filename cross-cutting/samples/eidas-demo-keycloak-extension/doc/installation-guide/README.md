# Installation Guide

The eIDAS Demo Keycloak Extension is delivered as a deployable JAR file.
During the build process, the project produces an artifact located in the target/deploy directory.
This file represents the Keycloak provider and must be added to the Keycloak installation so that it can be loaded at
startup.

### Build Instructions

You can follow these instructions to build the project manually:
From the project root:

``` bash
mvn package
```

The deployment artifact will be generated at:

    /target/deploy/<jar-name>.jar

Copy this file into your Keycloak container:

    /opt/keycloak/providers

Restart Keycloak afterwards.

---

## Provider Deployment

To install the component, the generated JAR must be placed inside the Keycloak providers directory.
A typical deployment places it under:

```
  /opt/keycloak/providers
```

(or the equivalent directory depending on the specific Keycloak distribution).

Once the file is present, Keycloak will detect and load the custom SPI module during its next startup.

## Required Configuration

The eIDAS Demo Keycloak Extension requires the configuration of eIDAS Identity Attributes in order to work.

By default, the configuration is bundled within the JAR file itself, but it can be overridden by providing a custom
environment variable.

### Required Environment Variables

No mandatory environment variables are required for the basic operation of the extension.

### Optional Environment Variables

| Variable                     | Description                                                                                                                   | Default |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| `EIDAS_ATTRIBUTES_FILE_PATH` | If set, loads the eIDAS attributes configuration from the specified path, otherwise uses the resource bundled within the JAR. | (empty) |

### eIDAS Attributes Configuration

The eIDAS attributes configuration file is a JSON file containing an array of objects representing the available eIDAS attributes. Each object should contain the following fields:

- `friendlyName`: A user-friendly name for the attribute (e.g., "BirthName")

- `humanReadableName`: A human-readable name for the attribute (e.g., "Names at Birth")

- `personType`: The type of person the attribute applies to (e.g., "NATURAL_PERSON" or "LEGAL_PERSON")

- `category`: The category of the attribute (e.g., "MANDATORY_MINIMUM_DATA_SET", "OPTIONAL_MINIMUM_DATA_SET", "COMMON", "SECTOR_SPECIFIC")

- `uri`: The URI of the attribute (e.g., "http://eidas.europa.eu/attributes/naturalperson/BirthName")