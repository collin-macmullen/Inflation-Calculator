with open("item_data.txt", "r", encoding="utf-8") as info:
    info = eval(info.read())

print(type(info))

# print(info['data'][0].keys())

print(info['data'][0]['items'][0]['price']['regular'])
