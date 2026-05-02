# Configuration Properties

|Name|Type|Source|Description|Default Value|
|----|----|------|-----------|-------------|
| document-validation-engine.enabled | java.lang.Boolean | eu.europa.ec.simpl.onboarding.properties.DocumentValidationProperties | Enables the document validation engine | true |
| document-validation-engine.mock | java.util.List<eu.europa.ec.simpl.onboarding.properties.DocumentValidationProperties$Mock> | eu.europa.ec.simpl.onboarding.properties.DocumentValidationProperties | Enables the mock version of the document validation engine | N/A |
| document-validation-engine.timeout | java.time.Duration | eu.europa.ec.simpl.onboarding.properties.DocumentValidationProperties | Timeout value (in milliseconds) for the document validation engine | N/A |
| eidas.attributes-file-path | java.lang.String | eu.europa.ec.simpl.onboarding.properties.EidasProperties | N/A | classpath:eidas/eidasAttributes.json |
| eidas.enabled | java.lang.Boolean | eu.europa.ec.simpl.onboarding.properties.EidasProperties | Indicates whether the eIDAS login feature is enabled. | false |
| eidas.integration.properties | java.util.Map<java.lang.String,java.lang.String> | eu.europa.ec.simpl.onboarding.properties.EidasProperties$EidasIntegration | N/A | N/A |
| eidas.integration.type | java.lang.String | eu.europa.ec.simpl.onboarding.properties.EidasProperties$EidasIntegration | N/A | N/A |
| email-service.onboarding-request-url.applicant-url-template | java.lang.String | eu.europa.ec.simpl.onboarding.properties.EmailServiceProperties$OnboardingRequestUrl | URL of the page where the applicant can view their onboarding request. Must include a placeholder for the onboarding request ID. | N/A |
| email-service.onboarding-request-url.notary-url-template | java.lang.String | eu.europa.ec.simpl.onboarding.properties.EmailServiceProperties$OnboardingRequestUrl | URL of the page where the notary can view the applicant's onboarding request. | N/A |
| keycloak.realm | java.lang.String | eu.europa.ec.simpl.onboarding.properties.KeycloakProperties | Keycloak realm used by the application | N/A |
| keycloak.service-account.client-id | java.lang.String | eu.europa.ec.simpl.onboarding.properties.KeycloakProperties$ClientProperties | Client ID for the Keycloak service account used by the application | N/A |
| keycloak.service-account.client-secret | java.lang.String | eu.europa.ec.simpl.onboarding.properties.KeycloakProperties$ClientProperties | Client secret for the Keycloak service account used by the application | N/A |
| keycloak.url | java.lang.String | eu.europa.ec.simpl.onboarding.properties.KeycloakProperties | Base URL of the Keycloak server | N/A |
| microservice.identity-provider.url | java.net.URI | eu.europa.ec.simpl.onboarding.properties.MicroserviceProperties$IdentityProvider | URL of the identity provider microservice | N/A |
| microservice.security-attributes-provider.url | java.net.URI | eu.europa.ec.simpl.onboarding.properties.MicroserviceProperties$SecurityAttributesProvider | URL of the security attributes provider microservice | N/A |
| microservice.users-roles.url | java.net.URI | eu.europa.ec.simpl.onboarding.properties.MicroserviceProperties$UsersRoles | URL of the users and roles microservice | N/A |
| pagination.page-size-limit | java.lang.Integer | eu.europa.ec.simpl.onboarding.properties.PaginationProperties | N/A | N/A |
| scheduled-tasks.delete-rejected-onboarding-requests.cron | java.lang.String | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$DeleteRejectedOnboardingRequests | Cron expression for the task that deletes rejected onboarding requests | */5 * * * * * |
| scheduled-tasks.delete-rejected-onboarding-requests.retention-time | java.time.Duration | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$DeleteRejectedOnboardingRequests | Retention time before deleting rejected onboarding requests | 10d |
| scheduled-tasks.evaluate-not-executed-validation-rules.cron | java.lang.String | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$EvaluateNotExecutedValidationRules | Cron expression for evaluating not-executed validation rules | */5 * * * * * |
| scheduled-tasks.evaluate-not-executed-validation-rules.rules-per-execution | java.lang.Integer | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$EvaluateNotExecutedValidationRules | Number of validation rules processed per task execution | 20 |
| scheduled-tasks.evaluate-rule-execution-results.cron | java.lang.String | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$EvaluateRuleExecutionResults | Cron expression for evaluating rule execution results | 15,45 * * * * * |
| scheduled-tasks.evaluate-rule-execution-results.onboarding-request-per-execution | java.lang.Integer | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$EvaluateRuleExecutionResults | Number of onboarding requests processed per task execution | 20 |
| scheduled-tasks.handle-stuck-onboarding-requests.cron | java.lang.String | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$HandleStuckOnboardingRequests | Cron expression for handling stuck onboarding requests | */5 * * * * * |
| scheduled-tasks.handle-stuck-onboarding-requests.retention-time | java.time.Duration | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$HandleStuckOnboardingRequests | Retention time threshold for evaluating stuck onboarding requests | 10m |
| scheduled-tasks.rejection-of-stale-onboarding-requests.cron | java.lang.String | eu.europa.ec.simpl.onboarding.properties.ScheduledTaskProperties$RejectionOfStaleOnboardingRequests | Cron expression for rejecting stale onboarding requests | */5 * * * * * |