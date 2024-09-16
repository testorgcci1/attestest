import requests


resp = requests.get("https://ipinfo.io/json")
print(resp.text)
