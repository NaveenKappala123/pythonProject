import os
from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

KEY_VAULT_URL = os.environ["Azure_key_vault"]


@app.route("/")
def home():
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(
            vault_url=KEY_VAULT_URL,
            credential=credential
        )

        username = client.get_secret("username").value

        return f"""
        <h1>Azure Key Vault App is Running</h1>
        <p>Username secret was retrieved successfully.</p>
        <p>Username: {username}</p>
        """

    except Exception as error:
        return f"<h2>Error</h2><pre>{error}</pre>", 500


if __name__ == "__main__":
    app.run()
