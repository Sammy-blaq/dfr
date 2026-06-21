import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Boxing Kit",
    'price': 134
}

headers = {
    "Authorization": "Bearer 1df4844cac8549c1d589b0a83e3bea9b479bd271"
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())