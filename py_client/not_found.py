import requests

endpoint = "http://127.0.0.1:8000/api/products/235893898"

response = requests.get(endpoint)
print(response.json())
