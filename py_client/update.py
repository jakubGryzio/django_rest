import requests

endpoint = "http://127.0.0.1:8000/api/products/5/update/"

data = {
    "title": "Hello world my old friend",
    "price": 129.99
}

response = requests.put(endpoint, json=data)
print(response.json())
