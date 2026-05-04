# Deployment guide

## Deployment on Kubernetes

To deploy Keycloak for an authority or participant on Kubernetes using Helm, you can use the Bitnami Keycloak chart with a custom values file.

Refer to [Keycloak Deployment Documentation](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/blob/develop/versioned_docs/2.9.x/README.md#keycloak) for a complete guide.

To enable this extension you need to deploy the custom SPI JAR file into Keycloak. You can achieve this by using an init container to download the JAR file and mount it into the Keycloak providers directory.

For example, with reference to the configuration provided in the documentation linked above, you can add edit the `values.yaml` file to configure the `init-spi` init container as follows:

```yaml
initContainers: 
  - name: init-spi
    image: curlimages/curl
    command: ["/bin/sh", "-c"]
    env:
      - name: ARTIFACT
        value: keycloak-authenticator
      - name: URL
        value: https://code.europa.eu/api/v4/projects/915/packages/maven/com/aruba/simpl/keycloak-authenticator/2.2.0/keycloak-authenticator-2.2.0.jar
      # Add the following lines to install eIDAS Demo Extension SPI
      - name: EIDAS_EXTENSION_ARTIFACT
        value: keycloak-eidas-demo-authenticator
      - name: EIDAS_EXTENSION_URL
        value: https://code.europa.eu/api/v4/projects/1313/packages/maven/eu/europa/ec/simpl/eidas-demo-keycloak-extension/0.0.1/eidas-demo-keycloak-extension-0.0.1.jar

    args:
      - |
        curl -o /custom-spi/${ARTIFACT}.jar ${URL};
      # Add the following line to install eIDAS Demo Extension SPI
        curl -o /custom-spi/${EIDAS_EXTENSION_ARTIFACT}.jar ${EIDAS_EXTENSION_URL};
    volumeMounts:
      - name: spi-volume
        mountPath: /custom-spi
```