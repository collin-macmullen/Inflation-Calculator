import pandas as pd
import json

with open("kroger/item_data/json_data/0076770700214_09700491_2025-12-18.json", "r") as f:
    data=json.loads(f.read())
    df=pd.json_normalize(data, record_path=["data", "items"])
    # data = pd.json_normalize(f, record_path=["data"])

print(df)

# This gets everything to be a flat table. Now need to filter down to relevant columns only.
# Need to add date column based on filename.
# Also need to loop through all json files and combine into one big dataframe.
# Then export to csv.