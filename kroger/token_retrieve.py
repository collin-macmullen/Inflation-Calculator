import requests
import base64
import sys

def get_client_credentials():
    with open("kroger/client_credentials.txt", "r") as cred_file:
        lines = cred_file.readlines()
        client_id = lines[1].strip()
        client_secret = lines[4].strip()
    return client_id, client_secret

# Kroger OAuth token endpoint
TOKEN_URL = "https://api.kroger.com/v1/connect/oauth2/token"

def get_client_credentials_token(client_id, client_secret):
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

        print("Token found")
        return token_data["access_token"]

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)
    except KeyError:
        print("Failed to retrieve access token. Check credentials and scopes.")
        sys.exit(1)

def save_access_token(token, filename="kroger/token.txt"):
    with open(filename, "w") as token_file:
        token_file.write(token)
    print("Token saved to temp file")
    

def run():
    creds=get_client_credentials()
    token = get_client_credentials_token(creds[0], creds[1])
    save_access_token(token)

# if __name__ == "__main__":
#     creds=get_client_credentials()
#     token = get_client_credentials_token(creds[0], creds[1])
#     save_access_token(token)