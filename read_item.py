import item_data
from datetime import date

def wanted_data(item_data):
    for f in item_data:
        with open(f"item_data/{f}", "r", encoding="utf-8") as info:
            info = eval(info.read())
            product_id=info['data'][0]['productId']
            description=info['data'][0]['description']
            price=info['data'][0]['items'][0]['price']['regular']
            category=info['data'][0]['items'][0]['categories'][0]
            date=date.today()
            



print(type(info))

# print(info['data'][0].keys())

print(info['data'][0]['items'][0]['price']['regular'])