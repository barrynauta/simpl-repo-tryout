# Vault configuration

This guide provides instructions on how to configure [`HashiCorp Vault`](https://www.vaultproject.io/) to create an environment with application credentials, policies, and a valid space for storing secrets.

## Prerequisites

- Vault is deployed and running. Please refer to the [Vault documentation](https://developer.hashicorp.com/vault/install) for more details.
- Vault is accessible via a valid token. Please refer to the [Vault documentation](https://developer.hashicorp.com/vault/docs/commands/token) for more details.
- Vault CLI is installed and available. Please refer to the [Vault documentation](https://developer.hashicorp.com/vault/docs/commands) for more details.

## Configuring Vault CLI

To interact with Vault, configure the following environment variables:

```bash
# example of VAULT_ADDR = http://vault-common.common.svc.cluster.local:8200
export VAULT_ADDR="<vault_address>"
export VAULT_TOKEN="<vault_token>"
```

## Enabling the Secrets Engine

To enable the KV (Key-Value) secrets engine, use the following commands:

```bash
SECRET_PATH="<secret_path>" # es: secret
vault secrets enable -path=$SECRET_PATH kv
vault secrets list
```

## Enabling AppRole Authentication Method

To enable the **AppRole** authentication method, execute:

```bash
vault auth enable approle
vault auth list
```

## Creating a Policy for Data Access

Define a policy to control access to secrets:

```bash
# es: SECRET_PATH=secret
SECRET_PATH="<secret_path>"
# es: SECRET_SUBPATH=authenticationprovider
SECRET_SUBPATH="<secret_subpath>"
# es: POLICY_NAME=my-policy
POLICY_NAME="<policy_name>"

cat <<EOF > my-policy.hcl
path "$SECRET_PATH/data/$SECRET_SUBPATH/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
path "$SECRET_PATH/metadata/$SECRET_SUBPATH/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
EOF

vault policy write $POLICY_NAME my-policy.hcl
vault policy list
```

Assign the policy to an **AppRole**:

```bash
vault write auth/approle/role/myapp-role \
    token_policies="$POLICY_NAME" \
    token_ttl=1h \
    token_max_ttl=4h
```

## Retrieving Role ID and Secret ID

To retrieve the Role ID and Secret ID for authentication:

```bash
ROLE_ID=$(vault read -field=role_id auth/approle/role/myapp-role/role-id)
SECRET_ID=$(vault write -f -field=secret_id auth/approle/role/myapp-role/secret-id)

echo "ROLE_ID: $ROLE_ID"
echo "SECRET_ID: $SECRET_ID"
```

## Testing AppRole login

To test authentication using the retrieved credentials:

```bash
vault write auth/approle/login role_id="$ROLE_ID" secret_id="$SECRET_ID"
```

