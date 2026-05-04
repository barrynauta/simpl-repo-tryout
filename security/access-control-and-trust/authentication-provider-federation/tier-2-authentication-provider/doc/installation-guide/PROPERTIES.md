# Configuration Properties

|Name|Type|Source|Description|Default Value|
|----|----|------|-----------|-------------|
| client.authority.url | java.net.URI | eu.europa.ec.simpl.authenticationprovider.properties.MtlsClientProperties$AuthorityProperties | URL of the authority service | N/A |
| crypto.secret-key-base64 | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.CryptoProperties | Base64-encoded secret key used for encrypting and decrypting sensitive data | N/A |
| keypair.algorithm | java.lang.String | eu.europa.ec.simpl.authenticationprovider.configurations.KeyPairGenerationAlgorithm | Algorithm used for key pair generation | ECDSA |
| keypair.key-length | java.lang.Integer | eu.europa.ec.simpl.authenticationprovider.configurations.KeyPairGenerationAlgorithm | Key length used in key pair generation | 256 |
| keypair.read-algorithm | java.lang.String | eu.europa.ec.simpl.authenticationprovider.configurations.KeyPairGenerationAlgorithm | Algorithm used for reading the key pair | EC |
| keypair.signature-algorithm | java.lang.String | eu.europa.ec.simpl.authenticationprovider.configurations.KeyPairGenerationAlgorithm | Algorithm used for digital signature generation | SHA256withECDSA |
| microservice.identity-provider.url | java.net.URI | eu.europa.ec.simpl.authenticationprovider.properties.MicroserviceProperties$IdentityProvider | URL of the identity provider microservice | N/A |
| microservice.security-attributes-provider.url | java.net.URI | eu.europa.ec.simpl.authenticationprovider.properties.MicroserviceProperties$SecurityAttributesProvider | URL of the security attributes provider microservice | N/A |
| openid-connect.certs-endpoint | java.net.URI | eu.europa.ec.simpl.authenticationprovider.properties.OpenIdConnectProperties | URL of the OpenID Connect provider's JWKS endpoint | N/A |
| security.secret.location | eu.europa.ec.simpl.authenticationprovider.properties.SecurityProperties$Location | eu.europa.ec.simpl.authenticationprovider.properties.SecurityProperties$SecretProperties | Location of the security secret (e.g., database or vault) | database |
| simpl.certificate.san | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.SimplProperties$Certificate | Subject Alternative Name (SAN) for the certificate | N/A |
| simpl.sync-credentials.job.cron | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.SimplProperties$SyncCredentials$Job | N/A | N/A |
| vault.authentication.path | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties$Authentication | Path used for Vault authentication | N/A |
| vault.authentication.role-id | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties$Authentication | Role ID used for Vault authentication | N/A |
| vault.authentication.secret-id | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties$Authentication | Secret ID used for Vault authentication | N/A |
| vault.base-path | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties | Base path in Vault for storing secrets | N/A |
| vault.secret-engine | java.lang.String | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties | Vault secret engine name | N/A |
| vault.uri | java.net.URI | eu.europa.ec.simpl.authenticationprovider.properties.VaultProperties | URI of the Vault server | N/A |