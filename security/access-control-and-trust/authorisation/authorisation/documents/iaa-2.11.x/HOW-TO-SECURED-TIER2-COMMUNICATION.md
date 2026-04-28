# How to realize secure Agent-to-Agent communication

<!-- Remember to keep the Tier1 and Tier2 Gateway links updated. -->
Developing component to be deployed within a SIMPL Open Agent and use the **Secure Agent-to-Agent** is a 3 steps procedure that consist in:

1. Configure and publish the *tier 1 part* of the component in the [Tier1 Gateway](./README.md#gateway-routes-configuration) so that it will be accessible only by authenticated users. Look at [example section below](#example-of-tier-1-gateway-configuration).

2. Configure and publish the *tier 2 part* component in the [Tier2 Gateway](./README.md#gateway-routes-configuration-1) so that it will be accessible only by other agents. Look at [example section below](#example-of-tier-2-gateway-configuration). 

3. Use the [`simpl-http-client`](https://code.europa.eu/simpl/simpl-open/development/iaa/simpl-http-client) library or use the [tier2-proxy](https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy) in the *tier 1 part* to secure communication using mTLS while interacting with the *tier 2 part* deployed in other agents.

In order to implement both *tier 1* and *tier 2* backend side, you can follow the template provided in [`echo-backend`](https://code.europa.eu/simpl/simpl-open/development/iaa/echo-backend/-/tree/develop?ref_type=heads#prerequisites) repository. This template is a perfect example of how to follow the three steps explained above and make use of the [`simpl-http-client`](https://code.europa.eu/simpl/simpl-open/development/iaa/simpl-http-client). 

## Example

When defining a set of APIs to be forwarded to a microservice, a *base path* or *context prefix* should be configured on the tier1 or tier2 gateway. This ensures that incoming requests are correctly routed to the appropriate microservice. The gateway will handle forwarding, while the client (e.g., a frontend application) must send API requests using the full path, including the defined context prefix.

Flow example using the tier1 configuration below:

- the client calls the API using `https://<tier1-gateway hostname>/pet-api/pets`.
- the gateway forwards the request to `http://pet-microservice:8080/pets`, stripping the `/pet-api` prefix.
- the microservice receives the request without the prefix, allowing it to handle the API logic seamlessly.

### Example of Tier 1 Gateway configuration

```yaml
appConfig:
  external-routes:
    public-urls:
      - method: GET # The http method of the public endpoint
        path: "/pet-api/pets" # the path of the public endpoint 
    denied-urls:
      - method: DELETE # The http method of the denied endpoint
        path: "/pet-api/pets/*" # the path of the denied endpoint 

    rbac:
      - method: POST
        path: "/pet-api/pets" # the path of the protected endpoint 
        roles: 
          - VET # the role of the user that can use the endpoint

    spring-route-definitions:
      - id: pet # Your microservice id
        uri: http://pet-microservice:8080 # Your microservice url
        predicates:
          - Path=/pet-api/** # Access to pet api with a context prefix named "pet-api"
        filters:
          - StripPrefix=1 # Remove the context prefix when gateway forward the request at the microservice

```


### Example of Tier 2 Gateway configuration

```yaml
appConfig:
  external-routes:
    public-urls:
      - method: GET # The http method of the public endpoint
        path: "/fruit-api/fruits" # the path of the public endpoint 
    denied-urls:
      - method: DELETE # The http method of the denied endpoint
        path: "/fruit-api/fruits/*" # the path of the denied endpoint 

    abac:
      - method: POST
        path: "/fruit-api/fruits" # the path of the protected endpoint 
        identity-attributes: 
          - FRUIT_SELLER # the attribute of the user that can use the endpoint
    
    spring-route-definitions:
      - id: fruit # Your microservice id
        uri: http://fruit-microservice:8080 # Your microservice url
        predicates:
          - Path=/fruit-api/** # Access to fruit api with a context prefix named "fruit-api"
        filters:
          - StripPrefix=1 # Remove the context prefix when gateway forward the request at the microservice

```
