import requests

endpoint = "http://localhost:8000/api/"

data = {"title":'robel', "content":"student"}

get_response = requests.post(endpoint, params={'abc': 123}, json=data)

# print(get_response.text)
# print(type(get_response.text))
print(get_response.json())
# print(type(get_response.json()))
print(f"Status Code: {get_response.status_code}")