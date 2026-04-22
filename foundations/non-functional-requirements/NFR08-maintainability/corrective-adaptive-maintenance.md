# Corrective & adaptive maintenance

## Overview

None.

## Corrective & adaptive maintenance

Description Simpl-Open shall support controlled, repeatable and testable corrective and adaptive maintenance procedures for all middleware components. This includes version upgrades, security patches, schema migrations, configuration adjustments, and compatibility updates required to ensure service continuity. Maintenance operations shall preserve existing data, configurations and identity attributes, unless explicitly stated otherwise, and shall not disrupt interoperability between participants, gateways and services.  SMART Breakdown Specific: Each Simpl component shall provide a documented maintenance and upgrade procedure covering configuration updates, schema migration steps, compatibility validation and rollback instructions, including preservation of existing data and configurations. Measurable: Maintenance success shall be verified through automated regression tests, smoke tests, loading and validation of existing configurations, observability checks and manual confirmation that no regressions or disruptions occur. Achievable: The maintenance capability shall rely on existing CI/CD pipelines, automated validation tooling, observability mechanisms, versioning frameworks and container-based deployment practices already used across Simpl. Realistic:  Simpl’s modular architecture, declarative configuration model and use of standardised components allow corrective and adaptive maintenance to be performed safely and without redesigning core building blocks. Timely:  Maintenance and upgrade procedures shall be validated as part of the release preparation workflow and executed within the same development cycle in which they are initiated.   Detailed

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/corrective-adaptive-maintenance](https://simpl-programme.ec.europa.eu/book-page/corrective-adaptive-maintenance)
