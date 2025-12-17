import requests
import sys

def get_data(token, item_id, location_id):
    kroger_url=f"https://api.kroger.com/v1/products?filter.productId={item_id}&filter.locationId={location_id}"
    headers = {
    'Authorization': f'Bearer {token}',
    'Cache-Control': 'no-cache'
    }

    response = requests.get(kroger_url, headers=headers)
    item_data=response.json()

    with open(f"item_data/{item_id}_{location_id}_{date.today()}.txt", "w") as outfile:
        outfile.write(str(item_data))



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

if __name__ == "__main__":
    with open("kroger_token.txt", "r") as token_file:
        token=token_file.read().strip()
    get_location(token, 27713)