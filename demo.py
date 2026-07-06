from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = "Azure_key_vault"

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url=vault_url,
    credential=credential
)

secret = client.get_secret("DatabasePassword")

print(secret.value)
