import requests

endpoint = "http://127.0.0.1:8000/api/products/"

headers = {
    "Authorization": "Bearer 8b6ebbdf9b6853391db0df3ad708ccc6158de000"
}
data = {
    "title": "This filed is done"
}

response = requests.post(endpoint, json=data, headers=headers)
print(response.json())
