import requests

response = requests.get("http://google.com")
print(response)
print(response.headers)