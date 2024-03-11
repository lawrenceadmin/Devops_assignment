import requests
import os

response = requests.get("http://localhost:5000/data")
if response.status_code == 200:
    data = response.json()
    os.makedirs("files", exist_ok=True)
    for sample in data["samples"]:
        filename = f"files/{sample['id']}.txt"
        with open(filename, "w") as f:
            f.write(sample["name"])
