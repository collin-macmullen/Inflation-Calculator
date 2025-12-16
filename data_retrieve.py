import requests
import binascii
import base64
import json

# with open("krogerkey.bin", "rb") as binary_file: binary_key = binary_file.read()
# krogerkey = binascii.hexlify(binary_key).decode('utf-8')


# kroger_url="https://api.kroger.com/v1/products/0001111041700&filter.locationId=01400441"
# headers = {
# 'Authorization': f'Bearer H4sIAAAAAAAA/6pWSi0qyi9SslIqzUssLcnIL8qsSk1R0oEIx6ekFicXZRaUZObnKVkpZeaVJeZkpigkF6WmpOaVZCbmFCvVAgIAAP//jwSFxUIAAAA=',
# 'Cache-Control': 'no-cache'
# }
# response=requests.get(kroger_url, headers=headers)
# print(response.status_code)
# print(response.json())

# response = requests.get(kroger_url, headers=headers)
# print(response.status_code)
# print(response.json())

# auth="https://api.kroger.com/v1/connect/oauth2/authorize?scope=product.compact&response_type=code&client_id=cmacmulleninflationcalculator-bbcblwvn&redirect_uri=http://localhost:3000/callback"
# headers ={'Cache-Control': 'no-cache',
#           'Content-Type': 'application/x-www-form-urlencoded'}

# response=requests.get(auth, headers=headers)
# print(response.status_code)
# print(response.json())




with open("tst.bin", "rb") as binary_file: binary_key = binary_file.read()
krogerkey = encoded_data = base64.b64encode(binary_key).decode('utf-8')

# binascii.hexlify(binary_key).decode('utf-8')
print(krogerkey)

