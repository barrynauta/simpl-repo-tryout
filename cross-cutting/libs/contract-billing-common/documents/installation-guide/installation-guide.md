# Installation Guide

## Overview
This guide will help you install and run **common** library on a fresh system. 
Follow the steps for your operating system and refer to troubleshooting if you encounter issues.

---

## Prerequisites

- **Java**: JDK 21 or higher
- **Maven**: 3.8.x or higher
- **Git**: Latest stable version
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for downloading dependencies

> **Note:** Ensure your `JAVA_HOME` and `MAVEN_HOME` environment variables are set correctly.

---

## Step-by-Step Installation

### 1. Add the Dependency: 

Include the common library in your microservice’s pom.xml:

```
    <dependency>
        <groupId>eu.europa.ec.simpl</groupId>
        <artifactId>COMMON</artifactId>
        <version>${simpl.common.version}</version>
    </dependency>
```

### 2. Build the Project

```
mvn clean install
```

---

## Example Output

After a successful build, you should see output similar to:
```
[INFO] BUILD SUCCESS
```

---
### 3. Run your Microservice Application

Refer to the documentation or run the generated JAR/WAR file as per your deployment needs.

---

## Troubleshooting

- **Java not found**: Ensure Java is installed and `JAVA_HOME` is set.
- **Maven not found**: Install Maven and add it to your PATH.
- **Dependency download errors**: Check your internet connection and proxy settings.

---

## Version Information

- **common**: v1.0.0 or higher
- **Java**: 21+
- **Maven**: 3.9+
