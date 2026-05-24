import requests

response = requests.post(
    "http://192.168.0.201:11434/api/generate",
    json={
        "model": "tinyllama",
        "prompt": "Explain APIs simply.",
        "stream": False
    }
)

data = response.json()

for item in data.keys():
    print(f"{item}: {data[item]}")
