# Deployment guide

## Deployment Keycloak on Kubernetes

The `import-realm` init container allows you to download and copy from `code.europa.eu` the exported realm to a volume for an authority or participant. The exported realm contains pre-configured users for initialisation and demo purposes.

<!-- --version 22.2.5 is the chart version that correspond to keycloak version 25.0.5 -->
```bash
helm install keycloak bitnami/keycloak \
--version 22.2.5 \
--values < authority or participant keycloak values path >
```

#### Example of values.yaml
```yaml
apiUrl: "<authority or participant endpoint>" # example: https://participant.be.aruba-simpl.cloud
                                              # example: https://authority.be.aruba-simpl.cloud
extraEnvVars: 
  - name: KC_HOSTNAME_ADMIN
    value: "< apiUrl as above >/auth" # update
  - name: KC_HOSTNAME
    value: "< apiUrl as above >/auth" # update
  - name: USERS_ROLES_BASE_URL
    value: "http://users-roles.{{ .Release.Namespace }}.svc.cluster.local:8080" # update
  - name: AUTHENTICATION_PROVIDER_BASE_URL
    value: "http://authentication-provider.{{ .Release.Namespace }}.svc.cluster.local:8080" # update
  - name: KEYCLOAK_BASE_URL
    value: "< apiUrl as above >/auth" # update
  - name: REALM
    value: "<authority or participant>" # set this
  - name: KEYCLOAK_EXTRA_ARGS
    value: --import-realm

auth:
  adminUser: "user" # update
  adminPassword: "admin" # update

postgresql:
  enabled: false

externalDatabase:
  annotations: {}
  database: keycloak
  existingSecret: ""
  existingSecretDatabaseKey: ""
  existingSecretHostKey: ""
  existingSecretPasswordKey: ""
  existingSecretPortKey: ""
  existingSecretUserKey: ""
  host: "postgresql.{{ .Release.Namespace }}.svc.cluster.local" # update
  password: keycloak
  port: 5432
  user: keycloak

extraVolumes:
  - name: spi-volume
    emptyDir: {}
  - name: realm-volume
    emptyDir: {}

extraVolumeMounts:
  - name: spi-volume
    mountPath: /opt/bitnami/keycloak/providers/keycloak-authenticator.jar
    subPath: keycloak-authenticator.jar
  - name: realm-volume
    mountPath: /opt/bitnami/keycloak/data/import/realm.json
    subPath: realm.json

initContainers: 
  - name: init-spi
    image: curlimages/curl
    command: ["/bin/sh", "-c"]
    env:
      - name: ARTIFACT
        value: keycloak-authenticator
      - name: URL
        value: https://code.europa.eu/api/v4/projects/915/packages/maven/com/aruba/simpl/keycloak-authenticator/2.2.0/keycloak-authenticator-2.2.0.jar
    args:
      - |
        curl -o /custom-spi/${ARTIFACT}.jar ${URL};
    volumeMounts:
      - name: spi-volume
        mountPath: /custom-spi

  - name: import-realm
    image: nginx:latest
    command: ["/bin/sh", "-c"]
    env:
      - name: REDIRECT_URIS
        # Adjust the array values accordingly, list all the needed frontend endpoints of other components
        value: |
          [ "https://fe.{{ .Release.Namespace }}.dev.simpl-europe.eu/*" ]
      - name: REALM_NAME
        value: realm
      - name: URL
        # uncomment below if you are deploying an authority
        # value: https://code.europa.eu/simpl/simpl-open/development/iaa/charts/-/raw/develop/samples/keycloak-realms/2.0.0/authority-realm-export.json?ref_type=heads
        # uncomment below if you are deploying a participant
        # value: https://code.europa.eu/simpl/simpl-open/development/iaa/charts/-/raw/develop/samples/keycloak-realms/2.0.0/participant-realm-export.json?ref_type=heads
    args:
      - |
        curl ${URL} | envsubst '$REDIRECT_URIS' > /config/${REALM_NAME}.json;
    volumeMounts:
      - name: realm-volume
        mountPath: /config
```

