import requests
import base64
import sys

token=


kroger_url="https://api.kroger.com/v1/products?filter.productId=0001111041700&filter.locationId=01400441"
headers = {
'Authorization': f'Bearer {token}',
'Cache-Control': 'no-cache'
}

response = requests.get(kroger_url, headers=headers)
item_data=response.json()

print(item_data)
print(response.status_code)

# outfile=open("item_data.txt", "w")
# outfile.write(str(item_data))