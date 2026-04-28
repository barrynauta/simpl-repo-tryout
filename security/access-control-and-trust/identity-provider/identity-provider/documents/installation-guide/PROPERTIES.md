# Configuration Properties

|Name|Type|Source|Description|Default Value|
|----|----|------|-----------|-------------|
| ejbca.ca-name | java.lang.String | eu.europa.ec.simpl.identityprovider.properties.EjbcaProperties | Name of the Certificate Authority (CA) used in EJBCA | OnBoardingCA |
| ejbca.end-entity-name | java.lang.String | eu.europa.ec.simpl.identityprovider.properties.EjbcaProperties | Name of the end entity registered in EJBCA | Onboarding TLS Profile |
| ejbca.profile-name | java.lang.String | eu.europa.ec.simpl.identityprovider.properties.EjbcaProperties | Name of the certificate profile used in EJBCA | Onboarding TLS Profile |
| ejbca.url | java.net.URI | eu.europa.ec.simpl.identityprovider.properties.EjbcaProperties | Base URL of the EJBCA service | N/A |
| microservice.security-attributes-provider.url | java.net.URI | eu.europa.ec.simpl.identityprovider.properties.MicroserviceProperties$SecurityAttributesProvider | URL of the security attributes provider microservice | N/A |
| simpl.authority-participant-type-placeholder | java.lang.String | eu.europa.ec.simpl.identityprovider.properties.SimplProperties | Placeholder value for the authority participant type | GOVERNANCE_AUTHORITY |
| simpl.automatic-renewal.default-duration-before-renewal | java.time.Duration | eu.europa.ec.simpl.identityprovider.properties.SimplProperties$AutoRenewal | Default duration before certificate expiration to trigger renewal | 20D |
| simpl.automatic-renewal.default-initialization.retry-backoff | java.time.Duration | eu.europa.ec.simpl.identityprovider.properties.SimplProperties$AutoRenewal$DefaultInitialization | N/A | 2s |
| simpl.automatic-renewal.default-initialization.use-api | java.lang.Boolean | eu.europa.ec.simpl.identityprovider.properties.SimplProperties$AutoRenewal$DefaultInitialization | Wether to use APi for default initialization or use direct service calls | true |
| simpl.automatic-renewal.job.cron | java.lang.String | eu.europa.ec.simpl.identityprovider.properties.SimplProperties$AutoRenewal$Job | Cron expression for the job | 0 0 2 * * ? |
| simpl.automatic-renewal.job.max-fetch-size | java.lang.Integer | eu.europa.ec.simpl.identityprovider.properties.SimplProperties$AutoRenewal$Job | The job will process renewals in batches of this size. | 100 |