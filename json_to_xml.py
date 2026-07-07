# json_to_xml.py

from dicttoxml import dicttoxml
import json
import os

os.makedirs("data/xml", exist_ok=True)

files = ["categories", "users", "products"]

for file in files:

    with open(f"data/json/{file}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    xml_data = dicttoxml(data)

    with open(f"data/xml/{file}.xml", "wb") as x:
        x.write(xml_data)

    print(f"{file}.xml created successfully")