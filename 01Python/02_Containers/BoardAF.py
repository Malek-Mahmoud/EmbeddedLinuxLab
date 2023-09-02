import requests

response = requests.get('http://www.boredapi.com/api/activity/')

data = response.json()

print(data.get('activity'))