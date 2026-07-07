print("Starting extraction...")

import requests
import json
import os

apis = {
    "categories": "https://api.escuelajs.co/api/v1/categories",
    "users": "https://api.escuelajs.co/api/v1/users",
    "products": "https://api.escuelajs.co/api/v1/products"
}

os.makedirs("data/json", exist_ok=True)

for name, url in apis.items():

    print(f"Fetching {name}...")

    response = requests.get(url)

    print(response.status_code)

    data = response.json()

    with open(f"data/json/{name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"{name}.json saved")