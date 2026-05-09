## Onboarding Frontend

### Install on Kubernetes
```shell
helm repo add fe-onboarding-charts https://code.europa.eu/api/v4/projects/1307/packages/helm/stable
helm install fe-onboarding fe-onboarding-charts/fe-onboarding \
--version <chart version> \
--values values.yaml
```

> **💡** The latest chart version can be found in the releases section of the project's repository. Please note that hotfixes may have been released since the last major update. Hotfixes may have been released. [Link to releases](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding/-/releases).

#### Example of values.yaml
```yaml
hostFe: fe.<agent-namespace>.fe.dev.simpl-europe.eu # this is an example, update this field
cors: # this is an example, update this field
  allowOrigin: https://t1.<agent-namespace>.dev.simpl-europe.eu,https://onboarding.<agent-namespace>.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:4203,http://localhost:3000
ingress:
  issuer: dev-prod

env:
  - name: API_URL
    value: "https://t1.<agent-namespace>.dev.simpl-europe.eu" # this is an example, update this field
  - name: KEYCLOAK_URL
    value: "https://t1.<agent-namespace>.dev.simpl-europe.eu/auth" # this is an example, update this field
  - name: KEYCLOAK_REALM
    value: "<onboarding>"
  - name: KEYCLOAK_CLIENT_ID
    value: "frontend-cli"
  - name: EIDAS_ENABLED
    value: "false"
```

### Configuration
The configuration provides details on the backend and frontend host URLs, CORS allowed origins, ingress issuer, and environment variables for the onboarding application. For further configuration, view the Helm template and update the values as required.

**Frontend Host Configuration**
- `hostFe`: The hostname for the frontend service. Value: `my.frontend.host`

**CORS Configuration - Allowed Origins**
- `cors.allowOrigin`: Specifies the origins that are allowed to access the application resources via cross-origin requests.
  - Value: `https://my.frontend.host, https://<agent-namespace>.fe.aruba-simpl.cloud, http://localhost:4202, http://localhost:4203, http://localhost:3000`

**Ingress Configuration - Issuer**
- `ingress.issuer`: The issuer for the ingress, which is typically used for managing TLS certificates. Value: `your-issuer-ingress`

**Environment Variables**
- `API_URL`: The URL for the API backend. Value: `https://my.backend.host`

**Keycloak Configuration**
- `KEYCLOAK_URL`: The URL for the Keycloak authentication service. Value: `https://my.backend.host/auth`
- `KEYCLOAK_REALM`: The Keycloak realm that the application uses for authentication. Value: `onboarding`
- `KEYCLOAK_CLIENT_ID`: The client ID used by the application to authenticate with Keycloak. Value: `frontend-cli`
>This component is a Keycloak oauth2 client. To make sure users access, ensure that the [registration](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication#enable-user-registration) is enabled.
> Refer to the `Onboarding Realm` document of [Tier1-authentication](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication) to configure the onboparding realm.
> Also refer to [tier1-authentication](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication/-/blob/main/README.md?ref_type=heads) to see the full list of configurations that may be enabled in Keycloak according to Governance Authority needs

**eIDAS Configuration**
- `EIDAS_ENABLED`: Enables eIDAS authentication, documents and rules Management. Value: `false`
  Note: Make sure to enable eIDAS in the [onboarding backend](https://code.europa.eu/simpl/simpl-open/development/iaa/onboarding/-/tree/main/documents/deployment-guide?ref_type=heads) as well.
