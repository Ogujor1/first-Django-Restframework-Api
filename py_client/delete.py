import requests

product_id = input("Enter the pruduct ID, it must be a whole number: ")

try:
  product_id = int(product_id)
except:
  product_id = None
  print(f'{product_id} is not a whole number.')  

endpoint = f'http://127.0.0.1:8000/product/{product_id}/delete'
response_delete = requests.delete(endpoint)
print(response_delete.status_code, response_delete.status_code == 204)