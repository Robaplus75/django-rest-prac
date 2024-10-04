import requests

endpoint = "http://localhost:8000/api/product/"

get_response = requests.post(endpoint, json={"title":"roba"})

print(get_response.json())
print(get_response.status_code)
