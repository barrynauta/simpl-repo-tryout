# Configuration Properties

|Name|Type|Source|Description|Default Value|
|----|----|------|-----------|-------------|
| database-seeding.security-attribute-provider-mapping.enabled | java.lang.Boolean | eu.europa.ec.simpl.securityattributesprovider.configurations.DBSeedingProperties$SecurityAttributeProviderMapping | Enables database seeding for the security attribute provider | true |
| database-seeding.security-attribute-provider-mapping.file-path | java.lang.String | eu.europa.ec.simpl.securityattributesprovider.configurations.DBSeedingProperties$SecurityAttributeProviderMapping | Path to the file used for seeding the security attribute provider | classpath:db.seeding/identityAttributes.default.json |
| microservice.authentication-provider.url | java.net.URI | eu.europa.ec.simpl.securityattributesprovider.configurations.MicroserviceProperties$AuthenticationProviderService | URL of the authentication provider microservice | N/A |
| microservice.identity-provider.url | java.net.URI | eu.europa.ec.simpl.securityattributesprovider.configurations.MicroserviceProperties$IdentityProvider | URL of the identity provider microservice | N/A |
| simpl.ephemeral-proof.expire-after | java.time.Duration | eu.europa.ec.simpl.securityattributesprovider.configurations.SimplProperties$EphemeralProof | Duration after which an ephemeral proof expires | 3m |
| simpl.ephemeral-proof.issuer-url | java.lang.String | eu.europa.ec.simpl.securityattributesprovider.configurations.SimplProperties$EphemeralProof | URL of the issuer for the ephemeral proof | N/A |
| simpl.ephemeral-proof.proof-of-possession.expiration-window.amount | java.lang.Long | eu.europa.ec.simpl.securityattributesprovider.configurations.SimplProperties$ExpirationWindow | Amount value for the expiration window of Proof of Possession | 1 |
| simpl.ephemeral-proof.proof-of-possession.expiration-window.chrono-unit | java.time.temporal.ChronoUnit | eu.europa.ec.simpl.securityattributesprovider.configurations.SimplProperties$ExpirationWindow | ChronoUnit used with the expiration window amount | minutes |
| simpl.ephemeral-proof.proof-of-possession.signature-algorithm | java.lang.String | eu.europa.ec.simpl.securityattributesprovider.configurations.SimplProperties$ProofOfPossession | Signature algorithm used for Proof of Possession in ephemeral proofs | ECDSA |