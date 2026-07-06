import os
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


def main():
    key_vault_url = "https://python1-keyvault.vault.azure.net/"
   
    tenant_id = os.getenv("AZURE_TENANT_ID")
    client_id = os.getenv("AZURE_CLIENT_ID")
    client_secret = os.getenv("AZURE_CLIENT_SECRET")

    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )
    client = SecretClient(vault_url=key_vault_url, credential=credential)

    username_secret = client.get_secret("username")
    password_secret = client.get_secret("password")

    print(f"Username: {username_secret.value}")
    print(f"Password: {password_secret.value}")


if __name__ == "__main__":
    main()
