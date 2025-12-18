import requests
import sys
import kroger.token_retrieve as token_retrieve
import kroger.utils as utils

if __name__ == "__main__":
    print("Retrieving token...")

    token_retrieve.run()

    print("Token retrieved.")

    with open("kroger/token.txt", "r") as token_file:
        token=token_file.read().strip()

    with open("kroger/location_id.txt", "r") as loc_file:
        location_id=loc_file.read().strip()
    with open("kroger/item_id.txt", "r") as item_file:
        lines = item_file.readlines()
        item_id = lines[1].strip()

    for location_id in location_id.split(','):
        location_id=location_id.strip()
        for item_id in item_id.split(','):
            item_id=item_id.strip()
            utils.get_data(token, item_id, location_id)

    print("Done!")
