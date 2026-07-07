import requests

print("Requests library is working!")

url = "https://api.escuelajs.co/api/v1/categories"

response = requests.get(url)

print("Status Code:", response.status_code)