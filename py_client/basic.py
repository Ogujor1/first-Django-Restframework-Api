import requests

data = {
  'title': input('Enter the title\n'),
  'content': input('Give Description\n'),
  'price': float(input('Enter price in 2 decimal places\n'))
}

endpoint = 'http://127.0.0.1:8000/product/list-create/'
response = requests.post(endpoint, json=data)
print(response.json())