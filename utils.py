import requests
import base64
import sys


# Uses client creds to get access token from Kroger API
def get_access_token(client_id, client_secret):
    try:
        # Encode client_id:client_secret in Base64 for Basic Auth
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "scope": "product.compact"  # Adjust scopes as needed
        }

        response = requests.post(TOKEN_URL, headers=headers, data=data, timeout=10)
        response.raise_for_status()

        token_data = response.json()
        return token_data["access_token"]

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)
    except KeyError:
        print("Failed to retrieve access token. Check credentials and scopes.")
        sys.exit(1)


# Save access token to a file for later use
def save_access_token(token, filename="kroger_token.txt"):
    with open(filename, "w") as token_file:
        token_file.write(token)