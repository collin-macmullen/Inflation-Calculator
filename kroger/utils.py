import requests
import base64
import sys
from datetime import date
import json


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


# Get product data from Kroger API using access token
def get_data(token, item_id, location_id):
    kroger_url=f"https://api.kroger.com/v1/products?filter.productId={item_id}&filter.locationId={location_id}"
    headers = {
    'Authorization': f'Bearer {token}',
    'Cache-Control': 'no-cache'
    }

    response = requests.get(kroger_url, headers=headers)
    item_data=response.json()

    try:
        with open(f"kroger/item_data/json_data/{date.today()}/{item_id}_{location_id}_{date.today()}.json", "w") as outfile:
            outfile.write(json.dumps(item_data))
    except Exception as e:
        print(f"Error writing data for item {item_id} at location {location_id}: {e}", file=sys.stderr)


# Get Kroger store location data near zip code
def get_location(token, zip):
    kroger_url=f"https://api.kroger.com/v1/locations?filter.zipCode.near={zip}"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(kroger_url, headers=headers)
        response.raise_for_status()

        location_data=response.json()    

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)
    except KeyError:
        print("Failed to retrieve access token. Check credentials and scopes.")
        sys.exit(1)
    with open(f"location_data/locations.txt", "w") as outfile:
        outfile.write(str(location_data))
        print('location data saved')