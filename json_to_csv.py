import pandas as pd
import json
import os

os.makedirs("data/csv", exist_ok=True)

files = ["categories", "users", "products"]

for file in files:

    with open(f"data/json/{file}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    df.to_csv(
        f"data/csv/{file}.csv",
        index=False
    )

    print(f"{file}.csv created successfully")