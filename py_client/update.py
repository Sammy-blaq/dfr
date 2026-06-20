import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "This is my updated title",
    "content": "This is my updated content"
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
