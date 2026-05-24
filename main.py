import requests

response = requests.get(
    "http://192.168.0.201:11434",
)

print(f"response: {response}")
print(f"status code: {response.status_code}")
print(f"text: {response.text}")
print(f"headers: {response.headers}")
