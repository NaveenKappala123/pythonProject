from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

key_vault_name = "my-key-vault"
vault_url = f"https://{key_vault_name}.vault.azure.net/"

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url=vault_url,
    credential=credential
)

secret = client.get_secret("DatabasePassword")

print(secret.value)