import requests
import binascii


# with open("krogerkey.bin", "rb") as binary_file: binary_key = binary_file.read()
# krogerkey = binascii.hexlify(binary_key).decode('utf-8')


# kroger_url="https://api.kroger.com/v1/products/0001111041700&filter.locationId=01400441"
# headers = {
# 'Authorization': f'Bearer bRis_vBewJWWjZCXS6sYs_SKVZFWve8EObklFVeg',
# 'Cache-Control': 'no-cache'
# }


# response = requests.get(kroger_url, headers=headers)
# print(response.status_code)
# print(response.json())

# auth="https://api.kroger.com/v1/connect/oauth2/authorize?scope=product.compact&response_type=code&client_id=cmacmulleninflationcalculator-bbcblwvn&redirect_uri=http://localhost:3000/callback"
# headers ={'Cache-Control': 'no-cache',
#           'Content-Type': 'application/x-www-form-urlencoded'}

# response=requests.get(auth, headers=headers)
# print(response.status_code)
# print(response.json())



# curl -X POST \
#   'https://api.kroger.com/v1/connect/oauth2/token' \
#   -H 'Content-Type: application/x-www-form-urlencoded' \
#   -H 'Authorization: Basic {{base64(CLIENT_ID:CLIENT_SECRET)}}' \
#   -d 'grant_type=authorization_code&code={{CODE}}&redirect_uri={{REDIRECT_URI}}' \
#   --output tokens.bin

with open("tokens.bin", "rb") as binary_file: binary_key = binary_file.read()
krogerkey = binascii.hexlify(binary_key).decode('utf-8')
print(krogerkey)