import requests
from json import load

response = requests.get('https://api.ipify.org/?format=json​')

print(response.text)