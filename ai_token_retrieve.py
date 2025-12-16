import requests
import base64
import sys

# Replace with your Kroger Developer credentials
CLIENT_ID = 
CLIENT_SECRET = 

# Kroger OAuth token endpoint
TOKEN_URL = "https://api.kroger.com/v1/connect/oauth2/token"

def get_client_credentials_token():
    try:
        # Encode client_id:client_secret in Base64 for Basic Auth
        credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
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

if __name__ == "__main__":
    token = get_client_credentials_token()
    print("Access Token:", token)