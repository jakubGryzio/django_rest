import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.post(endpoint, params={"product_id": 123}, json={"title": "This is not null", "content": 'Hello World v2', "price": 12})
print(response.json())