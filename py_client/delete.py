import requests

product_id = 3

endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

response = requests.delete(endpoint)
print(response.status_code)
