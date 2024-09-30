import requests
endpoint = 'http://127.0.0.1:8000/product/267567271'
response = requests.get(endpoint)
print(response.json())