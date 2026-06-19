import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Boxing Kit",
    'price': 134
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())